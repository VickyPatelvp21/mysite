from pymongo import MongoClient


connection_url="mongodb+srv://vicky:<password>@cluster0.uuvsk5a.mongodb.net/?retryWrites=true&w=majority"
mongo_client=MongoClient(connection_url)

Shop_database=mongo_client["Shop"]