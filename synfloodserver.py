import java.io.*;
import java.net.*;

public class MultiThreadServer implements Runnable {
   Socket s;

   MultiThreadServer(Socket s) {
      this.s = s;
   }

   public static void main(String args[]) throws Exception {
      ServerSocket ss = new ServerSocket(3636);
      System.out.println("Listening");

      while (true) 
      {
         Socket sock = ss.accept();
         System.out.println("Connected");
         new Thread(new MultiThreadServer(sock)).start();
      }
   }

 public void run() {
      try 
      {
         BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));		
         int a = Integer.parseInt(in.readLine());
         int b = Integer.parseInt(in.readLine());

         char[] op = (in.readLine().toCharArray());			
         PrintStream out = new PrintStream(s.getOutputStream()); 				
         switch(op[0])
         {
            case '+':
               out.println(a+b);
               break;
	case '-':
               out.println(a-b);
               break;
	case '*':
               out.println(a*b);
               break;
	case '/':
               out.println(a/b);
               break;
	case '%':
               out.println(a%b);
               break;
	default:
               out.println("Invalid operator");				
         }				
         System.out.println("Result sent on client machine...");
         out.close();
         s.close();
      } 
      catch (IOException e) 
      {
         System.out.println(e);
      }
   }
}
