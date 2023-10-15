# 🖨️ quick-print

This is a very niche thing I made. Berkeley has this wonderful facility called the [Open Computing Facility](https://www.ocf.berkeley.edu/); among other things, they have free printing for students. However, you need to print from their computers. For me, logging into my email can be a bit of a hassle (I keep forgetting my password!). So I over-engineered this thing.

Here's what it does:

* Creates a temporary `print` directory.
* Creates a Flask web server that serves files from that directory.
* Uses `ngrok` to create a tunnel to that web server.

And then I can get my files! Once I quit the program it deletes the `print` and takes down the web server.

<img width="682" alt="Screenshot 2023-10-14 at 8 49 28 PM" src="https://github.com/sampoder/quick-print/assets/39828164/8932649e-9c27-46e7-ae15-0366df419102">