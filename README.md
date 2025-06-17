# Analyzing-the-Olist-Marketing-Funnel-and-its-Impact-on-Seller-Success
# Olist MQL to Seller Conversion Analysis

## 1. Project Overview

In the competitive e-commerce landscape, attracting and converting high-quality sellers is paramount for platform growth. While significant resources are invested in generating **Marketing Qualified Leads (MQLs)**, a clear, data-driven understanding of the lead conversion funnel is essential to maximize marketing ROI and scale our acquisition efforts efficiently.

This project analyzes the Olist E-commerce dataset to trace the journey from MQL to active seller. The primary goal is to **clean and prepare the data** to answer critical business questions: How many MQLs convert to sellers? Where do leads drop off? And what characteristics define the most promising leads? The final cleaned dataset is intended for in-depth analysis and visualization in **Tableau**. 📊

## 2. The Dataset

This project utilizes the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and [Marketing Funnel by Olist](https://www.kaggle.com/datasets/olistbr/marketing-funnel-olist), which is available on Kaggle. These dataset is anonymized and split into multiple CSV files that map out different aspects of the e-commerce operation. 

The core datasets used in this analysis include:
- `olist_marketing_qualified_leads_dataset.csv`: Data on potential sellers who were contacted.
- `olist_closed_deals_dataset.csv`: Information about MQLs that successfully converted into sellers.
- `olist_sellers_dataset.csv`: General seller information.
- And other supplementary datasets for richer context (orders, products, etc.).

## 3. Project Structure

```
.
├── olist_analysis.py      
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

After the script runs, the data is ready to be loaded into Tableau for visualization. **Note:** The script itself does not output a new CSV, but it prepares the data in memory. You can easily add a line like `cleaned_data['df_name'].to_csv('cleaned_df.csv')` to the script to save the processed data.

## 6. Data Cleaning and Preparation

The `olist_analysis.py` script performs several key preprocessing steps:

-   **Data Type Conversion:** Correctly casts date/time columns to `datetime` objects and boolean columns to `bool`.
-   **Missing Value Imputation:** Strategically fills `NaN` values. For example, it fills numerical columns like `declared_product_catalog_size` with `0` and categorical columns like `business_segment` with an `unknown` category.
-   **Duplicate Removal:** Eliminates duplicate rows to ensure data integrity.
-   **Error Handling:** Invalid or missing critical data points (like `won_date` in the deals dataset) are dropped to maintain the quality of the dataset for analysis.

## 7. Analysis & Visualization Goals (in Tableau)

The cleaned data will be used to create an interactive dashboard in Tableau to explore the following:

-   **Marketing Funnel Analysis:** Build a funnel visualization to track the conversion rate from MQL to closed-deal seller and identify key drop-off points.
-   **Lead Source Effectiveness:** Analyze which lead origins (`organic_search`, `paid_search`, `social`, etc.) produce the most and highest-quality sellers.
-   **Successful Seller Profile:** Identify common characteristics (e.g., `business_segment`, `business_type`, `declared_monthly_revenue`) of sellers who successfully close deals.
-   **Geographic & Product Insights:** Map seller locations and analyze which product categories are associated with high-value sellers to inform targeted acquisition campaigns.

## 8. Libraries and Tools

-   [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
-   [NumPy](https://numpy.org/): For numerical operations.
-   [Matplotlib](https://matplotlib.org/): For data visualization.
-   [Seaborn](https://seaborn.pydata.org/): For enhanced statistical data visualization.
-   [Scipy](https://scipy.org/): For statistical tests.
-   [Tableau](https://www.tableau.com/): For final data visualization and dashboarding.
