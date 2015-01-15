class Student(object):
  """docstring for Student"""
  def __init__(self, name, family):
    self.name = name
    self.family = family
    self.courseMarks = {}

  def __str__(self):
    return "%s _ %s _ %d" %(self.name, self.family, self.average())

  def addCourse(self, course, mark):
    self.courseMarks[course] = mark
  
  def average(self):
    return sum(self.courseMarks.values()) / len(self.courseMarks)

student = Student("Mark", "Galloway")
student.addCourse("Math", 100)
student.addCourse("C410", 90)
print student