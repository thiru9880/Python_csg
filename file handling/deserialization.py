# import json
# json_data = '{"name": "john", "age": 45, "city": "new york"}'

# data = json.loads(json_data)
# print(data)

# print(data["name"])
# print(data["age"])
# print(data["city"])

import json

def save_user_data():
    user_list = []

    while True:
        name = input("enter the name or type quit to exit: ")
        if name == "quit":
            break
        email = input("enter the email: ")
        contact = input("enter the contact: ")

        # creating python dictionary
        user_data = {
            "name": name,
             "email": email,
             "contact": contact
        }

        user_list.append(user_data)

        with open("user_data.json", "a") as file:
            json.dump(user_list,file)
        
        print("user data is saved successfully")
save_user_data()
        



