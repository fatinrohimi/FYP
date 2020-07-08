import java.net.*;
import java.io.*;

class MyClient {
   public static void main(String[] args) {
      try
      {
         Socket s = new Socket("localhost",3636);
         PrintStream out = new PrintStream(s.getOutputStream());
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
         System.out.print("Enter Num 1 : ");
         out.println(br.readLine());			
         System.out.print("Enter Num 2 : ");			
         out.println(br.readLine());
         System.out.print("Enter operand : ");
         String op = br.readLine();
         out.println(op);
         System.out.println("\nResult : " + in.readLine());						
         s.close();
      }
      catch(Exception e)
      {
         e.printStackTrace();
      }
   }
}
