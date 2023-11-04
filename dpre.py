import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA

# Step 1: Data Cleaning
def data_cleaning(data):
    # Task 1: Drop rows with missing data
    clean_data = data.dropna()

    # Task 2: Remove duplicates
    clean_data = clean_data[~clean_data.duplicated()]

    return clean_data

# Step 2: Data Transformation
def data_transformation(data):
    # Task 1: Label Encoding for categorical columns
    le = LabelEncoder()
    data['gender'] = le.fit_transform(data['gender'])
    data['smoking_history'] = le.fit_transform(data['smoking_history'])

    # Task 2: No 'apply' function on the transformed_data1
    adata = ['ever', 'never', 'No Info', 'current', 'not current', 'former']
    transformed_data = le.fit_transform(adata)

    return data

# Step 3: Data Reduction
def data_reduction(data):
    reduced_data = data.iloc[:, :10] 

    # Task 1: Feature Selection Using Statistical Techniques (ANOVA F-value)
    X = reduced_data.drop('blood_glucose_level', axis=1)  # Features
    y = reduced_data['bmi']  # Target

    selector = SelectKBest(score_func=f_classif, k=5)
    selected_features = selector.fit_transform(X, y)
    reduced_data_1 = pd.DataFrame(selected_features, columns=X.columns[selector.get_support()])

    # Task 2: Principal Component Analysis (PCA)
    pca = PCA(n_components=5)  # Reduce to 5 principal components
    reduced_features = pca.fit_transform(X)
    reduced_data_2 = pd.DataFrame(reduced_features, columns=[f"PC{i}" for i in range(1, 6)])

    return reduced_data, reduced_data_1, reduced_data_2

# Step 4: Data Discretization
def data_discretization(data):
    # Task 1: Binning Multiple Columns
    columns_to_discretize = ['age', 'blood_glucose_level']
    discretized_data = data.copy()
    for col in columns_to_discretize:
        discretized_data[f'{col}_bins'] = pd.cut(data[col], bins=5, labels=False)
        
    # Task 2: Custom Binning Function
    def custom_binning(value):
        if value < 100:
            return 'Low'
        elif value < 150:
            return 'Normal'
        elif value < 200:
            return 'High'
        else:
            return 'Very High'
    
    discretized_data['blood_glucose_level_custom_bins'] = data['blood_glucose_level'].apply(custom_binning)
    
    return discretized_data

# Your main logic and file saving routine
if __name__ == "__main__":
    try:
        # Load the dataset
        file_path = input("Enter the path of the dataset file: ")
        data = pd.read_csv(file_path)

        # Apply the preprocessing steps
        cleaned_data = data_cleaning(data)
        transformed_data = data_transformation(cleaned_data)
        reduced_data, reduced_data_1, reduced_data_2 = data_reduction(transformed_data)
        discretized_data = data_discretization(reduced_data)

        # Display the processed data
        print("Cleaned Data:")
        print(cleaned_data.head())

        print("\nTransformed Data:")
        print(transformed_data.head())

        print("\nReduced Data:")
        print(reduced_data.head())
        print(reduced_data_1.head())
        print(reduced_data_2.head())

        print("\nDiscretized Data:")
        print(discretized_data.head())

        # Save the resulting DataFrames as new CSV files
        reduced_data.to_csv('reduced_data.csv', index=False)
        reduced_data_1.to_csv('reduced_data_1.csv', index=False)
        reduced_data_2.to_csv('reduced_data_2.csv', index=False)
        discretized_data.to_csv('res_dpre.csv', index=False)

    except Exception as e:
        print("Error occurred while preprocessing data:", e)
