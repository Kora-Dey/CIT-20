class Employee:
  def __init__(self,first_name,last_name,email,ssn):
    self.__first_name = first_name
    self.__last_name = last_name
    self.__email = email
    self.__ssn = ssn
  def get_first_name(self):
    return self.__first_name
  def set_first_name(self,new_first_name):
    self.__first_name = new_first_name
  def get_last_name(self):
    return self.__last_name
   
  def get_email(self):
    return self.__email
    
  def set_email(self,new_name):
    self.__email = new_email
    
  def get_ssn(self):
    return self.__ssn

  def set_ssn(self,new_ssn):
    self.__ssn = new_ssn

class Manager(Employee):
  def __init__(self,first_name,last_name,email,ssn,years, salary):
    Employee.__init__(self,first_name,last_name,email,ssn)
    self.__years = years 
    self.__salary = salary

  def get_years(self):
    return self.__years

  def set_years(self,new_years):
    self.__years = new_years
  def get_salary(self):
    return self.__salary

  def set_salary(self,new_salary):
    self.__salary = new_salary
    
  def get_net_income(self):
    tax_rate = 0.3
    bonus = self.__years * 1000
    gross_income = self.__salary + bonus
    income_tax = gross_income * tax_rate
    net_income = gross_income - income_tax
    return net_income

class Representative(Employee):

  def __init__(self,first_name,last_name,email,ssn,hours, pay_rate):
    Employee.__init__(self,first_name,last_name,email,ssn)
    self.__hours = hours
    self.__pay_rate= pay_rate
  def get_hours(self):
    return self.__hours
  def set_hours(self,new_hours):
    self.__hours - new_hours
  def get_pay_rate(self):
    return self.__pay_rate
  def set_pay_rate(self,new_pay_rate):
    self.__pay_rate= new_pay_rate
  def get_net_income(self):
    gross_income = self.__hours * 52 * self.__pay_rate
    tax_rate = 0.20
    income_tax = gross_income * tax_rate
    net_income = gross_income - income_tax
    return net_income

def display_title():
  print("Welcome to my App")
  print()
  print("EMPLOYEE DATA ENTRY")
  print()


def main():
  display_title()
  employees = []
  while True:
    choice= input('Manager or Representative? (m/r):')
    if choice.lower() == "m":
      first_name = input("First Name:")
      last_name = input("Last Name:")
      email = input("Email Address:" )
      ssn= input("SSN:")
      years = int(input("Years of Experience: "))
      salary = int(input("Annual Salary:"))

      manager = Manager(first_name,last_name,email,ssn,years,salary)
      employees.append(manager)

    elif choice.lower()== "r":
       first_name = input("First Name:")
       last_name = input("Last Name:")
       ssn = input("SSN:")
       email = input("Email Address:" )
       hours = int(input("Weekly Hours of Work:"))
       pay_rate = int(input("Pay Rate:"))

       representative = Representative(first_name,last_name,email,ssn,hours,pay_rate)
       employees.append(representative)
    else: 
      print("Invalid selection.")
      print()
   
    new_choice= input("Continue? (y/n): ")
    if new_choice == 'n':
      print("EMPLOYEE INFORMATION")
      for employee in employees:
        print(employee.get_last_name()+" "+ employee.get_first_name()," ",employee.get_email()+ ","+ employee.get_ssn()+" "+ str(employee.get_net_income()))
      break
main()
