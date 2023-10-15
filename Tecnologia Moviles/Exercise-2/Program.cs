namespace Exercise_2
{
public class Intel
{
    public static void Main()
    {
        University us = new University();
        Console.WriteLine("\nWelcome to university!");
        Console.WriteLine("\nBefore we start please create a class Subject\n");
        us.InsertClasses();

        Console.WriteLine("\nClass created, welcome!");

        bool quit = false;

        do
        {            
            Console.WriteLine("\n1 for adding new student");
            Console.WriteLine("2 for adding new professor");
            Console.WriteLine("3 for adding a new class");
            Console.WriteLine("4 to show all students");
            Console.WriteLine("5 to show all professors");
            Console.WriteLine("6 to show all classes\n");
            Console.WriteLine("9 to quit\n");

            int answer;
            if (!int.TryParse(Console.ReadLine(), out answer))
            {
                Console.WriteLine("\nInvalid input. Please enter a valid number.\n");
                continue;
            }  
            Console.WriteLine();

            switch (answer)
            {
                case 1:
                    us.InsertStudent();
                    break;
                case 2:
                    us.InsertProfessor();
                    break;
                case 3:
                    us.InsertClasses();
                    break;
                case 4:
                    Console.WriteLine();
                    us.PrintStudents();
                    break;
                case 5:
                    Console.WriteLine();
                    us.PrintTeachers();
                    break;
                case 6:
                    Console.WriteLine();
                    us.PrintClasses();
                    break;
                case 9:
                    quit = true;
                    break;
                default:
                    Console.WriteLine("\nInvalid choice. Please select a valid option.\n");
                    break;
            }
        }while (!quit);

    }
}
}