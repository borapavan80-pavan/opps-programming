class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print('marks:',self.marks)
    def check_result(self):
        if self.marks>=35:
            print("pass")
        else:
            print("fail")
s1=student("pavan",20,90)
s1.display()
s1.check_result()
s2=student("sai",21,30)
s2.display()
s2.check_result()
s3=student('sri',20,91)
s3.display()
s3.check_result()
s4=student("vasu",45,90)
s4.display()
s4.check_result()
s5=student("sandeep",28,30)
s5.display()
s5.check_result()                   



