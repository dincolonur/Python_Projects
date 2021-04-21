from abc import ABC, abstractmethod
from typing import List
from ..QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """IngestInterface Abstarct Class.

    IngestInterface Abstract class has common design
    pattern to structure ingest processes.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Controls input path is ingestable.

        :param path: File path
        :return: Can ingest True of False, boolean
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path) -> List[QuoteModel]:
        """ Parse Abstract Method.

        :param path: File path
        :return: List of structured quotes, List[QuoteModel]
        """
        pass
