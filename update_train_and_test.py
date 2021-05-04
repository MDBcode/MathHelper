import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


for index_label, row_series in train.iterrows():
    for i in range(0, len(train.columns)-1):
        train.at[index_label, "pixel" +
                 str(i)] = abs(row_series["pixel"+str(i)] - 255)

train.to_csv(r"train.csv", index=False)

for index_label, row_series in test.iterrows():
    for i in range(0, len(test.columns)-1):
        test.at[index_label, "pixel" +
                str(i)] = abs(row_series["pixel"+str(i)] - 255)

test.to_csv(r"test.csv", index=False)
