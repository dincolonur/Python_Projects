class QuoteModel:
    """QuoteModel object

    QuoteModel class is used to structure the Meme message.
    It has text and author information.

    """

    def __init__(self, quote, author):
        """Create a new `QuoteModel`.

        :param quote: Text Message, str
        :param author: Author of the Text Message, str
        """
        self._quote = quote
        self._author = author

    @property
    def body(self):
        """Return `self.quote`."""
        return self._quote

    @property
    def author(self):
        """Return `self.author`."""
        return self._author

    def __str__(self):
        """Return `str(self)`."""
        return f"Quote: {self._quote} - Author: {self._author}"
