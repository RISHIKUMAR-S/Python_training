import json

def load_dict(filename):
    with open(filename,"r") as f:
        read = json.load(f)
        return read

def save_dict(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
        
def del_dict():
    with open("data.json", "w") as f:
        json.dump({}, f, indent=2)

def add_list(students,i):
    choice = input("Do you want to add student details (add/stop) : ")
    while choice.lower() == "add":
        detail = dict()
        detail["name"] = input("Enter the no.{} student\'s name : ".format(i))
        detail["roll"] = int(input("Enter the rollno : "))
        detail["cgpa"] = int(input("Enter the cgpa : "))
        students.append(detail)
        i += 1
        choice = input("Do you want to continue (add/stop) : ")
    newlist = list((students,i))
    report = {"student" : newlist}
    print(report)
    return report

old_file = load_dict("data.json")
if old_file == None or old_file == {} :
    old_list = []
    serial = 1
else :
    old_list = old_file["student"][0]
    serial = old_file["student"][1]
report = add_list(old_list,serial)
save_dict(report)
del_choice = input("Do you want to clear the list (yes/no) : ")
if del_choice.lower() == "yes":
    del_dict()
    print("list is cleared successfully")
else :
    print("list is saved successfully")