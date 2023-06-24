import requests

url = "https://skyengpublic.notion.site/6-2-447316c27f204aeeb01aa70a4e01f414"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

req = requests.get(url, headers)
src = req.text

with open("index.html", "w", encoding='utf-8') as file:
    file.write(src)
