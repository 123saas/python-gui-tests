

# тестовый метод
def test_delete_first_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group("my group")  # нужно группу предварительно создать
    old_groups = app.groups.get_group_list()
    app.groups.delete_first_group()
    new_groups = app.groups.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
