# Afshin Masoudi
# CS50p/Problem Set 8/CS50 Shirtificate
# input : John Harvard
from fpdf import FPDF

fullname_png = "./shirtificate.png"
fullname_pdf = "./shirtificate.pdf"
text= "CS50 Shirtificate"

class CS50Shirtificate():
    def __init__(self, name):
        self.name = name
        self.shirtificate()

    def shirtificate(self):
        # create a PDF
        pdf = FPDF(orientation="portrait", format="A4", unit= "mm")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        # add the text at the top of the page
        pdf.set_font("helvetica", size=48)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 60, border=0, align="C", txt= text)
        pdf.ln()

        # add shirt image
        pdf.image(
            fullname_png,
            x=15,
            y=(297 / 4),
            w=180,
            alt_text=f"The words: {self.name} took CS50",
        )

        # add the text on top of the shirt
        pdf.set_font("helvetica", size=22)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 130, border=0, align="C", txt=f"{self.name} took CS50")

        # Save the the image as a PDF
        pdf.output(fullname_pdf)

    @classmethod
    def get(cls):
        name = input("Name: ").strip().title()
        return cls(name)

def main():
    CS50Shirtificate.get()

if __name__ == "__main__":
    main()