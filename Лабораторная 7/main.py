class Employee:

    def __init__(self, name = None, ID = None):
        self.name = name
        self.__id = ID

    def get_info(self):
        return self.name, self.__id

class Manager(Employee):
    def __init__(self, name, ID, department):
        self.department = department
        super().__init__(name, ID)

    def manage_project(self):
        pass

class Technician:

    def __init__(self, specialization):
        self.specialization = specialization

    def perform_maintenance(self):
        pass

class TechManager(Manager, Technician):

    # Не работают, разобраться с передачей информации о сотрудниках в список
    list_of_employee = ()
    def add_employee(self, name, ID, department, specialization):
        super().name = name
        super().ID = ID
        super().department = department
        super().specialization = specialization
        list_of_employee.append(name, ID, department, specialization)

    def get_team_info(self):
        return list_of_employee
