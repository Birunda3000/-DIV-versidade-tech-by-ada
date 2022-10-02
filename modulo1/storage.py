
class Storage:
    def __init__(self):
        self.db = Table()

    def register_loan(self) -> None:
        name = input('Enter name: ')
        amount = float(input('Enter amount: '))
        term = int(input('Enter payment term (in mouths): '))
        interest = float(input('Enter interest rate: '))
        system = input('Enter payment system 1 to Price and 2 to SAC: ')
        while True:
            if system == '1':
                system == 'Price'
                break
            elif system == '2':
                system == 'SAC'
                break
            else:
                print('Invalid system')
                system = input('Enter system (1 or 2): ')
        self.db.add(name=name, amount=amount, term=term, interest=interest, system=system)

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
    
    def add(self, name, amount, term, interest, system) -> None:
        self.table[name] = Loan(amount, term, interest, system)
    
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


class Loan:#UM EMPRESTIMO, SE PESQUISA PELA CHAVE MES PARA ACHAR UM PAYMENT
    def __init__(self, amount, term, interest, system):
        self.amount = amount
        self.term = term
        self.interest = interest
        self.system = system
        self.payment_list = {}
        #******************SEARCH FOR A MOUTH****************
        for i in range(1, term+1):
            self.payment_list[i] = Payment(
                mouth=i, 
                value_of_installment=amount/term, 
                interest=self.interest,
                amortized_payment=10,
                saldo_devedor=10,
                status='PENDING'
        )

    def show(self):
        print(f'Amount: {self.amount}')
        print(f'Term: {self.term}')
        print(f'Interest: {self.interest}')
        print(f'System: {self.system}')
        print('***Payment list***')
        for mouth in range(1, self.term+1):
            self.payment_list[mouth].show()
    
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
    
    def refresh(self):
        pass


class Payment:#PAGAMENTO DE UM MES, UMA LINHA POR MES
    def __init__(self, mouth, value_of_installment=10, interest=10, amortized_payment=10, saldo_devedor=10, status='PENDING'):
        self.mouth = mouth# 1 mes do emprestimo
        self.value_of_installment = value_of_installment# valor da prestação
        self.interest = interest# valor pago em juros naquele mes
        self.amortized_payment = amortized_payment#valor amortizado naquele mes
        self.saldo_devedor = saldo_devedor#saldo devedor atualizado
        self.status = status#status da prestação
    
    def show(self):
        print(f'''
        Mouth: {self.mouth}
        Value of installment: {self.value_of_installment}
        Interest: {self.interest}
        Amortized payment: {self.amortized_payment}
        Saldo devedor: {self.saldo_devedor}
        Status: {self.status}''')
    
    def pay(self):
        self.status = 'PAID'

