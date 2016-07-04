import java.io.*;
import java.util.*;
class file

{
public static void main (String args[]) throws FileNotFoundException
    {
    
Scanner sc = new Scanner(new File(args[0]));
int count=0;
int test=0;
while(sc.hasNext()){
    sc.next();
    count++;
}
System.out.println("Number of words: " + count);
//System.out.println(args[0]);
}
}
