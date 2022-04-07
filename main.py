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

    def computePayment(self, HoursWorked, date):
        #Overtime worked calculation
        Overtimeworked = HoursWorked - self.__RegHours
        print(Overtimeworked)

        Overtimerate = self.__HourlyRate * self.__OTMultiple
        print(Overtimerate)

        Regularpay = self.__RegHours * self.__HourlyRate
        print(Regularpay)

        Overtimepay = Overtimerate * Overtimeworked
        print(Overtimepay)

        GrossPay = Regularpay + Overtimepay
        print(GrossPay)

        Higherratepay = GrossPay - self.__StandardBand
        print(Higherratepay)

        Standardtax = GrossPay * 0.2
        roundstandardtax = round(Standardtax)
        print(roundstandardtax)

        Highertax = Higherratepay * 0.4
        print(Highertax)

        Totaltax = roundstandardtax + Highertax
        print(Totaltax)

        Nettax = Totaltax - self.__TaxCredit
        print(Nettax)

        PRSI = GrossPay * 0.04
        print(PRSI)

        Netdeduction = Nettax + PRSI
        print(Netdeduction)

        NetPay = GrossPay - Netdeduction
        print(NetPay)

e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
e.computePayment(42, '31/10/2022')

#TEST METHODS

class testEmployee(unittest.TestCase):

    # Net pay cannot exceed gross pay
    def testNetpaycannotexceedgrosspay(self):
        e = Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        pi = e.computePayment(42, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])
