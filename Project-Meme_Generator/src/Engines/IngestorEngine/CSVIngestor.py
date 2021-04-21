import pandas
from typing import List
from .IngestorInterface import IngestorInterface
from ..QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSVIngestor object

    CSVIngestor class is used to ingest CSV file format files.
    """

    allowed_extensions = ['csv']

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Controls input path is ingestable.

        :param path: CSV File path
        :return: Can ingest True of False, boolean
        """
        ext = path.split('.')[-1]
        if ext in cls.allowed_extensions:
            return True
        return False

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """ Parse Method realized from IngestorInterface

        :param path: CSV File path
        :return: List of structured quotes, List[QuoteModel]
        """
        quotes = []
        try:
            df = pandas.read_csv(path, header=0)

            for index, row in df.iterrows():
                quote = QuoteModel(row['body'], row['author'])
                quotes.append(quote)
        except IOError as e:
            print("I/O error while reading CSV file")
        except Exception as e:
            print("Unexpected error")
        return quotes
