# importando as bibliotecas
from random import choice
import string

# perguntandp quantos dígitos
tam_senha = int(input("Quantos dígitos voê quer na sua senha?: "))

# caracteres
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_final = ''
if tam_senha <= 5:
    print("Sua senha será muito curta!")
else:
    for i in range(tam_senha):
        senha_final += choice(caracteres)

    print(f"Sua senha está pronta: {senha_final} ")