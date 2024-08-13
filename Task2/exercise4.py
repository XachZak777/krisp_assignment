import io

def stream_payments(callback_fn):
    for i in range(10):
        callback_fn(i)

def store_payments(amount_iterator):
    for i in amount_iterator:
        print(i)

def payment_generator():
    def collect_payments(amount):
        yield amount

    stream_payments(lambda amount: next(collect_payments(amount)))

def process_payments_2():
    gen = payment_generator()
    store_payments(gen)

process_payments_2()