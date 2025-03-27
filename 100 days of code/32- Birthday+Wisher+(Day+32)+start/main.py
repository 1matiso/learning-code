from pandas import *
import datetime
import random
import smtplib

MY_EMAIL = "matheus.tambasco@gmail.com"
MY_PASSWORD = "Grandebandido4!"

data = read_csv("birthdays.csv")

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday!\n\n{contents}")



