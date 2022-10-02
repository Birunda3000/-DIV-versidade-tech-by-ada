import sys

class Menu:
    def run(self, storage) -> None:
        """List menu options and execute selected option"""
        _exit_ = False
        while not _exit_:
            print(
            '''
    ==================
    ===Python loans===
    ==================

    1) Register loan
    2) Consult extract
    3) Ordinary payment
    4) Extraordinary amortization
    5) Exit
    ==================\n
            '''
            )
            try:
                sys.stdout.flush()
                option = int(input('Enter option: '))
            except:
                print('Invalid option')
                continue

            print()
            if option == 1:
                print('*Register loan*')
                storage.register_loan()
            elif option == 2:
                print('*Consult extract*')
                storage.consult_extract()
            elif option == 3:
                print('*Ordinary payment*')
                storage.ordinary_payment()
            elif option == 4:
                print('*Extraordinary amortization*')
                storage.extraordinary_amortization()
            elif option == 5:
                print('Thank you for using Python loans\nGoodbye!')
                _exit_ = True
            else:
                print('Invalid option')
            
            storage.refresh()
            print(
            '''
==========================================================
==========================================================
            '''
            )