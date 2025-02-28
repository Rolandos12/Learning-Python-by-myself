# create a mini game about Heads or Tails coin
# import random
#
# print('Bine ai venit la jocul de noroc "Da cu banul". Trebuie sa alegi Cap sau Pajura.')
#
# pariu = input("Vrei sa fie mai fun jocul si ai vrea sa pariezi o suma de bani? (da/nu): ").strip().lower()
#
# suma_pariata = 0
#
# if pariu == "da":
#     while True:
#         try:
#             suma_pariata = int(input("Ce suma doresti sa pariezi: 5, 10, 50, 100 de lei? "))
#             if suma_pariata in [5, 10, 50, 100]:
#                 break
#             else:
#                 print("Te rog sa introduci doar 5, 10, 50 sau 100 de lei.")
#         except ValueError:
#             print("Te rog sa introduci un număr valid.")
#
#     castig_potential = suma_pariata * 2
#     print(f"Dacă ghicești, vei câștiga {castig_potential} lei!")
# else:
#     print("Pacat :( ar fi fost mai amuzant")
#
# choice = input("Alegerea ta (cap/pajura): ").strip().lower()
# nr_alegere = random.choice(["cap", "pajura"])
#
# print(f"A picat: {nr_alegere.capitalize()}")
#
# if choice == nr_alegere:
#     print("Felicitări! Ai câștigat!")
#     if pariu == "da":
#         print(f"Ai câștigat {castig_potential} lei!")
# else:
#     print("Ai pierdut. Mai încearcă!")
import random

# Lists
# Create a program which will select a random name from the list of names. The person selected has to pay the food bill.
#without using choice()
#import random

# names= input("Introdu numele tuturor persoanelor de la masa pentru a vedea cine va fii selectat pentru plata: ")
# names_split= names.split(" ")
# selectare= random.randint(0, len(names_split)-1)
# persoana=names_split[selectare]
# print(persoana.capitalize() + " ai fost selectat sa platesti nota")

#with choice() function
# names= input("Introdu numele tuturor persoanelor de la masa pentru a vedea cine va fii selectat pentru plata: ")
# names_split= names.split(" ")
# print(random.choice(names_split) + ", bravo, trebuie sa platesti pentru toti")

#create a game with rock paper and scissors
print("Hai sa jucam un joc, piatra foarfeca, hartie.")
alegere=str(input("Alege: "))
piatra=''' Piatra
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

foarfeca=''' Foarfeca
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) '''

hartie=''' Hartie
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    '''
lista=[piatra, foarfeca, hartie]
if alegere=="piatra":
    print(piatra)
elif alegere=="foarfeca":
    print(foarfeca)
elif alegere=="hartie":
    print(hartie)
else:
    print("Nu ai facut o alegere valida, te rog sa introduci una dintre urmatoarele: piatra, foarfeca sau hartie")

alegerea_botului= random.choice(lista)

print("BOTUL a ales" + alegerea_botului)

if alegere==hartie and alegerea_botului==hartie:
    print("Este egal X")
elif alegere==hartie and alegerea_botului==piatra:
    print("Ai castigat :)")
elif alegere==hartie and alegerea_botului==foarfeca:
    print("Ai pierdut :(")
elif alegere==piatra and alegerea_botului==foarfeca:
    print("Ai castigat <3")
elif alegere==piatra and alegerea_botului==hartie:
    print("Ai pierdut :(")
elif alegere==piatra and alegerea_botului==piatra:
    print("Este egal X")
elif alegere==foarfeca and alegerea_botului==piatra:
    print("Ai pierdut patroane :(")
elif alegere==foarfeca and alegerea_botului==hartie:
    print("Ai castigat :)")
else: #alegere==foarfeca and alegerea_botului==foarfeca
    print("Este egal X")