import random
response={
    "greeting":["hello","hiii","welcome to our grocery shop","hey!how i can help you to find?"],
    "farewell":["goodbye! have a great day!","thank you for visit.see you again soon","thank you"],
    "thanks":["no problem","My plessure","You are Welcome"],
    "prodcuts":["we have wide range of fresh fruits and vegetables","our dairy products are located in aisle 2","you can find canned goods in aisle 3."],
    "opening_hours":["We are open from 8 AM to 9 PM. From monday to saturday","we open at 8AM And close At 9 PM"],
    "location":["our grocery shop is located at 123 Main street"],
    "default":["I'm sorry, I didn't understand that.","could you please rephrase that?","I am not sure what you mean."]
}

def get_response(resp):
    
    if resp in ["hii","hello","hey"]:
        return random.choice(response["greeting"])
    elif resp in ["good bye","bye bye","goodbye"]:
        return random.choice(response["farewell"])
    elif resp in ["thank","thanks"]:
        return random.choice(response["thanks"])
    elif resp in ["grocerry","products"]:
        return random.choice(response["prodcuts"])
    elif "hours" in resp or "working" in resp:
        return random.choice(response["opening_hours"])
    elif "location" in resp or "address" in resp:
        return random.choice(response["location"])
    else:
        return random.choice(response["default"])
    
def main():

    print("welcome to chatbot")
    while True:
        intp=input("you : ")

        if(intp=="exit"):
            print("chatbot: thank you.")
            break
        else:
            r=get_response(intp)
            print("chatbot : ",r)

main()

