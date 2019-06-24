class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def is_user_in_group(self, group, user):
        if user in group.get_users():
            return True
        else:
            if len(group.get_groups()) == 0:
                return False
            else:
                for _group in group.get_groups():
                    is_in_group = self.is_user_in_group(_group, user)
                    if is_in_group == True:
                        return True
def test1():
    # User in sub_child
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(parent.is_user_in_group(parent, sub_child_user))

def test2():
    # User in child
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(parent.is_user_in_group(child, sub_child_user))

def test3():
    # Non-existent user
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(parent.is_user_in_group(child, "non-existent"))

test1()
test2()
test3()
