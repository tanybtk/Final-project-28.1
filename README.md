Тестирование авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии (https://b2c.passport.rt.ru/)

Тест-кейсы доступны по ссылке: https://docs.google.com/spreadsheets/d/1CMFbPN-9oIevZ5B_S70TImllDHfkaoK1CC6sHi2OT7M/edit?usp=sharing

Баг-репорты доступны по ссылке: https://docs.google.com/spreadsheets/d/1RRzZxy3wimGPycTVG_zRHW992XozXMyS8WfhFf60PuY/edit?usp=sharing

В папке pages в файле base_page.py находится конструктор webdriver и общие для всех тестируемых страниц методы.
Скачать вэбдрайвер подходящий браузеру.

В папке pages в файлах auth_page.py, change_pass_page.py, reg_page.py находятся методы проверок: файл auth_page.py содержит методы проверок формы авторизации; файл change_pass_page.py содержит методы проверок формы восстановления пароля; файл reg_page.py содержит методы проверок формы регистрации.

В папке tests в файлах test_auth_page.py, test_change_pass_page.py, test_reg_page.py находятся тесты. 

В папке pages в файле "locators.py находятся все локаторы.

В корне проекта в файле conftest.py находится фикстура с функцией открытия и закрытия браузера.

В корне проекта в файле settings.py находятся методы и переменные для параметризации тестов

В корне проекта в файле requirements.py описаны используемые библиотеки.
