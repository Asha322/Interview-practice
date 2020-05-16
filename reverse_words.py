#   reverse words in a string in place
#   Example:
#   message = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]
# # Prints: 'steal pound cake'


def reverse_one_word(string, left, right):
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1


def reverse_string(message):
    # reverse full message
    reverse_one_word(message, 0, len(message) - 1)
    # keep track of every word start
    start = 0
    for i in range(len(message) + 1):
        # reverse every word separately
        if (i == len(message)) or (message[i] == ' '):
            reverse_one_word(message, start, i - 1)
            start = i + 1
    return message


def test_one_word():
    assert reverse_string(list("oneword")) == list("oneword")


def test_multiple_words():
    assert reverse_string(list("reverse to words test")) == list("test words to reverse")