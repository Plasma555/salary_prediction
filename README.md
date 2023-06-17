This repository contains a salary prediction model implemented using Python and scikit-learn. 
The model is trained to predict salaries based on various features such as years of experience, education level, and job title. Additionally, a Flask web application has been developed to deploy the model and provide an interactive interface for users to make salary predictions.

Dataset
The dataset used for training and evaluation consists of a collection of salary data with corresponding features. It includes information on years of experience, education level, job title, and the corresponding salary for each sample. 
The dataset was carefully preprocessed and cleaned to ensure its quality and suitability for training the prediction model.

Model Training
The prediction model was trained using supervised learning techniques.
The dataset was split into training and validation sets to assess the model's performance and prevent overfitting. Various regression algorithms available in scikit-learn were explored, and the most suitable algorithm was selected based on performance metrics such as mean squared error (MSE) and R-squared (R²) score. The chosen algorithm was then trained on the training set to learn the relationships between the features and the corresponding salaries.

Model Deployment with Flask
To provide a user-friendly interface for salary prediction, a Flask web application was developed and deployed. 
The web application allows users to input their years of experience, education level, and job title, and based on these inputs, the deployed model predicts their salary. The application provides real-time predictions and displays the predicted salary to the user.
