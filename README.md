# SPA

Приложение реализовано с использованием языков программирования и технологий: HTML, CSS, JS, JQuery, Ajax, Python, Django, PostgreSQL.

Принцип работы и поведение:  
При загрузке страницы данные из БД выгружаются через класс-представление ListView стандартным методшом с пагинацией в 5 записей(исходное значение на поле для определения параметра пагинации).  
В зависимости от определенных параметров формы генерируется Ajax-запрос на сервер, где для него формируется и отправляется JSON ответ.  
Ответ парсится в JS и выгружается в таблицу, очищенную при его получении без ошибок.  
Для обработки исключений при отправке недопустимых параметров генерируется исключение и оповещает пользователя в JS-alert окне.  

Для параметров задано следующее поведение:  

0 - поле не заполнено  
1 - поле заполнено  

c - column  
fc - filter_condition  
ft - find_text  

c  fc ft  
0  0  0 - Вывод данных из таблицы без сортировки, с учетом параметра пагинации  
0  0  1 - Вывод данных из таблицы без сортировки, с учетом параметра пагинации  
0  1  0 - Вывод данных из таблицы без сортировки, с учетом параметра пагинации  
0  1  1 - Вывод данных из таблицы без сортировки, с учетом параметра пагинации  
1  0  0 - Сортировка по заданному полю  
1  0  1 - Однозначное соответствие c значению ft  
1  1  0 - Сортировка по заданному полю  
1  1  1 - Выборка по условию с учетом всех параметров (Для NAME только include, параметр '=' для него реализован в однозначном соответствии(1 0 1))  

Все операции совершаются без перезагрузки страницы.  

Таблица БД PostgreSQL, в формате CSV, лежит в каталоге other_data/postgresql_table.  

Скриншоты можно посмотреть в каталоге other_data/screenshots.  

--- Развертывание ---
* Создать БД и таблицу public.spa_app_table. Импортировать данные в таблицу: "spa\other_data\postgresql_table\spa_app_table".
* В файле "spa\spa_python\spa_python\settings.py" применить соответствующие настройки БД в блоке:  
DATABASES = {  
   'default': {  
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  
        'NAME': 'db_for_spa',  
        'USER': 'postgres',  
        'PASSWORD': 'password'  
    }  
}.  
* В CMD перейти в "\spa\spa_python>".
* Запустить сервер: python manage.py runserver.
* Перейти http://127.0.0.1:8000.
