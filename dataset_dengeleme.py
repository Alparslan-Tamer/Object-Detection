import pandas as pd
import os
import config

files_names = os.listdir("Custom_Dataset/labels")  # dir is your directory path
number_files = len(files_names)
print(number_files)

file_names = []
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

    deneme = []
    for k in range(counter):
        label = content.split("\n")
        label = int(label[k].split(" ")[0])
        deneme.append(label)

    if labels.count("Durak_Isareti") > 900 and (4 in deneme):
        pass
    elif labels.count("Sola_Mecburi_Donus") > 900 and (8 in deneme):
        pass
    elif labels.count("Ileri_ve_Saga_Donus") > 800 and (18 in deneme):
        pass
    elif labels.count("Saga_Donulemez") > 1000 and (5 in deneme):
        pass
    else:
        for l in deneme:
            labels.append(config.CUSTOM_CLASSES[l])
        file_names.append(files_names[i])
        

df = pd.DataFrame({'siniflar': labels})
new_file = pd.DataFrame({'labels': file_names})
new_file.to_csv("new_train.csv", index=False, header=False)
print(df.value_counts(ascending=True))