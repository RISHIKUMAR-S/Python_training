from tinydb import TinyDB,Query

def load_dict():
    return db.all() # to get all the data from the database

def save_dict(data):
    db.truncate()
    db.insert(data) # to insert new data into the database

def del_dict():
    db.truncate() #to erase the old data
    print("The detail have been erased")

def add_dict():
    choice = input("Do you want to add student details (add/stop) : ")
    while choice.lower() == "add":
        detail = dict()
        detail["name"] = input("Enter the student\'s name : ")
        detail["roll"] = int(input("Enter the rollno : "))
        detail["cgpa"] = int(input("Enter the cgpa : "))
        choice = input("Do you want to continue (add/stop) : ")
    for item in db:
        print(item)
    return detail

db = TinyDB("db.json")
old_dict = load_dict()
save_dict(add_dict())

minimum = Query()
print(db.search(minimum.cgpa > 8 ))   # to use query for searching a specific thing

del_choice = input("Do you want to clear the list (yes/no) : ")
if del_choice.lower() == "yes":
    del_dict()
else :
    print("list is saved successfully")
#db.update({'count': 10}, Fruit.type == 'apple')
#print(db.all())
#db.remove(Fruit.count < 5) # to remove all the specific thing from the database
#db.all()
#db.truncate()
#db.all()