from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.image.barcode import Barcode, BarcodeType
from decimal import Decimal


def main1(link="1234567890"):
    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add a Paragraph
    layout.add(
    Paragraph(
        """



                Please scan below QR code for your Food Menu



        """,  font_size=Decimal(21)
    )
)

    layout.add(
        Barcode(
            link,
            width=Decimal(256),
            height=Decimal(256),
            type=BarcodeType.QR))
    layout.add(
    Paragraph(
        """
                        Bon Appétit

        """,  font_size=Decimal(21)
    )
)

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main1(link)
