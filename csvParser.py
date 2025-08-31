import csv

input_files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
with open('outputFile.csv', mode='w') as outfile:
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for filename in input_files:
        with open(filename, newline='') as infile:
            csv_reader = csv.reader(infile, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    # Calculates sales
                    # row[1].lstrip('$') - takes out $ sign from the string
                    # float(...) - converts the string to a float
                    sales = float(row[1].lstrip('$')) * float(row[2])
                    print(f'Sales: ${sales:.2f}, Date: {row[3]}, Region: {row[4]}')
                    # Writes to the outputFile
                    writer.writerow({'sales': f'{sales:.2f}', 'date': row[3],'region': row[4]})
                    line_count += 1
    print(f'Processed {line_count} lines.')

   