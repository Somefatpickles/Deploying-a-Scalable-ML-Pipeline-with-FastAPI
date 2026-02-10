import pytest
import pandas as pd
from ml.data import process_data
from ml.model import (
    compute_model_metrics,
    train_model
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os
import math
import numpy as np

def test_algorithm():
    """
    Test to ensure the train_model() function uses the RandomForestClassifier algorithm.
    """
    
    # Assign RandomForestClassifier to a variable
    intended_model = RandomForestClassifier

    # Create a dataframe to test
    df = pd.DataFrame(
        {
            "feature_1": [1, 2, 3, 4, 5],
            "feature_2": [6, 7, 8, 9, 0],
            "label": [1, 0, 0, 0, 1]
        }
    )

    # Call process_data() on the dataframe
    X_train, y_train, _, _ = process_data(
        df,
        categorical_features=["feature_1"],
        label="label",
        training=True
    )

    # Train the dummy model for comparison
    trained_model = train_model(X_train, y_train)
    
    assert isinstance(trained_model, intended_model)

def test_size():
    """
    Test to confirm the expected sizes of the train and test datasets.
    """

    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    print(data_path)
    data = pd.read_csv(data_path)
    expected_train_size = math.floor(data.shape[0] - (data.shape[0] * 0.25))
    expected_test_size = math.ceil(data.shape[0] - (data.shape[0] * 0.75))

    train, test = train_test_split(data, test_size=0.25, random_state=42)

    assert train.shape[0] == expected_train_size
    assert test.shape[0] == expected_test_size

def test_metrics():
    """
    Test to determine whether the compute_model_metrics() function returns values as expected.
    """
    # Test arrays with which to compute p, r, fb
    y_true = np.array([1, 0, 0, 1, 0, 0, 0, 0])
    y_pred = np.array([1, 1, 0, 1, 1, 0, 0, 1])

    # Compute p, r, fb
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    # Establish variables with true p, r, fb values based on arrays
    expected_p = 0.400
    expected_r = 1.000
    expected_fb = 0.571

    assert round(precision, 3) == expected_p
    assert round(recall, 3) == expected_r
    assert round(fbeta, 3) == expected_fb
