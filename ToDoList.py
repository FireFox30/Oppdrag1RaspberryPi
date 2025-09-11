todolist = []
while True:
    Leggetil = input("Hva vil du legge til i listen? ")
    todolist.append(Leggetil)
    velge= int(input("skal du legge til mere? 1=Ja, 2=Nei: "))
    if velge == 1:
        continue
    elif velge == 2:
        print(todolist)
        break
svar = int(input("Velg tall på listen: "))
print(todolist[svar -1])

