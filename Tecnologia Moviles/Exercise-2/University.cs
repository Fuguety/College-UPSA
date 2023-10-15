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


        // Add student
        public void InsertStudent()
        {
            Students student = ss.ssBuilder();
            studentsList.Add(student);

            StudentToClass(student);
        }

        // Add Professor
        public void InsertProfessor()
        {
            Professor professor = pp.ppBuilder();
            professorList.Add(professor);

            ProfessorToClass(professor);
        }

        // Add Class
        public void InsertClasses()
        {
            classesList.Add(cc.ccBuilder());
        }

        // Print Students
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

        // Print Professors
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


        // Print CLasses
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


        // Select the student
        public void SelectStudent()
        {
            Console.WriteLine("Please select the number of student");
            PrintStudents();
            
            if (int.TryParse(Console.ReadLine(), out int studentNumber) && studentNumber >= 0 && studentNumber < studentsList.Count)
            {
                Students selectedStudent = studentsList[studentNumber];
                StudentToClass(selectedStudent);
            }
            
            else
            {
                Console.WriteLine("Invalid student number. Please select a valid student.");
            }

        }
        
        
        // Adds student to Classes
        private void StudentToClass(Students student)
        {
            Console.WriteLine("Do you want to enroll the student in a class? (Y/n)");
            string? response = Console.ReadLine();

            while (response == "y" || response == "" || response == " " || response == "Y")
            {
                Console.WriteLine("Enroll the student in a class. Choose the class number:");
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

                Console.WriteLine("Do you want to enroll the student in another class? (Y/n)");
                response = Console.ReadLine();
            }
        }



        //Add Student to the class
        private void EnrollStudentInClass(Students student, Classes classSubject)
        {
            student.EnrolledClasses.Add(classSubject);
            classSubject.EnrolledStudents.Add(student);
        }


        // Selects Professor
        public void SelectProfessor()
        {
            Console.WriteLine("Please select the number of student");
            PrintTeachers();
            
            if (int.TryParse(Console.ReadLine(), out int professorNumber) && professorNumber >= 0 && professorNumber < professorList.Count)
            {
                Professor selectedProfessor = professorList[professorNumber];
                ProfessorToClass(selectedProfessor);
            }
            
            else
            {
                Console.WriteLine("Invalid professor number. Please select a valid student.");
            }

        }
        
        
        // Adds professor to Classes
        private void ProfessorToClass(Professor professor)
        {
            Console.WriteLine("Do you want to enroll the professor in a class? (Y/n)");
            string? response = Console.ReadLine();

            while (response == "y" || response == "" || response == " " || response == "Y")
            {
                Console.WriteLine("Enroll the professor in a class. Choose the class number:");
                PrintClasses();

                if (int.TryParse(Console.ReadLine(), out int classNumber) && classNumber >= 0 && classNumber < classesList.Count)
                {
                    EnrollProfessorInClassSubjects(professor, classesList[classNumber]);
                    Console.WriteLine("Professor enrolled in the selected class.");
                }
                else
                {
                    Console.WriteLine("Invalid class number. Student not enrolled in a class.");
                }

                Console.WriteLine("Do you want to enroll the student in another class? (Y/n)");
                response = Console.ReadLine();
            }
        }

        // Add teacher to the class
        private void EnrollProfessorInClassSubjects(Professor professor, Classes classSubject)
        {
            professor.ProfessorClasses.Add(classSubject);
            classSubject.EnrolledProfessor.Add(professor);
        }



    }

}