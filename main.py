import PyPDF2
from pathlib import Path
import os
from tkinter import filedialog, Tk

def unir_pdf(lista_pdf: tuple) -> None:
    """
    Unir múltiples archivos PDF en un solo archivo PDF.

    Args:
        lista_pdf (tuple): Una tupla que contiene las rutas de los archivos PDF a unir.
    """
    pdf_merger = PyPDF2.PdfMerger()
    for filename in lista_pdf:
        with open(filename, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_merger.append(pdf_reader)

    resultado = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        confirmoverwrite=True,
        filetypes=[("Archivos PDF", "*.pdf")],
        initialdir=Path.home() / "Escritorio",
    )

    if resultado:
        with open(resultado, "wb") as output_pdf:
            pdf_merger.write(output_pdf)
        try:
            os.startfile(resultado)
        except Exception as e:
            print(f"No se pudo abrir el archivo: {e}")

def main() -> None:
    """
    Función principal para seleccionar archivos PDF y unirlos.
    """
    # Ocultar la ventana raíz de Tkinter
    root = Tk()
    root.withdraw()

    filenames = filedialog.askopenfilenames(
        filetypes=[("Archivos PDF", "*.pdf")],
        initialdir=Path.home() / "Downloads"
    )
    if filenames:
        unir_pdf(filenames)

if __name__ == "__main__":
    main()