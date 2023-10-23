## Purchase Prediction using Naïve Bayes Classifier

This Python program implements a Naïve Bayes Classifier to predict whether a customer will make a purchase or not based on a combination of features. The features include "Day," "Discount," and "Delivery." The dataset used for this prediction is provided in a text format.

### How the Code Works:

1. **Data Preparation**: The code begins by reading the dataset from a text block and organizes it into a structured data format. The header and values for each entry are extracted.

2. **Feature Combination to Predict**: You can define the combination of features you want to predict. In this example, the combination of features is set to:
   - Day = Weekday
   - Discount = No
   - Delivery = Yes

3. **Prior Probability Calculation**: The prior probabilities for the "Purchase" and "Not Purchase" classes are calculated. These probabilities provide an initial understanding of how often purchases and non-purchases occur in the dataset.

4. **Likelihood Probability Calculation**: The code calculates the likelihood probabilities for each feature ("Day," "Discount," "Delivery") and their corresponding values ("Weekday," "No," "Yes") concerning both "Purchase" and "Not Purchase" classes. These probabilities indicate how frequently certain features appear within each class.

5. **Posterior Probability Calculation**: For the defined combination of features, the code calculates the posterior probabilities for both the "Purchase" and "Not Purchase" classes. This calculation combines the prior probabilities and the likelihood probabilities for the specified features.

6. **Predict Class**: The program compares the calculated probabilities for "Purchase" and "Not Purchase" and predicts the class with the highest posterior probability. The result is printed as the predicted class.

### Usage:
- You can modify the `features_to_predict` dictionary to specify the combination of features you want to predict.
- Run the code, and it will provide the probabilities for "Purchase" and "Not Purchase" based on the chosen feature combination.