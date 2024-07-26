# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

# Qualquer metodo que usa o self é um método de instância
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        # setter
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG', msg)

def connection_log(msg):
        print('LOG', msg)
    
c1 = Connection()
c1.set_user('Victor')
c1.set_password('1234')

c2 = Connection.create_with_auth('Victor', '123')
print(c2.password, c2.user)

Connection.log('Essa é a mensagem de log')
connection_log('Essa é a mensagem de log')