# Check if a string is a permutation of a palindrome


def if_palindrome_permutation(check_string):
    check_set = set()
    for c in check_string:
        if c in check_set:
            check_set.remove(c)
        else:
            check_set.add(c)
    return len(check_set) <= 1


def test_one_letter():
    assert if_palindrome_permutation('a') is True


def test_palindrome():
    assert if_palindrome_permutation("abcba") is True


def test_palindrome_permutation():
    assert if_palindrome_permutation("cbacb") is True
