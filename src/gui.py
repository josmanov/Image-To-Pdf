import tkinter as tk
from tkinter.filedialog import askopenfilename
from pathlib import Path
import sys
import os

import constants as consts
from status import Status, ErrorStatus
from ocr import extract_text_data
from pdf_writer import image_to_pdf

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

def run_app():
    window = tk.Tk()
    window.title(consts.APP_TITLE)
    window.iconbitmap(os.path.join(base_path, "icon.ico"))

    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()
    width = consts.WINDOW_WIDTH
    height = consts.WINDOW_HEIGHT
    x = (screen_w - width) // 2
    y = (screen_h - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

    selected_path = tk.StringVar(value=ErrorStatus.NO_FILE.value)
    status = tk.StringVar(value=Status.READY.value)
    status_color = "gray"

    def on_select():
        image_path = askopenfilename(
            title="Choose an image", 
            filetypes=[("Image files", "*.png")]
        )
        if not image_path:
            status.set(ErrorStatus.NO_FILE.value)
            text_status.config(fg="red")
            return
        
        if Path(image_path).suffix.lower() not in consts.IMAGE_EXTS:
            status.set(ErrorStatus.NOT_IMAGE.value)
            text_status.config(fg="red")
            return
        
        selected_path.set(image_path)
        status.set(Status.IMAGE_SELECTED.value)
        text_status.config(fg="green")

        try:
            words = extract_text_data(image_path)
            image_to_pdf(image_path, words, None, False)
            status.set("PDF has been created")
            text_status.config(fg="green")
        except Exception:
            status.set("PDF creation failed")
            text_status.config(fg="red")

    text_welcome = tk.Label(window, text=consts.TEXT_WELCOME, font=("Arial", 16))
    text_help = tk.Label(window, text=consts.TEXT_HELP, font=("Arial", 10))
    select_button = tk.Button(window, text=consts.TEXT_SELECT_BUTTON, command=on_select)
    text_status = tk.Label(window, textvariable=status, fg=status_color)

    text_welcome.pack(pady=20)
    text_help.pack(pady=20)
    select_button.pack(pady=20)
    text_status.pack(pady=10)

    window.mainloop()
    return status.get()