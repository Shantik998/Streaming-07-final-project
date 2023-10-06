import csv
import random
import time
from queue import Queue
import threading

# Lists of specific values for variables
products = ['TM195', 'TM498', 'TM798']
marital_statuses = ['Single', 'Partnered']
usage = [3, 2, 4, 5, 6, 7]
fitness = [4, 3, 2, 1, 5]
educations = [14, 15, 12, 13, 16, 18, 20, 21]
ages = list(range(18, 51))

# Function to generate random fitness data
def generate_fitness_data():
    product = random.choice(products)
    age = random.choice(ages)
    gender = random.choice(['Male', 'Female'])
    education = random.choice(educations)
    marital_status = random.choice(marital_statuses)
    usage_val = random.choice(usage)
    fitness_val = random.choice(fitness)
    income = random.randint(20000, 100000)
    miles = random.randint(1, 50)

    return [product, age, gender, education, marital_status, usage_val,
            fitness_val, income, miles]

# Function to produce fitness data and write to CSV
def produce_data(producer_queue):
    while True:
        fitness_data = generate_fitness_data()
        producer_queue.put(fitness_data)
        time.sleep(1)  # Simulate data production every second

if __name__ == "__main__":
    producer_queue = Queue()
    producer_thread = threading.Thread(target=produce_data, args=(producer_queue,))
    producer_thread.start()

    # Write generated data to the CSV file
    with open('CardioGoodFitness.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        while True:
            fitness_data = producer_queue.get()
            csv_writer.writerow(fitness_data)
            csvfile.flush()  # Flush the buffer to ensure data is written immediately
