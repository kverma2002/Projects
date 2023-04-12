package chatRoom;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Vector;





public class Server {

	private static List<ServerThread> serverThreads = Collections.synchronizedList(new ArrayList<ServerThread>());
	public static Vector<Trades> trades;
	public Server(int port, Vector<Trades> trades, ArrayList<Traders> traders) {
		try {
			ServerSocket ss = new ServerSocket(port);
			System.out.println("Listening on port " + port);
			System.out.println("Waiting for traders...");
			serverThreads = new Vector<ServerThread>();
			int connections = 0;
			this.trades = trades;
			while(true) {
				Socket s = ss.accept(); // blocking
				System.out.println("Connection from: " + s.getInetAddress());
				ServerThread st = new ServerThread(s, this, traders.get(connections));
				serverThreads.add(st);
				
				st.start();
				connections += 1;
				if (connections == traders.size()) {
					this.broadcast("All traders have arrived!");
					Util u = new Util();
					this.broadcast(Long.toString(Util.startMs));
					int index = 0;
					this.broadcast("Starting service.");
					System.out.println("Starting Service.");
					while(ServerThread.done != serverThreads.size()) {
						if(trades.isEmpty()) {
							break;
						}
						while(trades.get(0).startTime > u.timePassed()) {
							
						}
						if(serverThreads.get(index).ready) {
							this.sendTrades(serverThreads.get(index).pw, serverThreads.get(index).trader, 
									serverThreads.get(index).trader.balance, serverThreads.get(index));
							serverThreads.get(index).ready = false;
						}
						if(index == serverThreads.size() - 1) {
							index = 0;
						}
						else {
							index += 1;
						}
					}
					this.broadcast("All done poggies");
					if(trades.isEmpty()) {
						this.broadcast("Incomplete Trades: None");
					}
					else {
						String incomplete = "";
						for(Trades trade : trades) {
							incomplete += trade.startTime + ", " + trade.ticker + ", " + trade.numStocks + ", ";
						}
						this.broadcast("Incomplete Trades: (" + incomplete + Util.timeAndDate() + ")");
					}
					ss.close();
					System.out.println("Processing complete.");
					break;
					
					
				}
				else {
					this.broadcast((traders.size()- connections) + " more trader is needed before the service can begin.");
					this.broadcast("Waiting...");
					System.out.println("Waiting for " + (traders.size() - connections) + " more trader(s)...");
				}
			}
			
		} catch (IOException ioe) {
			//System.out.println("ioe in ChatRoom constructor: " + ioe.getMessage());
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public synchronized void sendTrades(PrintWriter pw, Traders trader, int balance, ServerThread st) throws InterruptedException {
		boolean done = false;
		boolean sent = false;
		int i = 0;
		while(i < Server.trades.size()) {
			String send = "";
			//System.out.println(Util.timePassed());
			if(Server.trades.get(i).startTime <= Util.timePassed()) {
				if(Server.trades.get(i).numStocks > 0) {
					if(Server.trades.get(i).numStocks*Server.trades.get(i).price <= st.trader.balance) {
						sent = true;
						st.trader.balance -= (Server.trades.get(i).numStocks*Server.trades.get(i).price);
						send += Server.trades.get(i).numStocks +  "," + Server.trades.get(i).price + "," + Server.trades.get(i).ticker;
						pw.println(send);
						pw.flush();
						Server.trades.remove(i);
					}
					else {
						i += 1;
					}
				}
				else {
					sent = true;
					send += Server.trades.get(i).numStocks +  "," + Server.trades.get(i).price + "," + Server.trades.get(i).ticker;
					pw.println(send);
					pw.flush();
					Server.trades.remove(i);
				}
			}
			else {
				break;
			}
		}
		if(sent) {
			pw.println("done");
			pw.flush();
		}
		else if (trades.isEmpty()) {
			ServerThread.done +=1;
			st.donzo = true;
			st.interrupt();
		}
		else {
			if(i == Server.trades.size()) {
				ServerThread.done = Server.serverThreads.size();
				this.broadcast("noMore");
				st.interrupt();
				for(ServerThread sT: Server.serverThreads) {
					sT.donzo = true;
					sT.interrupt();
				}
			}
		}
	}
	public void broadcast(String message) {
		for(ServerThread threads : serverThreads) {
			threads.sendMessage(message);
		}
		
	}
	
	public static void main(String [] args) {
		while(true) {
			String fileCSV = "";
			InputStreamReader isr = new InputStreamReader(System.in);
			BufferedReader br = new BufferedReader(isr);
			try {
				// Source: https://www.javatpoint.com/how-to-read-csv-file-in-java
				String line = "";
				String split = ",";
				System.out.println("What is the name of the file containing the schedule information?");
				fileCSV = br.readLine();
				BufferedReader br2 = new BufferedReader(new FileReader(fileCSV));  
				Vector<Trades> exchange = new Vector();
				while ((line = br2.readLine()) != null)   //returns a Boolean value  
				{  
					String[] Trade = line.split(split);
					exchange.add(new Trades(Integer.parseInt(Trade[0]), Trade[1], Integer.parseInt(Trade[2])));
				}
				ArrayList<Traders> traders = new ArrayList();
				System.out.println("Scheudle file read correctly");
				System.out.println("What is the name of the file containing the traders information?");
				fileCSV = br.readLine();
				BufferedReader br3 = new BufferedReader(new FileReader(fileCSV));
				while ((line = br3.readLine()) != null)   //returns a Boolean value  
				{  
					String[] Trade = line.split(split);
					traders.add(new Traders(Integer.parseInt(Trade[0]), Integer.parseInt(Trade[1])));
				}
				System.out.println("Trader file read correctly");
				Server server = new Server(6789, exchange, traders);
				break;
				
			} catch(FileNotFoundException fnfe) {
				System.out.println("The file "+  fileCSV + "could not be found.");
			}
			catch (IOException ioe) {
				System.out.println(ioe.getMessage());
			}
			
		}
		
	}
}
