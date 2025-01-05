total = 0
for i in range(1,6):
    total = total+i
    print(total)
print(f'Sum of numbers from 1 to 5 : {total}')
# x = 0+1 
# x = 1+2
# x = 3+3
# x = 6+4
# x = 10+5
# x = 15+6
# % = residual
for i in range(9):
    if i %2 == 0:
        print(f'{i} in odd')

initial_balance = 1000
anual_deposit = 500
interest_rate = 0.05
years = 5
balance = initial_balance
for year in range(1,years+1):
    balance += anual_deposit
    balance *= 1+interest_rate
    print(f'Balance ${balance:.2f}')

counter = 5
while counter >= 0:
    print(f'Count : {counter}')
    counter = counter-1
# input เก็บตัวแปรในรูป string

#if break
for i in range(10):
    if i == 5:
        break
    print(i)
