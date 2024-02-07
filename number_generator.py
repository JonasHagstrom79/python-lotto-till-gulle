import random

def generate_series(count):
    """
    Generates and prints 'count' series of 7 unique random numbers between 1 and 35,
    ordered in ascending order.
    
    :param count: The number of series to generate.
    """
    for _ in range(count):
        series = sorted(random.sample(range(1, 36), 7))
        print(series)

if __name__ == "__main__":
    try:
        series_count = int(input("Enter the number of series to generate: "))
        generate_series(series_count)
    except ValueError:
        print("Please enter a valid integer.")
