def main():
    user_balance= float(input("How much would you like to balance? "))

  


    def display_balance():
        balance= current_balance()
        print(format(balance, '.2f'))

    def add_to_balance():
        addition= float(input("How much would you like to add? "))
        user_balance= current_balance() + addition
        print(f'Your new balance is {user_balance}')
        return user_balance


    def subtract_balance():
        subtraction= float(input("How much would you like to subtract? "))
        user_balance=  current_balance() - subtraction
        print(f'Your new balance is {user_balance}')
        return user_balance


main()