import json
name=input("enter name")
age=int(input("enter age"))
data={"name":name,"age":age}
stringify_json=json.dumps(data)
print("serialised data of json",stringify_json)