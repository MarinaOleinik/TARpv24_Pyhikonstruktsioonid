import json

andmed = {"nimi": "Anna", "vanus": 25, "abielus": False}
json_string = json.dumps(andmed, indent=2, sort_keys=True)
print(json_string)

#lisame failisse
with open("andmed.json", "w") as f:
    json.dump(andmed, f)

#loeme failist
with open("andmed.json","r") as f:
    andmed_failist=json.load(f)
print(andmed_failist)

klass = {
"opetaja": "Tamm",
"opilased": [
{"nimi": "Mari", "hinne": 5},
{"nimi": "Juri", "hinne": 4}
] }
with open("klass.json", "w") as f:
    json.dump(klass, f, indent=2)

import requests
linn = input("Sisesta linna nimi: ")
api_voti = "e37a5e5a9a44ad82935cc683dceced1a" #"SINU_API_VÕTI"
url =f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_voti}&units=metric&lang=et"
vastus = requests.get(url)
andmed = vastus.json()
if andmed.get("cod") != "404" and "main" in andmed and "weather" in andmed:
    peamine = andmed["main"]
    temperatuur = peamine["temp"]
    niiskus = peamine["humidity"]
    kirjeldus = andmed["weather"][0]["description"]
    tuul = andmed["wind"]["speed"]
    print(f"Ilm linnas {linn}:")
    print(f"Temperatuur: {temperatuur}C")
    print(f"Kirjeldus: {kirjeldus.capitalize()}")
    print(f"Niiskus: {niiskus}%")
    print(f"Tuule kiirus: {tuul} m/s")
else:
    print("Linna ei leitud.")
with open("ilm.json", "w", encoding="utf-8") as f:
    json.dump(andmed, f, ensure_ascii=False, indent=4)

#keerulised andmed
with open('andmed_keerulised.json', 'r', encoding='utf-8') as f:
    andmed = json.load(f)
andmed.append(
{
    "nimi": "Tiiu",
    "vanus": 30,
    "abielus": False,
    "lapsed": [],
    "koduloomad": [ "kass" ],
    "autod": [
      
    ]
  }
)
with open("andmed_keerulised.json", "w", encoding="utf-8") as f:
    json.dump(andmed, f, ensure_ascii=False, indent=4)
sisestatud_nimi = input("Sisesta nimi: ")
leitud = False
for kasutaja in andmed:
    if kasutaja.get("nimi") == sisestatud_nimi:
        leitud=True
        autod= kasutaja.get("autod", [])
        if autod:
            print(f"\nAutod kasutajal {sisestatud_nimi}:")
            for auto in autod:
                print(f"- {auto['muudel']} ({auto['varv']}, {auto['joud']} hj), number: {auto['number']}")
        else:
            print("Selle inimesel ei ole autosid.")
        break
if not  leitud:
    print("Selle nimega kasutajat ei leitud.")