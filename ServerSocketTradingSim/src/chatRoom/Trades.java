package chatRoom;

import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import com.google.gson.Gson;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;


public class Trades {

	public int startTime;
	public String ticker;
	public int numStocks;
	public double price;
	public Trades(int startTime, String ticker, int numStocks) {
		this.startTime = startTime;
		this.ticker = ticker;
		this.numStocks = numStocks;
		URL url;
		Gson gson = new Gson();
		try {
			url = new URL("https://finnhub.io/api/v1/quote?symbol=" + "TSLA" + "&token=cdku19qad3i4r9fupab0cdku19qad3i4r9fupabg");
			try (InputStream input = url.openStream()) {
		        InputStreamReader isr = new InputStreamReader(input);
		        BufferedReader reader = new BufferedReader(isr);
		        StringBuilder json = new StringBuilder();
		        int c;
		        while ((c = reader.read()) != -1) {
		            json.append((char) c);
		        }
		        FinhubClass fC = gson.fromJson(json.toString(), FinhubClass.class);
		        price = fC.c;
		    }
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
}
