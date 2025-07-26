import pandas as pd

# File paths for PCA-processed CSV files
pca_processed_files = {
    "Spectro_Magnesium_pca_processed.csv": "MAGNESIUM",
    "Spectro_Nitrogen_pca_processed.csv": "NITROGEN",
    "Spectro_Phosphorus_pca_processed.csv": "PHOSPHORUS",
    "Spectro_Potassium_pca_processed.csv": "POTASSIUM"
}

def process_pca_for_ml(pca_processed_files):
    """
    Processes PCA-processed files to extract features and prepare data for ML classification.
    Retains 'SAMPLE_CODE', 'Rule', PCA features (PC1, PC2, ...), and target nutrient levels.
    Encodes the 'Rule' column with custom labels for ML classification.
    - pca_processed_files: Dictionary of file paths and target column names.
    """
    # Define custom encoding for the Rule column
    rule_mapping = {
        "Normal": 1,
        "Low-deficiency": 2,
        "High-deficiency": 3
    }
    
    for file, target_column in pca_processed_files.items():
        # Load each PCA-processed file
        df = pd.read_csv(file)
        print(f"Loaded {file} with {df.shape[0]} rows and {df.shape[1]} columns.")

        # Retain specific columns: 'SAMPLE_CODE', 'Rule', PCA features, and target column
        retained_columns = ['SAMPLE_CODE', 'Rule'] + [col for col in df.columns if col.startswith("PC")] + [target_column]
        processed_df = df[retained_columns]

        # Map the 'Rule' column to the custom encoding
        processed_df['Rule_encoded'] = processed_df['Rule'].map(rule_mapping)

        # Save the processed file
        output_file = file.replace(".csv", "_ml_ready.csv")
        processed_df.to_csv(output_file, index=False)
        print(f"ML-ready dataset saved as: {output_file}")

# Process PCA files to prepare for ML
process_pca_for_ml(pca_processed_files)
