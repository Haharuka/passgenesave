import random
import string
import getpass

def generate_password(site_name):
    # パスワードの長さの最大値を決める
    max_length = 16

    # 使用できる文字を決める
    valid_chars = string.ascii_letters + string.digits + string.punctuation

    # パスワードを生成する
    password_length = random.randint(8, max_length)
    password = ''.join(random.choice(valid_chars) for i in range(password_length))

    # パスワードをファイルに保存する
    with open("passwords.txt", "a") as f:
        f.write(f"{site_name} : {password}\n")

    # パスワードを返す
    return password

def save_password():
    # パスワードを生成するためのサイト名を入力する
    site_name = input("Which website's password would you like to generate? ")

    # パスワードを生成する
    password = generate_password(site_name)

    # 生成されたパスワードを表示する
    print("Generated password: ", password)

def show_saved_passwords():
    # 保存されたパスワードをファイルから読み込む
    with open("passwords.txt", "r") as f:
        passwords = f.readlines()

    # 保存されたパスワードを表示する
    for password in passwords:
        print(password.strip())

# パスワードを保存するか、保存されたパスワードを見せるかを選択する
choice = input("What would you like to do? (generate/save/show): ")

if choice.lower() == "generate" or choice.lower() == "save":
    save_password()
elif choice.lower() == "show":
    show_saved_passwords()
else:
    print("Invalid choice.")
