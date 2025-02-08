from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

app = Flask(__name__)

class NBAPredictor:
    def __init__(self):
        self.model = None
        self.le_pos = LabelEncoder()
        self.scaler = StandardScaler()
        
    def preprocess_data(self, df):
        # Encode position
        df['Pos'] = self.le_pos.fit_transform(df['Pos'])
        
        # Select features for prediction
        features = ['Age', 'Pos', 'PTS', 'AST', 'TRB']
        X = df[features]
        y = df['Salary']
        
        return X, y
    
    def train(self, X, y):
        self.model = RandomForestRegressor(
            n_estimators=200,
            max_depth=10,
            random_state=42
        )
        self.model.fit(X, y)
    
    def predict(self, data):
        return self.model.predict(data)[0]

predictor = NBAPredictor()

# Load and train model on startup
df = pd.read_csv('AR_dataset_v1.csv')
X, y = predictor.preprocess_data(df)
predictor.train(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Create DataFrame from input
        input_data = pd.DataFrame({
            'Age': [float(data['Age'])],
            'Pos': [data['Pos']],
            'PTS': [float(data['PTS'])],
            'AST': [float(data['AST'])],
            'TRB': [float(data['TRB'])]
        })
        
        # Encode position
        input_data['Pos'] = predictor.le_pos.transform(input_data['Pos'])
        
        # Make prediction
        prediction = predictor.predict(input_data)
        
        return jsonify({
            'status': 'success',
            'predicted_salary': f'${prediction:,.2f}'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
