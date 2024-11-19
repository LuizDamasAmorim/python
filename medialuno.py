media = float(input("Digite a média do aluno: "))

if media >= 6:
    print(f"Aluno com media {media} esta aprovado ")
elif media <= 4:
    print(f"Aluno com media {media} esta reprovado")
else:
    print(f"Aluno com media {media} esta de recuperação")
