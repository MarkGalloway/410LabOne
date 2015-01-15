class Student():
  """A Student"""
  def __init__(self, name, family):
    self.name = name
    self.family = family
    self.courseMarks = {}

  def addCourse(self, course, mark):
    self.courseMarks[course] = mark
  
  def average(self):
    try:
      return sum(self.courseMarks.values()) / len(self.courseMarks) 
    except ZeroDivisionError:
      print("Student %s has no courses." % self.name)


# Test 1
student = Student("Mark", "Galloway")
student.addCourse("Math", 100)
student.addCourse("C410", 90)
student.addCourse("English 101", 80)
assert(student.average() == 90)

# Test 2
studentB = Student("Fred", "Flintstone")
studentB.average()  # Test no courses (visual print out)
studentB.addCourse("Dino101", 51)
assert(studentB.average() == 51)