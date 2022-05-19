import csv
import pandas

# TODO another way of doing the same thing with CSV Library
# data = []
# with open("weather_data.csv") as weather:
#     weather_file = weather.readlines()
#
#
# for w in weather_file:
#     new_weather = w.strip()
#     # print(new_weather)
#     data.append(new_weather)
# print(data)

# TODO another way of doing the same thing with CSV Library
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# print(temperature)

data = pandas.read_csv("weather_data.csv")
# print(max(data["temp"]))
print(data["temp"])

average_of_temp = sum(data["temp"]) // len(data["temp"])
print(f"Average Temperature of week is : {average_of_temp}")


# TODO One Way of printing complete Row from List
print(data[data.day == "Monday"])

print(data[data.temp == max(data["temp"])])

monday = data[data.day == "Monday"]
print(monday.condition)




