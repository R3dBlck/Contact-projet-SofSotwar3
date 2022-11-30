import hashlib
import os
from datetime import datetime


def heure_date_copy():
    hd = datetime.now()
    return hd

def Hash_itch_line_Admin():
    fichier_admin = open("Bdatos_Admin.txt", "r")
    Admin = fichier_admin.readlines()
    fichier_admin.close()
    l=[]
    for i in range(0, len(Admin)):
        b = "\""+'b'+Admin[i]+"\""
        a = hashlib.sha256(b.encode('utf-8')).hexdigest()
        l.append(a)
    return l

def Hash_itch_line_Contact():
    fichier_admin = open("Bdatos.txt", "r")
    Admin = fichier_admin.readlines()
    fichier_admin.close()
    l=[]
    for i in range(0, len(Admin)):
        b = "\""+'b'+Admin[i]+"\""
        a = hashlib.sha256(b.encode('utf-8')).hexdigest()
        l.append(a)
    return l

def write_hash_lines_Admin():
    l = Hash_itch_line_Admin()
    if os.path.exists('Line_Hash_Admin.txt'):
        os.remove('Line_Hash_Admin.txt')
        p = open('Line_Hash_Admin.txt', "w+")
        for i in range(0, len(l)):
            p.write(l[i])
            p.write("\n")
        open("Data_h_Line_Hash_Admin.txt", 'a').write(str(heure_date_copy()) + "\n")

    else:
        print("Err 118 218, Call manager Admin! ")


def write_hash_lines_Contact():
    l = Hash_itch_line_Contact()
    if os.path.exists('Line_Hash_Contact.txt'):
        os.remove('Line_Hash_Contact.txt')
        p = open('Line_Hash_Contact.txt', "w+")
        for i in range(0, len(l)):
            p.write(l[i])
            p.write("\n")
        open("Data_h_Line_Hash_Contact.txt", 'a').write(str(heure_date_copy()) + "\n")
    else:
        print("Err 118 218, Call manager Contact! ")

#write_hash_lines_Admin()
#write_hash_lines_Contact()