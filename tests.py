import pytest
from main import BooksCollector

@pytest.fixture
def setup_books_collector():
    collector = BooksCollector()
    collector.add_new_book("Книга1")
    collector.add_new_book("Книга2")
    collector.set_book_genre("Книга1", "Фантастика")
    collector.set_book_genre("Книга2", "Детективы")
    return collector

class TestBooksCollector:

    def test_add_new_book_success(self, setup_books_collector):
        collector = setup_books_collector
        collector.add_new_book("Новая Книга")
        assert "Новая Книга" in collector.get_books_genre()

    def test_add_new_book_duplicate(self, setup_books_collector):
        collector = setup_books_collector
        collector.add_new_book("Книга1")
        assert len(collector.get_books_genre()) == 2  # No duplicate added

    def test_add_new_book_name_too_long(self, setup_books_collector):
        collector = setup_books_collector
        long_name = "а" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    @pytest.mark.parametrize("book_name,genre,expected_genre", [
        ("Книга1", "Ужасы", "Ужасы"),
        ("Книга2", "Роман", "Детективы"),
        ("Несуществующая Книга", "Фантастика", None)
    ])
    def test_set_book_genre(self, setup_books_collector, book_name, genre, expected_genre):
        collector = setup_books_collector
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize("book_name,expected_genre", [
        ("Книга1", "Фантастика"),
        ("Книга3", None)
    ])
    def test_get_book_genre(self, setup_books_collector, book_name, expected_genre):
        collector = setup_books_collector
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize("genre,expected_books", [
        ("Фантастика", ["Книга1"]),
        ("Детективы", ["Книга2"]),
        ("Ужасы", [])
    ])
    def test_get_books_with_specific_genre(self, setup_books_collector, genre, expected_books):
        collector = setup_books_collector
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre(self, setup_books_collector):
        collector = setup_books_collector
        books_genre = collector.get_books_genre()
        assert "Книга1" in books_genre
        assert "Книга2" in books_genre

    def test_get_books_for_children(self, setup_books_collector):
        collector = setup_books_collector
        assert collector.get_books_for_children() == ["Книга1"]

    def test_add_book_in_favorites_success(self, setup_books_collector):
        collector = setup_books_collector
        collector.add_book_in_favorites("Книга1")
        assert "Книга1" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent_book(self, setup_books_collector):
        collector = setup_books_collector
        collector.add_book_in_favorites("Несуществующая Книга")
        assert "Несуществующая Книга" not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self, setup_books_collector):
        collector = setup_books_collector
        collector.add_book_in_favorites("Книга1")
        collector.add_book_in_favorites("Книга1")
        assert collector.get_list_of_favorites_books().count("Книга1") == 1

    def test_delete_book_from_favorites_success(self, setup_books_collector):
        collector = setup_books_collector
        collector.add_book_in_favorites("Книга1")
        collector.delete_book_from_favorites("Книга1")
        assert "Книга1" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_nonexistent_book(self, setup_books_collector):
        collector = setup_books_collector
        collector.delete_book_from_favorites("Несуществующая Книга")
        assert "Несуществующая Книга" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self, setup_books_collector):
        collector = setup_books_collector
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_non_empty(self, setup_books_collector):
        collector = setup_books_collector
        collector.add_book_in_favorites("Книга1")
        assert collector.get_list_of_favorites_books() == ["Книга1"]
