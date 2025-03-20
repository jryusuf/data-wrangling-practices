WITH LoyalCustomers AS (--filtering loyal customers e.g number of purchase >= 10
    SELECT 
        customer_id
    FROM 
        customer_purchases
    GROUP BY 
        customer_id
    HAVING 
        COUNT(*) >= 10
),
StandardizedPurchases AS(--mapping country names
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
    sp.product_id,
    sp.country,
    SUM(
        CASE 
            WHEN sp.quantity * pp.price >= 50 THEN sp.quantity * pp.price
            ELSE 0 
        END :: DECIMAL(8,2))  as total
FROM 
    StandardizedPurchases sp
INNER JOIN 
    LoyalCustomers lc
        ON sp.customer_id = lc.customer_id
LEFT JOIN 
    product_prices pp
        ON sp.product_id = pp.product_id AND 
        sp.purchase_date >= pp.valid_from AND
        (sp.purchase_date <= pp.valid_to OR pp.is_active = 1)
GROUP BY 
    sp.country, 
    sp.product_id
ORDER BY 
    total DESC;