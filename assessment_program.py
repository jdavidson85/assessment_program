old = int(input("How old are you currently?"))
retire_age = int(input("At what age you want to retire?"))
yearly_income = int(input("What is your yearly income?"))
save = int(input("What percentage of your income do you save?"))
saving = int(input("How much money do you currently have in saving?"))
year = 0

if retire_age > old:
    a = retire_age - old
    print("Year\tIncome\tSaving Contribution\tTotal Saving")

    while year < a:
        saving_contribution = int((yearly_income*save/100))
        rising = int((saving*.06))
        total_Saving = int((saving_contribution+saving+rising))
        print(year + 1, "\t\t", yearly_income, "\t\t", saving_contribution, "\t\t", total_Saving)
        increase_salary = int((yearly_income + (yearly_income * .03)))
        yearly_income = int(increase_salary)
        saving = int(total_Saving)
        year = year + 1

else:
    print("invalid numbers")
