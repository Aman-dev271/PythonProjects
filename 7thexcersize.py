def getDate():
    import datetime
    return datetime.datetime.now()
v = getDate()
print(v)
def heealthmanag():

    data  = int(input("Enter ONE for to retrive and Enter TWO for lock \n"))
    if data == 2:
        lock = int(input("Press one for aman and Two for Mandeep Three for POOJA\n"))
        if lock == 1:
            lock_what = int(input("Enter one for deight and two for excerise\n"))
            if lock_what == 1:
                a = open("amandeight.text" , "a")
                deight_desc = input("Enter deight for aman:\n")
                d= a.write(str(v) +" "+ deight_desc +"\n")
                print([d])
            elif lock_what == 2:
                a = open("amanexersize.text" , "a")
                Exc_desc = input("Enter Excersize for aman:\n")
                r= a.write(str(v)+" "+Exc_desc +"\n")
                print([r])
        elif lock == 2:
            lock_what = int(input("Enter one for deight and two for excerise\n"))
            if lock_what == 1:
                a = open("mandeepdeight.text" , "a")
                deight_desc = input("Enter deight for Mandeep:\n")
                d= a.write(str(v)+" "+deight_desc +"\n")
                print([d])
            elif lock_what == 2:
                a = open("mandeepexersize.text" , "a")
                Exc_desc = input("Enter Excersize for Mandeep:\n")
                r= a.write(str(v)+" "+ Exc_desc +"\n")
                print([r])
        elif lock == 3:
            lock_what = int(input("Enter one for deight and two for excerise\n"))
            if lock_what == 1:
                a = open("poojadeight.text" , "a")
                Deight_desc = input("Enter deight for Pooja:\n")
                d= a.write(str(v)+" "+Deight_desc +"\n")
                print([d])
            elif lock_what == 2:
                a = open("poojaexersize.text" , "a")
                Exc_desc = input("Enter Excersize for Pooja:\n")
                r= a.write(str(v)+" "+Exc_desc +"\n")
                print([r])
    if data == 1:
        lock = int(input("Press one for aman and Two for Mandeep Three for POOJA :\n"))
        if lock == 1:
            lock_what = int(input("Enter one for deight and two for excerise:\n"))
            if lock_what == 1:
                a = open("amandeight.text" , "rt")
                d = a.read()
                print([d])
                a.close()
            elif lock_what == 2:
                a = open("amanexersize.text" , "rt")
                r = a.read()
                print([r])
                a.close()
        elif lock == 2:
            lock_what = int(input("Enter one for deight and two for excerise:\n"))
            if lock_what == 1:
                a = open("mandeepdeight.text" , "rt")
                d= a.read()
                print([d])
                a.close()
            elif lock_what == 2:
                a = open("mandeepexersize.text" , "rt")
                r = a.read()
                print([r])
                a.close()
        elif lock == 3:
            lock_what = int(input("Enter one for deight and two for excerise:\n"))
            if lock_what == 1:
                a = open("poojadeight.text" , "rt")
                d= a.read()
                print([d])
                a.close()
            elif lock_what == 2:
                a = open("poojaexersize.text" , "rt")
                r = a.read()
                print([r])
                a.close()

heealthmanag()
i = int(input("Enter 1 for again run this entire function other wise 2 :\n"))
while i<2:
    heealthmanag()
