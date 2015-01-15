class Student():
  """docstring for Student"""
  def __init__(self, name, family):
    self.name = name
    self.family = family
    self.courseMarks = {}

  def addCourse(self, course, mark):
    self.courseMarks[course] = mark
  
  def average(self):
    return sum(self.courseMarks.values()) / len(self.courseMarks)

# Test
student = Student("Mark", "Galloway")
student.addCourse("Math", 100)
student.addCourse("C410", 90)
student.addCourse("English 101", 80)
assert(student.average() == 90)