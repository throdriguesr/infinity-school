'''
Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.

'''

frutas = set()

frutas.add("maçã")
frutas.add("banana")
frutas.add("uva")
frutas.add("laranja")
frutas.add("morango")

print('\n', frutas)

if "banana" in frutas:
    print("\nA fruta 'banana' está no conjunto.")
else:
    print("\nA fruta 'banana' não está no conjunto.")