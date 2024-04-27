# Flower Species Prediction using Logistic Regression

This Python script uses a trained logistic regression model to predict the species of a flower based on its sepal length, sepal width, petal length, and petal width.

## Usage

1. **Prerequisites**: Ensure you have the necessary dependencies installed. You can install them using `pip`:

    ```bash
    pip install numpy scikit-learn joblib
    ```

2. **Load Model**: Replace `'full/path/to/Species_mind.pk1'` in the script with the actual path to your trained model file (`.pkl` file).

3. **Run Script**: Execute the Python script in your terminal or Python environment.

    ```bash
    python predict_flower_species.py
    ```

4. **Enter Data**: Input the sepal length, sepal width, petal length, and petal width of the flower when prompted.

5. **Prediction**: The script will then predict the species of the flower based on the input data and display the result.

## Model Details

- **Algorithm**: Logistic Regression
- **Dependencies**:
  - `numpy`: For numerical operations
  - `scikit-learn`: For machine learning algorithms and evaluation metrics
  - `joblib`: For loading the trained model from disk

## Notes

- Ensure that you have the trained model file (`Species_mind.pk1`) available in the specified path before running the script.
- The script assumes that the trained model file contains a logistic regression model trained on flower dataset features (sepal length, sepal width, petal length, petal width) to predict flower species.

