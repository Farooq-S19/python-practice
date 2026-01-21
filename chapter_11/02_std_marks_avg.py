import math
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avg(self):
        return f"average marks of {self.name} is{round(sum(self.marks)/len(self.marks),2)}"

s1= student("rohan",[65,56,73])
print(s1.avg())
