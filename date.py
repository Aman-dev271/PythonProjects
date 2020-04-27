def getDate():
    import datetime
    return datetime.datetime.now()
v= getDate()
input  = input("enter the number ")
a = open("anamika.text" , "a")
a.write(str(v)+input)
