mensagem = 'Bem vindo a calculadora da Isadora, escolha seus números e uma operação.\nSelecione + para adiação.\nSelecione - para subtração.\nSelecione * para multiplicação.\nSelecione / para divisão.\nSelecione ^ para exponencial.'
print(mensagem)
numero1 = float(input('Insira um número = '))
numero2 = float(input('Insira outro número = '))
operacao = input('Insira a operação que deseja fazer = ')

if operacao == '+' :
    resultado = numero1 + numero2

elif operacao == '-' :
    resultado = numero1 - numero2

elif operacao == '*' :
    resultado = numero1 * numero2

elif operacao == '/' :
    if numero2 == 0 :
        print('Não é possível efetuar uma divisão por 0')
        exit(0)
    else :
        resultado = numero1 / numero2
elif operacao == '^' :
    resultado = numero1 ** numero2

print(f'{numero1} {operacao} {numero2} = {resultado:.2f}')
