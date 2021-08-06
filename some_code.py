import glob
import pandas as pd
import re

my_images = [f for f in glob.glob("images/*.jpg")]
df = pd.DataFrame({'images': my_images})
my_labels = []

for i in range(8905):
    list1 = df["images"][i].split("/")
    my_word = list1[1].split(".")[0]
    my_label = [f for f in glob.glob(f"labels/{my_word}.txt")]

    my_labels.append(my_label[0])

df["labels"] = my_labels
df = df.sample(frac=1).reset_index(drop=True)

df.replace(regex=r'^labels/.$', value='')

train_df = df[:7000]
test_df = df[7000:]

train_df.to_csv("deneme_train.csv", index=False, header=False)
test_df.to_csv("deneme_test.csv", index=False, header=False)

print(len(train_df))
print(len(test_df))
