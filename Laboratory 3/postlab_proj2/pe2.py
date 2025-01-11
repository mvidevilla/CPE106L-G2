import random

class Student:
    def __init__(self, name, num_scores):
        self.name = name
        self.scores = [0] * num_scores

    def set_score(self, index, score):
        self.scores[index - 1] = score

    def get_name(self):
        return self.name

    def __str__(self):
        scores_str = " ".join(map(str, self.scores))
        return f"Name: {self.name}, Scores: {scores_str}"

def main():

    students = [
        Student("Saging", 3),
        Student("Banana", 3),
        Student("Apple", 3)
    ]

    students[0].set_score(1, 100)
    students[0].set_score(2, 95)
    students[0].set_score(3, 90)

    students[1].set_score(1, 85)
    students[1].set_score(2, 75)
    students[1].set_score(3, 65)

    students[2].set_score(1, 90)
    students[2].set_score(2, 80)
    students[2].set_score(3, 70)

    random.shuffle(students)
    print("Shuffled Students:")
    for student in students:
        print(student)

    students.sort(key=lambda s: s.get_name())
    print("\nSorted Students:")
    for student in students:
        print(student)

if _name_ == "_main_":
    main()
