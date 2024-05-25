import requests
import json

BASE_URL = "http://legenduz.pythonanywhere.com/api/v1"


async def create_user(telegram_id, username):
    url = f"{BASE_URL}/users/"
    data = {
        "telegram_id": telegram_id,
        "username": username
    }
    headers = {
        'Content-Type': 'application/json'
    }

    check_user = f"{BASE_URL}/users/{telegram_id}/"
    check_user_response = requests.get(url=check_user)

    if check_user_response.status_code == 200:
        return True
    else:
        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        if response.status_code == 201:
            print("foydalanuvchi yaratildi")
        else:
            print("Xatolik yuz berdi", response.status_code, response.text)


async def get_user_language(telegram_id):
    url = f"{BASE_URL}/users/{telegram_id}/"

    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            user_data = response.json()
            language = user_data.get('language', {})
            if language:
                return language
            else:
                print("Language topilmadi")
        else:
            print(f"Response da xatolik {response.status_code},{response.text}")
    except Exception as e:
        print(f"Error: {e}")

    return None


async def update_language_user(user_id, language):
    url = f"{BASE_URL}/users/{user_id}/"
    data = {
        'language': language
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        check_user_response = requests.get(url=url)
        check_user_response.raise_for_status()

        if check_user_response.status_code == 200:
            response = requests.patch(url=url, data=json.dumps(data), headers=headers)
            response.raise_for_status()

            if response.status_code == 200:
                print(f"Foydalanuvchi tili yangilandi {language}")
            else:
                print(f"Xatolik yuz berdi:{response.status_code},{response.text}")
        else:
            print(f"Foydalanuvchi topilmadi")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


async def check_user_registration(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            user_data = response.json()
            phone_number, user_full_name = user_data.get('phone_number', {}), user_data.get('user_full_name', {})

            if phone_number and user_full_name is not None:
                return phone_number, user_full_name
            else:
                print(f"Foydalanuvchi raqami va username toplmadi")
        elif response.status_code == 404:
            print(f"User toplmadi")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
