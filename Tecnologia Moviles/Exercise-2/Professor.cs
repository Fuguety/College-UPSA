namespace Exercise_2
{
    public class Professor
    {
        private int codProfessor;
        private string? name;
        private string? lastName;

        public string? LastName { get => lastName; set => lastName = value; }
        public string? Name { get => name; set => name = value; }
        public int CodProfessor { get => codProfessor; set => codProfessor = value; }

        public List<Classes> ProfessorClasses { get; set; } = new List<Classes>();

    }
    
    public class ProfessorBuilder
    {
        public Professor ppBuilder()
        {
            Professor professor = new Professor();


            Console.WriteLine("Name of professor");
            professor.Name = Console.ReadLine();
        
            Console.WriteLine("Last name of professor");
            professor.LastName = Console.ReadLine();
        
            while (true)
            {
                Console.WriteLine("Code of professor");
                try 
                { 
                    professor.CodProfessor = Convert.ToInt32(Console.ReadLine());
                
                    if (professor.CodProfessor > 0)
                        break;
                    else
                        Console.WriteLine("Please insert a positive number\n");

                } 
                catch { Console.WriteLine("Please insert a number\n"); } 
            }

            return professor;
        }
    }


}