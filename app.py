from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline

# Initializing Flask App
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def homePage():
    return render_template("index.html")

# Route to train the prediction
@app.route("/train", methods = ["GET"])
def training():
    os.system("python main.py")
    return "Training Successful!"

# Route to show the prediction in a Web UI
@app.route("/predict", methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            # Reading the inputs given by the user
            fixed_acidity = float(request.form["fixed_acidity"])
            volatile_acidity = float(request.form["volatile_acidity"])
            citric_acid = float(request.form["citric_acid"])
            residual_sugar = float(request.form["residual_sugar"])
            chlorides = float(request.form["chlorides"])
            free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
            total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
            density = float(request.form["density"])
            pH = float(request.form["pH"])
            sulphates = float(request.form["sulphates"])
            alcohol = float(request.form["alcohol"])

            data = [fixed_acidity,
                    volatile_acidity,
                    citric_acid,
                    residual_sugar,
                    chlorides,
                    free_sulfur_dioxide,
                    total_sulfur_dioxide,
                    density,
                    pH,
                    sulphates,
                    alcohol]
            
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template("results.html", prediction = str(predict))
        
        except Exception as e:
            print(f"The Exception Message is: {e}")
            return "Something is Wrong!"
    else:
        return render_template("index.html")

# Hugging Face Checking
@app.route("/hf")
def huggingface():
    return """
    Welcome to the MLOps Flask App on Hugging Face Spaces!\n
    Hugging Face Route is working!
    """
    
if __name__ == "__main__":
    # app.run(host = "0.0.0.0", port = 8080)
    # 7860 is the Hugging Face Spaces default port to listen on
    app.run(host = "0.0.0.0", port = 7860, debug = True)