import random
import string
import getpass

def generate_password(site_name):
    
    max_length = 16

    
    valid_chars = string.ascii_letters + string.digits + string.punctuation

    # パスを生成する
    password_length = random.randint(8, max_length)
    password = ''.join(random.choice(valid_chars) for i in range(password_length))

    # パスをファイルに保存する
    with open("passwords.txt", "a") as f:
        f.write(f"{site_name} : {password}\n")

    
    return password

def save_password():
    # パスを生成するためのサイト名を入力する
    site_name = input("Which website's password would you like to generate? ")

    # パスを生成
    password = generate_password(site_name)

    # 生成されたパスワードを表示
    print("Generated password: ", password)

def show_saved_passwords():
    # パスワードをファイルから読み込む
    with open("passwords.txt", "r") as f:
        passwords = f.readlines()

    # 保存されたパス表示
    for password in passwords:
        print(password.strip())


choice = input("What would you like to do? (generate/save/show): ")

if choice.lower() == "generate" or choice.lower() == "save":
    save_password()
elif choice.lower() == "show":
    show_saved_passwords()
else:
    print("Invalid choice.")
