def study_plan(risk):

    if risk=="High":

        return """
### 🔴 High Risk Study Plan

• Study 3 hours daily

• Revise previous units

• Complete assignments

• Attend faculty doubt sessions

• Solve previous question papers

• Practice coding every day
"""

    elif risk=="Medium":

        return """
### 🟡 Medium Risk Study Plan

• Study 2 hours daily

• Revise weak subjects

• Complete assignments on time

• Take one mock quiz every week
"""

    else:

        return """
### 🟢 Low Risk Study Plan

• Continue your preparation

• Practice mock tests

• Learn advanced concepts

• Help classmates in group study
"""