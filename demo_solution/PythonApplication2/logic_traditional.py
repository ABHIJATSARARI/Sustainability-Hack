
# Import scikit-learn and other modules 
from sklearn.datasets import fetch_openml  
from sklearn.linear_model import LogisticRegression  
from sklearn.metrics import accuracy_score  
from sklearn.model_selection import train_test_split 

# Import pyRAPL module for measuring energy consumption
import pyRAPL

# Define a function for training and deploying locally using traditional way 
def train_deploy(task): 

   # Load data from demo dataset using numpy module
   import numpy as np

   data = np.loadtxt("demo_dataset.csv", delimiter=",")

   X = data[:, 1:]
   y = data[:, 0]

   if task == "Digit Recognition":
      y = y * 10
      y = y.astype(int)
      X = X * 255
   
   elif task == "Image Classification":
      y = y * 10
      y = y.astype(int)
      X = X * 255
   
   elif task == "Sentiment Analysis":
      y = y * 5
      y = y.astype(int)
      X = X * 100

   print(f"Demo dataset loaded for {task}")

   print(f"X shape: {X.shape}")
   print(f"y shape: {y.shape}")

   print(f"X sample: {X[0]}")
   print(f"y sample: {y[0]}")

   print(f"X min: {X.min()}")
   print(f"X max: {X.max()}")

   print(f"y min: {y.min()}")
   print(f"y max: {y.max()}")

   print(f"y unique values: {np.unique(y)}")

   print()

   # Split data into train and test sets 
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 

   print("Using traditional way...")
   if task == "Digit Recognition":
      model = LogisticRegression(max_iter=1000)  
   elif task == "Image Classification":
      model = LogisticRegression(max_iter=1000)  
   elif task == "Sentiment Analysis":
      model = LogisticRegression(max_iter=1000)  

   # Train the model on the train set and measure the energy consumption using pyRAPL
   print("Training the model...")
   pyRAPL.setup()
   meter = pyRAPL.Measurement("train")
   meter.begin()
   model.fit(X_train, y_train)
   meter.end()
   print(f"Energy consumption during training: {meter.result.pkg[0]} microjoules")

   # Evaluate the model on the test set and measure the energy consumption using pyRAPL
   print("Evaluating the model...")
   pyRAPL.setup()
   meter = pyRAPL.Measurement("test")
   meter.begin()
   y_pred = model.predict(X_test)
   meter.end()
   print(f"Energy consumption during testing: {meter.result.pkg[0]} microjoules")
      # Calculate the accuracy score of the model
   acc = accuracy_score(y_test, y_pred)
   print(f"Accuracy: {acc}")

   # Save the model as an ONNX file  
   from skl2onnx import convert_sklearn  
   from skl2onnx.common.data_types import FloatTensorType  
   initial_type = [('float_input', FloatTensorType([None, X.shape[1]]))]  
   onnx_model = convert_sklearn(model, initial_types=initial_type)  
   with open(f"{task}_model_traditional.onnx", "wb") as f:  
      f.write(onnx_model.SerializeToString())  



