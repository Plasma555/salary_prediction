import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')
model_columns_path = os.path.join(current_dir, 'model_columns.pkl')

model = pickle.load(open(model_path, 'rb'))
model_columns = pickle.load(open(model_columns_path, 'rb'))



#route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # for rendering results on html gui

    json_ = request.form.to_dict()
    query_ = pd.get_dummies(pd.DataFrame(json_, index = [0]), prefix=['Gender','Job Title','Education Level'], columns=['Gender','Job Title','Education Level'])

    query = query_.reindex(columns = model_columns, fill_value= 0)
    
    query["Age"] = pd.to_numeric(query["Age"], errors="coerce")
    query["Years of Experience"] = pd.to_numeric(query["Years of Experience"], errors="coerce")

    prediction=list(model.predict(query))
    output = round(prediction[0],2)


    return render_template('index.html', prediction_text="Employee Salary should be ${}".format(output))
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 5000)))

    
    
