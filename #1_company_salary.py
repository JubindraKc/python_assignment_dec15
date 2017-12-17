salary = [15000, 20000, 17000, 18900, 30000]

new_salary = []

for old_salary in salary:
    new_salary.append(old_salary + old_salary*0.23)

print(new_salary)
