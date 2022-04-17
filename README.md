# SPA

Приложение реализовано с использованием языков программирования и технологий: HTML, CSS, JS, JQuery, Ajax, Python, Django, PostgreSQL.

Принцип работы и поведение:
При загрузке страницы данные выгружаются через класс-представление ListView стандартным методшом с пагинацией в 5 записей(исходное значение на поле для определения параметра пагинации).
В зависимости от определенных параметров формы генерируется Ajax-запрос на сервер, где для него формируется и отправляется JSON ответ.
Ответ парсится в JS и выгружается в таблицу, очищенную при получении ответа без ошибок.
Для исключений при отправке недопустимых параметров генерируется исключение и оповещает пользователя в JS-alert окне.

 
