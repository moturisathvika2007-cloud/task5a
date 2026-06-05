import pandas as pd

# Create Dataset
data = {
    "Employee_ID": ["E101", "E102", "E103", "E104", "E105",
                    "E106", "E107", "E108", "E109", "E110"],

    "Name": ["Rahul", "Sneha", "Arjun", "Priya", "Kiran",
             "Meena", "Vikas", "Anjali", "Ramesh", "Kavya"],

    "Age": [25, 29, 31, 27, 35, 24, 30, 28, 32, 26],

    "Department": ["Sales", "HR", "IT", "Finance", "IT",
                   "Sales", "HR", "Finance", "IT", "Sales"],

    "Salary": [35000, 42000, 55000, 48000, 62000,
               34000, 45000, 50000, 58000, 36000],

    "Experience_Years": [2, 4, 6, 3, 8, 1, 5, 4, 7, 2],

    "Performance_Score": [78, 85, 90, 88, 92,
                          70, 86, 89, 91, 75],

    "City": ["Hyderabad", "Chennai", "Bangalore", "Mumbai", "Pune",
             "Hyderabad", "Delhi", "Chennai", "Bangalore", "Pune"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Employee Dataset")
print(df)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Save Cleaned Dataset
df.to_csv("cleaned_employee_dataset.csv", index=False)

print("\nData Wrangling Completed Successfully")