def login(uid,pwd):
    if uid=="ADMIN" and pwd=="St0rE@1":
        print("login successful")
        return 1
    else: print("Wrong credentials")
    return 0
count=0
while True:
    uid=input("Enter login id: ")
    pwd=input("Enter login password: ")
    output=login(uid,pwd)
    if output==1:
        break
    else: count+=1
    if count==3:
        print("account blocked")
        break