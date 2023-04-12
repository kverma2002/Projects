package chatRoom;

import java.awt.image.BufferedImage;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Vector;


public class ServerThread extends Thread{
	// to do --> private variables for the server thread 
	private Server server;
	public PrintWriter pw;
	public BufferedReader br;
	public Traders trader;
	public Socket s;
	public static int done = 0;
	public boolean ready = true;
	public boolean donzo = false;
	
	
	public ServerThread(Socket s, Server server, Traders trader) {
		try {
			// to do --> store them somewhere, you will need them later 
			this.s = s;
			this.br = new BufferedReader(new InputStreamReader(this.s.getInputStream()));
			this.pw = new PrintWriter(this.s.getOutputStream());
			this.server = server;
			this.trader = trader;
			pw.println(trader.balance);
			pw.flush();
			} catch (IOException ioe) {
			System.out.println("ioe in ServerThread constructor: " + ioe.getMessage());
		}
	}

	public void run() {
		while(!Thread.interrupted()) {
			try {
				/*
				trader.balance = server.sendTrades(pw, trader, trader.balance, this);
				System.out.println("Waititng");
				*/
				String line = "";
				while (!line.equalsIgnoreCase("done") && !donzo) {
					line = br.readLine();
					if(line == null) {
						break;
					}
				}
				ready = true;
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				//e1.printStackTrace();
			} 
			
		}
	}
	
	
	
	public void sendMessage(String message) {
		pw.println(message);
		pw.flush();
	}
	
	
	
	
	
}
