class UserAccount:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self,new_password):
        self.__password = new_password
    def check_password(self,password):
        return self.__password == password
    def get_password(self):
        return self.__password
userAccount = UserAccount('GoodOldPalMed','reverbsoundeffect@gmail.com','password')
userAccount.set_password('SaintSpring')
print(userAccount.check_password('SaintSpring'))
print(userAccount.get_password())



