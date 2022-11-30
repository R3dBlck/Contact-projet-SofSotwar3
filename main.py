###################         Import           ###################
from Copy_BdD import re_write_bdd_Contact, re_write_bdd_admin, copy_bdd_Admin, copy_bdd_Contact
from Writ_Hash_Files import save_full_hash_Admin, save_full_hash_Contact
from Writ_Hash_Files_Lines import write_hash_lines_Admin, write_hash_lines_Contact
from Compare_Hash import Contact_compare_err, Admin_compare_err
from menu import menu
from Gestion_de_la_bdd_contacto import *
from usuario import *
from seguridad_de_los_input import *
from read_db_user import recuperer_nombre_que_conozco, derechas_por_eso_menu
from Add_Admin import *

import sys


print("###############################################################################################")
print("# Hola ! Bienvenidos en el Aplicacion de gestion de contact.2.0                               #")
print("# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #")
print("# Autor : Laura AMIOT                                                                         #")
print("# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #")
print("###############################################################################################")

print("               _____            _             _                         _ _ \n              / ____|          | |           | |            /\         | (_)\n             | |     ___  _ __ | |_ __ _  ___| |_ ___      /  \   _ __ | |_ \n             | |    / _ \| '_ \| __/ _` |/ __| __/ _ \    / /\ \ | '_ \| | |\n             | |___| (_) | | | | || (_| | (__| || (_) |  / ____ \| |_) | | |\n             \_____\___/|_| |_|\__\__,_|\___|\__\___/  /_/    \_\ .__/|_|_|\n                                                                 | |        \n                                                                 |_|        ")


#Verification de la auth de los ficherons de datos
def _auth_ficheron_admin():
   if Admin_compare_err() == False:
       re_write_bdd_admin()
       write_hash_lines_Admin()
       save_full_hash_Admin()
       sys.exit()
   elif Admin_compare_err() == True:
       sys.exit()
   else:
       print("Everything is Ok nothing have change without you for Admin")


def _auth_ficheron_contact():
    if Contact_compare_err() == False:
        re_write_bdd_Contact()
        write_hash_lines_Contact()
        save_full_hash_Contact()
        sys.exit()
    elif Contact_compare_err() ==True:
        sys.exit()
    else:
        print("Everything is Ok nothing have change without you")


# Commenzar la entraga del Usuario.
def fct_por_el_usuario():
    _auth_ficheron_admin() # Verification de la integridad de las bdd
    _auth_ficheron_contact() # Integrity verification of bdd
    nombre_del_usuario_enter = enter_el_usuario()  # Call to write the name.
    if el_nombre_es_un_nombre(nombre_del_usuario_enter):  # check if it is indeed letters.
        nombre_correcat_user = re_escritura_del_nombre_del_usuario(
            nombre_del_usuario_enter)  # rewrite the name correctly to be able to compare it to the database.
        print("Vuestro nombre es : " + nombre_correcat_user)
        return nombre_correcat_user
    else:  # If typing error second chance before leaving.(same code)
        nombre_del_usuario_enter = enter_el_usuario()  # Call to write the name.
        if el_nombre_es_un_nombre(nombre_del_usuario_enter):  # check if it is indeed letters.
            nombre_correcat_user = re_escritura_del_nombre_del_usuario(
                nombre_del_usuario_enter)  # rewrite the name correctly to be able to compare it to the database.
            print("Vuestro nombre es : " + nombre_correcat_user)
            return nombre_correcat_user
        else:  # 2 mistakes, out!!!.
            sys.exit()  # Go out because it's not a name


def I_know_you_or_not(user):  # Do I know this user?
    if recuperer_nombre_que_conozco(user):  # If so, I know him, let's continue!
        print("OK !!! I know you !!!")
        return True
    else:  # If not, get out!
        print("Sorry little monster !! Get OUT !!")
        sys.exit()


def execute_menu(val_menu):
    if el_num_del_menu_es_correcto(val_menu):  # check that the menu entry is a number between 0 and 5
        if val_menu == "0":  # SALIR
            copy_bdd_Admin()
            copy_bdd_Contact()
            write_hash_lines_Admin()
            write_hash_lines_Contact()
            save_full_hash_Admin()
            save_full_hash_Contact()

            print("###############################################################################################")
            print("   ___                _               _               _                                _    \n  / _ \_ __ __ _  ___(_) __ _ ___    | |__   __ _ ___| |_ __ _   _ __  _ __ ___  _ __ | |_ ___  \n / /_\/  __/ _` |/ __| |/ _` / __|   |  _ \ / _  / __| __/ _  | |  _ \|  __/ _ \|  _ \| __/ _ \ \n/ /_\\| | | (_| | (__| | (_| \__ \_  | | | | (_| \__ \ || (_| | | |_) | | | (_) | | | | || (_) |\n\____/|_|  \__,_|\___|_|\__,_|___( ) |_| |_|\__,_|___/\__\__,_| | .__/|_|  \___/|_| |_|\__\___/ \n                                 |/                             |_|                             ")
            sys.exit()  # Exit of the apli

        if val_menu == "1":  # Agregar Contactos
            if derechas_por_eso_menu(nombre_correcat_user, val_menu) is True:
                agregar_contacto()
                new_val_menu = menu()
                execute_menu(new_val_menu)
                copy_bdd_Contact()
                write_hash_lines_Contact()
                save_full_hash_Contact()

            else:
                print(
                    "You don't have the rights for this. returns to the menu.")  # You don't have the rights for this. returns to the menu.
                new_val_menu = menu()
                execute_menu(new_val_menu)
        if val_menu == "2":  # Modificar Contactos
            if derechas_por_eso_menu(nombre_correcat_user, val_menu) is True:
                listar_contacto()
                num_ct = quien_tu_quiere_modif()
                if el_num_del_proximo_muerto_es_correcto(num_ct):
                    modif_contacto(num_ct)
                    copy_bdd_Contact()
                    write_hash_lines_Contact()
                    save_full_hash_Contact()

                new_val_menu = menu()
                execute_menu(new_val_menu)
            else:
                print(
                    "You don't have the rights for this. returns to the menu.")  # You don't have the rights for this. returns to the menu.
                new_val_menu = menu()
                execute_menu(new_val_menu)
        if val_menu == "3":  # Elmincar Contactos
            if derechas_por_eso_menu(nombre_correcat_user, val_menu) is True:
                listar_contacto()
                nom_kill_prox = Quien_kill()
                if el_num_del_proximo_muerto_es_correcto(nom_kill_prox):
                    function_de_la_muerte_de_los_contactos(nom_kill_prox)
                    copy_bdd_Contact()
                    write_hash_lines_Contact()
                    save_full_hash_Contact()

                new_val_menu = menu()
                execute_menu(new_val_menu)
            else:
                print(
                    "You don't have the rights for this. returns to the menu.")  # You don't have the rights for this. returns to the menu.
                new_val_menu = menu()
                execute_menu(new_val_menu)
        if val_menu == "4":  # Listar Contactos
            if derechas_por_eso_menu(nombre_correcat_user, val_menu) is True:
                listar_contacto()
                new_val_menu = menu()
                execute_menu(new_val_menu)
            else:
                print(
                    "You don't have the rights for this. returns to the menu.")  # You don't have the rights for this. returns to the menu.
                new_val_menu = menu()
                execute_menu(new_val_menu)
        if val_menu == "5":  # Agregar usario
            if derechas_por_eso_menu(nombre_correcat_user, val_menu):  # Check if the user has the rights to do this.
                nombre = El_nombre_del_nuevo_usario()  # input asks for the name of the new user.
                if Verificacion_de_la_escritura(nombre):  # check if they are indeed letters.
                    num_de_los_derechas_input = entraga_los_derechos()  # asks what type of rights the user will have
                    if verrif_la_entraga_de_los_derechos(
                            num_de_los_derechas_input):  # verify that the rights entry is correct. Whether it's a 1, 2 or 3
                        escritura_en_la_base(num_de_los_derechas_input, re_escritura_del_nombre_del_usuario(
                            nombre))  # writes new users to the database by forcing lowercase characters.
                        copy_bdd_Admin()
                        write_hash_lines_Admin()
                        save_full_hash_Admin()

                new_val_menu = menu()  # back to menu input
                execute_menu(new_val_menu)  # back to the menu
            else:
                print(
                    "You don't have the rights for this. returns to the menu.")  # You don't have the rights for this. returns to the menu.
                new_val_menu = menu()  # back to menu input
                execute_menu(new_val_menu)  # back to the menu
        else:
            print("Error en el system no es possible.")
            sys.exit()


nombre_correcat_user = fct_por_el_usuario()
I_know_you_or_not(nombre_correcat_user)
value_of_menu = menu()
execute_menu(value_of_menu)


