import cryptocode


def chifrre_fct(plb):
    str_encoded = cryptocode.encrypt(plb, "Hola!chicoKtal")
    return str_encoded


def dechifrre_fct(plb_cod):
    str_decoded = cryptocode.decrypt(plb_cod, "Hola!chicoKtal")
    return str_decoded

#C = chifrre_fct("Whats the hell")
#print(C)
#D = dechifrre_fct(C)
#print(D)



def encode_el_ficheron_entero():
    fichier_contact = open("Bdatos.txt", "r")
    contact = fichier_contact.readlines()
    print(contact)
    fichier_contact.close()
    fichier_contact = open("Bdatos.txt", "w+")
    fichier_contact.truncate()
    for i in range(0, len(contact)):
        c = contact[i].split(";")
        print(c)
        a = chifrre_fct(c[0]) +";"+ chifrre_fct(c[1])+";"+c[2]
        fichier_contact.write(a)

    fichier_contact.close()

#encode_el_ficheron_entero()

