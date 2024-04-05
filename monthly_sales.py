def calculate_sales(data):
    total_sales = []
    for row in data:
        monthly_sales = row['sales']
        total_sales.append(int(monthly_sales))
    return (len(total_sales), sum(total_sales))