# how to use

download [all-in-one.zip](https://github.com/HaoleiH/AI-driven-projects/releases/tag/v0.2). this zip file contains a portable python environment and the code need to start the local website.

unzip. double-click message.bat, give permission to python.exe in the pop-up window.

you will see it running on 3 addresses. 
use the last one, the one below "http://127.0.0.1:5000".
any device in local network should be able to visit that address.

the default password is 2887,
you can change it in app.py

the public folder stores the webpage.
the uploads folder stores the images you pasted.
data.json store the chat history.

you can delete uploads and data.json to clear chat history.
DO NOT delete public.

# what it is for

it is a local network picture and text sharing web server app. after clicking message.bat, it will run a simple python web server to serve public\index.html. you can access it in browser from local network using your other devices like cellphone. the website address is same as the one you used in your PC.

The front end is public\index.html. back end is app.py. all other files are python environment packed by conda-pack.

# if you have python in your local environment

make sure you have flask installed, or

> pip install flask

download app.py and public, put them in same directory, directly run 

> python app.py

then the webserver is running.

# result

![screenshot](./Screenshot1.png)
