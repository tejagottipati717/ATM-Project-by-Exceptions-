from ATMOperations import deposit,withdraw,balenq
from ATMMenu import menu
from ATMExcept import DepositError,WithdrawError,InsuffFundError
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("Don't try to Deposit alnums,str's and symbols")
                except DepositError:
                    print("Don't Enter -ve and zero as Deposit Amount")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("Don't try to Withdraw alnums,str's and symbols")
                except WithdrawError:
                    print("Don't Enter -ve and Zero as Withdraw Amount")
                except InsuffFundError:
                    print("Ur Account xxxxxxxxx123 does not have Suff Funds")
            case 3:
                balenq()
            case 4:
                print("Thanx for using Application")
                break
            case _:
                print("Ur Selection of operation is wrong---try again")

    except ValueError:
        print("Don't Enter ALNUM's,STR's and Symbols for Choice--try again")
