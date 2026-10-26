# solutions.py - Task 3: Python Coding & Problem-Solving


# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


# Q2. Find the Frequency of Each Character in a Word
def char_frequency(word):
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating(word):
    freq = char_frequency(word)
    for ch in word:
        if freq[ch] == 1:
            return ch
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return char_frequency(s1) == char_frequency(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating(text):
    seen = set()
    for ch in text:
        if ch in seen:
            return ch
        seen.add(ch)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros(nums):
    non_zeros = [n for n in nums if n != 0]
    zeros = [0] * (len(nums) - len(non_zeros))
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest(nums):
    first = None
    second = None
    for n in nums:
        if first is None or n > first:
            if first is not None:
                second = first
            first = n
        elif n != first and (second is None or n > second):
            second = n
    return second


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(nums):
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result


# Q9. Find the Missing Number from 1 to N
def find_missing(nums, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_pair(nums, target):
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None
    best = nums[0]
    for n in nums:
        if abs(n) < abs(best) or (abs(n) == abs(best) and n > best):
            best = n
    return best


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    in_second = set(list2)
    result = []
    for n in list1:
        if n in in_second and n not in result:
            result.append(n)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    best = nums[0] + nums[1]
    for i in range(1, len(nums) - 1):
        total = nums[i] + nums[i + 1]
        if total > best:
            best = total
    return best


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs(nums, target):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add((min(nums[i], nums[j]), max(nums[i], nums[j])))
    return [list(p) for p in sorted(pairs)]