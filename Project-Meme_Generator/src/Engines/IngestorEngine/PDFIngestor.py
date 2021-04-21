import subprocess
import os
import random
from typing import List
from .IngestorInterface import IngestorInterface
from ..QuoteEngine.QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDFIngestor object

    PDFIngestor class is used to ingest PDF file format files.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Controls input path is ingestable.

        :param path: PDF File path
        :return: Can ingest True of False, boolean
        """
        ext = path.split('.')[-1]
        if ext in cls.allowed_extensions:
            return True
        return False

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """ Parse Method realized from IngestorInterface.

        :param path: PDF File path
        :return: List of structured quotes, List[QuoteModel]
        """
        quotes = []
        try:
            tmp = f'./tmp/{random.randint(0,100000000)}.txt'
            subprocess.call(['pdftotext', '-layout', path, tmp])

            file_ref = open(tmp, "r")

            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0].strip(), parse[1].strip())
                    quotes.append(quote)

            file_ref.close()
            os.remove(tmp)
        except IOError as e:
            print("I/O error while reading PDF file")
        except Exception as e:
            print("Unexpected error")
        return quotes
