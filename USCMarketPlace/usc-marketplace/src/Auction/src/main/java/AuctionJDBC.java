import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class AuctionJDBC{
	public String searchBid(int newBid, String email) throws SQLException, ClassNotFoundException{
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/Auction?user=root&password=asdfghjkl");
		PreparedStatement ps = conn.prepareStatement("SELECT Highest FROM HighestBid");
		ResultSet rs = ps.executeQuery();
		int lastHighest = 0;
		boolean rsHasNext = false;
		PreparedStatement ps2;
		while(rs.next()) {
			lastHighest = rs.getInt("Highest");
			rsHasNext = true;
			System.out.println("Enter");
		}
		System.out.println(lastHighest);
		if(rsHasNext==false) {
			ps2= conn.prepareStatement("INSERT INTO HighestBid (Highest, Email) VALUES (?,?)");
			ps2.setString(1, Integer.toString(newBid));
			ps2.setString(2, email);
			int row = ps2.executeUpdate();
			ps2.close();
			conn.close();
			rs.close();
			ps.close();
			return "Highest";
		}
		else if(newBid>lastHighest) {
			ps2= conn.prepareStatement("UPDATE HighestBid SET Highest = ?, Email = ?");
			ps2.setString(1, Integer.toString(newBid));
			ps2.setString(2, email);
			int row = ps2.executeUpdate();
			ps2.close();
			conn.close();
			rs.close();
			ps.close();
			return "Highest";
		}
		conn.close();
		rs.close();
		ps.close();
		return "Fail";
	}
	
	public String latestAuction() throws SQLException, ClassNotFoundException {
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/Auction?user=root&password=asdfghjkl");
		PreparedStatement ps = conn.prepareStatement("SELECT Highest FROM HighestBid");
		ResultSet rs = ps.executeQuery();
		int lastHighest = 0;
		while(rs.next()) {
			lastHighest = rs.getInt("Highest");
		}
		conn.close();
		rs.close();
		ps.close();
		return Integer.toString(lastHighest);
	}
	
	public String latestEmail() throws SQLException, ClassNotFoundException {
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/Auction?user=root&password=asdfghjkl");
		PreparedStatement ps = conn.prepareStatement("SELECT Email FROM HighestBid");
		ResultSet rs = ps.executeQuery();
		String lastEmail = "";
		while(rs.next()) {
			lastEmail = rs.getString("Email");
		}
		conn.close();
		rs.close();
		ps.close();
		return lastEmail;
	}
	
	
}
