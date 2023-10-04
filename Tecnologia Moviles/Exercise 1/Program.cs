using Microsoft.VisualBasic;
using System.Text.Json;

public class Sensors{

// Prints Array
  public static void printArray(List<string> array)
  {
    foreach (string str in array)
    Console.Write(str + " ");
  }

// Write to Json file
  public static void writeJson(string filePath, List<string> array)
  {

    string existingJsonData = File.ReadAllText(filePath);
    List<List<string>>? existingPeople = JsonSerializer.Deserialize<List<List<string>>>(existingJsonData);

    existingPeople.Add(array);

    string updatedJsonData = JsonSerializer.Serialize(existingPeople);
    System.IO.File.WriteAllText(filePath, updatedJsonData);

  }

  public static void emptyArray(string filePath)
  {
    Console.WriteLine("Would you like to empty the json file?");

    string? arrayAnswer = Console.ReadLine().ToLower();
    
    if (arrayAnswer == "yes"){
      string temp = "[]";
      System.IO.File.WriteAllText(filePath, temp);
      Console.WriteLine("Json file sucessfully cleaned");
    }
  }


  // User interacts with array, select the array and the thingy within it
  public static void arrayCount(string filePath)
  {
    string existingJsonData = File.ReadAllText(filePath);
    List<List<string>>? arrayJson = JsonSerializer.Deserialize<List<List<string>>>(existingJsonData);
    Console.WriteLine("Amount of arrays: ", arrayJson.Count);
    

    Console.WriteLine("\nWich array would you like to select?\nPlease note that '0' is the first array");
    
    int arraySelect = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine("\n");

    foreach (string item in arrayJson[arraySelect])
        Console.Write(item + " ");
    
    Console.WriteLine("\nWich item of the array would you like to select?\nPlease note that '0' is the first item of the array");

    int arraySelectitem = Convert.ToInt32(Console.ReadLine());

    if (arraySelectitem < arrayJson[arraySelect].Count)
    {
        int r = 0;
        foreach (string item in arrayJson[arraySelect]){
            if (arraySelectitem == r)
              Console.WriteLine(item);
        
            r = r + 1;
        }
    }
    else { Console.WriteLine("Item in array doesn't exist"); }

    
    

  }


  public static void Main()
  {
    
    string filePath = "Array.json";

    emptyArray(filePath);

    Console.WriteLine("How many arrays would you like to create?");

    int sensors = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine("What is the size would you like the arrays to have?");

    int measuraments = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine("Would you like to use random numbers?");

    string? answer = Console.ReadLine().ToLower();

    Random random = new Random();

    for (int i=1; i <= sensors; i++)
    {
      // Creates array
      List<string> smt = new List<string>();


      // Populate Array
      for (int x=1; x<=measuraments; x++)
      {    
        if (answer == "yes")
          smt.Add(random.Next(1, 1000).ToString()); // Populate using random numbers
        
        else{
          Console.WriteLine("\nPlease add stuff to the array:");

          string? temp = Console.ReadLine(); // Populate yourself
          smt.Add(temp);

        }

        if (x == measuraments)
        {
          printArray(smt);
          Console.WriteLine("  ||  Array ended, creating another one...\n");
          writeJson(filePath, smt);
        }
      }
    }

    Console.WriteLine("\nWould you like to view all arrays?\n");

    string? arrayAnswer = Console.ReadLine().ToLower();

    if (arrayAnswer == "yes")
        Console.WriteLine(File.ReadAllText(filePath));

    Console.WriteLine("Would you like to interact with the arrays?");
    
    string? answerInteract = Console.ReadLine().ToLower();

    if (answerInteract == "yes")
      arrayCount(filePath);


    emptyArray(filePath);

    Console.WriteLine("Program finished");


  }
}
