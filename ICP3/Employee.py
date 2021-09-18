# create empty dictionary
employees = {}
# create class Employee
class Employee:
    employee_count = 0

    def __init__(self,id,name,department,salary,balance,isEmployed=True):
        """
        Constructor to initialize class members
        """
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        self.balance = balance
        self.isEmployed = isEmployed
        Employee.employee_count += 1                    # increament employee count

    def get_salary(self):
        """
        :return: The employee salary.
        """
        return self.salary

    def pay(self):
        """
        Adds employee salary to the employee balance.
        """
        self.balance = self.balance+self.salary

    def get_balance(self):
        """
        :return: Total balance of employee.
        """
        return self.balance

    def employee_fire(self):
        """
        Function to remove employees from payroll.Once fired then salary will be set to 0 and isEmployed will be false
        """
        self.salary = 0
        self.isEmployed = False

    def is_employed(self):
        """
        :return: The status specifying employment status of employee.
        """
        return self.isEmployed

    def get_id(self):
        """
        :return: The employee id.
        """
        return self.id

    def get_name(self):
        """
        :return: Name of the employee.
        """
        return self.name

    def get_department(self):
        """
        :return: Department of employee
        """
        return self.department

# create part time class and inherits properties from Employee class
class PartTime(Employee):
    # init method of parent class to create object
    def __init__(self, id, name, department, salary, balance):
        Employee.__init__(self, id, name, department, salary, balance)

    # Function to give 5% default raise to part time employee if specific raise is not mentioned in input.txt
    def giveRaise(self,percent_raise=5):
        self.salary = (self.salary * percent_raise / 100)+self.salary

# create Full time class and inherits properties from Employee class
class FullTime(Employee):
    # init method of parent class to create object
    def __init__(self, id, name, department, salary, balance):
        Employee.__init__(self, id, name, department, salary, balance)

    # Function to give 10% default raise to part time employee if specific raise is not mentioned in input.txt
    def giveRaise(self,percent_raise=10):
        self.salary = (self.salary * percent_raise / 100) + self.salary

def add_employee(tokens):
    """
    if the last token in input text is F then calling FullTime function and adding employee details(id,name,salary and department) into dictionary
    otherwise calling part time function adding employee details into dictionary
    """
    if tokens[-1] == 'F':
        emp = FullTime(int(tokens[1]),tokens[2] + " " + tokens[3],tokens[4],int(tokens[5]),0)
        employees[tokens[1]] = emp
    else:
        emp = PartTime(int(tokens[1]),tokens[2] + " " + tokens[3],tokens[4],int(tokens[5]),0)
        employees[tokens[1]] = emp

def give_raise(tokens):
    """
    Give raises to currently employed employees. If raise percentage is specified in the input, it is used to give raise
    otherwise, a default of 5% or 10% raise is given depending on type of employment(F or P).
    :param tokens: list containing employee id and raise percentage read from input file
    """
    if tokens[1] in employees:
        if employees[tokens[1]].is_employed():
            if len(tokens) == 3:
                employees[tokens[1]].giveRaise(int(tokens[-1]))
            else:
                employees[tokens[1]].giveRaise()

def give_pay():
    """
    Pay employee salary
    """
    for employee in employees.values():
        employee.pay()


def fire(tokens):
    """
    Function to remove employee from payroll.
    :param tokens: list containing employee id to fire read from input file
    """
    if tokens[1] in employees:
        employees[tokens[1]].employee_fire()


def average():
    """
    Function to compute average salary of Full time and part time employees
    :return:tuple of full time and part time employees average salary depending on employee status
            if employee is removed from payroll then fired employee count will not be considered while computing
            average salary of Full time and part time employees.
    """
    full_time_salary = 0.0
    part_time_salary = 0.0
    full_time_count = 0.0
    part_time_count = 0.0
    for employee in employees.values():
        # Use isinstance method to determine whether employee instance in dictionary is FullTime or PartTime.
        if isinstance(employee, FullTime):
            if employee.is_employed():
                full_time_salary = full_time_salary + employee.get_salary()
                full_time_count = full_time_count + 1
        else:
            if employee.is_employed():
                part_time_salary = part_time_salary + employee.get_salary()
                part_time_count = part_time_count + 1
    return (full_time_salary/full_time_count, part_time_salary/part_time_count)


def output():
    """
    Writes to output file in the format specified by the document.
    """
    with open('employeeoutput.txt','w') as outfile:
        for employee in employees.values():
            outfile.writelines([employee.get_name(), " ", str(employee.get_id()), " ", employee.get_department(), "\n"])
            if employee.is_employed():
                outfile.writelines("current salary: ${} \n" .format(employee.get_salary()))
            else:
                outfile.writelines("Not employed with the company. \n")
            outfile.writelines("pay earned to date: ${} \n".format(employee.get_balance()))
            if isinstance(employee, FullTime):
                outfile.writelines("Full-Time employee \n")
            else:
                outfile.writelines("Part-Time employee \n")
            outfile.writelines("\n")

        outfile.writelines("Total number of employee:${} \n".format(Employee.employee_count))
        ftavg,ptavg = average()
        outfile.writelines("Average Salary paid to all Full-time employees:${} \n".format(ftavg))
        outfile.writelines("Average Salary paid to all Part-time employees:${} \n".format(ptavg))

def main():
    """
    Reads the input file and calls appropriate methods to perform actions.
    """
    with open("input.txt",'r') as infile:
        for line in infile:
            tokens = line.split()
            if tokens[0] == 'NEW':
                add_employee(tokens)
            elif tokens[0] == 'RAISE':
                give_raise(tokens)
            elif tokens[0] == 'FIRE':
                fire(tokens)
            elif tokens[0] == 'PAY':
                give_pay()


if __name__ == '__main__':
    main()
    output()
















