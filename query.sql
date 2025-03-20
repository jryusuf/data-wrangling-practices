WITH LoyalCustomers AS (
    --filtering loyal customers e.g number of purchase >= 10
    SELECT 
        customer_id
    FROM 
        customer_purchases
    GROUP BY 
        customer_id
    HAVING 
        COUNT(*) >= 10
),
StandardizedCountries AS(
    --mapping country names
    SELECT 
        customer_id, purchase_date, product_id, quantity,
        CASE 
            WHEN country = 'UK' THEN 'United Kingdom'
            ELSE country
        END as country
    FROM 
        customer_purchases
)
SELECT
    sc.product_id,
    sc.country,
    SUM(
        CASE 
            WHEN sc.quantity * pp.price >= 50 THEN sc.quantity * pp.price
            ELSE 0 
        END :: INTEGER)  as total
FROM 
    StandardizedCountries sc
INNER JOIN 
    LoyalCustomers lc
        ON sc.customer_id = lc.customer_id
LEFT JOIN 
    product_prices pp
        ON sc.product_id = pp.product_id AND 
        sc.purchase_date >= pp.valid_from AND
        (sc.purchase_date <= pp.valid_to OR pp.is_active = 1)
GROUP BY 
    sc.country, 
    sc.product_id
ORDER BY 
    total DESC;