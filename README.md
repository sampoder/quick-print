# 🖨️ quick-print

This is a very niche thing I made. Berkeley has this wonderful facility called the [Open Computing Facility](https://www.ocf.berkeley.edu/); among other things, they have free printing for students. However, you need to print from their computers. For me, logging into my email can be a bit of a hassle (I keep forgetting my password!). So I over-engineered this thing.

Here's what it does:

* Creates a temporary `print` directory.
* Creates a Flask web server that serves files from that directory.
* Uses `ngrok` to create a tunnel to that web server.

And then I can get my files! Once I quit the program it deletes the `print` and takes down the web server.

https://github.com/sampoder/quick-print/assets/39828164/dd7b4d63-05c2-45b5-9fa9-64206c773e7a

