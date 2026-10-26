# main.py - calls every function from solutions.py
from solutions import (
    word_frequency, char_frequency, first_non_repeating, are_anagrams,
    first_repeating, move_zeros, second_highest, remove_duplicates,
    find_missing, two_sum_pair, closest_to_zero, common_elements,
    rotate_right, max_consecutive_sum, all_pairs,
)

print("Q1:", word_frequency("python is easy and python is powerful"))   # given example
print("Q1:", word_frequency("to be or not to be"))                      # extra test

print("Q2:", char_frequency("banana"))
print("Q2:", char_frequency("hello"))

print("Q3:", first_non_repeating("swiss"))
print("Q3:", first_non_repeating("aabb"))                               # None

print("Q4:", are_anagrams("listen", "silent"))
print("Q4:", are_anagrams("hello", "world"))

print("Q5:", first_repeating("programming"))
print("Q5:", first_repeating("abc"))                                    # None

print("Q6:", move_zeros([0, 3, 0, 1, 2, 0, 4]))
print("Q6:", move_zeros([0, 0, 5]))

print("Q7:", second_highest([10, 20, 40, 30, 40, 20]))
print("Q7:", second_highest([5, 5, 5]))                                 # None

print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8:", remove_duplicates([1, 1, 1]))

print("Q9:", find_missing([1, 2, 4, 5, 6], 6))
print("Q9:", find_missing([2, 3, 4, 5], 5))

print("Q10:", two_sum_pair([2, 7, 11, 15], 9))
print("Q10:", two_sum_pair([1, 2, 3], 10))                              # []

print("Q11:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11:", closest_to_zero([-4, 4, 9]))                              # 4

print("Q12:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12:", common_elements([1, 1, 2], [2, 1]))

print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13:", rotate_right([1, 2, 3], 5))

print("Q14:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14:", max_consecutive_sum([-3, -1, -5]))

print("Q15:", all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15:", all_pairs([1, 1, 2, 2], 3))                               # [[1, 2]]