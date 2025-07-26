import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# File paths and target columns for each nutrient
files = {
    "Spectro_Magnesium.xlsx": "MAGNESIUM",
    "Spectro_Nitrogen.xlsx": "NITROGEN",
    "Spectro_Phosphorus.xlsx": "PHOSPHORUS",
    "Spectro_Potassium.xlsx": "POTASSIUM"
}

# Retained metadata columns
retain_columns = ["SAMPLE_CODE", "Rule"]

# Explained variance threshold (increased to retain more components)
explained_variance = 0.98

def preprocess_and_pca(file, target_column, explained_variance, retain_columns):
    """
    Preprocesses a spectroradiometer dataset and applies PCA.
    Saves the results as a CSV file.
    """
    # Load the dataset
    df = pd.read_excel(file)
    
    # Ensure all column names are strings
    df.columns = df.columns.astype(str)
    
    # Retain metadata and target column
    metadata = df[retain_columns]
    target = df[target_column]
    
    # Select numeric features for PCA
    numeric_features = df.select_dtypes(include=["float64", "int64"]).drop(columns=[target_column])
    
    # Standardize numeric features
    X = StandardScaler().fit_transform(numeric_features)
    
    # Apply PCA to determine the number of components
    pca = PCA()
    pca.fit(X)
    cumulative_variance = pca.explained_variance_ratio_.cumsum()
    n_components = (cumulative_variance < explained_variance).sum() + 1
    print(f"{file}: Retaining {n_components} components to explain {explained_variance * 100}% variance.")
    
    # Transform data with the selected number of components
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(X)
    
    # Create a DataFrame for principal components
    principal_df = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(n_components)])
    
    # Combine metadata, principal components, and target column
    result_df = pd.concat([metadata.reset_index(drop=True), principal_df, target.reset_index(drop=True)], axis=1)
    
    # Save the result to a CSV file
    output_file = file.replace(".xlsx", "_pca_processed.csv")
    result_df.to_csv(output_file, index=False)
    print(f"Processed dataset saved as: {output_file}")

# Process all files
for file, target_column in files.items():
    preprocess_and_pca(file, target_column, explained_variance, retain_columns)
