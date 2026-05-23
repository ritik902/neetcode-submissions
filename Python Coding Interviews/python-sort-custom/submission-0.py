from typing import List

def z(l):
    return len(l)

def x(l):
    return abs(l)

def sort_words(words: List[str]) -> List[str]:
    # print(words)
    words.sort(key=z,reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=x)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
