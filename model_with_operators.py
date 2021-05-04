import tensorflow as tf
from tensorflow import keras
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


def processData(data, label):
    data.columns = ["pixel" + str(i)
                    for i in range(0, len(data.columns))]
    data.insert(loc=0, column="label", value=label)
    train_set, test_set = train_test_split(data, test_size=0.2, random_state=1)
    test_set = test_set.drop("label", 1)
    global train, test
    train = train.append(train_set, ignore_index=True)
    test = test.append(test_set, ignore_index=True)


times = pd.read_csv("times.csv")
div = pd.read_csv("div.csv")
plus = pd.read_csv("plus.csv")
minus = pd.read_csv("minus.csv")
bracket_l = pd.read_csv("bracket_l.csv")
bracket_r = pd.read_csv("bracket_r.csv")

# categorical: + = 10, - = 11, x = 12, / = 13, ( = 14, ) = 15
processData(times, 12)
processData(div, 13)
processData(plus, 10)
processData(minus, 11)
processData(bracket_l, 14)
processData(bracket_r, 15)

train = train.sample(frac=1).reset_index(drop=True)
test = test.sample(frac=1).reset_index(drop=True)
# print(train)

image = train.iloc[:, 1:]
lbl = train.iloc[:, 0:1]
img = image.values
img = img.reshape(-1, 28, 28, 1)
test_img = test.values
test_img = test_img.reshape(-1, 28, 28)

# print(img.shape, test_img.shape)

xtrain, xtest, ytrain, ytest = train_test_split(
    img, lbl, test_size=0.2, random_state=1)

xtrain = xtrain/255.0
xtest = xtest/255.0

grp = [xtrain, xtest, ytrain, ytest, test_img]
print([e.shape for e in grp])
print([type(e) for e in grp])

ytrain = ytrain.values.flatten()
ytest = ytest.values.flatten()

grp = [xtrain, xtest, ytrain, ytest, test_img]
print([e.shape for e in grp])
print([type(e) for e in grp])

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32, kernel_size=(3, 3),
                              activation='relu', input_shape=(28, 28, 1)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Dropout(0.25))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(16, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(xtrain, ytrain, epochs=2)

test_loss, test_acc = model.evaluate(xtest, ytest)
print('Test accuracy:', test_acc)

results = model.predict(xtest)
results = np.argmax(results, axis=1)
print(results)

model.save("saved_model.h5")
