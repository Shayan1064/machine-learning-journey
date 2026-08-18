# E-Commerce Sales & Customer Analytics — Messy Dataset

This dataset is intentionally dirty. Do NOT clean it before starting.

Files:
- customers.csv
- products.csv
- orders.csv
- reviews.csv
- employees.csv

Approximate raw sizes:
- Customers: 512
- Products: 105
- Orders: 4530
- Reviews: 2020
- Employees: 53

Intentional data-quality problems include:
- Missing values
- Duplicate rows
- Leading/trailing whitespace
- Upper/lower/title-case inconsistencies
- Mixed date formats
- Invalid dates/IDs
- Orphan customer/product IDs
- Impossible ages
- Invalid prices/costs
- Negative/zero/huge quantities
- Invalid discounts
- Invalid ratings
- Mixed categorical spelling/casing
- Numeric columns containing missing/object values
- Repeated names
- Potential outliers

Suggested workflow:
1. Load all files with Pandas.
2. Perform an initial data-quality audit.
3. Document every issue before fixing it.
4. Clean and standardize the data.
5. Validate relationships between tables.
6. Engineer useful features.
7. Analyze business questions.
8. Visualize findings with Matplotlib.
9. Export cleaned datasets.
10. Prepare an ML-ready customer/product/order dataset.
