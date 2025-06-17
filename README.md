# Analyzing-the-Olist-Marketing-Funnel-and-its-Impact-on-Seller-Success
# Olist E-Commerce Data Analysis

## 1. Project Overview

This project performs a comprehensive analysis of the Olist E-commerce dataset, a public dataset containing information on 100,000 orders from 2016 to 2018 made at multiple marketplaces in Brazil. The primary goal is to explore the relationships between marketing leads, sellers, products, and final sales to uncover insights into seller performance, marketing funnel effectiveness, and customer satisfaction.

The initial phase of this project focuses on data cleaning, preparation, and transformation using Python. A subsequent phase will involve in-depth analysis and data extraction using SQL.

## 2. The Dataset

This project utilizes the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), which is available on Kaggle. The dataset is anonymized and split into multiple CSV files that map out different aspects of the e-commerce operation.

The core datasets used in this analysis include:
- `olist_closed_deals_dataset.csv`: Information about marketing qualified leads (MQLs) that became sellers.
- `olist_marketing_qualified_leads_dataset.csv`: Data on potential sellers who were contacted.
- `olist_sellers_dataset.csv`: Seller information.
- `olist_orders_dataset.csv`: Core order information.
- `olist_order_items_dataset.csv`: Product-level data for each order.
- `olist_products_dataset.csv`: Product dimension and category data.
- `olist_order_reviews_dataset.csv`: Customer review data.
- `product_category_name_translation.csv`: Translation of product categories into English.

## 3. Project Structure

```
.
├── olist_analysis.py      
├── sql/                      
│   └── analysis.sql
├── requirements.txt          
└── README.md                 
```

## 4. Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- A virtual environment tool like `venv` or `conda`

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/](https://github.com/)[your-github-username]/[your-repository-name].git
    cd [your-repository-name]
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required Python libraries:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Download the data:**
    - Download the Olist dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
    - Unzip the archive and place all the `.csv` files into a `data/` directory in the project's root. Make sure the file names match those in the `olist_analysis.py` script.

## 5. How to Run the Code

To execute the data cleaning and preparation script, run the following command from the project's root directory:

```sh
python olist_analysis.py
```

The script will:
1.  Load all the necessary datasets from the `data/` directory.
2.  Perform cleaning operations (handle missing values, correct data types, remove duplicates).
3.  Print status messages to the console.

After the script runs, the cleaned data will be ready for further analysis.

## 6. Data Cleaning and Preparation

The `olist_analysis.py` script performs several key preprocessing steps:

-   **Data Type Conversion:** Correctly casts date/time columns to `datetime` objects and boolean columns to `bool`.
-   **Missing Value Imputation:** Strategically fills `NaN` values. For example, it fills numerical columns like `declared_product_catalog_size` with `0` and categorical columns like `business_segment` with an `unknown` category.
-   **Duplicate Removal:** Eliminates duplicate rows to ensure data integrity.
-   **Error Handling:** Invalid or missing critical data points (like `won_date` in the deals dataset) are dropped to maintain the quality of the dataset for analysis.

## 7. Future Work (SQL Analysis)

-   [ ]  Develop SQL scripts to perform complex joins and aggregations.
-   [ ]  Analyze the marketing funnel from MQL to a closed deal.
-   [ ]  Investigate the correlation between seller location, product category, and sales revenue.
-   [ ]  Explore the impact of shipping times on customer review scores.

## 8. Libraries and Tools

-   [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
-   [NumPy](https://numpy.org/): For numerical operations.
-   [Matplotlib](https://matplotlib.org/): For data visualization.
-   [Seaborn](https://seaborn.pydata.org/): For enhanced statistical data visualization.
-   [Scipy](https://scipy.org/): For statistical tests.
