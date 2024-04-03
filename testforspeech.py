import requests

url = "https://voicerss-text-to-speech.p.rapidapi.com/"
querystring = {"key": "6715231320574b7abd4a822d356445d0"}

payload = {
    "src": "",
    "hl": "en-us",
    "r": "0",
    "v": "John",
    "c": "mp3",
    "f": "48khz_8bit_stereo"
}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "f5a8740e35msh8878ed03198b554p1caabejsnaddf4cf093a5",
    "X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers, params=querystring)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the response content to a file
    with open("output.mp3", "wb") as file:
        file.write(response.content)
    print("File saved successfully as output.mp3")
else:
    print(f"Error: {response.status_code} - {response.text}")
