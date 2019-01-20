# How to use the classifier

To classify an image ``yourimage.jpg`` you can use following command line code:

First start the server by running ``python beton_server.py``, which initiates a server that runs on port 5000 by default. Next, send the image to the classifier using
``curl -X POST -F image=@yourimage.jpg "http://localhost:5000/beton"``

This last line returns a json response ``{"scheur": True/False, "success"=True/False}``,
the "success" key denotes whether the image was succesfully classified, the "scheur" key denotes whether a tear in the concrete was detected.
