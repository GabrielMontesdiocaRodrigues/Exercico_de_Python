"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

LETRA_NAO_DESCOBRETA = "*"

palavra_secreta = "Gabigol"
letras_acertadas = ""
tentativas = 0

os.system("cls")

while True :
    print("Vamos jogar um jogo? Tenho uma palavra secreta tente adivinhá-la.")

    letra_usuario = input("Digite uma letra: ").lower()    

    if  len(letra_usuario) > 1 : 
        print("Digite apenas uma letra. Vamos novamente? ")
        tentativas += 1 
        continue 

    if letra_usuario in palavra_secreta : 
        letras_acertadas +=  letra_usuario.lower() 

    palavra_resposta= "" 

    for letra_secreta in palavra_secreta: 
        if letra_secreta.lower() in letras_acertadas.lower() :
            palavra_resposta += letra_secreta.lower()
        else : 
            palavra_resposta += LETRA_NAO_DESCOBRETA

    print(palavra_resposta)

    tentativas += 1 

    if palavra_resposta.lower() == palavra_secreta.lower() : 
        print(f"Parabéns você acertou a palavra {palavra_resposta.capitalize()}")
        print(f"Você acertou em {tentativas} tentativas")
        break






        
        
    
