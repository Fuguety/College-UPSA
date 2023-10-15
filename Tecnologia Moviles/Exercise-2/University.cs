namespace Exercise_2
{

    public class University
    {
        StudentsBuilder ss = new StudentsBuilder();
        ClassesBuilder cc = new ClassesBuilder();
        ProfessorBuilder pp = new ProfessorBuilder();

        private List<Students> studentsList = new List<Students>();
        private List<Professor> professorList = new List<Professor>();
        private List<Classes> classesList = new List<Classes>();

        public void InsertStudent()
        {
            Students student = ss.ssBuilder();
            studentsList.Add(student);

            Console.WriteLine("Enroll the student in a class. Please choose the class number:");
            PrintClasses();

            if (int.TryParse(Console.ReadLine(), out int classNumber) && classNumber >= 0 && classNumber < classesList.Count)
            {
                EnrollStudentInClass(student, classesList[classNumber]);
                Console.WriteLine("Student enrolled in the selected class.");
            }
            else
            {
                Console.WriteLine("Invalid class number. Student not enrolled in a class.");
            }
        }

        public void InsertProfessor()
        {
            Professor professor = pp.ppBuilder();
            professorList.Add(professor);

            Console.WriteLine("Enroll the student in a class. Please choose the class number:");
            PrintClasses();

            if (int.TryParse(Console.ReadLine(), out int classNumber) && classNumber >= 0 && classNumber < classesList.Count)
            {
                EnrollProfessorInClassSubjects(professor, classesList[classNumber]);
                Console.WriteLine("Professor enrolled in the selected class.");
            }
            else
            {
                Console.WriteLine("Invalid class number. Professor not enrolled in a class.");
            }
        }

        public void InsertClasses()
        {
            classesList.Add(cc.ccBuilder());
        }

        public void PrintStudents()
        {
            int i = 0;
            foreach (Students student in studentsList)
            {
                Console.WriteLine("Student's number: " + i);
                Console.WriteLine("Name of the Student: " + student.Name);
                Console.WriteLine("Last Name of the Student: " + student.LastName);

                foreach (Classes classes in student.EnrolledClasses)
                    Console.WriteLine("Classes: " + classes.Name);

                i++;
            }
        }

        public void PrintTeachers()
        {
            int i = 0;
            foreach (Professor professor in professorList)
            {
                Console.WriteLine("Professor's number: " + i);
                Console.WriteLine("Name of the Professor: " + professor.Name);
                Console.WriteLine("Last Name of Professor: " + professor.LastName);

                foreach (Classes classes in professor.ProfessorClasses)
                    Console.WriteLine("Classes professor teach: " + classes.Name);

                i++;
            }
        }

        public void PrintClasses()
        {
            int i = 0;
            foreach (Classes classes in classesList)
            {
                Console.WriteLine("Class number: " + i);
                Console.WriteLine("Name of Class: " + classes.Name);

                foreach (Professor professor in classes.EnrolledProfessor)
                    Console.WriteLine("Professor of class: " + professor.Name);

                foreach (Students student in classes.EnrolledStudents)
                    Console.WriteLine("Students in class: " + student.Name);

                i++;
            }
        }



        private void EnrollProfessorInClassSubjects(Professor professor, Classes classSubject)
        {
            professor.ProfessorClasses.Add(classSubject);
            classSubject.EnrolledProfessor.Add(professor);
        }

        private void EnrollStudentInClass(Students student, Classes classSubject)
        {
            student.EnrolledClasses.Add(classSubject);
            classSubject.EnrolledStudents.Add(student);
        }

    }

}