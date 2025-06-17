# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

def load_datasets(file_paths):
    """
    Loads multiple CSV files into pandas DataFrames.

    Args:
        file_paths (dict): A dictionary where keys are dataframe names
                           and values are the file paths to the CSVs.

    Returns:
        dict: A dictionary of pandas DataFrames.
    """
    dataframes = {}
    print("--- 1. Loading Datasets ---")
    try:
        for name, path in file_paths.items():
            dataframes[name] = pd.read_csv(path)
        print("All required datasets loaded successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure all data files are in the correct directory.")
        return None
    return dataframes

def clean_and_prepare_data(dataframes):
    """
    Cleans and preprocesses the raw dataframes.

    This function handles missing values, converts data types,
    and removes duplicate entries.

    Args:
        dataframes (dict): The dictionary of raw pandas DataFrames.

    Returns:
        dict: The dictionary of cleaned pandas DataFrames.
    """
    print("\n--- 2. Cleaning and Preparing Data ---")

    # --- Set pandas display options ---
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.float_format', lambda x: f'{x:.2f}')

    # --- Clean df_mql ---
    df_mql = dataframes['df_mql']
    df_mql['first_contact_date'] = pd.to_datetime(df_mql['first_contact_date'], errors='coerce')
    df_mql.dropna(subset=['first_contact_date'], inplace=True)
    df_mql.drop_duplicates(inplace=True)
    df_mql['origin'].fillna('unknown', inplace=True)
    dataframes['df_mql'] = df_mql

    # --- Clean df_closed_deals ---
    df_closed_deals = dataframes['df_closed_deals']
    df_closed_deals['won_date'] = pd.to_datetime(df_closed_deals['won_date'], errors='coerce')
    df_closed_deals.dropna(subset=['won_date', 'seller_id'], inplace=True)
    df_closed_deals['business_segment'].fillna('unknown', inplace=True)
    df_closed_deals['lead_type'].fillna('unknown', inplace=True)
    df_closed_deals['lead_behaviour_profile'].fillna('unknown', inplace=True)
    df_closed_deals['has_company'] = df_closed_deals['has_company'].astype(bool)
    df_closed_deals['has_gtin'] = df_closed_deals['has_gtin'].astype(bool)
    df_closed_deals['average_stock'].fillna('unknown', inplace=True)
    df_closed_deals['business_type'].fillna('unknown', inplace=True)
    df_closed_deals['declared_product_catalog_size'].fillna(0, inplace=True)
    df_closed_deals['declared_monthly_revenue'].fillna(0, inplace=True)
    dataframes['df_closed_deals'] = df_closed_deals

    # --- Clean df_orders ---
    df_orders = dataframes['df_orders']
    date_cols_orders = [
        'order_purchase_timestamp', 'order_approved_at',
        'order_delivered_carrier_date', 'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]
    for col in date_cols_orders:
        df_orders[col] = pd.to_datetime(df_orders[col], errors='coerce')
    dataframes['df_orders'] = df_orders

    # --- Clean df_reviews ---
    df_reviews = dataframes['df_reviews']
    df_reviews['review_creation_date'] = pd.to_datetime(df_reviews['review_creation_date'], errors='coerce')
    df_reviews['review_answer_timestamp'] = pd.to_datetime(df_reviews['review_answer_timestamp'], errors='coerce')
    df_reviews['review_comment_title'].fillna('No Title', inplace=True)
    df_reviews['review_comment_message'].fillna('No Message', inplace=True)
    dataframes['df_reviews'] = df_reviews

    # --- Clean df_order_items ---
    df_order_items = dataframes['df_order_items']
    df_order_items['shipping_limit_date'] = pd.to_datetime(df_order_items['shipping_limit_date'], errors='coerce')
    dataframes['df_order_items'] = df_order_items

    # --- Clean df_products ---
    df_products = dataframes['df_products']
    df_products['product_category_name'].fillna('unknown', inplace=True)

    # Fill numerical product attributes with the median
    numeric_cols = [
        'product_name_lenght', 'product_description_lenght', 'product_photos_qty',
        'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'
    ]
    for col in numeric_cols:
        median_value = df_products[col].median()
        df_products[col].fillna(median_value, inplace=True)
    dataframes['df_products'] = df_products

    print("Data cleaning and preparation complete.")
    return dataframes

def main():
    """
    Main function to run the data analysis pipeline.
    """
    # Define the file paths for the datasets
    file_paths = {
        "df_closed_deals": "olist_closed_deals_dataset.csv",
        "df_mql": "olist_marketing_qualified_leads_dataset.csv",
        "df_sellers": "olist_sellers_dataset.csv",
        "df_order_items": "olist_order_items_dataset.csv",
        "df_orders": "olist_orders_dataset.csv",
        "df_reviews": "olist_order_reviews_dataset.csv",
        "df_products": "olist_products_dataset.csv",
        "df_product_category_translation": "product_category_name_translation.csv"
    }

    # Load the datasets
    dataframes = load_datasets(file_paths)

    if dataframes:
        # Clean and prepare the data
        cleaned_data = clean_and_prepare_data(dataframes)

        # You can now proceed with your data analysis using the 'cleaned_data' dictionary.
        # For example, to access the cleaned deals dataframe:
        # deals_df = cleaned_data['df_closed_deals']
        # print("\n--- Sample of Cleaned Closed Deals Data ---")
        # print(deals_df.head())
        # print(deals_df.info())

if __name__ == "__main__":
    main()

# --- Initial Exploratory Data Analysis (EDA) ---
print("\n--- Initial Exploratory Data Analysis (EDA) ---")
print("\n--- Marketing Qualified Leads (df_mql) ---")

print("Top 10 Marketing Channels (Origin):")
print(df_mql['origin'].value_counts().head(10))
plt.figure(figsize=(10, 6))
sns.countplot(y='origin', data=df_mql, order=df_mql['origin'].value_counts().index)
plt.title('Distribution of Marketing Qualified Leads by Origin')
plt.xlabel('Number of MQLs')
plt.ylabel('Marketing Channel Origin')
plt.show()

print("\n--- Closed Deals (df_closed_deals) ---")
print("Top 10 Business Segments for Acquired Sellers:")
print(df_closed_deals['business_segment'].value_counts().head(10))
plt.figure(figsize=(10, 6))
sns.countplot(y='business_segment', data=df_closed_deals, order=df_closed_deals['business_segment'].value_counts().index)
plt.title('Distribution of Acquired Sellers by Business Segment')
plt.xlabel('Number of Sellers')
plt.ylabel('Business Segment')
plt.show()

print("\nDescriptive statistics for declared_monthly_revenue (for acquired sellers > 0):")
print(df_closed_deals[df_closed_deals['declared_monthly_revenue'] > 0]['declared_monthly_revenue'].describe())
plt.figure(figsize=(10, 6))
sns.histplot(df_closed_deals[df_closed_deals['declared_monthly_revenue'] > 0]['declared_monthly_revenue'], bins=50, kde=True)
plt.title('Distribution of Declared Monthly Revenue (Acquired Sellers > 0)')
plt.xlabel('Declared Monthly Revenue')
plt.ylabel('Number of Sellers')
plt.xlim(0, df_closed_deals['declared_monthly_revenue'].quantile(0.95)) # Focus on the main distribution
plt.show()

print("\n--- Orders (df_orders) ---")
print("Order Status Distribution:")
print(df_orders['order_status'].value_counts())
plt.figure(figsize=(8, 5))
sns.countplot(x='order_status', data=df_orders, order=df_orders['order_status'].value_counts().index)
plt.title('Distribution of Order Status')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.show()

# Calculate delivery time (for delivered orders)
df_delivered = df_orders[df_orders['order_status'] == 'delivered'].copy()
df_delivered['actual_delivery_days'] = (df_delivered['order_delivered_customer_date'] - df_delivered['order_purchase_timestamp']).dt.days
df_delivered['estimated_delivery_days'] = (df_delivered['order_estimated_delivery_date'] - df_delivered['order_purchase_timestamp']).dt.days
df_delivered['delivery_difference_days'] = df_delivered['actual_delivery_days'] - df_delivered['estimated_delivery_days']

print("\nDescriptive statistics for actual delivery days (delivered orders):")
print(df_delivered['actual_delivery_days'].describe())
plt.figure(figsize=(10, 6))
sns.histplot(df_delivered['actual_delivery_days'].dropna(), bins=50, kde=True)
plt.title('Distribution of Actual Delivery Days (Delivered Orders)')
plt.xlabel('Days')
plt.ylabel('Number of Orders')
plt.show()

print("\n--- Reviews (df_reviews) ---")
print("Review Score Distribution:")
print(df_reviews['review_score'].value_counts().sort_index(ascending=False))

plt.figure(figsize=(8, 5))
# Use 'color' argument for a single color instead of 'palette' without 'hue'
sns.countplot(x='review_score', data=df_reviews, color='skyblue') # Or 'blue', '#1f77b4', etc.
plt.title('Distribution of Review Scores')
plt.xlabel('Review Score (1-5)')
plt.ylabel('Number of Reviews')
plt.show()

print("--- Inspecting df_products Columns ---")
print("Columns in df_products:")
print(df_products.columns) # This will print all column names in your DataFrame

print("\n--- Products (df_products) ---")
print("Top 10 Product Categories (English):")
print(df_products['product_category_name_english'].value_counts().head(10))
plt.figure(figsize=(10, 6))
sns.countplot(y='product_category_name_english', data=df_products,
              order=df_products['product_category_name_english'].value_counts().head(10).index)
plt.title('Top 10 Product Categories (English)')
plt.xlabel('Number of Products')
plt.ylabel('Product Category')
plt.show()

print("\n--- Sellers (df_sellers) ---")
print("Top 10 Seller States:")
print(df_sellers['seller_state'].value_counts().head(10))
plt.figure(figsize=(8, 5))
sns.countplot(x='seller_state', data=df_sellers, order=df_sellers['seller_state'].value_counts().head(10).index)
plt.title('Top 10 Seller States')
plt.xlabel('State')
plt.ylabel('Number of Sellers')
plt.show()

print("\n--- Data Cleaning and Initial EDA Complete ---")
print("All DataFrames are now cleaned and initial insights have been gathered.")

# --- GOAL : Quantifying Marketing Funnel Conversion Rates ---
print("\n--- Quantifying Marketing Funnel Conversion Rates ---")

# Step 1: Define the stages of the marketing funnel relevant to MQLs
# We'll focus on:
# 1. MQLs (Marketing Qualified Leads)
# 2. Closed Deals (MQLs that converted into active sellers)

# Count total MQLs
total_mqls = len(df_mql)
print(f"Total MQLs identified: {total_mqls}")

# Count MQLs that became Closed Deals (Won Deals)
df_marketing_won = pd.merge(df_mql, df_closed_deals, on='mql_id', how='inner')

# Drop rows where 'won_date' or 'first_contact_date' are NaT (invalid datetimes)
initial_rows_mql_won = len(df_marketing_won)
df_marketing_won.dropna(subset=['won_date', 'first_contact_date'], inplace=True)
if len(df_marketing_won) < initial_rows_mql_won:
    print(f"Dropped {initial_rows_mql_won - len(df_marketing_won)} rows with missing 'won_date' or 'first_contact_date' in df_marketing_won.")

converted_mqls = len(df_marketing_won)
print(f"MQLs converted to Closed Deals: {converted_mqls}")

# Step 2: Calculate Conversion Rates
mql_to_won_conversion_rate = (converted_mqls / total_mqls) * 100 if total_mqls > 0 else 0

print(f"\nMarketing Funnel Conversion Rates:")
print(f"  MQL to Won Deal Conversion Rate: {mql_to_won_conversion_rate:.2f}%")

# Identify MQLs that did NOT convert to won deals (lost opportunities)
lost_mqls_df = df_mql[~df_mql['mql_id'].isin(df_marketing_won['mql_id'])].copy()
num_lost_mqls = len(lost_mqls_df)
print(f"Number of MQLs that did NOT convert (lost/unresolved): {num_lost_mqls}")

# Step 4: Visualize the Funnel
funnel_data = {
    'Stage': ['MQLs', 'Closed Deals'],
    'Count': [total_mqls, converted_mqls]
}
df_funnel = pd.DataFrame(funnel_data)

plt.figure(figsize=(8, 6))

custom_palette = ['#E0E0E0', '#CCCCCC']

sns.barplot(x='Stage', y='Count', data=df_funnel,
            palette=custom_palette,
            hue='Stage',
            legend=False)

plt.title('Marketing Funnel Conversion (MQLs to Closed Deals)')
plt.xlabel('Funnel Stage')
plt.ylabel('Number of Leads')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

df_funnel_sorted = df_funnel.sort_values(by='Count', ascending=False)
custom_palette_funnel = ['#E0E0E0', '#CCCCCC']

plt.figure(figsize=(8, 6))
sns.barplot(x='Count', y='Stage', data=df_funnel_sorted,
            palette=custom_palette_funnel,
            hue='Stage',
            legend=False)

plt.title('Marketing Funnel (MQLs to Closed Deals)')
plt.xlabel('Number of Leads')
plt.ylabel('Funnel Stage')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print("\n--- Summary for Quantifying Marketing Funnel Conversion ---")
print("This analysis quantifies the overall efficiency of the marketing funnel from MQL acquisition to deal closure.")
print(f"The MQL to Won Deal Conversion Rate is {mql_to_won_conversion_rate:.2f}%.")
print(f"A significant number of MQLs ({num_lost_mqls}) do not proceed to become Closed Deals.")
print("This rate helps understand the general health of the sales process and highlights the primary drop-off point.")
