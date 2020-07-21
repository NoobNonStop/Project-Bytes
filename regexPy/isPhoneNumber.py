# Program to check whether a given expression is a phone number or not
#The pattern of a phone number is: 3 nos., a hyphen, 3 nos., another hyphen and 4nos. in the USA
#eg. 234-567-8910
def isPhoneNumber(text) :
    if (len(text) != 10) :
       return False
    else :
        for i in range(10) :
            if not text[i].isdecimal() :
                return False
        return True
def isPhoneNumberf(text) :
    if len(text) != 14 :
        return False
    

    else :
        if text[0:4:1] == "+91-" :
            for i in range(4,14,1) :
                if not text[i].isdecimal() :
                    return False
        else :     
            return False
    return True


def ultchk(text) :
    if isPhoneNumber(text) or isPhoneNumberf(text) :
        return True
    return False
#This is the Indian format
message = "djndcnkdnk fdjndimkd +91-3638477224 dsnkdn dhkasmjb +91-384893892 sdjkklsnujixcudsn ksdmkndkdnsjdn Isjs 493387473389329439. 388298387 duhcusjdioqj838293 idhiew93i3930 edud9j 29392497hffd."
for i in range(len(message)-11) :
    x = message[i:i+10]
    if ultchk(x) :
        print("This could be an Indian cell-phone number: " + x)
for j in range(len(message)-15) :
    z = message[i:i+14]
    if ultchk(z) :
        print("This could be an Indian cell-phone number: " + z)
