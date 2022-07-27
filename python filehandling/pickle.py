import pickle

def load_list(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

def save_list(data):
    try:
        with open("data1.pickle", "wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
        
def del_list():
    try:
        with open("data1.pickle", "wb") as f:
            pickle.dump([], f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

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
    report = list((students,i))
    print(report)
    return report

old_file = load_list("data.pickle")
if old_file == None or old_file == [] :
    old_list = []
    serial = 1
else :
    old_list = old_file[0]
    serial = old_file[1]
report = add_list(old_list,serial)
save_list(report)
del_choice = input("Do you want to clear the list (yes/no) : ")
if del_choice.lower() == "yes":
    del_list()
    print("list is cleared successfully")
else :
    print("list is saved successfully")