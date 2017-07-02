import csv
from datetime import datetime

with open("trade_data.csv", "r") as file:
    reader = csv.DictReader(file, quoting=csv.QUOTE_NONNUMERIC)
    fieldnames = reader.fieldnames
    dict_list = []
    for line in reader:
        line["trade_date"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        dict_list.append(line)

with open("trade_data.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    writer.writerows(dict_list)
