import pymongo

client = pymongo.MongoClient("mongodb+srv://praneeth:simhachary@praneeth.cpzwahk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
collection = database["table"]

data = data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

#collection.insert_many(data)
#fetch all data
#d = collection.find()
#look for the data where status = 'A'
#d = collection.find({'status':'A'})
#look for the data where status = 'A' or 'P'
#d = collection.find({'status':{'$in':['A','P']}})
#ststus should be greater than c
#d = collection.find({'status':{'$gte':'C'}})
#for i in d:
#    print(i)


#quantity >=100 or 75
#d = collection.find({'qty':{'$gte':75}})
#quantity >95 and item = sketchpad
#d = collection.find({'item':'sketch pad','qty':95})
#quantity >=75 and item = sketchpad
#d = collection.find({'item':'sketch pad','qty':{'$gte':95}})
#quantity >=75 or item = sketchpad
d = collection.find({'$or' :[{'item':'sketch pad'},{'qty':{'$gte':95}}]})
for i in d:
    print(i)