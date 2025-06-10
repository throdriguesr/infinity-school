'''
Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.

'''

frutas_vermelhas = set()

frutas_vermelhas.add("morango")
frutas_vermelhas.add("cereja")
frutas_vermelhas.add("framboesa")

print(frutas_vermelhas)

frutas_vermelhas.remove("cereja")

print(frutas_vermelhas)