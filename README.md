# Used Car Price Estimation



LINK TO APP:https://used-car-price-estimation.herokuapp.com/
![car-image](https://user-images.githubusercontent.com/72034856/121199174-9eb9d700-c86a-11eb-83b4-c82acddc6ef0.jpg)

## #Task: 
Build machine learning app that can predict the price of used car
# Functionality:
The app takes in inputs from the users, and predict the price for the used car the user is interested in
# Description
The used car price prediction is targeted towards the indian market using the cardekho dataset found on kaggle.
This project is for an end to end project where i analyse data ,build model and create a simple web ui for people to interact with.
Krish naik youtube tutorial was very crucial in the completion of this project.
The following steps where followed;
1) Feature Engineering: outliers where handled
2) Exporatory data analysis:I explored the data for insight
3) Feature selection: The features that where selected include-Present_Price,car_num_yrs,Fuel_Type,Seller_Type,Transmission_type and car_popularity
4) Feature Scaling: standard scaler was used
5) Model Building

    a) Lasso regression with r2 of 0.89, RMSE 1.24, MAE 0.8193465965229342 on test data 

    b) KNN regression with  r2 is: 0.97, MSE 0.44, RMSE 0.67, MAE 0.46 on test data

    c) Random forest regressor with r2 of 0.97, RMSE 0.79, MAE 0.46 on test data

    d) Ensemble method with r2 of 0.96, RMSE 0.58, MAE 0.47
    
    
 # Run Locally
  Run this commandon ur command line:https://github.com/Raph-09/Used-Car-Price-Estimation-End-To-End-Project.git
  
  Install the packages that are found in requirement.txt file
  
 # Tech Stack
 sklearn
 
 pandas
 
 numpy
 
 Flask
 
 css
 
 html
 
 bootstrap
                                                                                                                                                    
