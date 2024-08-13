def get_payments_storage():
    return open('/dev/null', 'wb')

def stream_payments_to_storage(storage):
    storage.write(bytes([1, 2, 3]))

def process_payments():
    checksum = 0

    class ChecksumWrapper:
        def __init__(self, wrapped):
            self.wrapped = wrapped

        def write(self, data):
            nonlocal checksum
            for byte in data:
                checksum += byte
            self.wrapped.write(data)

    storage = ChecksumWrapper(get_payments_storage())
    stream_payments_to_storage(storage)
    print(checksum)

process_payments()