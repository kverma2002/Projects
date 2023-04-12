package chatRoom;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;

import com.google.gson.Gson;

public class Trade {
	public String ticker;
	public int numStocks;
	public double value;
	public Trade(String ticker, int numStocks, double value) {
		this.ticker = ticker;
		this.numStocks = numStocks;
		this.value = value;
		
	}
}
