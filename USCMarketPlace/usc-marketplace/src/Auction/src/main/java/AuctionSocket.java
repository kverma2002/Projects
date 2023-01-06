import java.io.IOException;
import java.sql.SQLException;
import java.util.Vector;

import javax.websocket.OnClose;
import javax.websocket.OnError;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.Session;
import javax.websocket.server.ServerEndpoint;

@ServerEndpoint(value = "/ws")
public class AuctionSocket {
private static Vector<Session> sessionVector = new Vector<Session>();
private static int currentBidder = 0;
	
	@OnOpen
	public void open(Session session) throws ClassNotFoundException, SQLException, IOException {
		System.out.println("Connection made!");
		sessionVector.add(session);
		currentBidder++;
		updateAcution(session);
	}
	
	public void updateAcution(Session session) throws ClassNotFoundException, SQLException, IOException {
		AuctionJDBC jdbc = new AuctionJDBC();
		String currentBid = jdbc.latestAuction();
		for(Session s : sessionVector) {
			// getBasicRemote() is for synchronous communication
			// getAsyncRemote() is for asynchronous communication
			s.getBasicRemote().sendText("bidder/"+Integer.toString(this.currentBidder));
		}
		session.getBasicRemote().sendText("currentBid/"+currentBid);
	}
	@OnMessage
	public void onMessage(String message, Session session) throws IOException {
		System.out.println(message);
		String[] inputs = message.split("/");
		AuctionJDBC jdbc = new AuctionJDBC();
		try {
			if(inputs[0].equals("newBid")) {
				String result = jdbc.searchBid(Integer.parseInt(inputs[1]), inputs[2]);
				if(result.equals("Highest")) {
					for(Session s : sessionVector) {
						// getBasicRemote() is for synchronous communication
						// getAsyncRemote() is for asynchronous communication
						s.getBasicRemote().sendText(message);
					}
				}
				else if(result.equals("Fail")) {
					session.getBasicRemote().sendText(result);
				}
			}
			else if(inputs[0].equals("End")) {
				for(Session s : sessionVector) {
					// getBasicRemote() is for synchronous communication
					// getAsyncRemote() is for asynchronous communication
					s.getBasicRemote().sendText("End/"+jdbc.latestEmail());
				}
			}
		} catch (NumberFormatException ne) {
			// TODO Auto-generated catch block
			ne.printStackTrace();
		} catch (SQLException sqle) {
			// TODO Auto-generated catch block
			sqle.printStackTrace();
		} catch (IOException ioe) {
			// TODO: handle exception
			System.out.println("ioe: " + ioe.getMessage());
			close(session);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	@OnClose
	public void close(Session session) throws IOException {
		System.out.println("Disconnecting!");
		sessionVector.remove(session);
		this.currentBidder--;
		for(Session s : sessionVector) {
			// getBasicRemote() is for synchronous communication
			// getAsyncRemote() is for asynchronous communication
			s.getBasicRemote().sendText("bidder/"+Integer.toString(this.currentBidder));
		}
		
	}
	
	@OnError
	public void error(Throwable error) {
		System.out.println("Error!");
	}

}
