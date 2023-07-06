Автоматизированное ui-тестирование в личном кабинете от заказчика Ростелеком Информационные Технологии (https://b2c.passport.rt.ru/)

Для запуска теста:

pip3 install -r requirements
Установить Selenium WebDriver from https://chromedriver.chromium.org/downloads

python -m pytest -v --tb=line tests/test_authorization_page.py
python -m pytest -v --tb=line tests/test_change_pass_page.py
python -m pytest -v --tb=line tests/test_registration_page.py



Тест-кейсы: https://docs.google.com/spreadsheets/d/1CMFbPN-9oIevZ5B_S70TImllDHfkaoK1CC6sHi2OT7M/edit?usp=sharing

Баг-репорты: https://docs.google.com/spreadsheets/d/1RRzZxy3wimGPycTVG_zRHW992XozXMyS8WfhFf60PuY/edit?usp=sharing

В папке page:  в  authorization_page.py, change_pass_page.py, registration_page.py находятся методы проверок.

в файле "locators.py находятся локаторы.

В папке tests  находятся тесты проверок авторизации, востановления пароля, регистрации.




 в  requirements.py описаны используемые библиотеки.

