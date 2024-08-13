import itertools

def stream_payments(callback_fn):
    # Simulating a finite number of payments (for example, 5 payments).
    for i in range(5):  # Adjust this number as needed
        callback_fn(i * 100)  # Example payment amounts
    return

def store_payments(amount_iterator):
    # Iterates over the payment amounts from amount_iterator and stores them to a remote system.
    for amount in amount_iterator:
        print(f"Stored payment: {amount}")

def callback_example(amount):
    store_payments([amount])  # Store the payment amount as a single-element list

def process_payments_2():
    # Create a finite iterator for the range of payments
    amount_iterator = range(100, 600, 100)  # Payments: 100, 200, 300, 400, 500
    # Store the payments using `store_payments`
    store_payments(amount_iterator)
    # Stream the payments using `stream_payments`
    stream_payments(callback_example)

process_payments_2()