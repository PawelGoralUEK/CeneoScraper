import requests

respons = requests.get("https://www.ceneo.pl/71299209#tab=reviews")

print(respons.text)