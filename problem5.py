from datetime import datetime
import hashlib


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def get_utc_time(self):
        return datetime.utcfromtimestamp(float(self.timestamp))

    def calc_hash(self):
        encoded_data = hashlib.sha256(self.data.encode("utf-8"))
        encoded_timestamp = hashlib.sha256(self.timestamp.encode("utf-8"))
        encoded_data.hexdigest()
        encoded_timestamp.update(encoded_data.digest())
        if self.previous_hash is not None:
            encoded_timestamp.update(self.previous_hash.hash.encode("utf-8"))
        return encoded_timestamp.hexdigest()


class Block_Chain:
    def __init__(self):
        self.tail = None

    def add_block(self, data):
        if self.tail is None:
            self.tail = Block(str(datetime.now().timestamp()), data, None)
        else:
            tail = self.tail
            block = Block(str(datetime.now().timestamp()), data, tail)
            self.tail = block

        return self.tail

    def print_blockchain(self):
        tail = self.tail
        while tail is not None:
            print(
                "<<< Data: {} Hash: {} Timestamp: {} >>>".format(
                    tail.data, tail.hash, tail.get_utc_time()
                )
            )
            tail = tail.previous_hash


def test_blockchain():
    # Block Created
    blockchain = Block_Chain()
    blockchain.add_block("This")
    blockchain.add_block("is")
    blockchain.add_block("my")
    blockchain.add_block("blockchain")
    blockchain.print_blockchain()


def test_blockchain_1():
    # Hash Matching
    blockchain = Block_Chain()
    blockchain.add_block("This")
    blockchain.add_block("is")
    blockchain.add_block("my")
    blockchain.add_block("blockchain")
    after = blockchain.tail
    current = blockchain.tail.previous_hash
    while current is not None:
        current_hash = current.hash
        if after.previous_hash.hash != current_hash:
            return "Not Passed"
        after = current
        current = current.previous_hash

    return "Passed"


def test_blockchain_2():
    # Head is the Block created before
    blockchain = Block_Chain()
    start = blockchain.add_block("This")
    blockchain.add_block("is")
    blockchain.add_block("my")
    blockchain.add_block("blockchain")

    current = blockchain.tail
    while current.previous_hash is not None:
        current = current.previous_hash

    if current == start:
        return "Passed"
    else:
        return "Not Passed"


test_blockchain()
print(test_blockchain_1())
print(test_blockchain_2())
