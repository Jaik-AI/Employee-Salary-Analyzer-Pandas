import pandas as pd
# ₹
df = pd.read_csv("employees.csv")
print("\n========== EMPLOYEE DATASET ==========\n")
print(df)

print("\n=== HIGHEST PAID EMPLOYEE ===\n")
highest_paid = df['Salary'].idxmax()
print(f"Name       : {df.loc[highest_paid,'Name']}\nDepartment : {df.loc[highest_paid,'Department']}\nSalary     : ₹{df.loc[highest_paid,'Salary']:,}\nExperience : {df.loc[highest_paid,'Experience']} years\nAge        : {df.loc[highest_paid,'Age']} ")

print("\n=== LOWEST PAID EMPLOYEE ===\n")
lowest_paid = df['Salary'].idxmin()
print(f"Name       : {df.loc[lowest_paid,'Name']}\nDepartment : {df.loc[lowest_paid,'Department']}\nSalary     : ₹{df.loc[lowest_paid,'Salary']:,}\nExperience : {df.loc[lowest_paid,'Experience']} years\nAge        : {df.loc[lowest_paid,'Age']} ")

print("\n=== AVERAGE SALARY BY DEPARTMENT ===\n")
avg_sal_dep = df.groupby('Department')['Salary'].mean()
for dep,sal in avg_sal_dep.items():
    print(f"{dep:<9} : ₹{sal:,.2f}")

print("\n===  EMPLOYEES IN EACH DEPARTMENT ===\n")
emp_count = df['Department'].value_counts()
for dep,emp in emp_count.items():
    print(f"{dep:<9} : {emp} employees")

print("\n=== HIGHEST SALARY ===\n")
print(f"₹{df['Salary'].max():,}")

print("\n=== LOWEST SALARY ===\n")
print(f"₹{df['Salary'].min():,}")

print("\n=== AVERAGE AGE ===\n")
print(f"{df['Age'].mean():.2f} Years")

print("\n===  MOST EXPERIENCED EMPLOYEE ===\n")
most_exp = df['Experience'].idxmax()
print(f"Name       : {df.loc[most_exp,'Name']}\nExperience : {df.loc[most_exp,'Experience']} Years\nDepartment : {df.loc[most_exp,'Department']}")

print("\n=== YOUNGEST EMPLOYEE ===\n")
young_emp = df['Age'].idxmin()
print(f"Name       : {df.loc[young_emp,'Name']}\nAge        : {df.loc[young_emp,'Age']} Years\nDepartment : {df.loc[young_emp,'Department']}")

print("\n=== OLDEST EMPLOYEE ===\n")
old_emp = df['Age'].idxmax()
print(f"Name       : {df.loc[old_emp,'Name']}\nAge        : {df.loc[old_emp,'Age']} Years\nDepartment : {df.loc[old_emp,'Department']}")

print("\n=== EMPLOYEES ABOVE AVERAGE SALARY ===\n")
avg_salary = df['Salary'].mean()
print(f"\nAverage Salary : ₹{avg_salary:,.2f}\n")
above_avg_sal = df[df['Salary']>avg_salary].index
for i in above_avg_sal:
    print(f"{df.loc[i,'Name']:<6} | {df.loc[i,'Department']:<9} | ₹{df.loc[i,'Salary']:,}")

print("\n=== EXPERIENCED EMPLOYEES  ===\n")
more_5_exp = df[df['Experience']>5].index
for i in more_5_exp:
    print(f"{df.loc[i,'Name']:<6} | {df.loc[i,'Department']:<9} | {df.loc[i,'Experience']} Years")

print("\n=== TOP 3 HIGHEST PAID EMPLOYEES  ===\n")
top_3 = df.sort_values('Salary',ascending=False).head(3)
for i,(_,row) in enumerate(top_3.iterrows(),start=1):
    print(f"{i}. {row['Name']}")
    print(f"   Department : {row['Department']}")
    print(f"   Salary     : ₹{row['Salary']:,}")
    print(f"   Experience : {row['Experience']} Years\n")

print("\n=== DEPARTMENT WITH HIGHEST AVERAGE SALARY  ===\n")
high_dept_sal = df.groupby('Department')['Salary'].mean()
print(f"Department     : {high_dept_sal.idxmax()}\nAverage Salary : ₹{high_dept_sal.max():,.2f}")

print("="*40)
print("\tEMPLOYEE ANALYSIS REPORT")
print("="*40)
print()
print(f"Total Employees                    : {len(df)}\n")
print(f"Highest Paid Employee              : {df.loc[highest_paid,'Name']}\n")
print(f"Highest Salary                     : ₹{df['Salary'].max():,}\n")
print(f"Lowest Salary                      : ₹{df['Salary'].min():,}\n")
print(f"Average Salary                     : ₹{df['Salary'].mean():,.2f}\n")
print(f"Average Age                        : {df['Age'].mean():.2f} Years\n")
print(f"Department with the highest salary : {high_dept_sal.idxmax()}\n")
print(f"Most Experienced Employee          : {df.loc[most_exp,'Name']}\n")
