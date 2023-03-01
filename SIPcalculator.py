amount = float(input("Enter the monthly SIP amount: "))
years = int(input("Enter the number of years: "))
yearlyRate = float(input("Enter the yearly rate 1st of return: "))
# yearlyRate2 = float(input("Enter the yearly rate 2nd of return: "))
# yearlyRate3 = float(input("Enter the yearly rate 3rd of return: "))
yearlyRate2=yearlyRate+5
yearlyRate3=yearlyRate2+5

mx=amount/100
amount1=mx*65
amount2=mx*20
amount3=mx*15
total=int(amount*(years*12))

monthlyRate = yearlyRate/12/100
months = years * 12
futureValue = amount1 * ((((1 + monthlyRate)**(months))-1) * (1 + monthlyRate))/monthlyRate
futureValue = round(futureValue)

monthlyRate2 = yearlyRate2/12/100
months2 = years * 12
futureValue2 = amount2 * ((((1 + monthlyRate2)**(months2))-1) * (1 + monthlyRate2))/monthlyRate2
futureValue2 = round(futureValue2)


monthlyRate3 = yearlyRate3/12/100
months3 = years * 12
futureValue3 = amount3 * ((((1 + monthlyRate3)**(months3))-1) * (1 + monthlyRate3))/monthlyRate3
futureValue3 = round(futureValue3)
print("Total investment is:",total)
print('------------larg cab mutual fund----------------')
print("The 1st expected amount you will get is:",futureValue," 65%")
print('--------------mid cab mutual fund---------')
print("The 2nd expected amount you will get is:",futureValue2, " 20%")
print('--------------smoll cab mutual fund---------')
print("The 3rd expected amount you will get is:",futureValue3, " 15%")
print('------------Total mutual fund return----------------')
print("The final expected amount you will get total is:",futureValue2+futureValue3+futureValue, " 100%")
