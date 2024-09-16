
from doctr.io import DocumentFile
from doctr.models import ocr_predictor


# Load the OCR model
ocr_model = ocr_predictor(
    "db_resnet50",
    "crnn_mobilenet_v3_large",
    pretrained=True,
    assume_straight_pages=True,
)

def result_to_text(result) -> str:
    full_text = []
    for page in result.pages:
        text = ""
        for block in page.blocks:
            for line in block.lines:
                for word in line.words:
                    text += word.value + " "
            text += "\n"
        full_text.append(text)
    return "\n\n".join(full_text)


def extract_data_from_pdfs(docs, do_ocr=True):
    all_text = ""
    for doc in docs:
        if do_ocr:
            # Convert PDF to DocumentFile for OCR
            pdf_doc = DocumentFile.from_pdf(doc)
            result = ocr_model(pdf_doc)
            all_text += result_to_text(result) + "\n\n"
    return all_text

if __name__ == "__main__":
    # Provide a list of paths to your PDF documents
    pdf_docs = ["story.pdf"]
    text_data = extract_data_from_pdfs(pdf_docs, do_ocr=True)

    print(text_data)