import pandas as pd

data = pd.read_csv("squirrel_data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "fur color": ["gray", "cinnamon", "black"],
    "count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count],
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_fur_color_count.csv")
