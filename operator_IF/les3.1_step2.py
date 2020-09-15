salary = int(input())
tax = 13
if salary > 20000:
    print(salary - (salary * tax) / 100)
else:
    print(salary)
