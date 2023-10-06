import csv
import time

# Function to process fitness data
def process_fitness_data(data):
    # Replace this with your specific data processing logic
    print("Received fitness data:", data)

if __name__ == "__main__":
    while True:
        try:
            with open('CardioGoodFitness.csv', 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    process_fitness_data(row)
        except FileNotFoundError:
            print("File 'CardioGoodFitness.csv' not found. Waiting for data...")
            time.sleep(5)  # Wait for 5 seconds before checking again
