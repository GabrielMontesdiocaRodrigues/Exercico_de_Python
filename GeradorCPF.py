import random

def geraCpf (): 
    cpf_gerado = ''
    for num in range(9):
        cpf_gerado += str(random.randint(0, 9))
    digitos_cpf_gerado = list(cpf_gerado)
    digitos_cpf_gerado.append(str(calculaDigito(digitos_cpf_gerado)))
    digitos_cpf_gerado.append(str(calculaDigito(digitos_cpf_gerado)))
    cpf_validado = ''
    for digito in digitos_cpf_gerado : 
        cpf_validado += digito
    return cpf_validado
   
def calculaDigito (digitos_recebidos : list):
        multiplicador = len(digitos_recebidos) + 1 
        soma_digitos = 0 
        for digito in  digitos_recebidos :
            soma_digitos = int(digito) * multiplicador + soma_digitos
            multiplicador -= 1

        resto = soma_digitos % 11 
        parte_inteira = int(soma_digitos / 11) 
        
        if resto < 2 :
            digito_verificador = 0
        else : 
            digito_verificador = 11 - resto

        return digito_verificador  

print(geraCpf())