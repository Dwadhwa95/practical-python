# mortgage.py
#
# Exercise 1.7

principal = 500000
monthly_payment = 2684.11
months=0
total = 0
extra_payment_start_month = 0
extra_payment_end_month = 0
extra_payment = 0

extra_payment_start_month = input('Please enter extra payment start month:')
#print(extra_payment_start_month)
extra_payment_end_month = input('Please enter extra payment end month:')
#print(extra_payment_end_month)
extra_payment_amount = input('Please enter extra payment amount:')
#print(extra_payment_amount)

while principal >0: 
    if months >= int(extra_payment_start_month) -1 and months < int(extra_payment_end_month) and principal > monthly_payment:
      principal = principal * (1+(0.05/12))
      principal = principal - (monthly_payment + int(extra_payment_amount)) 
      total = total + monthly_payment + int(extra_payment_amount)
      months += 1 
      print(months, ' ', total, ' ', principal)

    elif principal <= monthly_payment:
     
      principal = principal * (1+(0.05/12))
      monthly_payment = principal	
      principal = principal - monthly_payment 
      total = total + monthly_payment
      months = months + 1 
      print(months, ' ', total, ' ', principal)
	
    else:
      principal = principal * (1+(0.05/12))
      principal = principal - monthly_payment 
      total = total + monthly_payment
      months = months + 1 
      print(months, ' ', total, ' ', principal)
    
  
print(total) 
print(months)
