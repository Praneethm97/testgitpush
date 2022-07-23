import pymongo

client = pymongo.MongoClient("mongodb+srv://praneeth:simhachary@praneeth.cpzwahk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
collection = database["table"]
#collection.update_one({'item':'canvas'},{'$set':{'item':'sudhanshu'}})
#to delete
collection.delete_one({'item':'sudhanshu'})
d=collection.find({'item':'sudhanshu'})
for i in d:
    print(i)
