import os

mensagem = input("Digite a mensagem do commit: ")  

os.system("git add .")  
os.system(f'git commit -m "{mensagem}"')  
os.system("git push origin main") 