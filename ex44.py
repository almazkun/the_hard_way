class Parent:
    def implicit(self):
        print("PARENT implicit() ")


class Child(Parent):
    pass


Parent().implicit()
Child().implicit()


class ParentOver:
    def override(self):
        print("PARENT override() ")


class ChildOver(ParentOver):
    def override(self):
        print("CHILD override() ")


ParentOver().override()
ChildOver().override()


class ParentSuper:
    def altered(self):
        print("PARENT altered() ")


class ChildSuper(ParentSuper):
    def altered(self):
        print("CHILD, BEFORE PARENT altered() ")
        super(ChildSuper, self).altered()
        print("CHILD, AFTER PARENT altered() ")


ParentSuper().altered()
ChildSuper().altered()


class ParentSupreme:
    def override(self):
        print("ParentSupreme override() ")

    def implicit(self):
        print("ParentSupreme implicit() ")

    def altered(self):
        print("ParentSupreme altered() ")


class ChildSupreme(ParentSupreme):
    def override(self):
        print("ChildSupreme override() ")

    def implicit(self):
        print("ChildSupreme implicit() ")

    def altered(self):
        super(ChildSupreme, self).altered()


print("\n\t WTF?")
ParentSupreme().override()
ParentSupreme().implicit()
ParentSupreme().altered()
print("\n\t WTF?")
ChildSupreme().override()
ChildSupreme().implicit()
ChildSupreme().altered()
print("\n\t WTF?")
ParentSupreme().altered()
ChildSupreme().altered()


class Other:
    def override(self):
        print("OTHER override() ")

    def implicit(self):
        print("OTHER implicit() ")

    def altered(self):
        print("OTHER altered() ")


class ChildOther(Other):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILDOTHER override() ")

    def altered(self):
        print("CHILDOTHER, before Other altered() ")
        self.other.altered()
        print("CHILDOTHER, after Other altered() ")


father = Other()
son = ChildOther()

print("\n\t WTF?")
father.implicit()
father.override()
father.altered()

print("\n\t WTF?")
son.implicit()
son.override()
son.altered()
