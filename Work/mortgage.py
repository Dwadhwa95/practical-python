# mortgage.py
#
# Exercise 1.7
principal = 500000
monthly_payment = 2684.11
month = 0
total = 0

while principal >0: 
  principal = principal*(1+(0.05/12))
  principal = principal - monthly_payment 
  total = total + 2684.11
  
print(total) 
