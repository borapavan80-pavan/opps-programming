class employ:
    def __init__(self,name,depement,domain,monthlysalary):
        self.name=name
        self.depement=depement
        self.domain=domain
        self.monthlysalary=monthlysalary
    def display(self):
        print("name",self.name)
        print("depement",self.depement)
        print("domain",self.domain)
        print("monthlysalary",self.monthlysalary)
    def check_salary(self):
        print("salary is",self.monthlysalary*12)
        print("bonus is",self.monthlysalary*12*0.1)
    def check_monthlyincrement(self):
        print("monthly increment is",self.monthlysalary*0.1)
name=employ("pavan","cse","python",500000)
name.display()
name.check_salary()
name.check_monthlyincrement()
name1=employ("sai","ece","java",400000)
name1.display()
name1.check_salary()
name1.check_monthlyincrement()
name2=employ("sri","mech","c++",300000)
name2.display()
name2.check_salary()
name2.check_monthlyincrement()
name3=employ("vasu","civil","c",200000)
name3.display()
name3.check_salary()
name3.check_monthlyincrement()
                
