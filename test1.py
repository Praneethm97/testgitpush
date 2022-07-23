import pymongo

client = pymongo.MongoClient("mongodb+srv://praneeth:simhachary@praneeth.cpzwahk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['myinfo']
collection = database["sudh"]
#req to pull records which have cmpny name
#data = collection.find({"companyName" : "iNeuron"})
data = collection.find({"courseOffered":{"$gt": "E"}}) #coursesoffered value should start with greater than E
for i in data:
    print(i)
