from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def create_math_test(pdf_name):
    # Set up the canvas
    c = canvas.Canvas(pdf_name, pagesize=letter)
    
    # Set margins and font
    margin = 1 * inch
    c.setFont("Helvetica", 12)
    
    # Header
    c.drawString(margin, letter[1] - 1.5*inch, "5th Grade Math Test")
    c.drawString(margin, letter[1] - 2.5*inch, "Instructions: Solve each problem and write your answer in the blank.")
    
    # Start position for questions
    y_pos = letter[1] - 3.5*inch
    
    # List of problems, each is a tuple (number, expression)
    addition = [(i+1, f"{(i+2)*10 + 5} + {(i+3)*10 + 8}") for i in range(10)]
    subtraction = [(i+1, f"{(i+5)*10} - {(i+2)*10}") for i in range(10)]
    
    # Add questions
    sections = [
        ("Addition", addition),
        ("Subtraction", subtraction)
    ]
    
    for section_title, problems in sections:
        c.setFontSize(14)
        c.drawString(margin, y_pos, f"\n{section_title}")
        c.setFontSize(12)
        
        for num, expr in problems:
            question = f"{num}. {expr} = ______"
            c.drawString(margin + 0.5*inch, y_pos, question)
            y_pos -= 0.3 * inch  # Adjust spacing based on font size
    
    # Save the PDF
    c.showPage()
    c.save()

# Usage example:
create_math_test("math_test.pdf")