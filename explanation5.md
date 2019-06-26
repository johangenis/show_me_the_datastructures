# Problem 5: Blockchain
A Linked List is used for this problem, since it is easier to keep track of previous items on the blockchain. Retrieval of the last block is O(1) and the first one is O(n).

 - hash_function: the hash function is calculated hashing the data with sha256 using utf-8 encoding. Then with the encoded data as hex string we add another encode that is the timestamp ciphering the data twice.

Hash function and inserting a block are O(1), printing the whole blockchain is O(n).
