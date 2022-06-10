import uuid
from flask import Flask
import os
import psycopg
import numpy as np
from keras.preprocessing import image
from tensorflow.keras.models import load_model
# from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, make_response
import tensorflow as tf
import os

labels = ["rendang", "ayam dada", "ayam paha", "bakso", "burger", "gado-gado", "kebab", "kentang", "makaroni","roti", "sosis", "takoyaki"]

def get_db():
    conn = psycopg.connect(
        host="34.101.73.30",
        dbname="caltrack",
        # user=os.environ['postgres'],
        # password=os.environ['admin'])
        user="postgres",
        password="admin"
    )
    return conn


def predict_image(IMG_PATH):
    model = load_model("my_model_92.h5")

    # img = image.load_img(IMG_PATH, target_size=(500, 375, 3))
    # x = image.img_to_array(img)
    img = tf.keras.utils.load_img(IMG_PATH, target_size=(500, 375, 3))
    x = tf.keras.utils.img_to_array(img)

    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)

    results = classes.flatten()
    # return results
    for (label, result) in zip(labels, results):
        if (result == 1):
            return label

app = Flask(__name__)


@app.route('/predict', methods=["POST"])
def predict_process():
    img = request.files["img"]

    img_file = str(uuid.uuid1()) + ".jpg"
    img.save(img_file)

    predict_result = predict_image(img_file)
    print(predict_result)

    os.remove(img_file)

    conn = get_db()
    cur = conn.cursor()
    result = cur.execute("select * from foods where name like (%s)", [predict_result])
    rows = result.fetchall()

    resp = jsonify({'message': 'FIle berhasil di upload'})
    resp.status_code = 201
    for r in rows:
        result = r
        print(r)

    resp = jsonify({'message': 'FIle berhasil di upload'})
    resp.status_code = 201
    return make_response(jsonify(result))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


