# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
  extra = extra_payment if (extra_payment_start_month <= month <= extra_payment_end_month) else 0
  payment = 2684.11 + extra
  if ((principal * (1+rate/12) - payment) < 0):
    payment = principal * (1+rate/12)

  principal = principal * (1+rate/12) - payment
  total_paid = total_paid + payment
  print(f'{month:d} {total_paid:.2f} {principal:.2f}')
  month += 1

print(f'Total paid {total_paid}')
print(f'Months {month-1:d}')

