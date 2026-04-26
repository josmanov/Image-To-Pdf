import tkinter as tk
from tkinter.filedialog import askopenfilename
from pathlib import Path

def on_select():
    image_path = askopenfilename(
        title="Choose an image", 
        filetypes=[("Image files", "*.png")]
    )
    if not image_path:
        print("No file selected")
        return
    
    if Path(image_path).suffix.lower() not in {
         ".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff"}:
            print ("Not an image file")
            return
    
    print(image_path)

def run_app():
    window = tk.Tk()
    window.title("Image To Searchable PDF")
    window.geometry("500x300")

    text_welcome = "Welcome To Image To Pdf"
    text_instruction = "Press the button to add your image"
    text1 = tk.Label(window, text=text_welcome, font=("Arial", 16))
    text2 = tk.Label(window, text=text_instruction, font=("Arial", 16))

    text_button = "Select"
    select_button = tk.Button(window, text=text_button, command=on_select)
    
    text1.pack(pady=20)
    text2.pack(pady=20)
    select_button.pack(pady=20)

    window.mainloop()
    return "No errors"