salario = float(input("Digite o valor do salário: "))

if salario <= 280:
    valor_aumento = salario * 20.0 / 100
    novo_salario = salario + valor_aumento
    print(f"O salário antigo é {salario:,.2f} e foi reajustado em 20%. O valor de aumento é {valor_aumento:,.2f} e novo salário é {novo_salario:,.2f}")
    
elif salario <=700:
    valor_aumento = salario * 15.0 / 100
    novo_salario = salario + valor_aumento
    print(f"O salário antigo é {salario:,.2f} e foi reajustado em 15%. O valor de aumento é {valor_aumento:,.2f} e novo salário é {novo_salario:,.2f}")
    
elif salario <= 1500:
    valor_aumento = salario * 10.0 / 100
    novo_salario = salario + valor_aumento
    print(f"O salário antigo é {salario:,.2f} e foi reajustado em 10%. O valor de aumento é {valor_aumento:,.2f} e novo salário é {novo_salario:,.2f}")
    
else:
    valor_aumento = salario * 5.0 / 100
    novo_salario = salario + valor_aumento
    print(f"O salário antigo é {salario} e foi reajustado em 5%. O valor de aumento é {valor_aumento:,.2f} e novo salário é {novo_salario}")