

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("dataset/employee_data.csv")

# ==========================================
# DISPLAY DATASET
# ==========================================

print("\n========== DATASET PREVIEW ==========\n")
print(df.head())

print("\n========== DATASET INFO ==========\n")
print(df.info())

print("\n========== DESCRIPTIVE STATISTICS ==========\n")
print(df.describe())

# ==========================================
# CHECK MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# ==========================================
# CHECK DUPLICATES
# ==========================================

print("\n========== DUPLICATE RECORDS ==========\n")
print(df.duplicated().sum())

# ==========================================
# DEPARTMENT COUNT
# ==========================================

print("\n========== EMPLOYEES BY DEPARTMENT ==========\n")
print(df['Department'].value_counts())

# ==========================================
# CITY COUNT
# ==========================================

print("\n========== EMPLOYEES BY CITY ==========\n")
print(df['City'].value_counts())

# ==========================================
# HISTOGRAM - SALARY DISTRIBUTION
# ==========================================

plt.figure(figsize=(8,5))
plt.hist(df['Salary'], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.savefig("charts/salary_distribution.png")
plt.show()

# ==========================================
# BAR CHART - DEPARTMENT COUNT
# ==========================================

plt.figure(figsize=(8,5))
df['Department'].value_counts().plot(kind='bar')
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.savefig("charts/department_count.png")
plt.show()

# ==========================================
# SCATTER PLOT - EXPERIENCE VS SALARY
# ==========================================

plt.figure(figsize=(8,5))
sns.scatterplot(x='Experience_Years', y='Salary', data=df)

plt.title("Experience vs Salary")
plt.xlabel("Experience Years")
plt.ylabel("Salary")

plt.savefig("charts/experience_vs_salary.png")
plt.show()

# ==========================================
# CORRELATION MATRIX
# ==========================================

correlation = df.corr(numeric_only=True)

print("\n========== CORRELATION MATRIX ==========\n")
print(correlation)

# ==========================================
# HEATMAP
# ==========================================

plt.figure(figsize=(8,5))

sns.heatmap(correlation, annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.savefig("charts/correlation_heatmap.png")

plt.show()

# ==========================================
# TOP PERFORMERS
# ==========================================

top_performers = df.sort_values(by='Performance_Score', ascending=False)

print("\n========== TOP PERFORMERS ==========\n")
print(top_performers[['Name', 'Department', 'Performance_Score']])

# ==========================================
# AVERAGE SALARY BY DEPARTMENT
# ==========================================

avg_salary = df.groupby('Department')['Salary'].mean()

print("\n========== AVERAGE SALARY BY DEPARTMENT ==========\n")
print(avg_salary)

# ==========================================
# SAVE CLEAN REPORT
# ==========================================

df.to_csv("dataset/final_employee_data.csv", index=False)

print("\n========== TASK COMPLETED SUCCESSFULLY ==========\n")