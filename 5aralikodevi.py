#02200201006 Samed Sonkaya
#Bu kodumda place.dog'dan rastgele bir görseli alıp isteğin başarılı olup olmadığını kontrol edip(status kodu olarak 200 olması) başarılıysa resimi indiriyor, başarılı değilse uyarı mesajı veriyor
import requests

url = "https://place.dog/300/200"
response = requests.get(url)

if response.status_code == 200:
    with open("5aralik_test_image.jpg", "wb") as file:
        file.write(response.content)
    print("Image downloaded successfully.")
else:
    print(f"Error: {response.status_code}")