package chatRoom;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class Util {
	
	public static long startMs;
	
	public Util() {
		startMs = System.currentTimeMillis();
	}

	public static void printTime(String message) {
		long x = System.currentTimeMillis() - startMs;
		long hours = TimeUnit.MILLISECONDS.toHours(x);
		long minutes = TimeUnit.MILLISECONDS.toMinutes(x)-TimeUnit.HOURS.toMinutes(TimeUnit.MILLISECONDS.toHours(x));
		long seconds = TimeUnit.MILLISECONDS.toSeconds(x) - TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(x));
		long ms = TimeUnit.MILLISECONDS.toMillis(x)- TimeUnit.SECONDS.toMillis(TimeUnit.MILLISECONDS.toSeconds(x));//a - TimeUnit.MILLISECONDS.toMinutes(x)-TimeUnit.HOURS.toMinutes(TimeUnit.MILLISECONDS.toHours(x));
		String datetime = "[" + String.format("%02d:%02d:%02d:%03d", hours, minutes, seconds, ms);
		System.out.println(datetime + "] " + message );
	}
	
	public static int timePassed() {
		long x = System.currentTimeMillis();
		return (int)((x - startMs)/1000);
	}
	
	public static String timeAndDate() {
		//https://stackoverflow.com/questions/26717733/print-current-date-in-java
		DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
	    //get current date time with Date()
	    Date date = new Date();
	    System.out.println(dateFormat.format(date));

	    //get current date time with Calendar()
	    Calendar cal = Calendar.getInstance();
	    return dateFormat.format(cal.getTime());
	}
}
