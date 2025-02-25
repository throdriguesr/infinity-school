import conversor

print("Conversor de Unidades")
print("1 - Metros para Pés")
print("2 - Quilogramas para Libras")
print("3 - Celsius para Fahrenheit")

opcao = input("\nEscolha uma opção (1, 2 ou 3): ")

if opcao == "1":
    metros = float(input("\nDigite o valor em metros: "))
    resultado = conversor.metros_para_pes(metros)
    print(f"{metros} metros é igual a {resultado:.2f} pés.")

elif opcao == "2":
    kg = float(input("\nDigite o valor em quilogramas: "))
    resultado = conversor.kg_para_libras(kg)
    print(f"{kg} kg é igual a {resultado:.2f} libras.")

elif opcao == "3":
    celsius = float(input("\nDigite a temperatura em Celsius: "))
    resultado = conversor.celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C é igual a {resultado:.2f}°F.")

else:
    print("\nOpção inválida!")