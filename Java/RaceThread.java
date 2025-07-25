import java.util.Random;

class ThreadRunner extends Thread{
	private String runnerName;  //name of the runner
	private int restTime;       //the resting time of each runner
	private int runnerSpeed;   //their speed
	private int position = 0;  //position of the runner
	private ThreadRunner opponent; // To interrupt the other runner

	
	
	ThreadRunner(String name, int rest, int speed){
		runnerName=name;
		restTime=rest;
		runnerSpeed=speed;
	}
	
	//getter method to get the runner name
	public String getRunnerName() {
		return runnerName;
	}
	
	//sets the other runner as the opponent
	 public void setOpponent(ThreadRunner other) {
	        this.opponent = other;
	    }
	
	
	public void run() {
		int random;
		Random rand=new Random();
		
		//keep running until 1000 meters
		while (position<1000) {
			
			
			//stop the race if the thread is interrupted
			if (Thread.interrupted()) {
                System.out.println(runnerName + " concedes the race.");
                return;
            }
			
			random= rand.nextInt(100)+1;
			if (random>restTime) {
				position+=runnerSpeed;
			    
				if (position>=1000) {
			    	RaceThread.finished(this);  //if runner passed 1000 meters we announce this runner as winner
			    	if (opponent != null) opponent.interrupt();  //stopping the opponent thread
			    	break;  //break the loop
			    } else {
			    	System.out.println(runnerName +" at "+ position +" meters. "); 
			}
			} else {
				System.out.println(runnerName + " is resting.");
			}   

			//pausing for 100ms to simulate time between moves
			try {
				Thread.sleep(100);
			}catch(InterruptedException e){
				System.out.println(runnerName+ " was interrupted and concedes.");
				return;
			}		
		}
		
	}
}

public class RaceThread{
	
	private static boolean raceOver = false;  //to check if race is over or not
	
	
	//synchronized because only there can be only one winner
    public static synchronized void finished(ThreadRunner runner) {
        if (!raceOver) {
            raceOver = true;
            System.out.println( runner.getRunnerName() + " WINS the race!");
            
            
        }
    }
	
	public static void main(String[] args) {
		ThreadRunner tortoise=new ThreadRunner("Tortoise", 0, 10);
		ThreadRunner hare=new ThreadRunner("Hare", 90, 100);
		
		//starting the threads and setting each other as opponents.
		
		tortoise.start();
		hare.start();
		
		
		
		 tortoise.setOpponent(hare);
	     hare.setOpponent(tortoise);
		
	}
}