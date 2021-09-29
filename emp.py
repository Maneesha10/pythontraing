class Employee:
    def __init__(self,empid,empname,empsal,empdept):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
        self.empdept=empdept
    def display(self):
        print(self.empname)
class Timesheet(Employee):
    def __init__(self,date,hrs,activity,desc,status):
        self.date=date
        self.hrs=hrs
        self.activity=activity
        self.desc=desc
        self.status=status
    def createTimesheet(self):
        print(self.activity)
b = Employee(102,"manu",20000,"accounts")
print(b.empname)
t = Timesheet("10-12=2020",2,"managing","manage data","wip")
t.createTimesheet()
print(getattr(t,"status"))
