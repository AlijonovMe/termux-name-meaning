import requests
from colorama import Fore, init

init(autoreset=True)

name = input(Fore.BLUE + "Ismingizni kiriting: ")

url = f"https://api.alijonov.uz/api/ismlar.php?name={name}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if data['success']:
        for item in data['data']:
            print(f"{Fore.GREEN}Ismi: {item['name']}\nMa'nosi: {item['meaning']}")
    else:
        print(f"{Fore.RED}Ism topilmadi.")
else:
    print(f"{Fore.RED}Xatolik: {response.status_code}")
