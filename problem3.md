# Problem 3: Huffman Coding
#### Methods and Time / Space Complexity

  - character_frequencies: gets the input and counts and updates character frequency on the input data, storing this information in a map: key = char and value = frequency. Time and space complexity is O(n).

  - sort_frequencies: sorts the output from the previous function. Time complexity (n)*log(n) space complexity O(n).

  - map_frequencies_to_nodes: each item on the sorted list is mapped to a list of nodes, making it easier to manipulate the data. Time and Space O(n).

  - huffman_encoding: creates the tree - the previous functions are used here, to start creating the tree. It takes the sorted list and starts removing the elements from the top of the list until there is only one element left. This operation takes O(1) * O(n-1) which is O(n).

  - encode_tree: this method generates the code for each char in the tree, placing a 0 if it traverses to the left or 1 to the right, finally returning a map with each generated code. Time and Space is O(n).

 The whole encode operation takes O(n) * log(n) as worst case scenario

 To decode the tree, recursion is used. The method iterates through the entire encoded string and traverses the tree finding the desired value on the branch. Time and Space Complexity for this operation is O(n).

Conclusion : Encode -> O((n) * log(n)),  Decode O(n)
