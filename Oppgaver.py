# oppgave 1
# navn=input("Hva heter du: ")
# print(f"Hei {navn}!")

# oppgave 2
# alder=int(input("Hvor gammel er du "))
# if alder >= 18:
#     print("du er gammel nok")
# else:
#     print("du er ikke gammel nok")

# oppgave 3
# tall=int(input("hvilke gangetabell? "))

# for i in range(10):
#     i += 1
#     # print(i * tall)

# oppgave 4

# from random import randint
# svar = randint(1, 20)
# counter = 0
# win = False
# while win == False and counter <= 5:
#     tall = int(input(f"Gjett et tall. {5-counter}: "))
#     if tall > svar:
#         print("for høyt")
#     if tall < svar:
#         print("for lavt")
#     if tall == svar:
#         win = True
#         print ("riktig")
#     counter += 1

# oppgave 2.4
# from random import randint
# tall = randint(0,10)
# tall2 = randint(0,10)

# svar = tall + tall2
# if svar > 10:
#     print("høyere en 10")
# elif svar < 10:
#     print("lavere en 10")
# else:
#     print("svaret er det samme")

# kalkulator
# tall1 = int(input("Tall 1: "))
# operator = input("Operator: ")
# tall2 = int(input("Tall 2: "))

# if operator == "*":
#     print(tall1 * tall2)
# elif operator == "-":
#     print(tall1 - tall2)
# elif operator == "+":
#     print(tall1 - tall2)
# elif operator == "/":
#     print(tall1 / tall2)
# else:
    # print("Feil! :( ") #hvist brukeren bruker et ugyldig tegn

# Liste
# listeMedDyr = ["Hund", "katt", "fugl", "hest"]
# listeMedDyr.append("gris")
# print(listeMedDyr)
# svar = int(input("Velg tall på listen: "))
# svar -= 1
# print(listeMedDyr[svar])

# oppgave 7