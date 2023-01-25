class Point:

    def __new__(cls, *args, **kwargs):
        print("Call method __new__ for " + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("call __init__ for " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)


class DataBase:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f"Connect to db: {self.user}, {self.password}, {self.port}")

    def close(self):
        print("Close connect to db")

    def read(self):
        return "data from db"

    def write(self, data):
        print(f"write to {data}")


db = DataBase('root', '1234', 80)
db2 =DataBase('boot', '2365', 40)
print(id(db), id(db2))

db.connect()
db2.connect()