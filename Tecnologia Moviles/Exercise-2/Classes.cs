namespace Exercise_2
{
    public class Classes
    {
        private int codClass;
        private string? name;
        private int credits;

        public List<Students> EnrolledStudents { get; set; } = new List<Students>();

        public List<Professor> EnrolledProfessor { get; set; } = new List<Professor>();

        public int CodClass { get => codClass; set => codClass = value; }
        public string? Name { get => name; set => name = value; }
        public int Credits { get => credits; set => credits = value; }
    }

    // Builder/Constructor
    public class ClassesBuilder
    {

        public Classes ccBuilder()
        {
            Classes classes = new Classes();

            Console.WriteLine("Name of class");
            classes.Name = Console.ReadLine();
        
            while (true)
            {
                Console.WriteLine("Credits of the class");
                try { 
                    classes.Credits = Convert.ToInt32(Console.ReadLine());
                
                    if (classes.Credits > 0)
                        break;
                    else
                        Console.WriteLine("Please insert a positive number\n");

                    } catch { Console.WriteLine("Please insert a number\n"); } 
            }

            while (true)
            {
                Console.WriteLine("Code of class");
                try { 
                    classes.CodClass =Convert.ToInt32(Console.ReadLine());
                
                    if (classes.CodClass > 0)
                        break;
                    else
                        Console.WriteLine("Please insert a positive number\n");

                    } catch { Console.WriteLine("Please insert a number\n"); } 
            }

            return classes;
        }
    }

}