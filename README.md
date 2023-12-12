## Flask Prediction Microservice

### Overview

This Python script runs on GCP to create a Flask app that generates a training dataset using the make_blobs function from the sklearn.datasets library. The LogisticRegression model is then fitted on the training dataset. The predict function defined in the code takes an input and generates a new dataset using make_blobs, fits the model on the new dataset, and returns a prediction in JSON format. The NpEncoder class is used to encode the NumPy arrays in the JSON output. Finally, the Flask app is run on the local server at port 8080.

### Usage
You can use the curl command to test the behavior of the Flask REST endpoint. For example, you can send a POST request to the URL http://localhost:8080/predict with an input of n_samples samples in JSON format to get a prediction in JSON format.

curl -d '{  
   "n_samples": 200
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:8080/predict | grep prediction

This command sends a POST request to the predict function with an input of 200 samples. The grep command filters the response to only show the prediction key in the JSON output. If the predict function works correctly, the output should contain the prediction key and its corresponding value.

### Dependencies
This script requires the following libraries:

* Flask

*scikit-learn

* NumPy

For now the prediction app can be called in the follwing way:

./script.sh <n_samples>.

### Makefile

This file is the recipe for setting up the environment. It installs or upgrades pip then goes ahead to install the necessary libraries and finally lints the code.
