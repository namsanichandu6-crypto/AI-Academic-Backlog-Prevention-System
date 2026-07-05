import os
from reportlab.platypus import SimpleDocTemplate, Paragraph  # type: ignore[import]
from reportlab.lib.styles import getSampleStyleSheet  # type: ignore[import]

def generate_report(name, roll, branch, semester, subject,
                    attendance, assignment, quiz,
                    internal, score, risk):

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    file_path = "reports/Backlog_Report.pdf"

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI-Based Academic Backlog Prevention Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Student Name:</b> {name}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Roll Number:</b> {roll}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Branch:</b> {branch}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Semester:</b> {semester}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Subject:</b> {subject}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Attendance:</b> {attendance}%", styles["BodyText"]))
    story.append(Paragraph(f"<b>Assignment Marks:</b> {assignment}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Quiz Marks:</b> {quiz}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Internal Marks:</b> {internal}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Candidate Score:</b> {score:.2f}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Backlog Risk:</b> {risk}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    if risk == "High":
        recommendation = """
        Study 3 hours daily.<br/>
        Complete assignments on time.<br/>
        Attend doubt sessions.<br/>
        Solve previous question papers.
        """
    elif risk == "Medium":
        recommendation = """
        Study 2 hours daily.<br/>
        Revise weak topics.<br/>
        Practice weekly quizzes.
        """
    else:
        recommendation = """
        Continue current preparation.<br/>
        Practice mock tests.<br/>
        Learn advanced concepts.
        """

    story.append(Paragraph("<b>AI Recommendation</b>", styles["Heading2"]))
    story.append(Paragraph(recommendation, styles["BodyText"]))

    doc.build(story)

    return file_path