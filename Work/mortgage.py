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
extra_payment_end_month = input('Please enter extra payment end month:')
extra_payment = input('Please enter extra payment amount:')

while principal >0: 
    if months >= extra_payment_start month and months < extra_payment_end_month + 1:
      principal = principal * (1+(0.05/12))
      principal = principal - (monthly_payment + extra_payment) 
      total = total + monthly_payment + extra_payment
      months = months + 1 
    else:
      principal = principal * (1+(0.05/12))
      principal = principal - monthly_payment 
      total = total + monthly_payment
      months = months + 1 
    
  
print(total) 
print(months)
