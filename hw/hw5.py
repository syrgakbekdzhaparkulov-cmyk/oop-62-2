import requests

def check_simba_server():
    print(f"--- Проверка связи банка Simba с внешним миром ---")
    
    try:
        response = requests.get('https://api.github.com')
        if response.status_code == 200:
            print("Связь установлена!")
            print(f"Сервер ответил: {response.json()['emojis_url'][:40]}...")
        else:
            print(f"Ошибка сервера: {response.status_code}")
            
    except Exception as e:
        print(f"Не удалось подключиться: {e}")

if __name__ == "__main__":
    check_simba_server()