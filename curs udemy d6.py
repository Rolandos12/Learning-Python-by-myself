#functions

#Scrie o funcție shopping_list() în care utilizatorul poate adăuga elemente într-o listă până când scrie stop. La final, afișează lista.
# Cerință: Folosește while și input().

# def shopping_list():
#     lista_cump = []
#     while True:
#         produs= input("Adauga pe lista ce vrei sa cumperi si apoi scrie stop cand lista e gata: ").lower()
#         if produs=="stop":
#             break
#         if produs.strip():
#             lista_cump.append(produs)
#         else:
#             print("Ai introdus un element invalid")
#     print("\nLista de cumparaturi finala este: ", lista_cump)
#
# shopping_list()

#Scrie o funcție `validate_emails(email_list)` care primește o listă de email-uri și returnează doar cele valide (conțin `@` și `.`).
# **Cerință**: Folosește `for`, `if`.

# def validate_emails():
#     email_list = []
#
#     nr_emailuri = int(input("Câte email-uri vrei să introduci? "))
#
#     for _ in range(nr_emailuri):
#         email = input("Adaugă adresa ta de email: ").lower()
#
#         if "@" in email and "." in email:
#             if len(email) > 4 and email[-3:] == "com" and email[-4] == ".":
#                 email_list.append(email)
#                 print("Email valid!")
#             else:
#                 print("Email invalid: trebuie să se termine cu '.com'")
#         else:
#             print("Email-ul nu este valid!")
#
#     print("\nLista de email-uri valide:")
#     for e in email_list:
#         print(e)
#
#
# validate_emails()


#Scrie o funcție `sales_report(sales)` care primește o listă de vânzări și returnează: * Totalul vânzărilor * Media vânzărilor * Numărul de vânzări peste 1000 RON
# **Cerință**: Folosește `for`, `if`, `sum()`, `len()`

def sales_report():
    preturi = {
        "tricouri": 90.39,
        "pantaloni": 220.87,
        "bluze": 144.99
    }

    vanzari = []

    for zi in range(1, 3):
        print(f"\nIntroduceti datele pentru ziua {zi}:")
        tricouri = int(input("Cate tricouri s-au vandut? "))
        pantaloni = int(input("Cati pantaloni s-au vandut? "))
        bluze = int(input("Cate bluze s-au vandut? "))

        vanzari_zi = (
            tricouri * preturi["tricouri"] +
            pantaloni * preturi["pantaloni"] +
            bluze * preturi["bluze"]
        )

        vanzari.append(vanzari_zi)
        print(f"Vanzari in ziua {zi}: {vanzari_zi:.2f} RON")

    total_vanzari = sum(vanzari)
    media_vanzari = total_vanzari / len(vanzari)
    vanzari_mari = sum(1 for v in vanzari if v > 1000)

    print("\n=== Raport final ===")
    print(f"Total vanzari: {total_vanzari:.2f} RON")
    print(f"Media vanzarilor: {media_vanzari:.2f} RON")
    print(f"Numar zile cu vanzari peste 1000 RON: {vanzari_mari}")

sales_report()







