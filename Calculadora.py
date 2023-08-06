""" Calculadora com while """

sair = False 

while not sair :  
    try : 
        operador_valido = False 
        num_1_str = input('Digite o primeiro número: ')
        num_1 = float(num_1_str)
        while not operador_valido : 
            operador = input('Digite a operação desejada: ')
            operador_valido = operador == '+' or operador ==  '-' or operador ==  '*' or operador ==  '/'
            if not operador_valido : 
                print('Operador inválido, digite novamente')
        num_2_str = input('Digite o segundo número : ')
        num_2 = float(num_2_str)
        if  operador == '+' : 
            print(f'A soma resultou em : {num_1 + num_2}')
        elif operador == '-' : 
            print(f'A subtração resultou em : {num_1 - num_2}')
        elif operador == '*' : 
            print(f'A multiplicação resultou em : {num_1 * num_2}')
        elif operador == '/' : 
            print(f'A divisão resultou em : {num_1 / num_2}')
        sair = input('Pressione [s] para sair: ').lower().startswith('s')
        if sair : 
            break
    except :  
        print('Isto não é um número, digite novamente')
        





