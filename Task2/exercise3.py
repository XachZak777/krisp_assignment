def get_payments_storage():
    return open('/dev/null', 'wb')

def stream_payments_to_storage(storage):
    for i in range(10):
        storage.write(bytes([1, 2, 3]))
        
class ChecksumStorage:
    def __init__(self, storage):
        self.storage = storage
        self.checksum = 0

    def write(self, buffer):
        self.checksum += sum(buffer)
        self.storage.write(buffer)

    def get_checksum(self):
        return self.checksum

def process_payments():
    storage = get_payments_storage()
    checksum_storage = ChecksumStorage(storage)

    stream_payments_to_storage(checksum_storage)
    
    print(checksum_storage.get_checksum())

process_payments()