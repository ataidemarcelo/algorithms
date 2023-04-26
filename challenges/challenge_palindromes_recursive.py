def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if low_index >= high_index:
        return True

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False


# word = "I"
# word = "GG"  # -> True
# word = "ANA"  # -> True
# word = "ESSE"  # -> True
# word = "SOCOS"  # -> True
# word = "REVIVER"  # -> True
# word = "AGUA"  # -> False
# word = ""  # -> False
# word = "A" * 200  # -> True

# word = "acararajadadajararaca"  # -> True
# word = "a cara rajada da jararaca"


# if __name__ == '__main__':
#     print(is_palindrome_recursive(word, 0, len(word) - 1))
