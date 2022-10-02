
class Storage:
    def __init__(self):
        self.db = Table()

    def register_loan(self) -> None:
        name = input('Enter name: ')
        amount = float(input('Enter amount: '))
        term = int(input('Enter payment term (in mouths): '))
        interest_rate = float(input('Enter interest rate (%): '))
        system = input('Enter payment system 1 to Price and 2 to SAC: ')
        while True:
            if system == '1' or system == 1:
                system == 'Price'
                break
            elif system == '2' or system == 2:
                system == 'SAC'
                break
            else:
                print('Invalid system')
                system = input('Enter system (1 or 2): ')
        self.db.add(name=name, amount=amount, term=term, interest_rate=interest_rate, system=system)

    def consult_extract(self) -> None:
        name = input('Enter name: ')
        print('_________________________________________________________')
        self.db.consult(name)

    def ordinary_payment(self) -> None:
        name = input('Enter name: ')
        self.db.ordinary_payment(name=name)

    def extraordinary_amortization(self) -> None:
        name = input('Enter name: ')

        a_type = input('Enter 1 to term reduction or 2 to installment value: ')
        while True:
            if a_type == '1':
                a_type == 'term reduction'
                break
            elif a_type == '2':
                a_type == 'installment value'
                break
            else:
                print('Invalid system')
                a_type = input('Enter 1 to term reduction or 2 to installment value: ')
        
        self.db.extraordinary_amortization(name=name, a_type=a_type)

    def refresh(self) -> None:
        self.db.refresh()


class Table:#TEM TODOS OS EMPRESTIMOS SE PESQUISA PELA CHAVE NOME PARA ACHAR UM LOAN
    def __init__(self):
        self.table = {}
    
    def add(self, name, amount, term, interest_rate, system) -> None:
        self.table[name] = Loan(amount=amount, term=term, interest_rate=interest_rate, system=system)
    
    def consult(self, name) -> None:
        if name in self.table:
            return self.table[name].show()
        else:
            return 'Not found'
    
    def ordinary_payment(self, name) -> None:
        self.table[name].ordinary_payment()
    
    def extraordinary_amortization(self, name, a_type) -> None:
        self.table[name].extraordinary_amortization(a_type)
    
    def refresh(self) -> None:
        for loan in self.table.values():
            loan.refresh()


def calculate_payment_price(pv, n, i):
    p = pv * (  ( (1+i)**n * i ) / ( (1+i)**n - 1 )  )  
    print(f'Payment: {p:.2f}')
    return p

class Loan:#UM EMPRESTIMO, SE PESQUISA PELA CHAVE MES PARA ACHAR UM PAYMENT
    def __init__(self, amount, term, interest_rate, system):
        self.amount = amount
        self.term = term
        self.interest_rate = interest_rate
        self.payment_list = {}
        if system == '1' or system == 1 or True:
            
            self.system = 'Price'
            saldo_devedor = self.amount

            for mouth in range(1, self.term+1):               
                prestacao = calculate_payment_price(
                        pv=self.amount,
                        n=self.term,
                        i=self.interest_rate/100)
                juros = saldo_devedor * self.interest_rate/100
                amortizacao = prestacao - juros
                #saldo_devedor = saldo_devedor - amortizacao
                

                print(f'Total: {self.amount}')
                print(f'Term: {self.term}')
                print(f'Interest rate (%): {self.interest_rate/100}')
                print('--------****------')
                print(f'-Prestação: {prestacao}')
                print(f'-Juros: {juros}')
                print(f'-Amortização: {amortizacao}')
                print(f'-Saldo devedor: {saldo_devedor}')
                print(f'-Mes: {mouth}')
                print('_________________________________________________________*')

                self.payment_list[mouth] = Payment(              
                    mouth=mouth, 
                    value_of_installment=prestacao,
                    interest=juros,
                    amortized_payment=amortizacao,
                    debit=saldo_devedor,
                    status='PENDING'
                )
                saldo_devedor = saldo_devedor - amortizacao


        elif system == '2' or system == 2:
            self.system = 'SAC'
            self.payment_list = self.initial_values_price()

    def show(self):
        print(f'Amount: {self.amount}')
        print(f'Term: {self.term}')
        print(f'Interest rate (%): {self.interest_rate}')
        print(f'System: {self.system}')
        print('***Payment list***')
        for mouth in range(1, self.term+1):
            self.payment_list[mouth].show()
            #print(self.payment_list)
    
    def ordinary_payment(self):
        for mouth in range(1, self.term+1):
            if self.payment_list[mouth].status == 'PENDING':
                self.payment_list[mouth].pay()
                break
    
    def extraordinary_amortization(self, a_type):#ESTA IGUAL AO PAGAMENTO NORMAL
        if a_type == 'term reduction':
            for mouth in range(1, self.term+1):
                if self.payment_list[mouth].status == 'PENDING':
                    self.payment_list[mouth].pay()
                    break
        elif a_type == 'installment value':
            for mouth in range(1, self.term+1):
                if self.payment_list[mouth].status == 'PENDING':
                    self.payment_list[mouth].pay()
                    break

   
    def refresh(self):#implementar o calculo dos novos valores
        pass


class Payment:#PAGAMENTO DE UM MES, UMA LINHA POR MES
    def __init__(self, mouth, value_of_installment=10, interest=10, amortized_payment=10, debit=10, status='PENDING'):
        self.mouth = mouth# 1 mes do emprestimo
        self.value_of_installment = value_of_installment# valor da prestação
        self.interest = interest# valor pago em juros naquele mes
        self.amortized_payment = amortized_payment#valor amortizado naquele mes
        self.debit = debit# atualizado
        self.status = status#status da prestação
    
    def show(self):
        print(f'''
        Mouth: {self.mouth}
        Value of installment: {self.value_of_installment}
        Interest: {self.interest}
        Amortized payment: {self.amortized_payment}
        Debit: {self.debit:.6f}
        Status: {self.status}''')
    
    def pay(self):
        self.status = 'PAID'