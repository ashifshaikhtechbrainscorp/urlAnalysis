import joblib
import pandas as pd
import json
import csv

csv_file_path = "DrugsCommon.csv"
data = pd.read_csv(csv_file_path)

def predict_drug_names(drug_list):
    # Define data and model paths
    model_output_path = "trained_model.pkl"  # Update with the correct path
    # data = pd.DataFrame()  # Update with your data

    def predict_drug_names_for_class(drug_class):
        # Load the trained model
        model = joblib.load(model_output_path)

        # Predict drug names based on the input drug class
        drug_names = []
        for class_name in drug_class.split(','):
            drug_names.extend(
                data[data['Drug Class'].str.contains(class_name.strip(), case=False)]['Drug Name'].tolist())
        return drug_names

    # Prepare a dictionary to store results
    result_dict = {}

    # Iterate through the drug list
    for drug in drug_list:
        drug_list1 = []
        # Split the items in the input list and save them into the output list
        drug_list1.extend(drug.split(','))

        drug_list2 = []
        for item in drug_list1:
            drug_list2.extend(item.split('AND'))

        for drg in drug_list2:
            drg_title = drg.title()
            drgNames = predict_drug_names_for_class(drg_title)
            result_dict[drg_title] = ', '.join(drgNames)

    return result_dict