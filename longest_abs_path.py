# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Suppose we represent our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
#
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
#
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
#
# Note:
#
# The name of a file contains at least a period and an extension.
#
# The name of a directory or sub-directory will not contain a period.

def longest_abs_path(string):
    if len(string) == 0:
        return 0
    parent_stack = []
    lines = string.split("\n")
    prev_number_tabs = -1
    max_len = 0
    for line in lines:
        tmp = line
        number_tabs = 0
        while tmp[0] == '\t':
            number_tabs += 1
            tmp = line[number_tabs:]
        assert number_tabs <= prev_number_tabs + 1
        if number_tabs == 0:
            parent_stack.append(len(tmp))
            max_len = len(tmp)
            prev_number_tabs = number_tabs
            continue
        if number_tabs == prev_number_tabs:
            del parent_stack[-1]
        elif number_tabs < prev_number_tabs:
            diff = prev_number_tabs-number_tabs
            del parent_stack[-(diff+1):]
        if parent_stack[-1]+len(tmp)+1 > max_len:
            max_len = parent_stack[-1]+len(tmp)+1
        parent_stack.append(parent_stack[-1]+len(tmp)+1)
        prev_number_tabs = number_tabs
    return max_len


print(longest_abs_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))#32