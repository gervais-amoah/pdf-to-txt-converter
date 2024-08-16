import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PyPDF2 import PdfReader

def select_files_or_folder():
    option = messagebox.askquestion("Sélectionnez une option", "Voulez-vous sélectionner un dossier contenant des PDFs ? Cliquez sur 'Oui'.\nOu sélectionner des fichiers PDF individuels ? Cliquez sur 'Non'.")
    if option == 'yes':
        folder = filedialog.askdirectory()
        if folder:
            pdf_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.pdf')]
            process_files(pdf_files)
    else:
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if files:
            process_files(files)

def process_files(pdf_files):
    for pdf_file in pdf_files:
        txt_file = os.path.splitext(pdf_file)[0] + '.txt'
        try:
            with open(pdf_file, 'rb') as f:
                reader = PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()

            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(f"❌ Impossible de traiter {pdf_file}: {str(e)}")
    messagebox.showinfo("✅ Terminé", "Les fichers PDF ont été convertis en TXT.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("PDF to TXT Converter, by @gev")
    root.geometry("500x300")
    
    btn = tk.Button(root, text="Choisissez les fichiers PDF ou un dossier", command=select_files_or_folder)
    btn.pack(expand=True)
    
    root.mainloop()
