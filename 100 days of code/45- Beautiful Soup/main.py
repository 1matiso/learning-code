from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")


# heading = soup.find(name="h1", id="name")

company_url = soup.select_one(selector="p a")
print(company_url)