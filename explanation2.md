# Problem 2: File Recursion
  Finding files starting from path x, the entire file directory is traversed to ensure everything is checked, so time complexity is O(n). Since recursion is used the previous recursive calls will be stored on a stack giving us O(n) in terms of space.

  This problem is best solved using recursion.  Starting at the root dir and then traversing every directory, checking its files is repeated until no subdirectories are available.
