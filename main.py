import PyPDF2
from pathlib import Path
import os
from tkinter import filedialog


def unir_pdf(lista_pdf: tuple) -> None: 
    pdf_merge = PyPDF2.PdfMerger()
    for filename in lista_pdf:
        with open(filename, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_merge.append(pdf_reader)

    resultado = filedialog.asksaveasfilename(
        defaultextension="pdf",
        confirmoverwrite=True,
        filetypes=[('PDF files', '*.pdf')],
        initialdir=Path.home() / "Escritorio",
        )
    
    if resultado:
        pdf_merge.write(resultado)    
        try:
            os.startfile(resultado)    
        except:
            pass

 
def main() -> None:
    filenames = filedialog.askopenfilenames(
        filetypes=[('PDF files', '*.pdf')],
        initialdir=Path.home() / "Downloads"                 
        )
    if filenames:
        unir_pdf(filenames)
        
if __name__ == "__main__":
    main()