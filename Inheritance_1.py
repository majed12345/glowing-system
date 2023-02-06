class LeaveSystem:
    def __init__(self, name, employeeId=1):
        self.name = name
        self.employeeId = employeeId
        # if (employeeId != '1'):
        #     exit


class Employee(LeaveSystem):
    def __init__(self, name, employeeId, department, title):
        super().__init__(name, employeeId)
        # LeaveSystem.__init__(name,employeeId)
        self.department = department
        self.title = title


class SickLeaves(LeaveSystem):
    def __init__(self, name, employeeId, totalSickLeave, remSickLeave):
        super().__init__(name, employeeId)
        # LeaveSystem.__init__(name,employeeId)
        self.totalSickLeave = totalSickLeave
        self.remSickLeave = remSickLeave


class Projects(LeaveSystem):
    def __init__(self, name, employeeId, bench, onProject):
        super().__init__(name, employeeId)
        # LeaveSystem.__init__(name,employeeId)
        self.bench = bench
        self.onProject = onProject


print("===============Test 1===================")
t1 = LeaveSystem("Elpsee Mendes", '1')
print("Employee Name = {} \nEmployee ID = {}".format(t1.name, t1.employeeId))


print("===============Test 2===================")
t2 = Projects("Wase Pur", 2, "Employee is on bench", "N/A")
print("Employee Name = {}\nEmployee ID = {}\nEmployee on bench = {}\nEmployee on project = {}".format(
    t2.name, t2.employeeId, t2.bench, t2.onProject))

print("===============Test 3===================")
t3 = SickLeaves("Big Shaw", 3, 4, 0)
print("Employee Name = {}\nEmployee ID = {}\nTotal Sick Leaves = {} \nRemaining Sick leaves = {}".format(
    t3.name, t3.employeeId, t3.totalSickLeave, t3.remSickLeave))
