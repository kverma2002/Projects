package chatRoom;

import java.util.concurrent.TimeUnit;

public class UtilClient {
	
	public long startMs;
		
		public UtilClient(long startMS) {
			this.startMs = startMS;
		}
	
		public void printTime(String message) {
			long x = System.currentTimeMillis() - startMs;
			long hours = TimeUnit.MILLISECONDS.toHours(x);
			long minutes = TimeUnit.MILLISECONDS.toMinutes(x)-TimeUnit.HOURS.toMinutes(TimeUnit.MILLISECONDS.toHours(x));
			long seconds = TimeUnit.MILLISECONDS.toSeconds(x) - TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(x));
			long ms = TimeUnit.MILLISECONDS.toMillis(x)- TimeUnit.SECONDS.toMillis(TimeUnit.MILLISECONDS.toSeconds(x));//a - TimeUnit.MILLISECONDS.toMinutes(x)-TimeUnit.HOURS.toMinutes(TimeUnit.MILLISECONDS.toHours(x));
			String datetime = "[" + String.format("%02d:%02d:%02d:%03d", hours, minutes, seconds, ms);
			System.out.println(datetime + "] " + message );
		}
		
		public int timePassed() {
			long x = System.currentTimeMillis();
			return (int)((x - this.startMs)/1000);
		}


}
