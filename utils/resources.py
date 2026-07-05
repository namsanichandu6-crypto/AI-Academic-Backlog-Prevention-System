import streamlit as st


def app():
    risk = ""

    st.title("AI-Based Academic Backlog Prevention System")
    st.write("Predict backlog risk based on attendance and academic performance.")

    student_name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")

    branch = st.selectbox(
        "Branch",
        [
            "Computer Science",
            "Information Technology",
            "Electronics",
            "Mechanical",
            "Civil"
        ]
    )

    semester = st.selectbox("Semester", [1, 2, 3, 4, 5, 6, 7, 8])
    subject = st.text_input("Subject")

    attendance = st.number_input("Attendance (%)", 0, 100)
    assignment_marks = st.number_input("Assignment Marks", 0, 100)
    quiz_marks = st.number_input("Quiz Marks", 0, 100)
    internal_marks = st.number_input("Internal Marks", 0, 100)

    if st.button("Predict Backlog"):
        if attendance < 75 or internal_marks < 40:
            risk = "High"
        elif attendance < 85:
            risk = "Medium"
        else:
            risk = "Low"

        st.success("Student details submitted successfully!")

        if risk == "High":
            st.error("🔴 High Risk of Backlog")
        elif risk == "Medium":
            st.warning("🟡 Medium Risk of Backlog")
        else:
            st.success("🟢 Low Risk of Backlog")
            score = (
                attendance + assignment_marks + quiz_marks + internal_marks
            ) / 4
            st.metric("Candidate Score", f"{score:.2f}")

            if score < 50:
                st.write(
                    "Study Plan\n\n"
                    "• Study 3 hours daily\n"
                    "• Revise previous units\n"
                    "• Practice important questions\n"
                    "• Meet faculty weekly\n"
                )
            elif score < 75:
                st.write(
                    "Study Plan\n\n"
                    "• Study 2 hours daily\n"
                    "• Complete assignments\n"
                    "• Take weekly quizzes\n"
                )
            else:
                st.write(
                    "Study Plan\n\n"
                    "• Continue current preparation\n"
                    "• Practice mock tests\n"
                )

        st.subheader("Learning Resources")
        st.write("• NPTEL")
        st.write("• GeeksforGeeks")
        st.write("• Microsoft Learn")
        st.write("• Coursera")
        st.write("• YouTube")


if __name__ == "__main__":
    app()
def study_plan(risk):

    if risk == "High":

        return """
Study Plan

• Study 3 hours daily

• Revise previous topics

• Complete all assignments

• Attend doubt sessions

• Practice previous papers
"""

    elif risk == "Medium":

        return """
Study Plan

• Study 2 hours daily

• Revise weak topics

• Take one quiz every week
"""

    else:

        return """
Study Plan

• Continue your current preparation

• Practice mock tests
"""