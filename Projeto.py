"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')  

try :
    numero_int = int(float(numero_str))
    isPar = (numero_int % 2) == 0 
    if numero_str.isdigit() :
        if isPar : 
            print(f'O número {numero_int} é par')
        else :
            print(f'O número {numero_int} é impar')
    else :
        print('Este número não é inteiro') 
except :
    print('Você não digitou um número')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""  

horario_str = input('Digite a hora atual: ')

INICIO_MANHA = 0
INICIO_TARDE = 11 
INICIO_NOITE = 17 

try : 
    horario_int = int(horario_str)
    horario_valido = 0 <= horario_int <= 23  

    manha = INICIO_MANHA <= horario_int <= INICIO_TARDE
    tarde = INICIO_TARDE <  horario_int <= INICIO_NOITE
    noite = INICIO_NOITE <  horario_int 

    if horario_valido : 
        if manha :  
            print('Bom dia!')
        elif tarde : 
            print('Boa tarde!')
        elif noite :  
            print('Boa noite!')
    else: 
        print('Horário inválido')
except : 
    print('Você não digitou um número')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite seu primeiro nome: ')

TAM_NOME_CURTO =  4 
TAM_NOME_NORMAL = 5
TAM_NOME_GRANDE = 6 

tamanho_nome = len(primeiro_nome)

nome_curto  = tamanho_nome <= TAM_NOME_CURTO
nome_normal = TAM_NOME_GRANDE > tamanho_nome >= TAM_NOME_NORMAL
nome_grande = tamanho_nome >= TAM_NOME_GRANDE

if nome_curto : 
    print("Seu nome é curto") 
elif nome_normal :
    print("Seu nome é normal") 
elif nome_grande : 
    print("Seu nome é grande") 