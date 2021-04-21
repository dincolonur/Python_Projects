import docx
from typing import List
from .IngestorInterface import IngestorInterface
from ..QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """DocxIngestor object

    DocxIngestor class is used to ingest DOCX file format files.
    """

    allowed_extensions = ['docx']

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Controls input path is ingestable.

        :param path: DOCX File path
        :return: Can ingest True of False, boolean
        """
        ext = path.split('.')[-1]
        if ext in cls.allowed_extensions:
            return True
        return False

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """ Parse Method realized from IngestorInterface

        :param path: DOCX File path
        :return: List of structured quotes, List[QuoteModel]
        """
        quotes = []

        try:
            doc = docx.Document(path)

            for para in doc.paragraphs:
                if para.text != "":
                    parse = para.text.split('-')
                    quote = QuoteModel(parse[0].strip(), parse[1].strip())
                    quotes.append(quote)
        except IOError as e:
            print("I/O error while reading DOCX file")
        except Exception as e:
            print("Unexpected error")

        return quotes
