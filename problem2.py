import os

TEST_DIR = "./testdir"


def find_files(suffix=None, path=None):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    if not suffix or not path or not os.path.isdir(path):
        return []

    path_content = os.listdir(path)
    files_found = []

    for path_item in path_content:
        if os.path.isfile(os.path.join(path, path_item)) and path_item.endswith(suffix):
            files_found.append(os.path.join(path, path_item))
        if os.path.isdir(os.path.join(path, path_item)):
            files_found += find_files(suffix, os.path.join(path, path_item))
    return files_found


# normal case
def test_sample_dir():
    files = find_files(".c", ".")
    print(files)


# empty suffix
def test_sample_dir_2():
    files = find_files("", ".")
    print(files)


# not a dir
def test_sample_dir_3():
    files = find_files(".c", ".h")
    print(files)


test_sample_dir()
test_sample_dir_2()
test_sample_dir_3()
