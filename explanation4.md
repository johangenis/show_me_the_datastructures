# Problem 4: Active Directory
This problem was solved using recursion. Starting from the root, each group is visited checking if the user is present. If the user matches, it is returned.

Since the number files to be iterated through is unknown, its easier to iterate with recursion by visiting the group and making a recursive call for each of its children.

Worst case scenario is if the user is not present in any group and the group structure has the same subgroups, thus O(n!). Since a stack if iterated recursively would have a space complexity of O(n).
