import collections
import select
from pymongo import MongoClient
from pymongo import errors
connection_string = "mongodb+srv://ozan:1234@ozan.zgre1.mongodb.net/?retryWrites=true&w=majority&appName=Ozan"
try: 
    client = MongoClient(connection_string)
    client.admin.command('ping')
    print("Bağlantı Başarılı")
    dbs = client.list_database_names()
    selected_db = client['Kullanıcılar']
    selected_collection = selected_db['MESAJLAR']
    print (selected_collection)
    
except errors.ConnectionFailure as conn_fail:
    print(conn_fail)
    
except Exception as e:
    print(e)
    
finally:
    if  'client' in locals():
        client.close()
        print("Bağlantı Kapatıldı")