import io

def get_payments_storage():
    return open('/dev/null', 'wb')

def stream_payments_to_storage(storage):
    storage.write(bytes([1, 2, 3]))

class ChecksumStorage(io.BufferedWriter):
    def __init__(self, storage):
        self._storage = storage
        self._checksum = 0

    def write(self, buffer):
        self._checksum += sum(buffer)
        return self._storage.write(buffer)

    def get_checksum(self):
        return self._checksum

def process_payments():
    storage = get_payments_storage()
    checksum_storage = ChecksumStorage(storage)
    stream_payments_to_storage(checksum_storage)
    print(checksum_storage.get_checksum())

process_payments()