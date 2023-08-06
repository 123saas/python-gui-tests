def test_add_group(app): # в качестве параметра будет принимать фикстуру app
    old_list = app.groups.get_group_list() # сначала получаем старый список групп
    app.groups.add_new_group("my group") # выполняем какие-то действия. в качестве параметра будет передаваться имя группы
    new_list = app.groups.get_group_list() # получаем новый список групп
    assert len(old_list) + 1 == len(new_list)
    old_list.append("my group") # новый должен отличаться от старого одним элементом, то есть сюда должен быть добавлен элемент "my group",
    # причем old_list и new_list будет списком названий групп
    # assert sorted(old_list) == sorted(new_list)
    assert sorted(old_list) == sorted(new_list)
