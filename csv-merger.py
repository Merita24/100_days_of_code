import csv
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')

def merge_csv(input_files,output_file):
    logging.info("Starting CSV merger....")
    try:
        with open(output_file,"w",newline="") as outfile:
            writer=None
            for f in input_files:
                try:
                    with open(f,"r",newline="") as infile:
                        reader=csv.DictReader(infile)
                        if writer is None:
                            writer=csv.DictWriter(outfile,fieldnames=reader.fieldnames)
                            writer.writeheader()
                        for row in reader:
                            writer.writerow(row)
                            logging.info(f"Merged {f} successfully")
                except FileNotFoundError:
                    logging.error(f"File {f} not found. Skipping.")
                except PermissionError:
                    logging.error(f"Permission denied for {f}")
                except Exception as e:
                    logging.error(f"An error occurred while processing {f}: {e}")
    except Exception as e:
        logging.critical("Failed to merge CSV files: {e}")
    logging.info("CSV merging completed.")
                
if __name__=="__main__":
    input_files=["data1.csv","data2.csv"]
    merge_csv(input_files,"merged_output.csv")