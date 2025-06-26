def tax_calculator(subtotal, sales_tax = 0.06):
    
    tax = subtotal * sales_tax
    total = subtotal + tax
    
    return[subtotal, tax, total]

tax_calculator(100, 0.08)