# upper = converte caracteres para maiúsculos
# lower = converte caracteres para maiúsculos
sexo = input("Digite M se for Masculino ou F se for feminino: ").lower()

# sexo = sexo.lower()
if sexo.lower() == "f":
    print("Seu sexo é feminino")
elif sexo.lower() == "m":
    print("Seu sexo é masculino")
else:
    print("Sexo inválido")