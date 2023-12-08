import requests
key = "93789642-2750-49eb-bef1-c576e4ee0b5f"  # TODO подставьте значение вашего ключа доступа к API
lat = "59.93"  # широта в градусах
lon = "30.31"  # долгота в градусах

url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
headers={"X-Yandex-API-Key": f"{key}"}

response = requests.get(url, headers=headers)
print(response.json())

