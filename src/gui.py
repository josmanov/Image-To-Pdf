import tkinter as tk
from tkinter.filedialog import askopenfilename
from pathlib import Path

def run_app():
    window = tk.Tk()
    window.title("Image To Searchable PDF")
    window.geometry("500x300")

    selected_path = tk.StringVar(value="No image selected")
    status = tk.StringVar(value="Ready")

    image_exts = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff"}

    def on_select():
        image_path = askopenfilename(
            title="Choose an image", 
            filetypes=[("Image files", "*.png")]
        )
        if not image_path:
            status.set("Not an image file")
            return
        
        if Path(image_path).suffix.lower() not in image_exts:
            status.set("No file selected")
            return
        
        selected_path.set(image_path)
        status.set("Image selected")
        print(image_path)

    text_welcome = "Welcome To Image To Pdf"
    text_help = "Press the button to add your image"
    text_button = "Select"

    text1 = tk.Label(window, text=text_welcome, font=("Arial", 16))
    text2 = tk.Label(window, text=text_help, font=("Arial", 16))
    select_button = tk.Button(window, text=text_button, command=on_select)
    status_label = tk.Label(window, textvariable=status, fg="green")

    text1.pack(pady=20)
    text2.pack(pady=20)
    select_button.pack(pady=20)
    status_label.pack(pady=10)

    window.mainloop()
    return "No errors"