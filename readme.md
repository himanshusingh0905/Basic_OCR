This script is a simple tool for extracting text from PDF documents using Optical Character Recognition (OCR) with the Doctr library. It uses a pre-trained OCR model to automatically scan and pull text from PDFs, making it super easy to get the content in a readable format.

What Does It Do?
1. Loads an OCR Model: We’re using a combo of db_resnet50 (for detecting text) and crnn_mobilenet_v3_large (for recognizing it) – both pre-trained and ready to go!

2. Processes PDFs: You can feed the script one or more PDFs, and it’ll handle them for you, converting each into a format suitable for OCR.

3. Extracts Text: The script goes through each page, block, line, and word to create a plain-text version of the content. Perfect for scanned PDFs or image-heavy docs!

4. Batch Processing: Got multiple PDFs? No problem – just pass them all in, and the script will handle each one.

5. How to Use:
* Install the required packages (like doctr).
* Add your PDF file paths to the pdf_docs list.
* Run the script, and it’ll print out all the extracted text from the PDFs. Easy as that