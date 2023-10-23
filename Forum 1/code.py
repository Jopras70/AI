data = """Day Discount Free Delivery Purchase
Weekday Yes Yes Yes Yes
Weekday Yes Yes Yes Yes
Weekday No No No No
Holiday Yes Yes Yes Yes
Weekend Yes Yes Yes Yes
Holiday No No No No
Weekend Yes No Yes Yes
Weekday Yes Yes Yes Yes
Weekend Yes Yes Yes Yes
Holiday Yes Yes Yes Yes
Holiday No Yes Yes Yes
Holiday No No No No
Weekend Yes Yes Yes Yes
Holiday Yes Yes Yes Yes
Holiday Yes Yes Yes Yes
Weekday Yes Yes Yes Yes
Holiday No Yes Yes Yes
Weekday Yes No Yes Yes
Weekend No No Yes Yes
Weekend No Yes Yes Yes
Weekday Yes Yes Yes Yes
Weekend Yes Yes No Yes
Holiday No Yes Yes Yes
Weekday Yes Yes Yes Yes
Holiday No No No Yes
Weekday No Yes No Yes
Weekday Yes Yes Yes Yes
Weekday Yes Yes Yes Yes
Holiday Yes Yes Yes Yes
Weekend Yes Yes Yes No
"""

data = data.strip().split('\n')
header = data[0].split()
dataset = []

for row in data[1:]:
    values = row.split()
    
    if len(values) == len(header):
        entry = {}
        for i, feature in enumerate(header):
            entry[feature] = values[i]
        dataset.append(entry)

# Define the combination of features to predict
features_to_predict = {'Day': 'Weekday', 'Discount': 'No', 'Delivery': 'Yes'}

# Create a function to calculate the probability for a given class label
def calculate_probability(class_label):
    posterior_prob = 1.0
    for feature, value in features_to_predict.items():
        prob = likelihood(feature, value, class_label, dataset)
        posterior_prob *= prob
    posterior_prob *= (class_label == 'Yes' and prior_purchase or prior_not_purchase)
    return posterior_prob

# Calculate prior probabilities
total_rows = len(dataset)
purchase_count = sum(1 for row in dataset if row['Purchase'] == 'Yes')
not_purchase_count = total_rows - purchase_count

# Check if the dataset is not empty before calculating prior probabilities
if total_rows > 0:
    prior_purchase = purchase_count / total_rows
    prior_not_purchase = not_purchase_count / total_rows
    print("Prior Probability (Purchase):", prior_purchase)
    print("Prior Probability (Not Purchase):", prior_not_purchase)
else:
    print("The dataset is empty")

# Create a function to calculate likelihood probabilities
def likelihood(feature, value, class_label, dataset):
    count = sum(1 for row in dataset if row[feature] == value and row['Purchase'] == class_label)
    total_class_count = sum(1 for row in dataset if row['Purchase'] == class_label)
    
    # Check if the denominator is not zero before calculating likelihood
    if total_class_count > 0:
        return count / total_class_count
    else:
        return 0.0

# Calculate and print the probabilities for Purchase and Not Purchase
probability_purchase = calculate_probability('Yes')
probability_not_purchase = calculate_probability('No')

print("Probability (Purchase):", probability_purchase)
print("Probability (Not Purchase):", probability_not_purchase)

# Compare the probabilities to predict the class
predicted_class = 'Purchase' if probability_purchase > probability_not_purchase else 'Not Purchase'
print("Predicted Class:", predicted_class)
