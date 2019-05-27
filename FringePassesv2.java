//Veronica Tang  05/27/19
//trying to get the hashmap to work
//got rid of all lowercase letters

import java.util.*;
import java.nio.file.*;
import java.io.*;
import java.lang.*;
import java.nio.charset.*;

public class FringePassesv2
{
  private static final char[] NUMSANDLETTERS = {'A', 'B', 'C', 'D', 'E' ,'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
  static final String[] passcodes = {"03","05","10", "CC","01", "AC", "VP"};
  static final boolean testing = true;
  
  //TEST FONTS!  CAP "S" WORKS OR  NO?  Hopefully will work...??  
  
  public static void main(String[] args)
  {
    int numOfThree = 0;
    int numOfFive = 0;
    int numOfTen = 0;
    int numOfComp = 0;
    int numBomb = 0;
    int numOfArtistComp = 0;
    int numOfVIP = 0;
    int[] tasks = {numOfThree, numOfFive, numOfTen, numOfComp, numBomb,numOfArtistComp, numOfVIP};
    
    //Create hashmap with pre-existing codes
    //this part works
    HashMap<String, String> codes = new HashMap<String, String>();
    try
    {
      List<String> numbers = Files.readAllLines(Paths.get("C:\\Veronica\\Fringe\\2018\\AllCodes.txt"), StandardCharsets.UTF_8);
      for(int i = 0 ; i< numbers.size(); i++)
      {
        codes.put(numbers.get(i), numbers.get(i));
      }
      System.out.println("here");
      System.out.println(codes);
    }
    catch(Exception hi)
    {
      System.out.println("nope");
    }
    
    try
    {
      File file = new File("BOCode.txt"); //most recent stuff, spaced in 15s for printing
      // creates the file
      file.createNewFile();
      // creates a FileWriter Object
      FileWriter writer = new FileWriter(file);
      File programFile = new File("NewCodes.txt");
      programFile.createNewFile();
      FileWriter codeWriter = new FileWriter(programFile);
      
      int count = 0; //count = number of codes generated thus far (at any point in the next chunk of code)
      int limit = 0;
      for (int a: tasks)
        limit+=a; // so limit becomes the total number of codes to generate; each index of task represents the number of codes to generate for a specific type of code       
      //generate all the codes
      for(int x = 0; x<tasks.length; x++)
      {
        for(int y = 0; y<tasks[x]; y++)
        {
          String passcode = generate(x, codes);
          codes.put(passcode, passcode);
          count++;
          System.out.println(passcode);
          // Writes the content to the files
          writer.write(passcode+System.getProperty("line.separator"));
          if((count)%15 == 0)
            writer.write(System.getProperty("line.separator"));
          //this next part is just so we don't get an awkward space at the end of the program.
          if(count!=limit)
            codeWriter.write(passcode+ System.getProperty("line.separator"));
          else
            codeWriter.write(passcode);
        }          
      }
      writer.flush();
      writer.close();
      codeWriter.flush();
      codeWriter.close();
    }
    catch(Exception hi)
    {
      System.out.println("Printing problem");
    }
    
    System.out.println(codes);
    System.out.println("Done");
  }
  public static String generate(int x, HashMap<String,String> codes)
  {
          String passcode = passcodes[x]; //passcodes gives us the prefix, originally
          for(int i = 0; i<7; i++)
          {
            passcode = passcode + NUMSANDLETTERS[((int)(Math.random() * (NUMSANDLETTERS.length)))]; //append the random string stuffs
          }
          if(testing)
          {
            passcode = passcode + "TEST";
            if(codes.containsKey(passcode))
              passcode = generate(x, codes);
          }
      return passcode;
  }
}