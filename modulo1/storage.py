import pprint

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
        pass

    def refresh(self) -> None:
        pass


class Table:
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


class Loan:
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
                value_of_installment=10, 
                interest=10,
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


class Payment:
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

