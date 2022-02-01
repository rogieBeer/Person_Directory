import random

data = {}
keys = []
first_name = []
last_name = []
email = []
fname_file = open("fname.txt", "r+")
fname_file_text = fname_file.read()
fname_file.close()
lname_file = open("lname.txt", "r+")
lname_file_text = lname_file.read()
lname_file.close()
email_file = open("email.txt", "r+")
email_file_text = email_file.read()
email_file.close()
person_list = open("person_list.txt", "wb")


def random_random(x, y, z):
    text_stripper(x, 1)
    text_stripper(y, 2)
    text_stripper(z, 3)
    f = random.choice(first_name)
    l = random.choice(last_name)
    r = random.randint(300, 3000)
    e = random.choice(email)
    dict_create(f, l, r, e)


def phone_number():
    start = ["021", "022", "027", "020"]
    x = ""
    for z in range(8):
        num = random.randint(0, 9)
        x += str(num)
    y = random.choice(start)
    number = y+x
    return number


def dict_create(fNam, lNam, rNum, eOpt):
    age = random.randint(18, 55)
    age = str(age)
    phone = phone_number()
    email = fNam+lNam+str(rNum)+"@"+eOpt
    email = email.lower()
    lNam = lNam.title()
    data[fNam] = {"First Name": fNam, "Last Name": lNam,
                  "Age": age, "Email": email, "Phone": phone}
    keys.append(fNam)
    write = fNam + ":"+"First Name"+"=" + fNam+"," + "Last Name""=" + lNam + \
        ","+"Age"+"="+age+","+"Email""="+email+","+"Phone"+"="+phone+"\n"
    person_list.write(bytes(write, "UTF-8"))
    return


def text_stripper(file_in, opt):
    x = ""
    for name in file_in:
        if name == "\n":
            if opt == 1:
                first_name.append(x)
                x = ""
            elif opt == 2:
                last_name.append(x)
                x = ""
            elif opt == 3:
                email.append(x)
                x = ""
        else:
            x += name


def loop():
    # n = input("How many people would you like to create: ")
    # for x in range(int(n)):
    for x in range(15):
        random_random(fname_file_text, lname_file_text, email_file_text)
    return


loop()
person_list.close()
