
cupcake_invoices = open("CupcakeInvoices.csv");

for row in cupcake_invoices:
    print(row);
    
cupcake_invoices.close()

cupcake_invoices = open("CupcakeInvoices.csv");
    
for row in cupcake_invoices:
    row = row.rstrip('\n').split(',')
    print(row[2]);
    
cupcake_invoices = open("CupcakeInvoices.csv");

for row in cupcake_invoices:
    row = row.rstrip('\n').split(',')
    quantity = float(row[3])
    price = float(row[4])
    total = quantity * price
    limited_total = round(total, 2)
    print(limited_total);

cupcake_invoices.close()

cupcake_invoices = open("CupcakeInvoices.csv");

allTotal = 0
for row in cupcake_invoices:
    row = row.rstrip('\n').split(',')

    quantity = float(row[3])
    price = float(row[4])
    total = quantity * price
    allTotal += total;
    

limited_all_total = round(allTotal, 2)

print(limited_all_total)

cupcake_invoices.close()