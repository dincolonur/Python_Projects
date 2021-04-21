from .IngestorInterface import IngestorInterface
from ..QuoteEngine.QuoteModel import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    """TextIngestor object

    TextIngestor class is used to ingest PDF file format files.
    """

    allowed_extensions = ['txt']

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Controls input path is ingestable.

        :param path: TXT File path
        :return: Can ingest True of False, boolean
        """
        ext = path.split('.')[-1]
        if ext in cls.allowed_extensions:
            return True
        return False

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """ Parse Method realized from IngestorInterface

        :param path: TXT File path
        :return: List of structured quotes, List[QuoteModel]
        """
        quotes = []

        try:
            with open(path, mode="r") as data:
                lines = data.readlines()

            content = [line.strip('\n') for line in lines]

            for item in content:
                parse = item.split('-')
                quote = QuoteModel(parse[0].strip(), parse[1].strip())
                quotes.append(quote)
        except IOError as e:
            print("I/O error while reading TXT file")
        except Exception as e:
            print("Unexpected error")

        return quotes
