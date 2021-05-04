import tensorflow as tf
from tensorflow import keras
import numpy as np
import scanner
import solver


def boss(image):
    saved_model = keras.models.load_model("saved_model.h5")

    rez = saved_model.predict(scanner.scan(image))
    rez = np.argmax(rez, axis=1)
    print("Predicted labels: ", rez)

    string = ""
    for x in rez:
        if x == 10:
            string += "+"
        elif x == 11:
            string += "-"
        elif x == 12:
            string += "x"
        elif x == 13:
            string += "/"
        elif x == 14:
            string += "("
        elif x == 15:
            string += ")"
        else:
            string += str(x)

    print("The expression is: " + string)

    result = solver.solve_brackets_get_result(solver.to_list(string))
    print("Result: ", result)
    return result
