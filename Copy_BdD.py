import os
from datetime import datetime

def heure_date_copy():
    hd = datetime.now()
    return hd

def copy_bdd_Admin():
    data = open("Bdatos_Admin.txt", 'r').read()
    if os.path.exists('Copy_Bdatos_Admin.txt'):
        os.remove('Copy_Bdatos_Admin.txt')
        open("Copy_Bdatos_Admin.txt", 'w').write(data)
        open("Data_h_last_save_Admin.txt", 'a').write(str(heure_date_copy())+"\n")
    else:
        print("I can't do copy of Admin BdD")


def copy_bdd_Contact():
    data = open("Bdatos.txt", 'r').read()
    if os.path.exists('Copy_Bdatos_Contact.txt'):
        os.remove('Copy_Bdatos_Contact.txt')
        open("Copy_Bdatos_Contact.txt", 'w').write(data)
        open("Data_h_last_save_Contact.txt", 'a').write(str(heure_date_copy())+"\n")

    else:
        print("I can't do copy of contact BdD")

def re_write_bdd_admin():
    data = open("Copy_Bdatos_Admin.txt", 'r').read()
    if os.path.exists('Bdatos_Admin.txt'):
        os.remove('Bdatos_Admin.txt')
        open("Bdatos_Admin.txt", 'w').write(data)
    else:
        print("I can't do copy of contact BdD")

def re_write_bdd_Contact():
    data = open("Copy_Bdatos_Contact.txt", 'r').read()
    if os.path.exists('Bdatos.txt'):
        os.remove('Bdatos.txt')
        open("Bdatos.txt", 'w').write(data)
    else:
        print("I can't be back BDD call Laura")




# copy_bdd_Admin()
# copy_bdd_Contact()
# re_write_bdd_Contact()
# re_write_bdd_admin()