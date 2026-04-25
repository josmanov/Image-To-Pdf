import tkinter as tk

def run_app():
    window = tk.Tk()
    window.title("Image To Searchable PDF")
    window.geometry("500x300")

    text_welcome = "Welcome To Image To Pdf"
    text_instruction = "Press the button to add your image"
    text1 = tk.Label(window, text=text_welcome, font=("Arial", 16))
    text2 = tk.Label(window, text=text_instruction, font=("Arial", 16))

    text_button = "Select"
    select_button = tk.Button(window, text=text_button,)
    
    text1.pack(pady=20)
    text2.pack(pady=20)
    select_button.pack(pady=20)

    window.mainloop()
    return "yes it works"