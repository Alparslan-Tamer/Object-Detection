import pandas as pd
import os
import config

files_names = os.listdir("Custom_Dataset/labels")  # dir is your directory path
number_files = len(files_names)
print(number_files)

labels = []
for i in range(number_files):
    # Opening a file
    file = open("Custom_Dataset/labels/" + files_names[i], "r")
    counter = 0

    # Reading from file
    content = file.read()
    co_list = content.split("\n")

    for j in co_list:
        if j:
            counter += 1

    for k in range(counter):
        label = content.split("\n")
        label = int(label[k].split(" ")[0])
        labels.append(config.CUSTOM_CLASSES[label])

df = pd.DataFrame({'siniflar': labels})
print(df.value_counts(ascending=True))
