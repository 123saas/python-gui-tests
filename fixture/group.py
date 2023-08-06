import time
import pywinauto

class GroupHelper:
    # в конструктор будет передаваться в качестве дополнительного параметра ссылка на application, то есть на тот
    # объект, который среди прочего хранит ссылку на главное окно тестируемого приложения
    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()  # это мы найдем элемент Contact groups и дальше надо получить те узлы, которые в него вложены
        group_list = [node.text() for node in root.children()]  # но нам нужны не сами элементы управления, нужно их преобразовать в список строк. воспользуемся конструкцией лист комприхеншен. именно такая конструкция сформирует нам список названий групп, который метод get_group_list будет возвращать в качестве результата
        self.close_group_editor()
        return group_list

    def add_new_group(self, name): # с дополнительным параметром name
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click() # нажать на кнопку New
        input = self.group_editor.window(class_name="Edit") # это будет поле ввода
        input.set_text(name) # в это поле ввода нужно ввести нужное значение
        input.type_keys("\n") # чтобы завершит редактирование, нужно нажать enter
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible") # подождать пока окно станет видимым

    def close_group_editor(self):
        self.group_editor.close()

    def delete_first_group(self):
        contact_groups = 'Contact groups'
        self.open_group_editor() #открыть окно
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        for node in root.children(): # проходит по списку групп
            if node.text() != contact_groups: # если название не равно 'Contact groups', то выполнять следующие действия
                time.sleep(5)
                node.click() # нажать на группу
                self.open_delete_group() # открытие окна Delete group
                self.delete_group.window(auto_id="uxOKAddressButton").click() # в окне нажать на ОК
                break
        self.close_group_editor()


    def open_delete_group(self): # окно Delete group
        self.group_editor.window(auto_id="uxDeleteAddressButton").click() # нажать на кнопку Delete
        self.delete_group = self.app.application.window(title="Delete group") # self.app.application.window(title="Delete group") пишется так, чтобы во всем приложении нашел этот заголовок
        self.delete_group.wait("visible")

