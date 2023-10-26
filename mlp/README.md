# Multi-Layer Perceptron

## Table of contents

- [General info](#general-info)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Coding](#coding)
- [Testing](#testing)
- [Deployment](#deployment)
- [Standard](#standard)

## **General info**

This example implements a multi layer perceptron network for classifying patients into two categories, diabetes patient or not. The trained model is wrapped in a Flask api to make inference accessible through a rest API. Please note that both training script and the flask implementation are done for beginers. Hence, certain development and ml best practices (eg: validation of model against a validation test etc.) have been excluded. They will be gradually introduced in the upcoming implementations.

## **Prerequisites**
This script can be run both locally and in a cloud environment like Google Colab. 

### - Python

Google Colab comes with pre-installed python, so no need to install manually. If you run this locally, make sure that you have Python installed.
- `$ python --version` to check the python version.

### - Weights & Biases

[Weights & Biases](https://wandb.ai/site) is used for monitoring the training.

- `$ pip install wandb -qU` in local environment and `$ !pip install wandb -qU` in colab to install

### - Flask

Selected python framework for REST API development. [Flask](https://flask.palletsprojects.com/en/3.0.x/) is a micro framework for web application development

- `$ pip install flask` to install

## **Setup**

### Create a Python virtual environment and activate

We should always maintain isolated environments for projects to avoid issues with python package versions etc. (no need to do in Colab)

- `$ cd mlp` from thr project root

- `$ python -m venv <env-name>` to create an environment

- `$ source <env-name>/bin/activate` to activate the environment

### Training

Provide the correct paths in `mlp_training.ipynb` file and execute the training script.

### Flask APP

After training and saving the model artifacts in the model folder, run `$ python app.py` to start the flask server for inference.

- The server will be available locally on `localhost:5000` and you can call the endpoint `http://127.0.0.1:5000/predict` to call the api.

- The api request should be a `POST` request and the post body should look like this. 
  ```{
    "no_pregnency": 3,
    "glucose": 300,
    "bp": 100,
    "skin_fold": 342,
    "insulin": 34,
    "bmi": 23.4,
    "age": 43
  }
  ```

- If everything went well, you should get a reponse with the prediction and the probability.

Experiment with the implementation and reach out to me if you got any issues.

Happy Coding!