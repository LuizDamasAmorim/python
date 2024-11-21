num = []

for p in range(1,71):
    v = int(input(f"Digite o {p}º número: "))
    # adicionar o valor de v na lista num
    num.append(v)

for x in num:
    print(x, end= " - ")