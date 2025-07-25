class PrintDemo {
   public void printCount() {

      try {
         for(int i = 5; i >  0; i--) {
            Thread.sleep(50);
           System.out.println("Counter   ---   "  + i );
         }

      } catch (Exception e) {
         System.out.println("Thread  interrupted.");
      }
   }

}


class ThreadDemo extends Thread {

   private Thread t;
   private String threadName;
   PrintDemo  printDemo;


   ThreadDemo( String name,  PrintDemo pd) {
      threadName = name;
      printDemo = pd;
   }

   public void run() {
      printDemo.printCount();
      System.out.println("Thread " +  threadName + " exiting.");
   }

public void start () {
      System.out.println("Starting " +  threadName );
      if (t == null) {
         t = new Thread (this, threadName);
         t.start ();

      }

   }

}


public class TestThread {

   public static void main(String args[]) {

      PrintDemo printDemo = new PrintDemo();
      ThreadDemo t1 = new ThreadDemo( "Thread - 1 ", printDemo );
      ThreadDemo t2 = new ThreadDemo( "Thread - 2 ", printDemo );

      t1.start();
      t2.start();

      // wait for threads to end

         try {
         t1.join();
         t2.join();

      } catch ( Exception e) {
         System.out.println("Interrupted");
      }

   }

}