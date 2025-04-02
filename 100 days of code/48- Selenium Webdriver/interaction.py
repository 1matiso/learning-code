## printar o número de artigos da wikipedia

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

##aprendendo como clicar em um link usando click()
# artigos = driver.find_element(By.XPATH, value = "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/ul/li[2]/a[1]")
# print(artigos.text)
# artigos.click()


##aprendendo a escrever e usar uma key
# search = driver.find_element(By.NAME, value = "search")
# search.send_keys("Python", Keys.ENTER)


##testando colocar os dados num site
driver.get("https://secure-retreat-92358.herokuapp.com/")



##opção preguiçosa
#first_name.send_keys("Matheus", Keys.TAB, "Tambasco", Keys.TAB, "mtambascof@gmail.com")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value = "lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("Matheus")
last_name.send_keys("Tambasco")
email.send_keys("mtambascof@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()







