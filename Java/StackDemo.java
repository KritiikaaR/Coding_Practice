import java.util.Stack;
import java.util.EmptyStackException;

public class StackDemo {
	
   static void showpush(Stack<Integer> st, int a) {
      st.push(a);
      System.out.println("push(" + a + ")");
      System.out.println("stack: " + st);

   }


   static void showpop(Stack<Integer> st) {
      System.out.print("pop -> ");
      Integer a = (Integer) st.pop();
      System.out.println(a);
      System.out.println("stack: " + st);

   }


   public static void main(String args[]) {
      Stack<Integer> st = new Stack<>();

      System.out.println("stack: " + st);
      showpush(st, 42);
      showpush(st, 66);
      showpush(st, 99);
      showpop(st);
      showpop(st);
      showpop(st);

     try {
         showpop(st);
      } catch (EmptyStackException e) {
         System.out.println("empty stack");
      }

   }

}