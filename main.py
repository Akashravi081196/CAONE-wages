#Mathematical calculations for reference
#regular pay = regular rate * hours worked
#overtime rate = hourly rate * OT multiple
#gross pay = regular pay + overtime pay
#standard rate =710 (fixed)
#higher rate = 2 (gross pay - standard rate)
#standard tax = gross pay * 20%
#higher tax = gross pay * 40%
#total tax = standard tax + higher tax
#tax credit = 72
#net tax = total tax - tax credit
#PRSI = gross pay * 4%
#net deductions = net tax + PRSI
#net pay = gross pay - net deductions

#Creating a class with employee details as per the Question in CA ONE

class Employee:
    def __init__(self, StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
        self.__StaffID = StaffID
        self.__LastName = LastName
        self.__FirstName = FirstName
        self.__RegHours = RegHours
        self.__HourlyRate = HourlyRate
        self.__OTMultiple = OTMultiple
        self.__TaxCredit = TaxCredit
        self.__StandardBand = StandardBand


#Create a dictionary and giving value so that we can use in feature for the wage calculation and for the test
    def computePayment(self, HoursWorked, date):
        dict = {
                "name": self.__FirstName + " " + self.__LastName,
                "Regular Hours Worked": self.__RegHours,
                "Regular Rate": self.__HourlyRate,
                "Standard Rate Pay": self.__StandardBand,
                "Tax Credit": self.__TaxCredit,
                }
        print(dict)

e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
e.computePayment(42,'31/10/2022')

