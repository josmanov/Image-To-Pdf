# ImageToPDF

ImageToPDF turns a normal image into a PDF that still looks like the original, but behaves like real text. <br>
You can open the PDF, search it, copy words from it, and share it like any other document.

## Download the Release

If you just want to try it, grab the latest release and open the `ImageToPDF.exe` inside the provided folder. <br>
The app is built as a folder-based Windows release, so the `.exe` should be run from inside that folder, not copied out by itself.

## What It Does

1. Open the app.
2. Choose an image.
3. ImageToPDF creates a PDF in the same folder as the image.

The output PDF keeps the image visually intact, while adding hidden searchable text underneath.

## Why it's useful

The file looks like a plain image, but the PDF engine can still find the words. That means:

- the page looks clean and unchanged
- the text is selectable and searchable
- copied text comes from the image automatically
- the result feels like a smart document, not just a picture

## How It Works

ImageToPDF uses OCR to read the text inside the image, finds the position of each word, and places that text back into the PDF at the same coordinates. The text is rendered invisibly using a PDF text render mode, so the image stays visible while the text layer stays hidden.

In simple terms: the app draws the picture first, then adds invisible words in the right places so the PDF can be searched later.

## Built With

- **Python** - main application language
- **Tkinter** - simple desktop interface
- **Tesseract OCR** - extracts text from images
- **Pillow** - image handling
- **reportlab** - creates the PDF and invisible text layer
- **PyInstaller** - packages the Windows release as a folder with dependencies

## Example

- Input: `invoice.png`
- Output: `invoice.pdf`
- Result: same image appearance, searchable text inside

- If you are using the release build, keep the whole folder together when sharing it.