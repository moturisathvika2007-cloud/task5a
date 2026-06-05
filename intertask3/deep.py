import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# EMPLOYEE DATA
# ==========================================

data = {
    "Employee_ID": ["E101","E102","E103","E104","E105","E106","E107","E108","E109","E110"],
    "Name": ["Rahul","Sneha","Arjun","Priya","Kiran","Meena","Vikas","Anjali","Ramesh","Kavya"],
    "Age": [25,29,31,27,35,24,30,28,32,26],
    "Department": ["Sales","HR","IT","Finance","IT","Sales","HR","Finance","IT","Sales"],
    "Salary": [35000,42000,55000,48000,60000,34000,45000,50000,58000,36000],
    "Experience_Years": [2,4,6,3,8,1,5,4,7,2],
    "Performance_Score": [78,85,90,87,92,68,83,86,89,75],
    "City": ["Hyderabad","Chennai","Bangalore","Mumbai","Delhi",
             "Hyderabad","Pune","Chennai","Bangalore","Pune"]
}

df = pd.DataFrame(data)

# ==========================================
# CREATE DASHBOARD
# ==========================================

fig = plt.figure(figsize=(15,10))
fig.suptitle("Deep Dive Analysis and Interactive Dashboard",
             fontsize=18, fontweight='bold')

# ==========================================
# 1. EMPLOYEES BY DEPARTMENT
# ==========================================

plt.subplot(2,2,1)

dept_count = df["Department"].value_counts()

plt.bar(dept_count.index,
        dept_count.values)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")

# ==========================================
# 2. PERFORMANCE SCORE BY EMPLOYEE
# ==========================================

plt.subplot(2,2,2)

plt.bar(df["Name"],
        df["Performance_Score"])

plt.title("Performance Score by Employee")
plt.xlabel("Employee")
plt.ylabel("Performance Score")

plt.xticks(rotation=45)

# ==========================================
# 3. DEPARTMENT DISTRIBUTION PIE CHART
# ==========================================

plt.subplot(2,2,3)

plt.pie(dept_count.values,
        labels=dept_count.index,
        autopct="%1.1f%%")

plt.title("Employees Distribution by Department")

# ==========================================
# 4. EXPERIENCE VS SALARY
# ==========================================

plt.subplot(2,2,4)

plt.scatter(df["Experience_Years"],
            df["Salary"])

plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

# ==========================================
# SHOW DASHBOARD
# ==========================================

plt.tight_layout()
plt.show()