#match statment
sevice=input("Please enter a sevice number (1/2/3):")


match sevice:
    case "1":
        print("You have selected service 1")
        def Deposit_money():
          print("Please enter the amount you want to deposit:")
          Deposit_money=input()
          print("The deposit amount is",Deposit_money)
        Deposit_money()

    case "2":
        print("You have selected service 2")
        def Withdraw_money():
          print("Please enter the amount you want to withdraw:")
          Withdraw_money=input()
          print("The withdraw amount is",Withdraw_money)
        Withdraw_money()

    case "3":
        print("You have selected service 3")
        def Transfer_money():
          print("Please enter the amount you want to transfer:")
          Transfer_money=input()
          print("The transfer amount is",Transfer_money)
        Transfer_money()

