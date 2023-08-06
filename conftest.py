# в этом файле будет находиться функция, которая фикстуру инициализирует

import pytest
from fixture.application import Application
# так будет помечена функция, которая инициализирует фикстуру. Фикстуру сделаем глобальной, так чтобы приложение запускалось один раз для всех тестов: scope="session"


@pytest.fixture (scope="session")
def app(request):
    fixture = Application("C:\\Program Files (x86)\\GAS Softwares\\Free Address Book\\AddressBook.exe") # именно эта фикстура и будет возвращаемым значением инициализирующей функции. В скобках передаем путь к исполняемому файлу
    request.addfinalizer(fixture.destroy) # нужно зарегистрировать финализатор. здесь нам не нужно вызывать метод destroy, поэтому после него скобки не нужны, нам нужно передать ссылку на этот метод в функцию addfinalizer
    return fixture