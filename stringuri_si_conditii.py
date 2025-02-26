# text = "messi da gol in finala carnatilor vababonzi"
# print(len(text))
# print(text[16:23])   #cand printezi asa nr 16 este este al 17-lea caracter de la stanga la dreapta,
# iar 23 rep cate caractere sunt extrase din sir de la nr 16 la dreapta


# text = "vandam"
# actiune = "da cu pumnu"
# mesaj= '{} tare rau {}'.format(actiune[2:8],text)
# print(mesaj, len(mesaj))

#print(help(str))  #functia help afiseaza toate comenzile clasei str

text= "jacuzzi vrea mioara in gradina"
# print(text.count('z'))                 #functia .count('') numara cate subcaractere se gasesc in sir/string
# print(text.upper())   #functia upper si lower transforma sirul in caractere mari sau mici
# print (text.lower())
#print(text.replace(old, new))  inlocuieste un cuvant cu altul nou
#print(text.replace('gradina', 'casa'))


# user= 'mircea'
# parola= 'jambon'
#
# username = input('Introduceti numele contului: ')
# password = input('Introduceti parola: ')
#
# if username != user and password == parola:
#     print('Numele este gresit')
# elif username == user and password != parola:
#     print('parola este gresita')
# elif username != user and password != parola:
#     print('Ambele sunt gresite')
# else:
#     username == user and password == parola
#     print('Datele au fost introdus corect')

s= input('beau pespsi cu messi')
if "twist" not in s:
    new_s=' beau pepsi twist cu messi.'
    print(new_s + ' am adaugat twist pentru ca nu s-a gasit in string')
elif "twist" in s:
    new_ss= "beau cu messi pepsi twist"
    print(new_ss)




