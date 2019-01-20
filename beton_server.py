# import the necessary packages
from PIL import Image
from keras.models import model_from_json
import numpy as np
import tensorflow as tf
import flask
import io

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
# global graph,model
# graph = tf.get_default_graph()
# model = None


def load_model():
    # load the pre-trained Keras model
    global model
    global graph
    with open('model_architecture.json', 'r') as f:
        model = model_from_json(f.read())
    model.load_weights("weights_test.hdf5")
    graph = tf.get_default_graph()


def prepare_image(image, target):
    # resize the input image
    image = image.resize(target)
    image = np.array(image)
    image = image / 255
    image = np.expand_dims(image, axis=0)

    # return the processed image
    return image


@app.route("/beton", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # preprocess the image and prepare it for classification
            image = prepare_image(image, target=(64, 64))

            with graph.as_default():
                # classify the input image
                preds = model.predict(image)
                print(preds)
                if preds >= 0.5:
                    data["scheur"] = True
                else:
                    data["scheur"] = False

                # indicate that the request was a success
                data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    load_model()
    app.run()
