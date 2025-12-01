class Employee:

    def __init__(self, name = None, ID = None, list_of_employee = ()):
        self.name = name
        self.__id = ID
        self.list_of_employee = list_of_employee

    def get_info(self):
        return self.name, self.__id
