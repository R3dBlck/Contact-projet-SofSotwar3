import hashlib
import os
from datetime import datetime


def heure_date_copy():
    hd = datetime.now()
    return hd

def Hash_full_Admin():
    fileObj = open("Bdatos_Admin.txt", 'rb')
    m = hashlib.md5()
    m.update(fileObj.read())
    return m.hexdigest()


def Hash_full_Contact():
    fileObj = open("Bdatos.txt", 'rb')
    m = hashlib.md5()
    m.update(fileObj.read())
    return m.hexdigest()


def save_full_hash_Admin():
    MDfive = Hash_full_Admin()
    open("Full_Hash_Admin.txt", 'w').write(MDfive)
    open("Data_h_Full_Hash_Admin.txt", 'a').write(str(heure_date_copy()) + "\n")


def save_full_hash_Contact():
    MDfive = Hash_full_Contact()
    os.remove('Full_Hash_Contact.txt')
    open("Full_Hash_Contact.txt", 'w').write(MDfive)
    open("Data_h_Full_Hash_Contact.txt", 'w').write(str(heure_date_copy()) + "\n")





#save_full_hash_Admin()
#save_full_hash_Contact()
