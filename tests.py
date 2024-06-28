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


def test_add_new_book(setup_books_collector):
    collector = setup_books_collector

    # Добавление новой книги успешно
    collector.add_new_book("Новая Книга")
    assert "Новая Книга" in collector.get_books_genre()

    # Попытка добавить дубликат книги
    collector.add_new_book("Книга1")
    assert "Книга1" in collector.get_books_genre()
    assert len(collector.get_books_genre()) == 3

    # Попытка добавить книгу с именем длиннее 40 символов
    long_name = "а" * 41
    collector.add_new_book(long_name)
    assert long_name not in collector.get_books_genre()


def test_set_book_genre(setup_books_collector):
    collector = setup_books_collector

    # Установка жанра для книги
    collector.set_book_genre("Книга1", "Ужасы")
    assert collector.get_book_genre("Книга1") == "Ужасы"

    # Установка жанра для книги, которой нет в коллекции
    collector.set_book_genre("Несуществующая Книга", "Фантастика")
    assert collector.get_book_genre("Несуществующая Книга") is None

    # Установка жанра с недопустимым значением
    collector.set_book_genre("Книга2", "Роман")
    assert collector.get_book_genre("Книга2") == "Детективы"


def test_get_book_genre(setup_books_collector):
    collector = setup_books_collector

    # Получение жанра существующей книги
    assert collector.get_book_genre("Книга1") == "Фантастика"

    # Получение жанра для несуществующей книги
    assert collector.get_book_genre("Несуществующая Книга") is None


def test_get_books_with_specific_genre(setup_books_collector):
    collector = setup_books_collector

    # Получение списка книг определенного жанра
    assert collector.get_books_with_specific_genre("Фантастика") == ["Книга1"]
    assert collector.get_books_with_specific_genre("Детективы") == ["Книга2"]
    assert collector.get_books_with_specific_genre("Ужасы") == []


def test_get_books_genre(setup_books_collector):
    collector = setup_books_collector

    # Получение полного словаря books_genre
    books_genre = collector.get_books_genre()
    assert "Книга1" in books_genre
    assert "Книга2" in books_genre


def test_get_books_for_children(setup_books_collector):
    collector = setup_books_collector

    # Получение списка книг подходящих для детей
    assert collector.get_books_for_children() == ["Книга1"]


def test_add_book_in_favorites(setup_books_collector):
    collector = setup_books_collector

    # Добавление книги в избранное
    collector.add_book_in_favorites("Книга1")
    assert "Книга1" in collector.get_list_of_favorites_books()

    # Добавление несуществующей книги в избранное
    collector.add_book_in_favorites("Несуществующая Книга")
    assert "Несуществующая Книга" not in collector.get_list_of_favorites_books()

    # Добавление одной и той же книги в избранное дважды
    collector.add_book_in_favorites("Книга1")
    assert collector.get_list_of_favorites_books().count("Книга1") == 1


def test_delete_book_from_favorites(setup_books_collector):
    collector = setup_books_collector

    # Удаление книги из избранного
    collector.delete_book_from_favorites("Книга1")
    assert "Книга1" not in collector.get_list_of_favorites_books()

    # Удаление несуществующей книги из избранного
    collector.delete_book_from_favorites("Несуществующая Книга")
    assert collector.get_list_of_favorites_books() == []


def test_get_list_of_favorites_books(setup_books_collector):
    collector = setup_books_collector

    # Получение списка избранных книг
    assert collector.get_list_of_favorites_books() == []

    # Добавление книги в избранное и проверка списка
    collector.add_book_in_favorites("Книга1")
    assert collector.get_list_of_favorites_books() == ["Книга1"]
