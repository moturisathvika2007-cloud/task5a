import pandas as pd
import matplotlib.pyplot as plt

# Employee Data
data = {
    'Employee': ['Rahul', 'Sneha', 'Arjun', 'Priya', 'Kiran',
                 'Meena', 'Vikas', 'Anjali', 'Ramesh', 'Kavya'],
    'Department': ['Sales', 'HR', 'IT', 'Finance', 'IT',
                   'HR', 'Sales', 'Finance', 'IT', 'Sales'],
    'Salary': [35000, 42000, 55000, 45000, 60000,
               48000, 50000, 58000, 62000, 36000],
    'Experience_Years': [2, 4, 6, 5, 8,
                         3, 4, 7, 8, 2],
    'Performance_Score': [78, 85, 90, 88, 92,
                          70, 86, 90, 91, 75]
}

df = pd.DataFrame(data)

# Department Counts
dept_counts = df['Department'].value_counts()

# Create Dashboard
fig, axs = plt.subplots(2, 2, figsize=(14, 8))
fig.suptitle('Data Story Telling and Statistical Validation',
             fontsize=16, fontweight='bold')

# -------------------------------
# 1. Employees by Department
# -------------------------------
axs[0, 0].bar(dept_counts.index, dept_counts.values)
axs[0, 0].set_title('Employees by Department')
axs[0, 0].set_xlabel('Department')
axs[0, 0].set_ylabel('Count')

# -------------------------------
# 2. Performance Score by Employee
# -------------------------------
axs[0, 1].bar(df['Employee'], df['Performance_Score'])
axs[0, 1].set_title('Performance Score by Employee')
axs[0, 1].set_xlabel('Employee')
axs[0, 1].set_ylabel('Performance Score')
axs[0, 1].tick_params(axis='x', rotation=45)

# -------------------------------
# 3. Employees Distribution Pie Chart
# -------------------------------
axs[1, 0].pie(
    dept_counts.values,
    labels=dept_counts.index,
    autopct='%1.1f%%'
)
axs[1, 0].set_title('Employees Distribution by Department')

# -------------------------------
# 4. Experience vs Salary
# -------------------------------
axs[1, 1].scatter(
    df['Experience_Years'],
    df['Salary']
)
axs[1, 1].set_title('Experience vs Salary')
axs[1, 1].set_xlabel('Experience (Years)')
axs[1, 1].set_ylabel('Salary')

# -------------------------------
# Insights Text
# -------------------------------
fig.text(
    0.15, 0.52,
    'HR and Finance departments have smaller teams (20% each).',
    fontsize=9
)

fig.text(
    0.62, 0.52,
    'Most employees score above 80, indicating strong overall performance.',
    fontsize=9
)

fig.text(
    0.15, 0.04,
    'Workforce distribution is relatively balanced.',
    fontsize=9
)

fig.text(
    0.62, 0.04,
    'Strong positive correlation exists between experience and salary.',
    fontsize=9
)

plt.tight_layout()
plt.show()