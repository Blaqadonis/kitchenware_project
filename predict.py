import requests
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.xception import preprocess_input
import tensorflow.lite as tflite
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Loading the model
interpreter = tflite.Interpreter(model_path='kitchenware_model.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
input_index = input_details[0]['index']
output_details = interpreter.get_output_details()
output_index = output_details[0]['index']

# Labels for the model's output
labels = {
    0: 'cup',
    1: 'fork',
    2: 'glass',
    3: 'knife',
    4: 'plate',
    5: 'spoon'
}

@app.route('/predict', methods=['POST'])
def predict():
    # Getting the image URL from the request
    data = request.get_json()
    url = data.get('img_url')
    if not url:
        return jsonify(error="No 'img_url' parameter provided"), 400
    # Downloading the image
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
     # Resize the image to 299x299
    img = img.resize((299, 299))
    # Preprocess the image
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    # Invoke the model
    interpreter.set_tensor(input_index, x)
    interpreter.invoke()
    # Getting the output of the model
    preds = interpreter.get_tensor(output_index)
    prediction = np.argmax(preds[0])
    # Return the label
    label = labels[prediction]
    return jsonify({'prediction': label})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
