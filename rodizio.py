placa = int(input("Digite o final da placa do veiculo: "))

if placa == 1 or placa == 2:
    print(f"As placas com o final {placa} não roda na segunda-feira")
elif placa == 3 or placa == 4:
    print(f"As placas com o final {placa} não roda na terça-feira")
elif placa == 5 or placa == 6:
    print(f"As placas com o final {placa} não roda na quarta-feira")
elif placa == 7 or placa == 8:
    print(f"As placas com o final {placa} não roda na quinta-feira")
elif placa == 9 or placa ==  0:
    print(f"As placas com o final {placa} não roda na sexta-feira")
else:
    print("Placa inválida")