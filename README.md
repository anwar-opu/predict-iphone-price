# iPhone Price Prediction

This repository contains a simple Python script that uses linear regression to predict the price of an iPhone based on its version.

## Files

- `iphone_price.csv`: A CSV file containing historical data of iPhone versions and their corresponding prices.
- `iphone_predict_price.py`: The main Python script that reads the data, fits a linear regression model, and predicts the price of an iPhone version entered by the user.

## Dependencies

The script requires the following Python libraries:

- `pandas`
- `scikit-learn`

You can install these dependencies using pip:

```bash
pip install pandas scikit-learn
```
### How It Works
- The script imports the necessary libraries and reads the iPhone data from the iphone_price.csv file.
- It fits a linear regression model using the version column as the input feature and the price column as the target variable.
- The user is prompted to enter an iPhone version for which they want to predict the price.
- The script then predicts and prints the price for the entered version using the trained model.

### Usage
1. Clone the repository and navigate to the project directory.
```bash 
git clone https://github.com/anwar-opu/predict-iphone-price.git
cd predict-iphone-price

```
2. Ensure that you have the necessary dependencies installed.

3. Run the script:
```bash
python iphone_predict_price.py 
```
4. Enter an iPhone version when prompted to receive the predicted price.

### Example
If you run the script and input the version 12, the output will be the predicted price for the iPhone 12 based on the linear regression model trained on the data.

### Visualization (Optional)
The script also contains commented-out code for visualizing the data using Matplotlib. If you'd like to visualize the data, you can uncomment the relevant lines and install Matplotlib:
```bash
pip install matplotlib
```
Then, you can run the script again to see scatter plots or bar charts of the iPhone versions and their prices.
