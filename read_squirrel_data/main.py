import pandas

data = pandas.read_csv("weather/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


colors = ["Gray", "Black", "White"]
fur_color = data["Primary Fur Color"]
squirrels = []

for color in colors:
    squirrels.append(
        {
            "total": len(data[data["Primary Fur Color"] == color]),
            "color": color,
        }
    )


new_data = pandas.DataFrame(squirrels)
new_data.to_csv("weather/squirrel_count.csv")

