# Meower3DS
Meower client that works on O3DS consoles!

# How does it work?
Your computer will connect to Meower's server, and run an API that your 3DS can talk to, and your 3DS will open up the HTML client that handles sending requests. This project is barebones, intended to be a "proof of concept" of sorts, however you can get and create posts.

# Setup
Download this repository (you could use the "Download .ZIP" button or git), change the variables user, pswd, and hostip in main.py to their respective values, then change the ip in index.html to it's respective value.

Run main.py, it will connect to Meower and ready the API. Then run an http server (something like `python3 -m http.server` should do), and open it on your 3DS. You are now ready to use Meower3DS!
