from ATMExcept import DepositError,WithdrawError,InsuffFundError
bal=500.0
def deposit():
    damt=float(input("Enter ur Deposit Amount:")) #ValueError--alnums,str's,symbols
    if damt<=0:
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxxxxxx123 Deposited with INR:{}".format(damt))
        print("Now Ur Account xxxxxxxxx123 Balance INR:{}".format(bal))

def withdraw():
    global bal
    wamt=float(input("Enter Ur Withdraw Amount:"))
    if wamt<=0:
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InsuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxxxxx123 Debited with INR:{}".format(wamt))
        print("Now Ur Account xxxxxxxxx123 Balance INR:{}".format(bal))

def balenq():
    print("Ur Account xxxxxxxxx123 Balance INR:{}".format(bal))