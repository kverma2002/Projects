package chatRoom;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;
import java.util.Vector;


import java.math.RoundingMode;  
import java.text.DecimalFormat;  

public class ChatClient extends Thread {

	private BufferedReader br;
	private PrintWriter pw;
	private UtilClient u;
	private double balance;
	private double profit = 0;
	private static final DecimalFormat decfor = new DecimalFormat("0.00");
	public ChatClient(String hostname, int port) {
		try {
			System.out.println("Trying to connect to " + hostname + ":" + port);
			Socket s = new Socket(hostname, port);
			System.out.println("Connected to " + hostname + ":" + port);
			br = new BufferedReader(new InputStreamReader(s.getInputStream()));
			pw = new PrintWriter(s.getOutputStream());
			try {
				String line = br.readLine();
				balance = Integer.parseInt(line);
				pw.println("Hi there");
				line = br.readLine();
				System.out.println(line);
				while(!line.equalsIgnoreCase("All traders have arrived!")) {
					line = br.readLine();
					System.out.println(line);
				}
				line = br.readLine();
				u = new UtilClient(Long.parseLong(line));
				line = br.readLine();
				System.out.println(line);
				Vector<Trade> trades = new Vector();
				line = br.readLine();
				while(!line.equalsIgnoreCase("noMore")) {
					while(!line.equalsIgnoreCase("done")) {
						String[] trade = line.split(",");
						trades.add(new Trade(trade[2], Integer.parseInt(trade[0]), Double.parseDouble(trade[1])));
						line = br.readLine();
					}
					if(line.equals("noMore")) {
						break;
					}
					this.processTrades(trades);
					pw.println("done");
					pw.flush();
					line = br.readLine();
				}
				while(!line.equalsIgnoreCase("All done poggies")) {
					line = br.readLine();
				}
				line = br.readLine();
				u.printTime(line);
				System.out.println("Total profit: $" + decfor.format(this.profit));
				System.out.println("Proccesing Complete");
				
				
				
			} catch (IOException ioe) {
				System.out.println("ioe in ChatClient.run(): " + ioe.getMessage());
			}
			
		} catch (IOException ioe) {
			System.out.println("ioe in ChatClient constructor: " + ioe.getMessage());
		}
	}
	
	public void processTrades(Vector<Trade> trades) {
		for(Trade trade : trades) {
			if(trade.numStocks > 0) {
				u.printTime("Assigned purchase of " + trade.numStocks + "stock(s) of " + trade.ticker + ". Total cost estimate = $" + trade.value
						 + " * " + trade.numStocks + " = " + decfor.format(trade.numStocks*trade.value));
			}
			else if(trade.numStocks < 0) {
				u.printTime("Assigned Sale of " + -1*trade.numStocks + " stock(s) of " + trade.ticker + ". Total gain estimate = $" + trade.value
						 + " * " + -1*trade.numStocks + " = " + decfor.format(-1*trade.numStocks*trade.value));
			}
			
		}
		for(Trade trade : trades) {
			if(trade.numStocks > 0) {
				u.printTime("Starting Purchase of " + trade.numStocks + " stock(s) of " + trade.ticker);
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				this.balance -= (trade.numStocks*trade.value);
				u.printTime("Finsihed Purchase of " + trade.numStocks + " stocks of " + trade.ticker);
				System.out.println("Current balance after trade: $" + decfor.format(this.balance));
				
				
			}
			else if(trade.numStocks < 0) {
				u.printTime("Starting Sale of " + -1*trade.numStocks + " stock(s) of " + trade.ticker);
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				u.printTime("Finsihed Sale of " + -1*trade.numStocks + " stocks of " +trade.ticker);
				profit += -1*trade.numStocks*trade.value;
			}
		}
		trades.clear();
	}
	
	public static void main(String [] args) {
		System.out.println("Welcome to SalStocks v2.0!");
		System.out.println("Enter the server hostname");
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		try {
			String in = br.readLine();
			System.out.println("Enter the server port");
			int port = Integer.parseInt(br.readLine());
			ChatClient cc = new ChatClient(in, port);
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
