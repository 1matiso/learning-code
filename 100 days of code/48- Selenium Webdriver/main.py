from selenium import webdriver
from selenium.webdriver.common.by import By


##manter o chrome aberto depois que o programa fechar
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
##

driver = webdriver.Chrome(options=chrome_options)


##teste de palavra do dia em alemão
# driver.get("https://www.duden.de/wort-des-tages")
# wort_des_tages = driver.find_element(By.CLASS_NAME, value = "scene__title-link")
# print(f"Das Wort des Tages ist {wort_des_tages.text}")
##

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget time")

# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# for name in event_names:
#     print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
            "name": event_names[n].text
    }

print(events)


driver.quit()