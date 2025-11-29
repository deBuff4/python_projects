class Employee:

    def __init__(self, name, ID):
        self.name, self.ID = name, ID
    def get_info(self):
        return self.name, self.ID

class Manager(Employee):
    def __init__(self, name, ID, department):
        self.department = department
        super().__init__(name, ID)

    def get_info(self):
        return super().get_info(), self.department

    def manage_project(self):
        pass                                        # ХЗ что делает

class Technician:

    def __init__(self, specialization):
        self.specialization = specialization


    def perform_maintenance(self):
        pass                                        # ХЗ что делает

class TechManager(Manager, Technician):

    def __init__(self, name, ID, department, specialization):
        super().__init__(ID, name, department)
        self.specialization = specialization

    def manage_project(self):
        pass

    def perform_maintenance(self):
        pass

    def add_employee(self, name, ID, department, specialization):
        super().name = name
        super().ID = ID
        super().department = department
        super().specialization = specialization

    ### Как сделать так, чтобы сюда передавались данные всех обьектов? - сделать все атрибуты в виде списка, и просто сделать .append()
    def get_team_info(self):


employee1 = Employee("John", 1)
manager1 = Manager("Jack", 2, "Rescue")
technician1 = Technician("PC administration")
tech_manager1 = TechManager("Ellie", 3, "HR", "Recruiting")
print(employee1.get_info())
print(manager1.get_info())
print(technician1.perform_maintenance())
print(tech_manager1.get_team_info())
