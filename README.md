# Sales Recommendation Engine

A sales recommendation engine that uses data-driven business rules to suggest relevant products to customers."

---

## Project Overview

This project analyzes user-product interaction data and generates personalized product recommendations using a weighted scoring formula based on revenue, units sold, customer ratings, and return rates. The system is designed to improve customer engagement and assist businesses in identifying relevant product suggestions.

---

## Features

- Synthetic sales data generation with seasonality
- Data preprocessing and statistical analysis
- Weighted score-based recommendation logic
- Automated pipeline execution
- Data visualization for sales trends

---

## Tech Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core programming language       |
| Pandas     | Data preprocessing and analysis |
| NumPy      | Numerical computations          |
| Matplotlib | Data visualization              |

---

## Project Structure

```bash
sales-recommendation-system/
│
├── data/
│   ├── generate_data.py          # Data generation script
│   └── monthly_sales_data.csv    # Generated synthetic dataset
├── outputs/
│   ├── category_statistics.csv   # Aggregated statistics
│   ├── monthly_trends.csv
│   ├── product_statistics.csv
│   ├── ranked_products.csv       # Final recommendations
│   ├── revenue_trend.png
│   └── top_products.png
├── data_visualization.py         # Generates plots
├── descriptive_statistics.py     # Computes base statistics
├── gui_app.py                    # Placeholder for GUI
├── main.py                       # Pipeline orchestrator
├── recommendation_system.py      # Core ranking logic
├── requirements.txt              # Dependencies
└── README.md
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/MohitXGandhi/sales-recommendation-system.git
cd sales-recommendation-system
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the full data generation, analysis, and recommendation pipeline:

```bash
python main.py
```

Check the `outputs/` directory for the resulting statistics, visualizations, and the final `ranked_products.csv`.

---

## How It Works

1. **Data Generation**: `generate_data.py` creates a synthetic dataset of product sales, incorporating seasonal trends, returns, and discounts.
2. **Descriptive Statistics**: Key metrics (revenue, units sold) are aggregated by product, category, and month.
3. **Data Visualization**: Matplotlib is used to plot monthly revenue trends and top-performing products.
4. **Recommendation Logic**: Products are ranked based on a composite score:
   - 35% Net Revenue
   - 30% Units Sold
   - 20% Customer Rating
   - 15% Return Rate (Inversely proportional)
5. **Output**: The final ranked list is exported to `outputs/ranked_products.csv`.

---

## Future Improvements

- Machine Learning integration (Collaborative filtering)
- Real-time recommendation generation
- Web-based deployment or GUI implementation
- User authentication system
- Interactive dashboard visualization

---

## Author

**Mohit Gandhi**  
BTech CSE (Data Science & AI/ML)
\