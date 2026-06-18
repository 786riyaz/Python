import requests
from bs4 import BeautifulSoup

def decode_google_doc(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    lines = [p.get_text(strip=True) for p in soup.find_all("p")]

    data = []
    i = 0

    while i + 2 < len(lines):
        try:
            x = int(lines[i])
            ch = lines[i + 1]
            y = int(lines[i + 2])

            data.append((x, y, ch))
            i += 3
        except ValueError:
            i += 1

    max_x = max(x for x, _, _ in data)
    max_y = max(y for _, y, _ in data)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, ch in data:
        grid[y][x] = ch

    for row in grid:
        print("".join(row))


decode_google_doc("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")