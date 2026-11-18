import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

def dashboard(total_patients,
              diabetes_patients,
              non_diabetes_patients,
              mean_bmi_diabetes,
              mean_bmi_non,
              mean_glucose_diabetes,
              mean_glucose_non):

    fig = plt.figure(figsize=(16,9))
    fig.suptitle("DIABETES PROGRESSION METRICS",
                 fontsize=20,
                 fontweight="bold")

    # -----------------------
    # Graph 1
    # -----------------------
    plt.subplot(2,2,1)

    sns.barplot(
        x=["Diabetes","Non-Diabetes"],
        y=[diabetes_patients,non_diabetes_patients],
        hue=["Diabetes","Non-Diabetes"],
        palette=["red","dodgerblue"],
        legend=False
    )

    plt.title("Patient Distribution")


    # -----------------------
    # Graph 2
    # -----------------------
    plt.subplot(2,2,2)

    sns.barplot(
        x=["Diabetes","Non-Diabetes"],
        y=[mean_bmi_diabetes,mean_bmi_non],
        hue=["Diabetes","Non-Diabetes"],
        palette=["red","dodgerblue"],
        legend=False
    )

    plt.title("Average BMI")


    # -----------------------
    # Graph 3
    # -----------------------
    plt.subplot(2,2,3)

    sns.barplot(
        x=["Diabetes","Non-Diabetes"],
        y=[mean_glucose_diabetes,mean_glucose_non],
        hue=["Diabetes","Non-Diabetes"],
        palette=["red","dodgerblue"],
        legend=False
    )

    plt.title("Average Blood Glucose")


    # -----------------------
    # Summary Box
    # -----------------------
    plt.subplot(2,2,4)
    plt.axis("off")

    summary = f"""
Total Patients : {total_patients}

Diabetes Patients : {diabetes_patients}

Non-Diabetes Patients : {non_diabetes_patients}

Average BMI (Diabetes) : {mean_bmi_diabetes:.2f}

Average BMI (Non-Diabetes) : {mean_bmi_non:.2f}

Average Glucose (Diabetes) : {mean_glucose_diabetes:.2f}

Average Glucose (Non-Diabetes) : {mean_glucose_non:.2f}
"""

    plt.text(
        0,
        1,
        summary,
        fontsize=12,
        verticalalignment="top",
        bbox=dict(facecolor="lightblue")
    )

    plt.tight_layout()

    plt.show()