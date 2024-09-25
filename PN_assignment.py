import csv # Executing CSV built-in mode to work with csv files

# File paths
input_file_path ='C:\\Users\\xnikpa\\Downloads\\Assignment\\brca_cnvs_tcga-1-2.csv'  # Remember to replace with your actual file path
output_file_path ='C:\\Users\\xnikpa\\Downloads\\Assignment\\output.csv'  # Remember to replace with your actual output file path

# Open the input and output files
with open(input_file_path, mode='r') as infile, open(output_file_path, mode='w', newline='') as outfile:
    # Create CSV reader and writer objects
    csv_reader = csv.DictReader(infile)
    fieldnames = csv_reader.fieldnames + ['length']  # Add 'length' to the existing field names
    csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    # Write the header to the output file
    csv_writer.writeheader()

    # Process each row
    for row in csv_reader:
        # Calculate the segment length
        loc_start = int(row['loc.start'])
        loc_end = int(row['loc.end'])
        row['length'] = loc_end - loc_start

        # Write the updated row to the output file
        csv_writer.writerow(row)

print("Great job! CSV file has been processed successfully!")
