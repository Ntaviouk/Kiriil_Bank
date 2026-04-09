from cesar import encrypt

SECRET_KEY = 8

def save_data(bank):
    file = open("bank.txt", "w")
    file.write(str(bank))
    file.close()


def load_data():
        file = open("bank.txt", "r")
        data = file.read()
        file.close()
        return eval(data)


def add_user(bank):
    user_id = int(input("ID: "))
    if user_id in bank:
        print("User already exist")
        return

    name = input("Ім'я: ")
    balance = 0
    password = input("Enter pass: ")
    hashed_password = encrypt(password, SECRET_KEY)

    bank[user_id] = {
        "name": name,
        "balance": balance,
        "password": hashed_password
    }
    save_data(bank)




def add_money(bank):
    user_id = int(input("ID: "))

    if user_id not in bank:
        print("User not found")
        return
    
    


    amount = float(input("Enter summa: "))

    bank[user_id]["balance"] += amount
    save_data(bank)

def withdraw_money(bank):
    user_id = int(input("ID: "))

    if user_id not in bank:
        print("User not found")
        return

    password = input("Enter pass: ")
    hashed_password = encrypt(password, SECRET_KEY)
    if hashed_password != bank[user_id]["password"]:
        print("Incorrect password")
        return
    
    amount = float(input("Enter summa: "))
    if bank[user_id]["balance"] >= amount:
        bank[user_id]["balance"] -= amount
    else:
        print("Not money")
    save_data(bank)


     

if __name__ == "__main__":
    while True:
        bank = load_data()
        print("-------BANK-------")
        print("1. Add User")
        print("2. Add Money")
        print("3. Withdraw Money")
        print("4. All users")
        print("0. EXIT")

        a = int(input("Enter: "))

        match a:
            case 1:
                add_user(bank)
            case 2: 
                add_money(bank)
            case 3: 
                withdraw_money(bank)



          
          

     
     