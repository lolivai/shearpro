import os
import json

class JsonDatabase(object):
    def __init__(self,path='newdb'):
        self.path = f'{path}.jdb'
        self.items = {}

    def check_create(self):
        exist = os.path.isfile(self.path)
        if not exist:
            db = open(str(self.path), 'w')
            db.write('')
            db.close()

    def save(self):
        dbfile = open(self.path, 'w')
        i = 0
        for user in self.items:
            separator = ''
            if i < len(self.items) - 1:
                separator = '\n'
            dbfile.write(user + '=' + str(self.items[user]) + separator)
            i += 1
        dbfile.close()

    def propietario(self,name):
        self.items[name] = {'ip': '152.206.177.14',
                     'rango_minimo': 1080,
                     'rango_maximo': 2000,
                     'admin': 1}

    def create_user(self,name):
        self.items[name] = {'ip': '152.206.177.14',
                     'rango_minimo': 1080,
                     'rango_maximo': 2000,
                     'admin': 0}

    def is_admin(self,user):
        User = self.get_user(user)
        if User:
            return User['admin'] == 1
        return False

    def remove(self,name):
        try:
            del self.items[name]
        except:pass

    def get_user(self,name):
        try:
            return self.items[name]
        except:
            return None

    def save_data_user(self,user, data):
        self.items[user] = data

    def load(self):
        dbfile = open(self.path, 'r')
        lines = dbfile.read().split('\n')
        dbfile.close()
        for lin in lines:
            if lin == '': continue
            tokens = lin.split('=')
            user = tokens[0]
            data = json.loads(str(tokens[1]).replace("'", '"'))
            self.items[user] = data
