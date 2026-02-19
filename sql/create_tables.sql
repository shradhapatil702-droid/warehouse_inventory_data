CREATE TABLE dim_category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE dim_location (
    location_id VARCHAR(10) PRIMARY KEY,
    zone VARCHAR(5),
    layout_efficiency_score FLOAT
);

CREATE TABLE fact_inventory (
    item_id VARCHAR(20) PRIMARY KEY,
    category_id INT,
    location_id VARCHAR(10),
    stock_level INT,
    daily_demand FLOAT,
    unit_price FLOAT,
    KPI_score FLOAT,
    FOREIGN KEY (category_id) REFERENCES dim_category(category_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id)
);


