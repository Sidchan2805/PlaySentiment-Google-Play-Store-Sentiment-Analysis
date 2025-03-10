import pandas as pd

def load_data(url: str):
    """
    Load dataset from the given URL.
    """
    print("🔄 Loading dataset...")
    df = pd.read_csv(url)
    
    # Drop missing values
    df = df.dropna()
    print(f"✅ Dataset loaded successfully! {df.shape[0]} rows, {df.shape[1]} columns.")
    
    return df
