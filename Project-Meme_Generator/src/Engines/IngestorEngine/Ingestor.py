from typing import List
from .IngestorInterface import IngestorInterface
from ..QuoteEngine.QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Ingestor object

    Ingestor class is used for the strategy determination and
    implementation of the ingestion process
    """

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse Method realized from IngestorInterface.

        In this method, file path is checked by its
        file format and parse design is selected.
        Regarding determined parse strategy, parse operation is implemented.
        :param path: File path
        :return: List of structured quotes, List[QuoteModel]
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
