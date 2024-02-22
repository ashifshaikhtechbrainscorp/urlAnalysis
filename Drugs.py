import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load the CSV file
csv_file_path = "DrugsCommon.csv"
data = pd.read_csv(csv_file_path)

# Extract features (Drug Name) and labels (Drug Class)
X = data['Drug Name']
y = data['Drug Class']

# Define a pipeline with CountVectorizer and Multinomial Naive Bayes classifier
pipeline = Pipeline([
    ('vect', CountVectorizer()),  # Convert text to a matrix of token counts
    ('clf', MultinomialNB()),     # Multinomial Naive Bayes classifier
])

# Train the model
pipeline.fit(X, y)

# Save the trained model
model_output_path = "trained_model.pkl"
joblib.dump(pipeline, model_output_path)
print(f"Model saved to {model_output_path}")

# Function to predict drug names based on drug class
def predict_drug_names(drug_class):
    # Load the trained model
    model = joblib.load(model_output_path)

    # Predict drug names based on the input drug class
    drug_names = data[data['Drug Class'] == drug_class]['Drug Name'].tolist()
    return drug_names

# Example usage:
user_input_class = input("Enter a drug class: ").title()
predicted_drug_names = predict_drug_names(user_input_class)
print(f"Drug names in the class '{user_input_class}':")
print(predicted_drug_names)
