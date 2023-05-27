from numpy import void
import pywhatkit

phonenumber = input("Phone Number: ")
msg = input('MSG here: ');

pywhatkit.sendwhatmsg_instantly(phonenumber, msg, 2)