#Mathematical calculations for reference in this program
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

import unittest

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

    def computePayment(self, HoursWorked, Date):
        #Overtime worked calculation
        if (self.__RegHours > HoursWorked):
            raise ValueError("Regular Hours Worked should never exceed hours worked")
        else:
            Overtimeworked = HoursWorked - self.__RegHours
        #print(Overtimeworked)

        # overtime rate calculation
        Overtimerate = self.__HourlyRate * self.__OTMultiple
        #print(Overtimerate)

        #Regularpay calculation
        Regularpay = self.__RegHours * self.__HourlyRate
        #print(Regularpay)

        #Overtimepay calculation
        Overtimepay = Overtimerate * Overtimeworked
        if (Overtimepay < 0):
            raise ValueError('Overtimepay should not be negative')
        #print(Overtimepay)


        #Grosspay calculation
        GrossPay = Regularpay + Overtimepay
        #print(GrossPay)

        #Higherrate pay calculation
        Higherratepay = GrossPay - self.__StandardBand
        #print(Higherratepay)

        #Standard tax calculation 20% of grosspay(20% = 0.2)
        Standardtax = GrossPay * 0.2
        roundstandardtax = round(Standardtax)
        #print(roundstandardtax)

        # Higher tax calculation 40% of Higherratepay(40% = 0.4)
        Highertax = Higherratepay * 0.4
        if (Highertax < 0):
            raise ValueError("highertax should not be negative")
        #print(Highertax)


        #Total taxt calculation
        Totaltax = roundstandardtax + Highertax
        #print(Totaltax)

        #Nettax calculation
        Nettax = Totaltax - self.__TaxCredit
        #print(Nettax)

        #PRSI Calculation 4% of Grosspay (4% =0.04)
        PRSI = GrossPay * 0.04
        #print(PRSI)

        #Netdeduction calculation
        Netdeduction = Nettax + PRSI
        #print(Netdeduction)

        #Netpay calculation
        if (Netdeduction > 0):
            raise ValueError("netpay should not be negative")
        else:
            NetPay = GrossPay - Netdeduction
        if (Netdeduction < 0):
            raise ValueError("netpay should never exceed grosspay")
        #print(NetPay)

        employeeDict = {
            "name": self.__FirstName + " " + self.__LastName,
            "Date": Date,
            "Hours Worked": HoursWorked,
            "Regular Hours Worked": self.__RegHours,
            "Overtime Hours Worked": Overtimeworked,
            "Regular Rate": self.__HourlyRate,
            "Overtime Rate": Overtimerate,
            "Regular Pay": Regularpay,
            "Overtime Pay": Overtimepay,
            "Gross Pay": GrossPay,
            "Standard Rate Pay": self.__StandardBand,
            "Higher Rate Pay": Higherratepay,
            "Standard Tax": roundstandardtax,
            "Higher Tax": Highertax,
            "Total Tax": Totaltax,
            "Tax Credit": self.__TaxCredit,
            "Net Tax": Nettax,
            "PRSI": PRSI,
            "Net Deductions": Netdeduction,
            "Net Pay": NetPay
        }

        print(employeeDict)

        return employeeDict


#TEST METHODS

class test_employeetestclass(unittest.TestCase):

    # Testing1 = Higher Tax should not be negative.
    def test_highertaxshouldnotbenegative(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 715)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(0, pi["Higher Tax"])

    # Testing2 = Net pay should never exceed Gross Pay
    def test_netpayshouldneverexceedgrosspay(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 550, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])

    # Testing3 =  Net Pay should not be negative
    def test_netpayshouldnotbenegative(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(0, pi["Net Pay"])

    # Testing4 = Overtime pay should not be negative.
    def test_overtimepayshouldnotbenegative(self):
        e = Employee(12345, 'Green', 'Joe', 37, -16, 1.5, 72, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(0, pi["Overtime Pay"])

    # Testing5 = Regular Hours should never exceed hours worked
    def test_regularhoursworkedshouldneverexceedhoursworked(self):
            e = Employee(12345, 'Green', 'Joe', 73, 16, 1.5, 72, 710)
            pi = e.computePayment(42, '31/10/2021')
            self.assertLessEqual(pi["Regular Hours Worked"], pi["Hours Worked"])

unittest.main(argv=['ignored'], exit=False)
