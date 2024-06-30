test_add_new_book_success: Проверка успешного добавления новой книги.
test_add_new_book_duplicate: Проверка, что дубликат книги не добавляется.
test_add_new_book_name_too_long: Проверка, что книга с именем длиннее 40 символов не добавляется.
test_set_book_genre: Проверка установки жанра для книги (с использованием параметризации для проверки различных сценариев).
test_get_book_genre: Проверка получения жанра книги по её названию (с использованием параметризации для проверки различных сценариев).
test_get_books_with_specific_genre: Проверка получения списка книг с определённым жанром (с использованием параметризации для проверки различных жанров).
test_get_books_genre: Проверка получения полного словаря books_genre.
test_get_books_for_children: Проверка получения списка книг, подходящих для детей.
test_add_book_in_favorites_success: Проверка успешного добавления книги в избранное.
test_add_book_in_favorites_nonexistent_book: Проверка, что несуществующая книга не добавляется в избранное.
test_add_book_in_favorites_duplicate: Проверка, что дублирующаяся книга не добавляется в избранное дважды.
test_delete_book_from_favorites_success: Проверка успешного удаления книги из избранного.
test_delete_book_from_favorites_nonexistent_book: Проверка, что удаление несуществующей книги из избранного не вызывает ошибок.
test_get_list_of_favorites_books_empty: Проверка получения пустого списка избранных книг.
test_get_list_of_favorites_books_non_empty: Проверка получения списка избранных книг после добавления книги.
