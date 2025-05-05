# class variables =  share instances of a class
#                    Defined outside the constructor
#                    Allow you to share data  among all objects created from that class


class Student:
  # class variable that will be share inside this class student 
  
  class_year = 2024
  num_students = 0
  
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
    Student.num_students += 1 
 
# student_1 is the class object and it is initialized by invoking the constructor method initialize    
student_1 =Student("Titus Kiptoo", 24, 'A')
student_2 =Student("Kiptoo", 29, 'C')
student_3 =Student("Malia", 4, 'A')

student_4 =Student("Mercy Jeptoo", 34, 'B')

print(student_1.class_year)
print(student_1.grade)
print(Student.class_year)

print(Student.num_students)