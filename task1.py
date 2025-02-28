class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: str):
        self._author = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError
        self._pages = value

    def __str__(self):
        return super().__str__() + f". Страниц: {self.pages}"

    def __repr__(self):
        return f"{super().__repr__()}, pages={self.pages!r}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError
        self._duration = float(value)

    def __str__(self):
        return super().__str__() + f". Длительность: {self.duration} часов"

    def __repr__(self):
        return f"{super().__repr__()}, duration={self.duration!r})"