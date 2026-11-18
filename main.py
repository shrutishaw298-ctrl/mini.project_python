from cleaning import clean_data
from analysis import calculate_metrics, patient_statistics
from visualization import dashboard

print("=" * 60)
print("        DIABETES PROGRESSION METRICS PROJECT")
print("=" * 60)

# Step 1: Load and clean dataset
df = clean_data()

# Step 2: Separate diabetes and non-diabetes patients
diabetes_df = df[df["diabetes"] == 1]
non_diabetes_df = df[df["diabetes"] == 0]

# Step 3: Calculate patient statistics
(
    total_patients,
    diabetes_patients,
    non_diabetes_patients,
    diabetes_percentage,
    non_diabetes_percentage
) = patient_statistics(df)

# Step 4: Print statistics
print("\nPatient Statistics")
print("-" * 30)
print(f"Total Patients        : {total_patients}")
print(f"Diabetes Patients     : {diabetes_patients}")
print(f"Non-Diabetes Patients : {non_diabetes_patients}")
print(f"Diabetes Percentage   : {diabetes_percentage:.2f}%")
print(f"Non-Diabetes Percentage : {non_diabetes_percentage:.2f}%")

# Step 5: Calculate BMI and Blood Glucose metrics
(
    mean_bmi_diabetes,
    mean_bmi_non,
    mean_glucose_diabetes,
    mean_glucose_non
) = calculate_metrics(diabetes_df, non_diabetes_df)

# Step 6: Print metrics
print("\nAverage BMI")
print("-" * 30)
print(f"Diabetes Patients     : {mean_bmi_diabetes:.2f}")
print(f"Non-Diabetes Patients : {mean_bmi_non:.2f}")

print("\nAverage Blood Glucose Level")
print("-" * 30)
print(f"Diabetes Patients     : {mean_glucose_diabetes:.2f}")
print(f"Non-Diabetes Patients : {mean_glucose_non:.2f}")

# Step 7: Show Graphs
dashboard(
    total_patients,
    diabetes_patients,
    non_diabetes_patients,
    mean_bmi_diabetes,
    mean_bmi_non,
    mean_glucose_diabetes,
    mean_glucose_non
)

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)

print("1. Diabetic patients have a higher average BMI than non-diabetic patients.")
print("2. Diabetic patients have a higher average blood glucose level.")
print("3. BMI and Blood Glucose Level are important indicators associated with diabetes.")

print("\nProject Completed Successfully!")