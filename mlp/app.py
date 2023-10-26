from flask import Flask, request
import torch
from model.model import Perceptron

app = Flask('diabetics')

# Import the model
perceptron = Perceptron(input_features=7)

# loading the model artifacts
perceptron.load_state_dict(torch.load('model/perceptron.pth'), strict=False)

# Putting the model in evaluation mode
perceptron.eval()

# Routes
@app.route('/predict', methods=['POST'])
def predict_diabetics():

  # Receive input data from the user
  response_body = request.get_json()

  print(f"request body:  {response_body}")

  values = list(response_body.values())

  print(f"values: {values}")

  with torch.no_grad():
    input_tensor = torch.tensor(values, dtype=torch.float)

    prediction = perceptron(input_tensor)

    print(f"prediction ====> {prediction.item()}")

    category = 'yes' if prediction > 0.5 else 'no'

  return {
    'diabetics_patient': category,
    'probability': prediction.item()
  }

if __name__ == '__main__':
  app.run(debug=True)