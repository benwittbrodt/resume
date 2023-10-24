from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Create a PDF resume
def create_pdf_resume(output_filename, name, contact_info, summary, education, experience):
    # Create a PDF document
    doc = SimpleDocTemplate(output_filename, pagesize=letter)

    # Create a story (list of elements) to add to the PDF
    story = []

    # Set up some basic styles
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']

    # Add name and contact info
    story.append(Paragraph(name, styles['Title']))
    story.append(Paragraph(contact_info, normal_style))

    # Add a summary section
    story.append(Spacer(1, 12))  # Add some space
    story.append(Paragraph("Summary", styles['Heading2']))
    story.append(Paragraph(summary, normal_style))

    # Add an education section
    story.append(Spacer(1, 12))  # Add some space
    story.append(Paragraph("Education", styles['Heading2']))
    for item in education:
        story.append(Paragraph(item, normal_style))

    # Add an experience section
    story.append(Spacer(1, 12))  # Add some space
    story.append(Paragraph("Experience", styles['Heading2']))
    for item in experience:
        story.append(Paragraph(item, normal_style))

    # Build the PDF document
    doc.build(story)

if __name__ == '__main__':
    output_filename = 'my_resume.pdf'
    name = "John Doe"
    contact_info = "Email: john.doe@example.com | Phone: (123) 456-7890"
    summary = "A highly motivated and experienced professional with a strong background in Python programming."
    education = [
        "Bachelor of Science in Computer Science, University of XYZ, 2015",
        "Master of Science in Software Engineering, ABC University, 2017",
    ]
    experience = [
        "Software Developer, XYZ Corporation, 2017 - Present",
        "Intern, ABC Tech, 2016",
    ]

    create_pdf_resume(output_filename, name, contact_info, summary, education, experience)
