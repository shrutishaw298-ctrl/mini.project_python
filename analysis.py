def calculate_metrics(diabetes_df, non_diabetes_df):

    mean_bmi_diabetes = diabetes_df["bmi"].mean()
    mean_bmi_non = non_diabetes_df["bmi"].mean()

    mean_glucose_diabetes = diabetes_df["blood_glucose_level"].mean()
    mean_glucose_non = non_diabetes_df["blood_glucose_level"].mean()

    return (
        mean_bmi_diabetes,
        mean_bmi_non,
        mean_glucose_diabetes,
        mean_glucose_non
    )
def patient_statistics(df):

    total_patients = len(df)

    diabetes_patients = len(df[df["diabetes"] == 1])

    non_diabetes_patients = len(df[df["diabetes"] == 0])

    diabetes_percentage = (diabetes_patients / total_patients) * 100

    non_diabetes_percentage = (non_diabetes_patients / total_patients) * 100

    return (
        total_patients,
        diabetes_patients,
        non_diabetes_patients,
        diabetes_percentage,
        non_diabetes_percentage
    )    