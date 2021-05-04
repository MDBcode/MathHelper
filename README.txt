This app evaluates simple math expressions using machine learning model for digit (0-9) and operator (+,-,x,/,(,)) classification and computer vision module for symbol detection and extraction.

Procedure:

Open app in web browser on your smartphone and take capture of a handwritten math expression on a blank paper, using phone camera.
This photo is passed into backend where scanner.py detects digits and operators in the expression, extracts them as single images and passes them to the model.
Then, the model predicts the labels of these images and forms the corresponding string of the given expression. Later, that string is evaluated and the result is shown in the browser.

Instructions for running MathHelper app:

1. clone repo and open with the editor(e.g. VSCode)
2. ensure your PC and smartphone are connected to the same local network (e.g. wifi)
3. run "app.py" script
4. find your IPv4 adress (click on wifi properties)
5. open chrome on your smartphone and type http://<your IPv4 adress>:5000 ; this will run app in web browser on your phone
6. click "Odaberi datoteku" button to take capture
7. click "Upload" button to upload image and get result
