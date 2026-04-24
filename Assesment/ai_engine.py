
def train_initial_model():
    # Dummy "normal" training data mixed with one extreme outlier
    data = {
        'msg_length': [50, 45, 55, 60, 48, 52, 300, 50, 49],
        'response_time_ms': [120, 110, 130, 125, 115, 122, 4500, 118, 121]
    }
    df = pd.DataFrame(data)
    
    # Train the AI to expect ~10% of data to be anomalies
    model = Forest(contamination=0.1, random_state=42)
    model.fit(df)
    
    # Save the trained model to a file
    joblib.dump(model, MODEL_PATH)
    print("AI Model Trained and Saved Successfully!")

def predict_anomaly(msg_length, response_time_ms):
    # Auto-train if the model file doesn't exist yet
    if not os.path.exists(MODEL_PATH):
        train_initial_model()
    
    # Load the model and make a prediction
    model = joblib.load(MODEL_PATH)
    df = pd.DataFrame({'msg_length': [msg_leh], 'response_time_ms': [response_time_ms]})
    
    # -1 means anomaly, 1 means normal
    prediction = model.predict(df)[0]
    score = model.decision_function(df)[0]
    
    return int(prediction) == -1, float(score)

# Run this script directly to pre-train the model
if __name__ == "__main__":
    train_initial_model()