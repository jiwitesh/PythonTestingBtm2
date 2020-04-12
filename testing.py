import argparse

from test_code_btm2_dao.DAO import DBObject
from test_code_btm2_dao.daoutils import createSqlQuery

listOfColumns = ["Car_Color", "Car_Price", "Car_Model"]


def formCarDetailsDict(carObjlist):
    listOfCarObjDict = []

    try:
        for carObj in carObjlist:
            userDetailsObj = {listOfColumns[0]: carObj.color, listOfColumns[1]: carObj.price, listOfColumns[2]: carObj.carName}
            listOfCarObjDict.append(userDetailsObj)
    except Exception as e:
        print(e)
    return listOfCarObjDict


class Car:
    def __init__(self, color, price, carName):
        self.color = color
        self.price = price
        self.carName = carName

    # *args Explanation
    # def __init__(self, *args):
    # 	# way to extract value
    # 	for arg in args:
    # 		print("Arguments inside *args : ", arg)

    # 	# another way to extract value
    # 	# if you know that this much value you are going to get it at any cost
    # 	self.color = args[0]
    # 	self.price = args[1]
    # 	self.carName = args[2]

    # **kwargs explanation
    # def __init__(self, **kwargs):
    #     # way to extract value
    #     for key, value in kwargs.items():
    #         print("Arguments inside *kwargs : key = {} and value = {}".format(key, value))
    #
    #     # another way to extract value
    #     # if you know that this much value you are going to get it at any cost
    #     self.color = kwargs['color']
    #     self.price = kwargs['price']
    #     self.carName = kwargs['carName']

    # def initialiseVars(self, color, price, carName):
    # 	self.color = color
    # 	self.price = price
    # 	self.carName = carName

    def getCarColor(self, carName):
        print("self.carName called for : ", carName)
        if self.carName == carName:
            return self.color, self.price


# ap = argparse.ArgumentParser()
# ap.add_argument("--color", required=True,
#                 help="Car color")
# ap.add_argument("--price", default="25000$",
#                 help="Car price")
# ap.add_argument("--name", default="BMWX1",
#                 help="car name")
# args = vars(ap.parse_args())

# **kwargs
# carObj1 = Car(color = args['color'], price = args['price'], carName = args['name'])

# **kwargs
# kwargs = {"color": args['color'], "price": args['price'], "carName": args['name']}
# carObj1 = Car(**kwargs)

# *args
# args = (args['color'], args['price'], args['name'])
# carObj1 = Car(*args)

# *args 
carObj1 = Car("Red", '25000$', "BMWX1")
carObj2 = Car('Blue', '35000$', 'AUDIQ1')
carObj3 = Car("GREEN", '45000$', "BMWX3")
carObj4 = Car('WHITE', '55000$', 'AUDIQ2')
carObj5 = Car("ORANGE", '65000$', "BMWXS")
carObj6 = Car('MATTBLACK', '75000$', 'AUDIQ3')

listOfCarObj = [carObj1, carObj2, carObj3, carObj4, carObj5, carObj6]
# carObj1 = Car()
# carObj1.initialiseVars('Red', '25000$', 'BMWX1')
# carObj2 = Car()
# carObj2.initialiseVars('Blue', '35000$', 'AUDIQ1')

# color1, price1 = carObj1.getCarColor('BMWX1')
# color2, price2 = carObj2.getCarColor('AUDIQ1')
#
# print('color : ', color1)
# print("Price : ", price1)
#
# print('color : ', color2)
# print("Price : ", price2)

host = "localhost"
port = "3307"
connUserName = "root"
connPassword = ""
dbName = "testDatabase"
tableName = "carDetails"

try:
    listOfCarDetailsDict = formCarDetailsDict(listOfCarObj)
    # mysql.connector.connect(user='root', password='', host='localhost', port='3307')
    dao = DBObject(connUserName, connPassword, host, port, listOfColumns)
    # dao.connect()
    if not dao.checkIfDatabaseExists(dbName):
        dao.createDatabase(dbName)
    if not dao.checkIfTableExists(dbName, tableName):
        dao.createTable(dbName, tableName)

    query, records_to_insert = createSqlQuery(tableName, listOfCarDetailsDict, listOfColumns)
    dao.insertDataInTable(dbName, query, records_to_insert)
except Exception as e:
    print(e)