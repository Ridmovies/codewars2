import codewars_test as test


# def high(x):
#     #################### VERSION 3 #######################
#
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


#################### VERSION 2 #######################
# x = x.split()
# l = []
# for i in list(map(lambda n: list(n), x)):
#     l.append(sum(list(map(lambda n: ord(n)-96, i))))
#
# return x[l.index(max(l))]


#################### VERSION 1 #######################
# Code here
# import string
# s = (string.ascii_lowercase)
# a = []
# a1 = []
# k = []
#
# for i in x.split():
#     a1.append(str(''.join(i)))
#     a.append(str(''.join(set(i))))
# print(a)
#
# for i in a1:
#     r = 0
#     for j in i:
#         r += s.index(j)+1
#     k.append(r)
# print(k)
# return a1[(k.index(max(k)))]

# print(high('what time are we climbing up the volcano'))


# def is_prime(num):
#     # if num == 1 or num == 0 or num > 0
#     #     return False
#     # return False if [i for i in range(2, num) if num % i == 0] else True
#     count = num - 1
#     while count != 1:
#         print(num)
#         if num % count == 0:
#             print(num, count)
#             return False
#         count -= 1
#     return True
#
# print(is_prime(11))


# def decode_morse(morse_code):

#     import re
#     MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
#                        'C': '-.-.', 'D': '-..', 'E': '.',
#                        'F': '..-.', 'G': '--.', 'H': '....',
#                        'I': '..', 'J': '.---', 'K': '-.-',
#                        'L': '.-..', 'M': '--', 'N': '-.',
#                        'O': '---', 'P': '.--.', 'Q': '--.-',
#                        'R': '.-.', 'S': '...', 'T': '-',
#                        'U': '..-', 'V': '...-', 'W': '.--',
#                        'X': '-..-', 'Y': '-.--', 'Z': '--..',
#                        '1': '.----', '2': '..---', '3': '...--',
#                        '4': '....-', '5': '.....', '6': '-....',
#                        '7': '--...', '8': '---..', '9': '----.',
#                        '0': '-----', ', ': '--..--', '.': '.-.-.-',
#                        '?': '..--..', '/': '-..-.', '-': '-....-',
#                        '(': '-.--.', ')': '-.--.-',
#                        'SOS': '...---...', '!': '-.-.--'}
#
#     inverted_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
#     a = []
#
#     for i in morse_code.strip().split(' '):
#         a.append(inverted_dict.get(i))
#
#     b = ([' ' if i == None else i for i in a ])
#     result = re.sub('  ', ' ', ''.join(b))
#     return result
#
#     # return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
#
#
# print(decode_morse('...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.- '))


# def delete_nth(order,max_e):
#     a = []
#     for i in order:
#         if a.count(i) < max_e:
#             a.append(i)
#     return a
#
#
# print(delete_nth([1,1,3,3,7,2,2,2,2], 3))


# def valid_braces(string):
#     close = [')', ']', '}']
#     opposite = {')': '(', ']': '[', '}': '{'}
#
#     a = []
#     for i in string:
#         if i in close:
#             if a and a[-1] == opposite[i]:
#                 a.remove(opposite[i])
#             else:
#                 return False
#         else:
#             a.append(i)
#         print(a)
#
#     return True if len(a) == 0 else False
#
# print(valid_braces('[(])'))


# def expanded_form(num):
# x = num

# for n in range(1, len(str(num))):
#     if str(num)[n] != '0':
#         z = int(str(num)[n:])
#         a.append(str(x - z))
#         a.append(' + ')
#         x = z
#         if len(str(x)) == 1:
#             a.append(str(x))
# return ''.join(a)

# a = []
# for n, i in enumerate(str(num)[::-1]):
#     if i != '0':
#         a.append(str(i)+('0'*n))
# return ' + '.join(a[::-1])

#     return ' + '.join([(i + ('0'*n)) for n, i in enumerate(str(num)[::-1]) if i != '0'][::-1])
#
#
# print(expanded_form(704))

# array1 = [56, 67, 86, 62, 69, 25, 24, 29, 91, 30, 99, 46, 31, 4, 16, 26, 60, 61, 62]
# array2 = [576, 3136, 256, 625, 9801, 8281, 900, 7396, 3721, 841, 3600, 676, 961, 3844, 16, 3844, 2116, 4782, 4489]
#
#
# def comp(array1, array2):
#     array1 = list(map(lambda x: abs(x), array1))
#     if array2 == [] or array1 == []: return False
#     for i in array2:
#         print(array2.count(int(i)), int(i), array1.count(int(i**0.5)), int(i), len(array1), len(array2))
#         if array2.count(int(i)) != array1.count(abs(int(i**0.5))):
#             return False
#     return True
#
#
#
# print(comp(array1, array2))


### English beggars

# def beggars(values, n):
#     res = []
#     if not values:
#         return 0
#     for i in range(n):
#         return values[0] + beggars(values[n:], n)
#
#
# test.describe("Basic tests")
# test.assert_equals(beggars([1,2,3,4,5],1),[15])
# test.assert_equals(beggars([1,2,3,4,5],2),[9,6])
# test.assert_equals(beggars([1,2,3,4,5],3),[5,7,3])
# test.assert_equals(beggars([1,2,3,4,5],6),[1,2,3,4,5,0])
# test.assert_equals(beggars([1,2,3,4,5],0),[])


### Array Deep Count

# def deep_count(a):
#     cnt = 0
#     for i in a:
#         if type(i) == list:
#             cnt += deep_count(i) + 1
#         else:
#             cnt += 1
#     return cnt
#
#
#
# test.assert_equals(deep_count([]), 0)
# test.assert_equals(deep_count([1, 2, 3]), 3)
# test.assert_equals(deep_count(["x", "y", ["z"]]), 4)
# test.assert_equals(deep_count([1, 2, [3, 4, [5]]]), 7)
# test.assert_equals(deep_count([[[[[[[[[]]]]]]]]]), 8)


### Mutual Recursion

# def f(n):
#     if n == 0:
#         return 1
#     return n - m(f(n-1))
#
# def m(n):
#     if n == 0:
#         return 0
#     return n - f(m(n-1))
#
#
# test.it("Basic tests")
# test.assert_equals(f(0),1)
# test.assert_equals(f(5),3)
# test.assert_equals(f(10),6)
# test.assert_equals(m(0),0)
# test.assert_equals(m(5),3)
# test.assert_equals(m(10),6)


# ### Parse a linked list from a string    !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
#     def __str__(self):
#         return f'{self.data}'
#
# # ### recursion
# def linked_list_from_string(s):
#     head = None
#     prev = None
#     s = s.split(' -> ')
#     for i in range(len(s)):
#         print(s[i])
#         if s[i] == 'None':
#             return
#         return linked_list_from_string(Node(s[i], s[i+1]))
#     return head
#
#
# print(linked_list_from_string("0 -> 1 -> 4 -> 9 -> 16 -> None"))

### iteration
# def linked_list_from_string(s):
#     head = None
#     prev = None
#     s = s.split(' -> ')
#
#     for i in range(1, len(s)):
#         if s[i] != 'None':
#             obj = Node(int(s[i]))
#             if head is None:
#                 head = Node(int(s[i-1]), next=obj)
#             if prev:
#                 prev.next = obj
#             prev = obj
#         elif s[i] == 'None' and not head:
#             head = Node(int(s[i - 1]))
#
#     return head
#
#
# print(linked_list_from_string("0 -> 1 -> 4 -> 9 -> 16 -> None"))


### Look and say numbers
### iteration
# def look_and_say(data='1', maxlen=5):
#     res = []
#     res.append(data)
#     for n in range(maxlen):
#         if len(res[n]) == 1:
#             res.append('1' + res[n])
#         else:
#             cnt = 1
#             cur = res[n]
#             tmp = ''
#             for i in range(len(cur)-1):
#                 if cur[i] == cur[i+1]:
#                     cnt += 1
#                 else:
#                     tmp += str(cnt) + str(cur[i])
#                     cnt = 1
#             tmp += str(cnt) + str(cur[i+1])
#             res.append(tmp)
#
#     return res[1:]


### The Book of Mormon

# def mormons(starting_number, reach, target):
#     if starting_number >= target:
#         return 0
#     return mormons(starting_number * reach + starting_number, reach, target) + 1
#
# test.describe("Basic tests")
# test.assert_equals(mormons(10, 3, 9),
#                    0)  # No missions are needed because the number of followers already exceeds target
# test.assert_equals(mormons(99, 2, 99), 0)
# test.assert_equals(mormons(40, 2, 120), 1)
# test.assert_equals(mormons(40, 2, 121), 2)
# test.assert_equals(mormons(20000, 2, 7000000000), 12)  # Mormons dominate the world!


### Words to Hex
### iteration
# def words_to_hex(words):
#     res = []
#     for w in words.split():
#         tmp = ['#']
#         for i in range(3):
#             try:
#                 tmp.append(hex(ord(w[i]))[2:])
#             except:
#                 tmp.append('00')
#         res.append("".join(tmp))
#     return res


# def words_to_hex(words):
#     return [f"#{w[:3].hex():0<6}" for w in words.encode().split()]
#
# test.assert_equals(words_to_hex("Hello, my name is Gary and I like cheese."),
#                    ['#48656c', '#6d7900', '#6e616d', '#697300', '#476172', '#616e64', '#490000', '#6c696b',
#                     '#636865']);
# test.assert_equals(words_to_hex("0123456789"), ['#303132']);
# test.assert_equals(words_to_hex("ThisIsOneLongSentenceThatConsistsOfWords"), ['#546869']);
# test.assert_equals(words_to_hex("Blah blah blah blaaaaaaaaaaaah"), ['#426c61', '#626c61', '#626c61', '#626c61']);
# test.assert_equals(words_to_hex("&&&&& $$$$$ ^^^^^ @@@@@ ()()()()("),
#                    ['#262626', '#242424', '#5e5e5e', '#404040', '#282928']);


# def digital_root(n):
#     """ Sum of Digits / Digital Root """
#     if n < 10:
#         return n
#     return digital_root(n % 10 + n // 10)
#
#
# test.assert_equals(digital_root(16), 7)
# test.assert_equals(digital_root(942), 6)
# test.assert_equals(digital_root(132189), 6)
# test.assert_equals(digital_root(493193), 2)


### Array.diff
# def array_diff(a, b):
#     for i in b:
#         while i in a:
#             a.remove(i)
#     return a
#
#
# test.assert_equals(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
# test.assert_equals(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
# test.assert_equals(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
# test.assert_equals(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
# test.assert_equals(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
# test.assert_equals(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")


### Bit Counting
# def count_bits(n):
#     return str(bin(n)[2:]).count('1')
#
# test.assert_equals(count_bits(1234), 5)


### Counting Duplicates
# def duplicate_count(text):
#     # Your code goes here
#     dic = {}
#     for i in text.lower():
#         if i not in dic:
#             dic[i] = 0
#         dic[i] += 1
#
#     cnt = 0
#     for i in dic:
#         if dic[i] > 1:
#             cnt += 1
#     return cnt


### Duplicate Encoder
# def duplicate_encode(word):
#     dic = {}
#     for i in word.lower():
#         if i not in dic:
#             dic[i] = '('
#         else:
#             dic[i] = ')'
#     res = []
#     for i in word.lower():
#         res.append(dic[i])
#     return "".join(res)


# def alphabet_position(text):
# """Replace With Alphabet Position"""
#     # res = []
#     # for word in list(text.split(' ')):
#     #     for i in word:
#     #         if i.isalpha():
#     #             i = i.lower()
#     #             res.append(str(ord(i) - 96))
#     # return ' '.join(res)
#
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
#
#
# test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")


# from functools import reduce
# def persistence(n, cnt=0):
#     """Persistent Bugger."""
#     # cnt = 0
#     # while n > 9:
#     #     cnt += 1
#     #     n = reduce(lambda a, b: a*b, list(map(int, list(str(n)))))
#     # return cnt
#     ### recursion
#     # if n < 10:
#     #     return cnt
#     # n = reduce(lambda a, b: a * b, list(map(int, list(str(n)))))
#     # return persistence(n, cnt+1)
#
#
# test.assert_equals(persistence(39), 3)
# test.assert_equals(persistence(4), 0)
# test.assert_equals(persistence(25), 2)
# test.assert_equals(persistence(999), 4)


# def order(sentence):
# """Your order, please"""
# if not sentence:
#     return ''
# sentence = sentence.split(' ')
# res = [0] * len(sentence)
# for word in sentence:
#     for i in word:
#         if i.isdigit():
#             res[int(i)-1] = word
# return ' '.join(res)

### return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))

# test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
# test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
# test.assert_equals(order(""), "")


# def to_camel_case(text):
#     """Convert string to camel case"""
#     text = text.replace('_', '-')
#     text = list(text)
#     for i in range(len(text)):
#         if text[i] == '-':
#             text[i+1] = text[i+1].upper()
#
#     return ''.join(text).replace('-', '')
#
#
# test.assert_equals(to_camel_case(""), "", "An empty string was provided but not returned")
# test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior",
#                    "to_camel_case('the_stealth_warrior') did not return correct value")
# test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior",
#                    "to_camel_case('The-Stealth-Warrior') did not return correct value")
# test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")


# def tribonacci(signature, n):
#     """Tribonacci Sequence"""
#     res = [0] * n
#     for i in range(n):
#         if i < len(signature):
#             res[i] = signature[i]
#         else:
#             res[i] = sum(res[i - len(signature):i])
#     return res
#
#
# test.assert_equals(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
# test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])


# def unique_in_order(sequence):
#     """Unique In Order"""
#     if len(sequence) == 1:
#         return [sequence[0]]
#     elif not sequence:
#         return []
#
#     res = []
#     for i in range(1, len(sequence)):
#         if sequence[i] != sequence[i-1]:
#             res.append(sequence[i-1])
#     res.append(sequence[-1])
#     return res
#
#
# test.assert_equals(unique_in_order("AA"), ["A"])
# test.assert_equals(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])


# def narcissistic(value):
#     # res = 0
#     # tmp = value
#     # while tmp > 0:
#     #     res += (tmp % 10) ** len(str(value))
#     #     tmp //= 10
#     # return bool(res == value)
#
#     return value == sum([int(i)**len(str(value)) for i in str(value)])
#
#
# test.assert_equals(narcissistic(371), True, '371 is narcissistic');


# MORSE_CODE = {".-": "A",
#           "-...": "B",
#           "-.-.": "C",
#           "-..": "D",
#           ".": "E",
#           "..-.": "F",
#           "--.": "G",
#           "....": "H",
#           "..": "I",
#           ".---": "J",
#           "-.-": "K",
#           ".-..": "L",
#           "--": "M",
#           "-.": "N",
#           "---": "O",
#           ".--.": "P",
#           "--.-": "Q",
#           ".-.": "R",
#           "...": "S",
#           "-": "T",
#           "..-": "U",
#           "...-": "V",
#           ".--": "W",
#           "-..-": "X",
#           "-.--": "Y",
#           "--..": "Z",
#           "-----": "0",
#           ".----": "1",
#           "..---": "2",
#           "...--": "3",
#           "....-": "4",
#           ".....": "5",
#           "-....": "6",
#           "--...": "7",
#           "---..": "8",
#           "----.": "9"}


# def decode_morse(morse_code):
#     res = []
#     morse_code = morse_code.replace('  ', ' ^ ')
#     for i in morse_code.split():
#         if i in MORSE_CODE:
#             res.append(MORSE_CODE[i])
#         if i not in MORSE_CODE:
#             res.append(i)
#     morse_code = ''.join(res)
#     return morse_code.replace('^', ' ').strip()


# def dig_pow(n, p):
#     res = 0
#     for i in str(n):
#         res += int(i) ** p
#         p += 1
#     k = res / n
#     return k if int(k) == k else -1
#
# test.assert_equals(dig_pow(89, 1), 1)
# test.assert_equals(dig_pow(92, 1), -1)
# test.assert_equals(dig_pow(46288, 3), 51)
# test.assert_equals(dig_pow(41, 5), 25)
# test.assert_equals(dig_pow(114, 3), 9)
# test.assert_equals(dig_pow(8, 3), 64)


# def find_even_index(arr):
#     for i in range(0, len(arr)):
#         if sum(arr[0:i]) == sum(arr[i+1:]):
#             return i
#     return -1
#
#
# test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)


# def is_pangram(s):
#     alphaset = set()
#     for i in s:
#         if i.isalpha():
#             alphaset.add(i.lower())
#     print(alphaset)
#     return len(alphaset) == 26
#
#
# test.assert_equals(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
# test.assert_equals(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)


# def find_uniq(arr):
#     # your code here
#     a = None
#     b = None
#     for i in arr:
#         if a is None:
#             a = i
#         elif i != a and b is None:
#             b = i
#         elif i == a and b is not None:
#             return b
#         elif i == b and a is not None:
#             return a
#     return b
#
#
# test.assert_equals(find_uniq([1, 1, 1, 1, 1, 2]), 2)
# test.assert_equals(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
# test.assert_equals(find_uniq([3, 10, 3, 3, 3]), 10)
# test.assert_equals(find_uniq([10, 3, 3, 3, 3]), 10)


# def solution(s):
#     if len(s) % 2 != 0:
#         s += '_'
#     res = []
#     i = 0
#     for _ in range(len(s) // 2):
#         res.append(s[i:i+2])
#         i += 2
#     return res


# def sort_array(source_array):
#     odd = []
#     for i in source_array:
#         if i % 2:
#             odd.append(i)
#             odd.sort()
#
#     cnt = 0
#     for n, i in enumerate(source_array):
#         if i % 2:
#             source_array[n] = odd[cnt]
#             cnt += 1
#
#     return source_array
#
#
# test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
# test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
# test.assert_equals(sort_array([]),[])


# def find_missing_letter(chars):
#     start = ord(chars[0])
#     cnt = 0
#     for i in range(start, start+26):
#         if chr(i) != chars[cnt]:
#             return chr(i)
#         cnt += 1
#
#
# test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
# test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')


# def tower_builder(n_floors):
#     ascii_list = []
#     for n in range(1, n_floors+1):
#         s = ' ' * (n_floors - n) + '*' * (n*2-1) + ' ' * (n_floors - n)
#         ascii_list.append(s)
#
#     return ascii_list
#
#
# test.assert_equals(tower_builder(1), ['*', ])
# test.assert_equals(tower_builder(2), [' * ', '***'])
# test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])


# def high(x):
#     dic = {}
#     for i in x.split():
#         dic[i] = sum([ord(k)-96 for k in i])
#     max_word = max(dic, key=dic.get)
#     return max_word
#
# test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
# test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
# test.assert_equals(high('take me to semynak'), 'semynak')
# test.assert_equals(high('aa b'), 'aa')
# test.assert_equals(high('b aa'), 'b')
# test.assert_equals(high('bb d'), 'bb')
# test.assert_equals(high('d bb'), 'd')
# test.assert_equals(high("aaa b"), "aaa")


# def delete_nth(order,max_e):
#     res = []
#     for i in order:
#         if res.count(i) < max_e:
#             res.append(i)
#
#     return res
#
#
# test.assert_equals(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
# test.assert_equals(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])


# import re
#
#
# def count_smileys(arr):
#     pattern = r"[:;][-~]?[)D]"
#     count = 0
#
#     # Iterate over each string in the array
#     for s in arr:
#         # Use the re.match() function to check if the string matches the pattern
#         if re.match(pattern, s):
#             count += 1
#
#     # Return the final count
#     return count
#
#
# test.assert_equals(count_smileys([]), 0)
# test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
# test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
# test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)


# def find_nb(m):
#     volume = 0
#     n = 1
#     while volume < m:
#         volume += n**3
#         if volume == m:
#             return n
#         n += 1
#     return -1
#
#
# test.assert_equals(find_nb(4183059834009), 2022)
# test.assert_equals(find_nb(24723578342962), -1)
# test.assert_equals(find_nb(135440716410000), 4824)
# test.assert_equals(find_nb(40539911473216), 3568)
# test.assert_equals(find_nb(26825883955641), 3218)


# def is_prime(num):
#     if num <= 0 or num == 1:
#         return False
#     else:
#         for i in range(2, round(num**0.5)+1):
#             if num % i == 0:
#                 return False
#
#     return True
#
#
# test.assert_equals(is_prime(0), False, "0  is not prime")
# test.assert_equals(is_prime(1), False, "1  is not prime")
# test.assert_equals(is_prime(2), True, "2  is prime")
# test.assert_equals(is_prime(73), True, "73 is prime")
# test.assert_equals(is_prime(75), False, "75 is not prime")
# test.assert_equals(is_prime(-1), False, "-1 is not prime")
# test.assert_equals(is_prime(4),  False, "1  is not prime")
# test.assert_equals(is_prime(3),  True, "3  is prime")


# def longest_consec(strarr, k):
#     if len(strarr) < k or k <= 0:
#         return ''
#
#     chr = []
#     max_avg = 0
#     position = None
#     for i in strarr:
#         chr.append(len(i))
#
#     for j in range(len(chr)):
#         avg_char = sum(chr[j:j+k])
#         if avg_char > max_avg:
#             max_avg = avg_char
#             position = j
#
#     return ''.join(strarr[position:position+k])
#
#
# def testing(actual, expected):
#     test.assert_equals(actual, expected)
#
# test.describe("longest_consec")
# test.it("Basic tests")
# testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
# testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
# testing(longest_consec([], 3), "")
# testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
# testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
# testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
# testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
# testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
# testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")


# def expanded_form(num):
#     res = []
#     x = 10
#     while num >= 1:
#         residue = num % x
#         if residue:
#             res.append(residue)
#         num -= residue
#
#         x *= 10
#     res = (list(map(str, res)))
#     res.reverse()
#
#     return ' + '.join(res)
#
# test.assert_equals(expanded_form(12), '10 + 2')
# test.assert_equals(expanded_form(42), '40 + 2')
# test.assert_equals(expanded_form(70304), '70000 + 300 + 4')


# def solution(s):
#     res = ''
#     for i in s:
#         if i.islower():
#             res += i
#         else:
#             res += f' {i}'
#
#     return res
#
# test.assert_equals(solution("helloWorld"), "hello World")
# test.assert_equals(solution("camelCase"), "camel Case")
# test.assert_equals(solution("breakCamelCase"), "break Camel Case")


# def comp(array1, array2):
#     # print(array1)
#     # print(array2)
#     # if array1 and array2:
#     #     array2 = list(map(lambda x: int(x ** 0.5), array2))
#     #     array1.sort()
#     #     array2.sort()
#     #     print(array1)
#     #     print(array2)
#     #     return array1 == array2
#     # else:
#     #     return False
#     # return None not in (a1, a2) and [i * i for i in sorted(a1)] == sorted(a2)
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False


#
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
# test.assert_equals(comp(a1, a2), True)
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
# test.assert_equals(comp(a1, a2), False)
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
# test.assert_equals(comp(a1, a2), False)
#
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# test.assert_equals(comp(a1, a2), True)
#
# a1 = []
# a2 = None
# test.assert_equals(comp(a1, a2), False)
#
#
# a1 = [11, 19, 19, 19, 121, 144, 144, 161, 1008]
# a2 = [11, 19, 19, 121, 144, 144, 161, 190]
# test.assert_equals(comp(a1, a2), False)

# a1 = [64, 38, 73, 75, 76, 11, 79, 72, 77, 37, 55, 96, 95, 34, 17, 100, 31, 25, 99, 57]
# a2 = [961, 9801, 5329, 1369, 5776, 5929, 9216, 121, 10000, 625, 289, 4096, 1156, 9029, 5625, 1444, 6241, 3249, 5184, 3025]
# test.assert_equals(comp(a1, a2), False)


# def bouncing_ball(h, bounce, window):
#     if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
#         return -1
#     exp = 0
#     while h > window:
#         exp += 2
#         h *= bounce
#
#     return exp-1
#
#
# @test.describe('Tests')
# def fixed_tests():
#     def testing(h, bounce, window, exp):
#         actual = bouncing_ball(h, bounce, window)
#         test.assert_equals(actual, exp)
#
#     @test.it('Fixed Tests')
#     def tests():
#         testing(2, 0.5, 1, 1)
#         testing(3, 0.66, 1.5, 3)
#         testing(30, 0.66, 1.5, 15)
#         testing(30, 0.75, 1.5, 21)


#
# def in_array(array1, array2):
#     r = []
#     for i in array1:
#         for j in array2:
#             if i in j:
#                 if i not in r:
#                     r.append(i)
#
#     return sorted(r)
#
#
#
# import codewars_test as test
#
#
# @test.describe("in_array")
# def tests():
#     def testing(array1, array2, expect):
#         actual = in_array(array1, array2)
#         test.assert_equals(actual, expect)
#
#     @test.it("Basic tests")
#     def basics():
#         a1 = ["live", "arp", "strong"]
#         a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#         r = ['arp', 'live', 'strong']
#         testing(a1, a2, r)
#         a1 = ["arp", "mice", "bull"]
#         a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#         r = ['arp']
#         testing(a1, a2, r)
#


# def queue_time(customers, n):
#
#     till = {}
#     for t in range(n):
#         till[t] = [0]
#
#     for c in customers:
#         till[sorted(till, key=lambda x: sum(till[x]))[0]].append(c)
#
#     return max([sum(till[x]) for x in range(len(till))])


# till = {1:[1,2,100], 2:[1,2,10]}
# print(sorted_till(till))


# total_time = 0
# for j in range(n):
#     temp_time = sum(customers[j::n])
#     if temp_time > total_time:
#         total_time = temp_time
#
# return total_time

# test.assert_equals(queue_time([10,2,3,3], 2), 10)
# test.assert_equals(queue_time([2,3,10], 2), 12)
# test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
# test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
# test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
# test.assert_equals(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
# test.assert_equals(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
# test.assert_equals(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")


# def count(s):
#     return {i: s.count(i) for i in s}
#
#
# test.assert_equals(count('aba'), {'a': 2, 'b': 1})
# test.assert_equals(count(''), {})
# test.assert_equals(count('aa'), {'a': 2})
# test.assert_equals(count('aabb'), {'b': 2, 'a': 2})


# def two_sum(numbers, target):
#     for n, i in enumerate(numbers):
#         for k, j in enumerate(numbers[n+1:]):
#             if i + j == target:
#                 return [n, k+n+1]
#     return []
#
#
# test.assert_equals(sorted(two_sum([1, 2, 3], 4)), [0, 2])
# test.assert_equals(sorted(two_sum([1234, 5678, 9012], 14690)), [1, 2])
# test.assert_equals(sorted(two_sum([2, 2, 3], 4)), [0, 1])


# def sum_dig_pow(a, b):
#     res = []
#     for i in range(a, b+1):
#         sm = 0
#         spl = (list(map(int, str(i))))
#         for s in range(len(spl)):
#             sm += spl[s] ** (s+1)
#             if i == sm:
#                 res.append(int(''.join(map(str, spl))))
#
#     return res
#
#
# test.assert_equals(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
# test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
# test.assert_equals(sum_dig_pow(10, 89), [89])
# test.assert_equals(sum_dig_pow(10, 100), [89])
# test.assert_equals(sum_dig_pow(90, 100), [])
# test.assert_equals(sum_dig_pow(89, 135), [89, 135])

#
# def solution(n):
#
#     dic = {1: 'I', 4: 'IV', 5: 'V', 6: 'VI', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
#
#     lst = []
#     string_n = str(n)[::-1]
#     for x in range(len(string_n)):
#         foundation = int(string_n[x])
#         rest = 10 ** x
#         figure = int(foundation * rest)
#         if figure in dic:
#             lst.append(dic[figure])
#         elif foundation in [2, 3]:
#             lst.append(dic[rest]*foundation)
#         elif foundation in [4]:
#             lst.append(dic[rest]+dic[rest*5])
#         elif foundation in [6, 7, 8]:
#             lst.append(dic[rest*5]+dic[rest]*(foundation-5))
#         elif foundation in [9]:
#             lst.append(dic[rest] + dic[rest*10])
#     return ''.join(lst[::-1])


# test.assert_equals(solution(1), 'I', "solution(1),'I'")
# test.assert_equals(solution(4), 'IV', "solution(4),'IV'")
# test.assert_equals(solution(6), 'VI', "solution(6),'VI'")
# test.assert_equals(solution(14), 'XIV', "solution(14),'XIV")
# test.assert_equals(solution(21), 'XXI', "solution(21),'XXI'")
# test.assert_equals(solution(89), 'LXXXIX', "solution(89),'LXXXIX'")
# test.assert_equals(solution(91), 'XCI', "solution(91),'XCI'")
# test.assert_equals(solution(984), 'CMLXXXIV', "solution(984),'CMLXXXIV'")
# test.assert_equals(solution(1000), 'M', 'solution(1000), M')
# test.assert_equals(solution(1889), 'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
# test.assert_equals(solution(1989), 'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")

# test.assert_equals(solution(1420), 'MCDXX', "solution(1420),'MCDXX'")
# # 'MXX' should equal 'MCDXX'


# def solution(roman):
#     """complete the solution by transforming the roman numeral into an integer"""
#     dic = {'I': 1, 'IV':4, 'V':5, 'VI':6 , 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#     res = []
#     for i in range(len(roman)-1):
#         if dic[roman[i]] >= dic[roman[i+1]]:
#             res.append(dic[roman[i]])
#         else:
#             res.append(dic[roman[i]] * (-1))
#     res.append(dic[roman[-1]])
#     return sum(res)
#
#
# test.assert_equals(solution('XXI'), 21, 'XXI should == 21')
# test.assert_equals(solution('I'), 1, 'I should == 1')
# test.assert_equals(solution('IV'), 4, 'IV should == 4')
# test.assert_equals(solution('MMVIII'), 2008, 'MMVIII should == 2008')
# test.assert_equals(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')


# def camel_case(s):
#     res = []
#     s = s.split()
#     for i in s:
#         res.append(i.title())
#     return ''.join(res)
#
#
# def camel_case(s):
#     return s.title().replace(' ','')
#
#
# test.assert_equals(camel_case("test case"), "TestCase")
# test.assert_equals(camel_case("camel case method"), "CamelCaseMethod")
# test.assert_equals(camel_case("say hello "), "SayHello")
# test.assert_equals(camel_case(" camel case word"), "CamelCaseWord")
# test.assert_equals(camel_case(""), "")


# def decrypt(encrypted_text, n):
#     for _ in range(n):
#         res = []
#         for i in range(len(encrypted_text)//2):
#             res.append(encrypted_text[len(encrypted_text)//2 + i])
#             res.append(encrypted_text[i])
#         if len(encrypted_text) % 2:
#             res.append(encrypted_text[-1])
#         encrypted_text = ''.join(res)
#     return encrypted_text
#
#
# def encrypt(text, n):
#     for _ in range(n):
#         res = []
#         for i in text[1::2]:
#             res.append(i)
#         res.append(text[::2])
#         text = ''.join(res)
#     return text


# test.assert_equals(encrypt("012345", 1), "135024")
# test.assert_equals(encrypt("012345", 2), "304152")
# test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
# test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
# test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
# test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
# test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
# test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
# test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")


# test.assert_equals(decrypt("135024", 1), "012345")
# test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
# test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
# test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
# test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
# test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
# test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
# test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")
# #
# test.assert_equals(encrypt("", 0), "")
# test.assert_equals(decrypt("", 0), "")
# test.assert_equals(encrypt(None, 0), None)
# test.assert_equals(decrypt(None, 0), None)


# def to_weird_case(words):
#     lst = words.split()
#     res = []
#     temp = []
#     for word in lst:
#         word.lower()
#         for n, i in enumerate(word.lower()):
#             if not n % 2:
#                 temp.append(i.capitalize())
#             else:
#                 temp.append(i)
#         res.append(''.join(temp))
#         temp = []
#     return ' '.join(res)
#
#
# test.assert_equals(to_weird_case('THIs iS a TEST'), 'ThIs Is A TeSt')



# def diamond(n):
#     if n > 0 and n % 2 == 1:
#         diamond = ""
#         for i in range(n):
#             diamond += " " * abs((n/2) - i)
#             diamond += "*" * (n - abs((n-1) - 2 * i))
#             diamond += "\n"
#         return diamond
#     else:
#         return None


# test.assert_equals(diamond(1), "*\n")
# test.assert_equals(diamond(2), None)
# test.assert_equals(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
# test.assert_equals(diamond(0), None)
# test.assert_equals(diamond(-3), None)


# def title_case(title, minor_words=''):
#     title = title.capitalize().split()
#     minor_words = minor_words.lower().split()
#
#     return ' '.join([word if word in minor_words else word.capitalize() for word in title])
#
#
# test.assert_equals(title_case(''), '')
# test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
# test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
# test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')


# def parse(data):
#     res = []
#     cur = 0
#     for i in data:
#         if i == 'o':
#             res.append(cur)
#         elif i == 'i':
#             cur += 1
#         elif i == 'd':
#             cur -= 1
#         elif i == 's':
#             cur *= cur
#     return res
#
#
# test.assert_equals(parse("ooo"), [0, 0, 0])
# test.assert_equals(parse("ioioio"), [1, 2, 3])
# test.assert_equals(parse("idoiido"), [0, 1])
# test.assert_equals(parse("isoisoiso"), [1, 4, 25])
# test.assert_equals(parse("codewars"), [0])


# def stock_list(list_of_art, list_of_cat):
#     dic = {}
#
#     for i in list_of_art:
#         b, v = i.split()
#         if b[0] not in dic:
#             dic[b[0]] = 0
#         dic[b[0]] += int(v)
#
#     res = []
#     flag = False
#     for i in list_of_cat:
#         if i in dic:
#             res.append(f'({i} : {dic[i]})')
#             flag = True
#         else:
#             res.append(f'({i} : 0)')
#
#     if not flag:
#         return ''
#
#     return ' - '.join(res)
#
#
# @test.describe("Testing")
# def _():
#     @test.it("Tests")
#     def _():
#         b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
#         c = ["A", "B", "C", "D"]
#         test.assert_equals(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")
#
#         b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
#         c = ["A", "B"]
#         test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")



# def multiplication_table(size):
#     # res = []
#     # for i in range(size):
#     #     line = []
#     #     for j in range(size):
#     #         line.append((i+1)*(j+1))
#     #     res.append(line)
#     # return res
#
#     return [[(i+1)*(j+1) for j in range(size)] for i in range(size)]
#
#
# test.assert_equals(multiplication_table(1), [[1]])
# test.assert_equals(multiplication_table(2), [[1, 2], [2, 4]])
# test.assert_equals(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
# test.assert_equals(multiplication_table(4), [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]])
# test.assert_equals(multiplication_table(5),
#                    [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]])


# def good_vs_evil(good, evil):
#     good_list = list(map(int, good.split()))
#     evil_list = list(map(int, evil.split()))
#
#     good_worth = [1, 2, 3, 3, 4, 10]
#     evil_worth = [1, 2, 2, 2, 3, 5, 10]
#
#     good_value = []
#     evil_value = []
#
#     for i in range(len(good_list)):
#         good_value.append(good_list[i] * good_worth[i])
#
#     for i in range(len(evil_list)):
#         evil_value.append(evil_list[i] * evil_worth[i])
#
#     if sum(good_value) > sum(evil_value):
#         return 'Battle Result: Good triumphs over Evil'
#     elif sum(good_value) < sum(evil_value):
#         return 'Battle Result: Evil eradicates all trace of Good'
#     else:
#         return 'Battle Result: No victor on this battle field'


# test.assert_equals(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'), 'Battle Result: Evil eradicates all trace of Good')
# test.assert_equals(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'), 'Battle Result: Good triumphs over Evil')
# test.assert_equals(good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0'), 'Battle Result: No victor on this battle field')


#
# def parts_sums(ls):
#     res = []
#     total = sum(ls)
#     res.append(total)
#     for i in range(len(ls)):
#         total -= ls[i]
#         res.append(total)
#     return res
#
#
# @test.describe('Tests')
# def fixed_tests():
#     def dotest(ls, expected):
#         actual = parts_sums(ls)
#         test.assert_equals(actual, expected)
#
#     @test.it('Basic')
#     def basic_tests():
#         dotest([], [0])
#         dotest([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0])
#         dotest([1, 2, 3, 4, 5, 6], [21, 20, 18, 15, 11, 6, 0])
#
#         dotest([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358],
#                [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358,
#                 0])


# def rev_rot(strng, sz):
#     if len(strng) < sz or sz <= 0:
#         return ''
#     else:
#         res = []
#         for i in range(len(strng)//sz):
#             chunk = sum([int(i) ** 2 for i in strng[i*sz:i*sz + sz]])
#             if chunk % 2 == 0:
#                 res.append(strng[i*sz:i*sz + sz][::-1])
#             else:
#                 res.append(strng[i*sz+1:i*sz + sz])
#                 res.append(strng[i*sz])
#     return ''.join(res)


# def find_missing(sequence):
#     miss = None
#     delta = sequence[1] - sequence[0]
#     delta2 = sequence[-1] - sequence[-2]
#
#     cnt = 0
#     for n in range(1, len(sequence)):
#         if sequence[n] != sequence[n-1] + delta:
#             miss = sequence[n - 1] + delta
#             cnt += 1
#
#     if cnt == 1:
#         return miss
#     else:
#         cnt = 0
#         for n in range(1, len(sequence)):
#             if sequence[n] != sequence[n - 1] + delta2:
#                 miss = sequence[n - 1] + delta2
#                 cnt += 1
#         if cnt == 1:
#             return miss


# def find_missing(sequence):
#     t = sequence
#     return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)
#
#
# test.assert_equals(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
# test.assert_equals(find_missing([1, 3, 4, 5, 6, 7, 8, 9]), 2)
# test.assert_equals(find_missing([1, 3, 5, 9, 11]), 7)



# def encrypt_this(text):
#     res = []
#     tmp = []
#     for word in text.split():
#         if len(word) >= 3:
#             tmp.append(str(ord(word[0])))
#             tmp.append(word[-1])
#             tmp.append(word[2:-1])
#             tmp.append(word[1])
#
#         else:
#             tmp.append(str(ord(word[0])))
#             tmp.append(word[1:])
#
#         res.append(''.join(tmp))
#         tmp = []
#     return ' '.join(res)
#
#
# tests = [
#     # ("", ""),
#     ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
#     ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
#     ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
#     ("Why can we not all be like that wise old bird", "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
#     ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
# ]
#
# for t in tests:
#     inp, exp = t
#     test.assert_equals(encrypt_this(inp), exp)



# def data_reverse(data):
#     segments = [data[i:i+8] for i in range(0, len(data), 8)]
#     segments.reverse()
#     reversed_data = [bit for segment in segments for bit in segment]
#     return reversed_data
#
# data1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
# data2 = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# test.assert_equals(data_reverse(data1), data2)
#
# data3 = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
# data4 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
# test.assert_equals(data_reverse(data3), data4)


# def meeting(s):
#     res = []
#     s = s.split(';')
#     for i in s:
#         i = i.split(':')
#         string = f'({i[1].upper()}, {i[0].upper()})'
#         res.append(string)
#
#     res.sort()
#
#     output = ""
#     for j in res:
#         output += j
#     return output


# def solve(s):
#     score = 0
#     highest = 0
#     ban = ["a", "e", "i", "o", "u"]
#     for i in s:
#         if i not in ban:
#             score += ord(i) - 96
#             if score >= highest:
#                 highest = score
#         else:
#             score = 0
#
#     return highest
#
#
# test.assert_equals(solve("cozy"), 51)
# test.assert_equals(solve("xyzzy"), 126)
# test.assert_equals(solve("zodiac"), 26)
# test.assert_equals(solve("chruschtschov"), 80)
# test.assert_equals(solve("khrushchev"), 38)
# test.assert_equals(solve("strength"), 57)
# test.assert_equals(solve("catchphrase"), 73)
# test.assert_equals(solve("twelfthstreet"), 103)
# test.assert_equals(solve("mischtschenkoana"), 80)


# def clean_string(s):
#     res = []
#     for i in s:
#         if i == '#':
#             if res:
#                 res.pop()
#         else:
#             res.append(i)
#     return ''.join(res)
#
#
# test.assert_equals(clean_string('abc#d##c'), "ac")
# test.assert_equals(clean_string('abc####d##c#'), "" )
# test.assert_equals(clean_string("#######"), "" )
# test.assert_equals(clean_string(""), "" )




# def triple_double(num1, num2):
#     return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])
#
#
# test.assert_equals(triple_double(451999277, 41177722899), 1)
# test.assert_equals(triple_double(1222345, 12345), 0)
# test.assert_equals(triple_double(12345, 12345), 0)
# test.assert_equals(triple_double(666789, 12345667), 1)
# test.assert_equals(triple_double(10560002, 100), 1)
# test.assert_equals(triple_double(1112, 122), 0)


# def race(v1, v2, g):
#     if v2 <= v1:
#         return None
#     total = g / (v2 - v1)
#     return [int(total), int(total * 60) % 60, int(total * 3600) % 60]
#
#
# test.assert_equals(race(720, 850, 70), [0, 32, 18])
# test.assert_equals(race(80, 91, 37), [3, 21, 49])
# test.assert_equals(race(820, 81, 550), None)


# def up_array(arr):
#
#     if not arr or min(arr) < 0 or max(arr) > 9:
#         return None
#
#     number = int(''.join(map(str, arr)))
# 
#     number += 1
#
#     number = str(number)
#
#     if len(arr) > len(number):
#         number = number.rjust(len(arr), '0')
#
#     return [int(i) for i in number]
#
#
#
#
# test.assert_equals(up_array([2, 3, 9]), [2, 4, 0])
# test.assert_equals(up_array([9, 9]), [1, 0, 0])
# test.assert_equals(up_array([0, 4, 2]), [0, 4, 3])
# test.assert_equals(up_array([4, 3, 2, 5]), [4, 3, 2, 6])
# test.assert_equals(up_array([1, 2, 3, 9]), [1, 2, 4, 0])
# test.assert_equals(up_array([9, 9, 9, 9]), [1, 0, 0, 0, 0])
# test.assert_equals(up_array([0, 1, 3, 7]), [0, 1, 3, 8])
# test.assert_equals(up_array([1, -9]), None)


# def Xbonacci(signature,n):
#     len_s = len(signature)
#
#     if n == 0:
#         return []
#     elif n < len_s:
#         return signature[:n]
#
#     for i in range(n - len_s):
#         signature.append(sum(signature[i:i+len_s]))
#     return signature
#
#
# test.describe("Basic tests")
# test.assert_equals(Xbonacci([0,1],10),[0,1,1,2,3,5,8,13,21,34])
# test.assert_equals(Xbonacci([1,1],10),[1,1,2,3,5,8,13,21,34,55])
# test.assert_equals(Xbonacci([0,0,0,0,1],10),[0,0,0,0,1,1,2,4,8,16])
# test.assert_equals(Xbonacci([1,0,0,0,0,0,1],10),[1,0,0,0,0,0,1,2,3,6])
# test.assert_equals(Xbonacci([1,0,0,0,0,0,0,0,0,0],20),[1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256])


# def solution(number):
#     return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])


# def validate(n):
#     res = list(map(int, str(n)))
#     if len(str(n)) % 2 == 0:
#         res = [i * 2 if n % 2 == 0 else i for n, i in enumerate(res)]
#     else:
#         res = [i * 2 if n % 2 else i for n, i in enumerate(res)]
#
#     new_res = []
#     for i in res:
#         if i > 9:
#             new_res.append(sum(map(int, str(i))))
#         else:
#             new_res.append(i)
#
#     return not sum(new_res) % 10


# test.assert_equals(validate(1714), False)
# test.assert_equals(validate(12345), False)
# test.assert_equals(validate(891), False)
# test.assert_equals(validate(123), False)
# test.assert_equals(validate(1), False)
# test.assert_equals(validate(2121), True)
# test.assert_equals(validate(1230), True)


# def play_pass(s, n):
#     # Step 1, 2, 3
#     shiftText = ""
#     for char in s:
#         if char.isdigit():
#             shiftText += str(9 - int(char))
#         elif char.isalpha():
#             shifted = ord(char.lower()) + n
#             shiftText += chr(shifted) if shifted <= ord('z') else chr(shifted - 26)
#         else:
#             shiftText += char
#
#     # Step 4
#     caseText = ""
#     for i in range(len(shiftText)):
#         caseText += shiftText[i].upper() if i % 2 == 0 else shiftText[i].lower()
#
#     # Step 5
#     return caseText[::-1]
#
#
#
# test.assert_equals(play_pass("I LOVE YOU!!!", 1), "!!!vPz fWpM J")
# test.assert_equals(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2),
#     "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")


# def pyramid(n):
#     # res = []
#     # for i in range(1, n+1):
#     #     res.append([1] * i)
#     #
#     # return res
#
#     return [[1] * i for i in range(1, n+1)]
#
#
# test.assert_equals(pyramid(0), [])
# test.assert_equals(pyramid(1), [[1]])
# test.assert_equals(pyramid(2), [[1], [1, 1]])
# test.assert_equals(pyramid(3), [[1], [1, 1], [1, 1, 1]])


# def highest_rank(arr):
#     # dic = {}
#     # mx = 0
#     # numb = None
#     # for i in arr:
#     #     if i not in dic:
#     #         dic[i] = 0
#     #     dic[i] += 1
#     #     if dic[i] > mx:
#     #         mx = dic[i]
#     #         numb = i
#     #     elif dic[i] == mx and i > numb:
#     #         numb = i
#     # return numb
#
#     return max(sorted(arr, reverse=True), key=arr.count)
#
#
# test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
# test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)


# def reverse_alternate(s):
#     # res = []
#     # for n, i in enumerate(s.split()):
#     #     if n % 2:
#     #         res.append(i[::-1])
#     #     else:
#     #         res.append(i)
#     # return ' '.join(res)
#
#     return ' '.join([i[::-1] if n % 2 else i for n, i in enumerate(s.split())])
#
#
# test.assert_equals(reverse_alternate("Did it work?"), "Did ti work?")
# test.assert_equals(reverse_alternate("I really hope it works this time..."), "I yllaer hope ti works siht time...")
# test.assert_equals(reverse_alternate("Reverse this string, please!"), "Reverse siht string, !esaelp")
# test.assert_equals(reverse_alternate("Have a beer"), "Have a beer")
# test.assert_equals(reverse_alternate("   "), "")
# test.assert_equals(reverse_alternate("This is not a test "), "This si not a test")
# test.assert_equals(reverse_alternate("This       is a  test "), "This si a tset")


# def calc(expr):
#     stack = []
#     for token in expr.split():
#         if token.isdigit():
#             stack.append(int(token))
#         else:
#             b = stack.pop()
#             a = stack.pop()
#             if token == '+':
#                 stack.append(a + b)
#             elif token == '-':
#                 stack.append(a - b)
#             elif token == '*':
#                 stack.append(a * b)
#             elif token == '/':
#                 stack.append(a / b)
#     return stack[-1] if stack else 0
#
#
# # test.assert_equals(calc(""), 0, "Should work with empty string")
# # test.assert_equals(calc("3"), 3, "Should parse numbers")
# # test.assert_equals(calc("3.5"), 3.5, "Should parse float numbers")
# # test.assert_equals(calc("1 3 +"), 4, "Should support addition")
# # test.assert_equals(calc("1 3 *"), 3, "Should support multiplication")
# # test.assert_equals(calc("1 3 -"), -2, "Should support subtraction")
# # test.assert_equals(calc("4 2 /"), 2, "Should support division")
# test.assert_equals(calc("5 1 2 + 4 * + 3 -"), 14, "Should support division")

#
# def kebabize(st):
#     # res = []
#     # if st[0].isalpha():
#     #     res.append(st[0].lower())
#     # for i in st[1::]:
#     #     if i.isupper():
#     #         if res:
#     #             res.append(f'-{i.lower()}')
#     #         else:
#     #             res.append(i.lower())
#     #     elif i.isalpha():
#     #         res.append(i)
#     # return ''.join(res)
#     # return ''.join(c if c.islower() else '-' + c.lower() for c in st if c.isalpha()).strip('-')
#
#     return ''.join([i if i.islower() else '-'+i.lower() for i in st if i.isalpha()]).strip('-')
#
#
# test.assert_equals(kebabize('6IpMOsat3p6gxf81hgAmd'), 'ip-m-osatpgxfhg-amd')
# test.assert_equals(kebabize('myCamelCasedString'), 'my-camel-cased-string')
# test.assert_equals(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
# test.assert_equals(kebabize('SOS'), 's-o-s')
# test.assert_equals(kebabize('42'), '')
# test.assert_equals(kebabize('CodeWars'), 'code-wars')


# def abbreviate(s):
#     res = []
#     tmp = []
#     for n, i in enumerate(s):
#         if i.isalpha():
#             tmp.append(i)
#         else:
#             if len(tmp) >= 4:
#                 res.append(tmp[0]+str(len(tmp)-2) + tmp[-1])
#             else:
#                 res.append(''.join(tmp))
#             res.append(i)
#             tmp = []
#
#     if tmp:
#         if len(tmp) >= 4:
#             res.append(tmp[0] + str(len(tmp) - 2) + tmp[-1])
#         else:
#             res.append(''.join(tmp))
#
#     return ''.join(res)
#
#
# test.assert_equals(abbreviate("doggy; is, the_"), "d3y; is, the_")
# test.assert_equals(abbreviate("internationalization"), "i18n")
# test.assert_equals(abbreviate("accessibility"), "a11y")
# test.assert_equals(abbreviate("Accessibility"), "A11y")
# test.assert_equals(abbreviate("elephant-ride"), "e6t-r2e")


# def presses(phrase):
#     res = []
#     lst = ['1', '*', '#', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', ' 0']
#
#     for letter in phrase:
#         for part in lst:
#             if letter.upper() in part:
#                 res.append(part.index(letter.upper())+1)
#     return sum(res)
#
# test.assert_equals(presses("WHERE DO U WANT 2 MEET L8R"), 47)
# test.assert_equals(presses("0123456789"), 37)
# test.assert_equals(presses("abcdefghijklmnopqrstuvwxyz"), 56)
# test.assert_equals(presses("LOL"), 9)
# test.assert_equals(presses("HOW R U"), 13)



# def to_nato(words):
#     NATO = {
#         'A': 'Alfa',  'B': 'Bravo',   'C': 'Charlie',
#         'D': 'Delta',  'E': 'Echo',    'F': 'Foxtrot',
#         'G': 'Golf',   'H': 'Hotel',   'I': 'India',
#         'J': 'Juliett','K': 'Kilo',    'L': 'Lima',
#         'M': 'Mike',   'N': 'November','O': 'Oscar',
#         'P': 'Papa',   'Q': 'Quebec',  'R': 'Romeo',
#         'S': 'Sierra', 'T': 'Tango',   'U': 'Uniform',
#         'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
#         'Y': 'Yankee', 'Z': 'Zulu'}

#     return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')
#
#     # res = []
#     # for i in words:
#     #
#     #     if i.upper() in d:
#     #         res.append(d[i.upper()])
#     #     elif i == ' ':
#     #         pass
#     #     else:
#     #         res.append(i)
#     # return ' '.join(res)
#
#
#
# test.assert_equals(to_nato('ljlm[-&C'),
#                    "Lima Juliett Lima Mike [ - & Charlie")
# test.assert_equals(to_nato('Did not see that coming'),
#                    "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf")
# test.assert_equals(to_nato('.d?d!'), '. Delta ? Delta !')



# def decipher_this(s):
#     res = []
#     dig = []
#     w = []
#
#     for word in s.split():
#         for i in word:
#             if i.isdigit():
#                 dig.append(i)
#             else:
#                 w.append(i)
#         if len(w) > 1:
#             res.append(chr(int(''.join(dig)))+w[-1]+''.join(w[1:-1])+w[0])
#         elif len(w) == 1:
#             res.append(chr(int(''.join(dig))) + w[0])
#         else:
#             res.append(chr(int(''.join(dig))))
#         dig = []
#         w = []
#
#     return ' '.join(res)
#
#
# # test.assert_equals(decipher_this("65"), 'A')
# test.assert_equals(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"), "A wise old owl lived in an oak")
# test.assert_equals(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
#                    "The more he saw the less he spoke")
# test.assert_equals(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
#                    "The less he spoke the more he heard")
# test.assert_equals(decipher_this("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
#                    "Why can we not all be like that wise old bird")
# test.assert_equals(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"), "Thank you Piotr for all your help")
