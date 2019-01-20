To classify an image "yourimage.jpg" you can use following command line code:

python beton_server.py # Starts the server, which runs on port 5000 by default
curl -X POST -F image=@yourimage.jpg "http://localhost:5000/beton" # send image yourimage.jpg to the classifier

This last line returns a json response {"scheur": True/False, "success"=True/False},
the "success" key denotes whether the image was succesfully classified, the "scheur" key denotes whether a tear in the concrete was detected.
