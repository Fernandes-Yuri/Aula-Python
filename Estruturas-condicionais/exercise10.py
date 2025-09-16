salary = float(input('Digite o salário do funcionário: R$ '))
sales = float(input('Digite o valor total das vendas do funcionário: R$ '))

if sales <= 1500:
    commission = sales * 0.03  
elif sales > 1500:
    commission = sales * 0.05

total_salary = salary + commission
print(f'O salário total do funcionário, incluindo a comissão, é: R$ {total_salary:.2f}')