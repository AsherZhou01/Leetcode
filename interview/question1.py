# Time: O(m*n), Space: O(1)
def min_subseq(source, target):
        def find(i, j):
            while i < len_src and j < len_target:
                if source[i] == target[j]:
                    j += 1
                i += 1
            return j

        len_src, len_target = len(source), len(target)
        subseq_count = 0
        # initiate two pointers
        i, j = 0, 0
        while j < len_target:
            j_next = find(0, j)
            # there are no character in src match target[j]
            if j == j_next:
                return -1
            j = j_next
            # increment by 1 and start the next search
            subseq_count += 1
        return subseq_count

# testcase
print(min_subseq("abc", "abcbc"))  # output: 2
print(min_subseq("abc", "acdbc"))  # output: -1
print(min_subseq("xyz", "xzyxz"))  # output: 3
print(min_subseq("", "abc"))       # output: -1
print(min_subseq("abc", ""))       # output: 0
print(min_subseq("", ""))          # output: 0
print(min_subseq("ab", "a"))       # output: 1