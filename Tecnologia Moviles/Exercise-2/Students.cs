namespace Exercise_2
{
    public class Students
    {
        private int expedient;
        private string? name;
        private string? lastName;

        public string? Name { get => name; set => name = value; }
        public string? LastName { get => lastName; set => lastName = value; }
        public int Expedient { get => expedient; set => expedient = value; }

        public List<Classes> EnrolledClasses { get; set; } = new List<Classes>();

    }

    // Builder/Constructor
    public class StudentsBuilder
    {
        public Students ssBuilder()
        {
            Students students = new Students();

            Console.WriteLine("Name of student");
            students.Name = Console.ReadLine();

            Console.WriteLine("Last name of student");
            students.LastName = Console.ReadLine();

            while (true)
            {
                Console.WriteLine("Expedient of the student");
                try
                {
                    students.Expedient = Convert.ToInt32(Console.ReadLine());

                    if (students.Expedient > 0)
                        break;
                    else
                        Console.WriteLine("Please insert a positive number\n");
                }
                catch { Console.WriteLine("Please insert a number\n"); }
            }

            return students;
        }
    }
}