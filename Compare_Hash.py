# !!!!!!!!!! Recuperation of each files last Hash save & Date  !!!!!!!!!!
# --------------------------         Hash    SAve    ------------------------
import hashlib




def Recup_Ultimo_Hash_File_Admin():
    ficheron = open("Full_Hash_Admin.txt", 'r')
    Admin = ficheron.readlines()
    ficheron.close()
    l = Admin[0].strip('\n')
    return l

#print(Recup_Ultimo_Hash_File_Admin())

def Recup_Ultimo_Hash_File_Contacto():
    ficheron = open("Full_Hash_Contact.txt", 'r')
    Admin = ficheron.readlines()
    ficheron.close()
    l = Admin[0].strip('\n')
    return l


# --------------------------         Date        ------------------------

def Recup_Utlimo_Data_h_File_Admin():
    ficheron = open("Data_h_Full_Hash_Admin.txt", 'r')
    Admin = ficheron.readlines()
    ficheron.close()
    l = Admin[len(Admin) - 1].strip('\n')
    return l


def Recup_Ultimo_Data_h_File_Contacto():
    ficheron = open("Data_h_Full_Hash_Contact.txt", 'r')
    Admin = ficheron.readlines()
    ficheron.close()
    l = Admin[len(Admin) - 1].strip('\n')
    return l

# --------------------------         Hash actual        ------------------------

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

# !!!!!!!!!! Compare of each files last Hash save & Actual  !!!!!!!!!!
# ----------------------         Admin        ------------------------
def Compare_Admin_Hash_full_file():
    Hash_last_Guard = Recup_Ultimo_Hash_File_Admin()
    Hash_actual = Hash_full_Admin()
    if Hash_actual == Hash_last_Guard:
        return True
    else:
        return False


def Compare_Contacto_Hash_full_file():
    Hash_last_Guard = Recup_Ultimo_Hash_File_Contacto()
    #print(Hash_last_Guard)
    Hash_actual = Hash_full_Contact()
    #print(Hash_actual)
    if Hash_actual == Hash_last_Guard:
        return True
    else:
        return False


# !!!!!! Recuperation of each files last Hash save & Date for EACH LINES !!!!!!
# --------------------------         Hash Saved       ------------------------


def Recup_Cada_linea_Hash_Admin():
    ficheron = open("Line_Hash_Admin.txt", 'r')
    Admin = ficheron.readlines()
    ficheron.close()
    l = []
    for i in range(0, len(Admin)):
        l.append(Admin[i].strip('\n'))
    return l


def Recup_Cada_linea_Hash_Contacto():
    ficheron = open("Line_Hash_Contact.txt", 'r')
    Admin = ficheron.readlines()
    ficheron.close()
    l = []
    for i in range(0, len(Admin)):
        l.append(Admin[i].strip('\n'))
    return l



# --------------------------         Date Saved       ------------------------

def Recup_Utlimo_Data_h_Line_Admin():
    ficheron = open("Data_h_Line_Hash_Admin.txt", 'r')
    Admin = ficheron.readlines()
    ficheron.close()
    l = Admin[len(Admin) - 1].strip('\n')
    return l


def Recup_Ultimo_Data_h_Line_Contacto():
    ficheron = open("Data_h_Line_Hash_Contact.txt", 'r')
    Admin = ficheron.readlines()
    ficheron.close()
    l = Admin[len(Admin) - 1].strip('\n')
    return l

# --------------------------         HAsh Actual       ------------------------

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

# !!!!!!!!!! Compare of each files last Hash for each lines save & Actual  !!!!!!!!!!
# ----------------------         Admin        ------------------------
def Compare_Admin_Hash_lines_file():
    Hash_last_Guard = Recup_Cada_linea_Hash_Admin()
    Hash_actual = Hash_itch_line_Admin()
    if len(Hash_actual) == len(Hash_last_Guard):
        a = 0
        for i in range(0, len(Hash_actual)):
            if Hash_actual[i] != Hash_last_Guard[i]:
                a += 1
                print("La linea : ", i, "was corrupt")
        if a != 0:
            return False
    else:
        return True


# ----------------------         Contacto        ------------------------

def Compare_Contacto_Hash_lines_file():
    Hash_last_Guard = Recup_Cada_linea_Hash_Contacto()
    Hash_actual = Hash_itch_line_Contact()
    if len(Hash_actual) == len(Hash_last_Guard):
        a = 0
        for i in range(0, len(Hash_actual)):
            if Hash_actual[i] != Hash_last_Guard[i]:
                a += 1
                print("La linea : ", i, "was corrupt")
        if a != 0:
            return False
    else:
        return True



def Admin_compare_err():
    if Compare_Admin_Hash_full_file() == False:
        print("Have problem !! File Admin havebeen corumpt.")
        print("The last save hash I've done was : ", Recup_Utlimo_Data_h_File_Admin())
        print("I will check wich line was corrumpt ! wait a 0.001 sec Please.")
        Cada_ultima_lineas_A = Compare_Admin_Hash_lines_file()
        print("Ultima guard was : ", Recup_Utlimo_Data_h_Line_Admin())
        print(Cada_ultima_lineas_A)
        if Cada_ultima_lineas_A == True:
            print("Show your Data base have a line add or supp and you don't know")
            return False
        else:
            print("What do you want to do ? Power up the last save or nothing i'm shutdown and you will see what do ? (last save = y) (shutdown = n)")
            so = input("Answare ... ")
            if so == "y":
                return False
            else :
                return True

def Contact_compare_err():
    if Compare_Contacto_Hash_full_file() == False:
        print("Have problem !! Contacto Admin havebeen corumpt.")
        print("The last save hash I've done was : ", Recup_Ultimo_Data_h_File_Contacto())
        print("I will check wich line was corrumpt ! wait a 0.001 sec Please.")
        Cada_ultima_lineas_C = Compare_Contacto_Hash_lines_file()
        print("Ultima guard was : ", Recup_Ultimo_Data_h_Line_Contacto())
        if Cada_ultima_lineas_C== True:
            print("Show your Data base have a line add or supp and you don't know")
            return False
        else:
            print("What do you want to do ? Power up the last save or nothing i'm shutdown and you will see what do ? (last save = y) (shutdown = n)")
            so = input("Answare ... ")

            if so == "y":
                return False
            else:
                return True

# Contact_compare_err() # A lancer pour faire la verification a chaque demarrage COnctact
# Admin_compare_err() # A lancer pour faire la verificattion a chaque demarrage Admin