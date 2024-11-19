turno = input("Digite M para matutino, V para vespertino ou N para noturno: ")

if turno == 'm' or turno == 'M':
    print(f"O seu turno é matutino")
elif turno == 'v' or turno == 'V':
    print(f"O seu turno é vespertino")
elif turno == 'n' or turno == 'N':
    print(f"O seu turno é noturno")
else:
    print("Turno inválido ")