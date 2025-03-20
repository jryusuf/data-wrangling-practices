import pandas as pd


def main():
    customer_purchases = pd.read_csv("customer_purchases.csv")

    product_price = pd.read_csv("product_price.csv")

    #1 data cleaning and type conversion
    customer_purchases['purchase_date'] = pd.to_datetime(customer_purchases['purchase_date'])
    product_price['valid_from'] = pd.to_datetime(product_price['valid_from'])
    product_price['valid_to'] = pd.to_datetime(product_price["valid_to"], errors='coerce')
    product_price['price'] = pd.to_numeric(product_price['price'])

    #2 loyal customers logic
    loyal_customers = customer_purchases.groupby('customer_id').size()
    loyal_customer_ids = loyal_customers[loyal_customers >= 10].index.to_list()
    
    #4 join and filter loyal customers
    loyal_purchases = customer_purchases[customer_purchases['customer_id'].isin(loyal_customer_ids)]

    #3 standardized purchases logic
    standardized_purchases = loyal_purchases.copy()
    standardized_purchases['country'] = standardized_purchases['country'].apply(lambda c: 'United Kingdom' if c == 'UK' else c)
    merged_df = pd.merge(standardized_purchases, product_price, on='product_id', how='left')

    #5 apply data filtering
    filtered_merged_df = merged_df[
        (merged_df['purchase_date'] >= merged_df['valid_from']) &
        ((merged_df['purchase_date'] <= merged_df['valid_to']) | (merged_df['valid_to'].isnull()) | (merged_df['is_active'] == 1)) # Added is_active condition
    ].copy()
    

    #6 calculate total revenue and group
    filtered_merged_df['purchase_value'] = filtered_merged_df['quantity'] * filtered_merged_df['price']
    filtered_merged_df['revenue'] = filtered_merged_df['purchase_value']
    filtered_merged_df.loc[filtered_merged_df['purchase_value'] < 50, 'revenue'] = 0
    grouped_revenue = filtered_merged_df.groupby(['country', 'product_id'])['revenue'].sum().reset_index(name='total')
    
    #7 order results
    final_result = grouped_revenue.sort_values(by='total', ascending=False)
    print(final_result)

if __name__ == "__main__":
    main()
