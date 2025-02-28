#Module_4_Lab_4
#Michele Mora
#2/21/2025
#simulation of monthly sales and according bonuses

#variables

storeBonus = 0 #store bonus amount
employeeAmount = 0 #employee bonus amount
salesIncrease = 0 #sales increase amount
prompt = 0

#monthly sales 
monthlySales = float(input ('Enter monthly sales amount:' ))

#store bonus amount based on monthly sales
if monthlySales >= 110000:
    storeBonus = 6000
elif monthlySales >= 100000:
    storeBonus = 5000
elif monthlySales >=90000:
    storeBonus = 4000
elif monthlySales >= 80000:
    storeBonus = 3000
else:
    storeBonus = 0


#code that gets percent of sales increase
salesIncrease = float(input ('Enter monthly sales increase:' ))
salesIncrease = salesIncrease / 100

#code that determines employee bonuses based on sales increase
if salesIncrease >= .05:
    employeeAmount = 75
elif salesIncrease >= .04:
    employeeAmount = 50
elif salesIncrease >= .03:
    employeeAmount = 40
else:
    employeeAmount = 0


#This code prints the bonus information
print("The store bonus amount is $", storeBonus)
print("The employee bonus amount is $", employeeAmount)
if (storeBonus == 6000) and (employeeAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')
