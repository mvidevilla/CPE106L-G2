"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
               
    def compareEqualAverage(self, target):
        if(self.getAverage() == target.getAverage()):
            return self.getName() + " and " + target.getName() + " have the same grade average."
        else:
            return "The average scores of " + self.getName() + " and " + target.getName() +" are not equal"
            
    def compareLessThanAverage(self, target):
        if(self.getAverage() < target.getAverage()):
            return self.getName() + " has a grade average less than " + target.getName()
        else:
            return self.getName() + " does not have a grade average less than " + target.getName()
            
    def compareGreaterThanOrEqualAverage(self, target):
        if(self.getAverage() >= target.getAverage()):
            return self.getName() + " has a grade average greater than or equal to " + target.getName()
        else:
            return self.getName() + " does not have a grade greater than or equal to " + target.getName()
        
def main():
    """A simple test."""
    student1 = Student("Saging", 3)
    for i in range(1, 4):
        student1.setScore(i, 100)
    print(student1)
    
    student2 = Student("Banana", 3)
    student2.setScore(1, 99.99)
    student2.setScore(2, 70)
    student2.setScore(3, 65)
    print(student2)
    
    print("")
    
    print(student1.compareEqualAverage(student2))
    print(student1.compareLessThanAverage(student2))
    print((student1).compareGreaterThanOrEqualAverage(student2))
    
if __name__ == "__main__":
    main()