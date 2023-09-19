import codewars_test as test


# ### Moving Zeros To The End
# def move_zeros(lst):
#     zero = 0
#     pnt = 0
#     while pnt < len(lst) and zero < len(lst):
#         if lst[zero] == 0:
#             if lst[pnt] != 0:
#                 lst[pnt], lst[zero] = lst[zero], lst[pnt]
#             else:
#                 pnt += 1
#         else:
#             zero += 1
#             pnt += 1
#     return lst
#
#
# # print(move_zeros([0, 0, 0, 0]))
# test.assert_equals(move_zeros([1,0,0,1]), [1,1,0,0])
# test.assert_equals(move_zeros(
#     [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
#     [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
# test.assert_equals(move_zeros(
#     [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
#     [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# test.assert_equals(move_zeros([0, 0]), [0, 0])
# test.assert_equals(move_zeros([0]), [0])
# test.assert_equals(move_zeros([]), [])


# def pig_it(text):
#     """Simple Pig Latin"""
#     res = []
#     exceptions = ['!', '?', ',', '-']
#     for word in text.split():
#         if word not in exceptions:
#             res.append(word[1:] + word[0] + 'ay')
#         else:
#             res.append(word)
#     return ' '.join(res)
#
#
# test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')


# def make_readable(seconds):
#     """Human Readable Time"""
#     ss = seconds % 60
#     mm = seconds // 60 % 60
#     hh = seconds // 3600
#     return f"{(str(hh)).rjust(2, '0')}:{(str(mm)).rjust(2, '0')}:{(str(ss)).rjust(2, '0')}"
#
# test.assert_equals(make_readable(0), "00:00:00")
# test.assert_equals(make_readable(5), "00:00:05")
# test.assert_equals(make_readable(60), "00:01:00")
# test.assert_equals(make_readable(86399), "23:59:59")
# test.assert_equals(make_readable(359999), "99:59:59")


# def rgb(r, g, b):
#     """RGB To Hex Conversion"""
#     args = r, g, b
#     res = ''
#     for a in args:
#         if a < 0:
#             res += '00'
#         elif a > 255:
#             res += 'FF'
#         else:
#             res += str(hex(a))[2:].rjust(2, '0').upper()
#
#     return res
#
#
# test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
# test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
# test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
# test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
# test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")


# def dirReduc(arr):
#     """Directions Reduction"""
#     res = []
#     if arr:
#         res.append(arr[0])
#     else:
#         return arr
#     for i in range(1, len(arr)):
#         if arr[i] == 'NORTH' and res and res[-1] == 'SOUTH':
#             res.pop()
#         elif arr[i] == 'SOUTH' and res and res[-1] == 'NORTH':
#             res.pop()
#         elif arr[i] == 'EAST' and res and res[-1] == 'WEST':
#             res.pop()
#         elif arr[i] == 'WEST' and res and res[-1] == 'EAST':
#             res.pop()
#         else:
#             res.append(arr[i])
#     return res
#
#
# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# test.assert_equals(dirReduc(a), ['WEST'])
# u=["NORTH", "WEST", "SOUTH", "EAST"]
# test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])



# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)
#
# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y
#
# test.describe('Basic Tests')
# test.assert_equals(seven(times(five())), 35)
# test.assert_equals(four(plus(nine())), 13)
# test.assert_equals(eight(minus(three())), 5)
# test.assert_equals(six(divided_by(two())), 3)



# def rot13(message):
#     """Rot13"""
#     res = []
#     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     for i in list(message):
#         if i in alpha:
#             res.append(alpha[alpha.index(i)+13] if alpha.index(i) < 13 else alpha[alpha.index(i)-13])
#         elif i.lower() in alpha:
#             i = i.lower()
#             res.append((alpha[alpha.index(i)+13] if alpha.index(i) < 13 else alpha[alpha.index(i)-13]).upper())
#         else:
#             res.append(i)
#     return ''.join(res)
#
#
# test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
# test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
# test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')


# def max_sequence(arr):
#     """Maximum subarray sum"""
#     left = 0
#     right = len(arr) - 1
#     max_sum = sum(arr)
#     for i in range(1, right):
#         if sum(arr[i:]) > max_sum:
#             left = i
#             max_sum = sum(arr[i:])
#     for i in range(right+1, left, -1):
#         # print(i, sum(arr[left:i]))
#         if sum(arr[left:i]) > max_sum:
#             right = i-1
#             max_sum = sum(arr[left:i])
#
#     return max_sum if max_sum > 0 else 0
#
#
#
# test.assert_equals(max_sequence([]), 0)
# test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
# test.assert_equals(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
# test.assert_equals(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)


# def generate_hashtag(s):
# """The Hashtag Generator"""
#     return '#' + s.title().strip().replace(' ', '') if 140 > len(s) > 1 else False


# def productFib(prod):
#     """Product of consecutive Fib numbers"""
#     fibo = [0, 1]
#     while fibo[-1] * fibo[-2] < prod:
#         fibo.append(fibo[-1] + fibo[-2])
#     return [fibo[-2], fibo[-1], True] if fibo[-1] * fibo[-2] == prod else [fibo[-2], fibo[-1], False]
#
#
# test.assert_equals(productFib(4895), [55, 89, True])
# test.assert_equals(productFib(5895), [89, 144, False])


# def cakes(recipe, available):
#     """Pete, the baker"""
#     return min([available[i] // recipe[i] if i in available else 0 for i in recipe])
#
#
# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# test.assert_equals(cakes(recipe, available), 2, 'example #1')
#
# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}
# test.assert_equals(cakes(recipe, available), 0, 'example #2')


# def first_non_repeating_letter(string):
#     """First non-repeating character"""
#     res = {}
#     for i in string:
#         i = i.lower()
#         if i not in res:
#             res[i] = 0
#         res[i] += 1
#
#     for i in string:
#         if res[i.lower()] == 1:
#             return i
#     return ''
#
#
# test.assert_equals(first_non_repeating_letter('a'), 'a')
# test.assert_equals(first_non_repeating_letter('stress'), 't')
# test.assert_equals(first_non_repeating_letter('moonmen'), 'e')
# test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')


# def order_weight(strng):
#     lst = list(map(int, strng.split()))
#     lst.sort(key=lambda x: str(x))
#     # lst.sort(key=lambda x: sum(map(int, list(str(x)))))
#     res = sorted(lst, key=lambda x: sum(map(int, list(str(x)))))
#
#     return ' '.join(map(str, res))
#
#
# test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
# test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"),
#                    "11 11 2000 10003 22 123 1234000 44444444 9999")
# test.assert_equals(order_weight(""), "")


# def domain_name(url):
#     url= url.replace("http://", "")
#     url = url.replace("https://", "")
#     url = url.replace("www.", "")
#     return url.split('.')[0]
#
#
# test.assert_equals(domain_name("http://google.com"), "google")
# test.assert_equals(domain_name("http://google.co.jp"), "google")
# test.assert_equals(domain_name("http://www.xakep.ru"), "xakep")
# test.assert_equals(domain_name("xakep.ru"), "xakep")
# test.assert_equals(domain_name("www.xakep.ru"), "xakep")
# test.assert_equals(domain_name("https://youtube.com"), "youtube")


# def increment_string(strng):
#     if not strng:
#         return '1'
#     elif strng[-1].isalpha():
#         return strng + '1'
#
#     for i in range(len(strng)-1, -1, -1):
#         if not strng[i].isdigit():
#             i += 1
#             return strng[:i] + f'{int(strng[i:])+1:0{len(strng[i:])}}'
#
#     return f'{int(strng)+1:0{len(strng)}}'
#
#
# test.assert_equals(increment_string("foo"), "foo1")
# test.assert_equals(increment_string("foobar001"), "foobar002")
# test.assert_equals(increment_string("foobar1"), "foobar2")
# test.assert_equals(increment_string("foobar00"), "foobar01")
# test.assert_equals(increment_string("foobar99"), "foobar100")
# test.assert_equals(increment_string("foobar099"), "foobar100")
# test.assert_equals(increment_string("fo99obar99"), "fo99obar100")
# test.assert_equals(increment_string(""), "1")
# test.assert_equals(increment_string("Q45134102363748756945"), "Q45134102363748756946")
# test.assert_equals(increment_string("#4<8597291000000063457"), "#4<8597291000000063458")


# def scramble(s1, s2):
#     """Scramblies"""
#     d1 = {}
#     d2 = {}
#     for i in s1:
#         if i not in d1:
#             d1[i] = 0
#         d1[i] += 1
#
#     for i in s2:
#         if i not in d2:
#             d2[i] = 0
#         d2[i] += 1
#
#     for i in d2:
#         if i not in d1 or d1[i] < d2[i]:
#             return False
#     return True


# def score(dice):
#     score = 0
#     for i in set(dice):
#         if i == 1:
#             score += (dice.count(1) // 3) * 1000 + (dice.count(1) % 3) * 100
#         elif i == 5:
#             score += (dice.count(5) // 3) * 500 + (dice.count(5) % 3) * 50
#         else:
#             score += (dice.count(i) // 3) * i * 100
#
#     return score
#
#
# test.assert_equals(score([1, 1]), 200)
# test.assert_equals(score([5, 1, 3, 4, 1]), 250)
# test.assert_equals(score([1, 1, 1, 3, 1]), 1100)
# test.assert_equals(score([2, 3, 4, 6, 2]), 0)
# test.assert_equals(score([4, 4, 4, 3, 3]), 400)
# test.assert_equals(score([2, 4, 4, 5, 4]), 450)


# def zeros(n):
#     zeros = 0
#     i = 5
#     while n//i > 0:
#         zeros += n//i
#         i*=5
#     return zeros
#
#
# test.assert_equals(zeros(0), 0, "Testing with n = 0")
# test.assert_equals(zeros(6), 1, "Testing with n = 6")
# test.assert_equals(zeros(30), 7, "Testing with n = 30")
# test.assert_equals(zeros(10000), 2499, "Testing with n = 30")


# def perimeter(n):
# """Perimeter of squares in a rectangle"""
#     a = [1, 1]
#     for i in range(2, n+1):
#         a.append(a[i-2] + a[i-1])
#     return sum(a) * 4
#
#
# test.assert_equals(perimeter(5), 80)
# test.assert_equals(perimeter(7), 216)
# test.assert_equals(perimeter(20), 114624)
# test.assert_equals(perimeter(30), 14098308)


# def list_squared(m, n):
# """Integers: Recreation One"""
#     cache = {1: 1, 42: 2500, 246: 84100, 287: 84100, 728: 722500, 1434: 2856100, 1673: 2856100,
#              1880: 4884100, 4264: 24304900, 6237: 45024100, 9799: 96079204, 9855: 113635600, 18330: 488410000
#              }
#
#     res = []
#     for i in range(m, n):
#         if i in cache:
#             res.append([i, cache[i]])
#         elif i >= 20000:
#             divlst = []
#             for div in range(1, i+1):
#                 if i % div == 0:
#                     divlst.append(div**2)
#             if (sum(divlst) ** 0.5) % 1 == 0:
#                 res.append([i, sum(divlst)])
#     return res
#
#
# list_squared(2000, 20000)
# test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
# test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
# test.assert_equals(list_squared(250, 500), [[287, 84100]])


# def sum_pairs(lst, s):
#     """Sum of Pairs"""
#     cache = set()
#     for i in lst:
#         if s - i in cache:
#             return [s - i, i]
#         cache.add(i)


# def find_prime(m, n):
#     prime = []
#     i = m
#     while i < n:
#
#         for d in range(2, i-1):
#             if i % d == 0:
#                 print('i:', i, 'd:', d)
#                 i += 1
#                 break
#
#             prime.append(i)
#         i += 1
#     return prime
#
#
# print(find_prime(2, 10))


# def gap(g, m, n):
#     prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
#              89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
#              179, 181, 191, 193, 197, 199]
#
#
#     for i in range(m, n):
#         if i in prime and i+g in prime:
#             return [i, i+g]
#     return None
#
#
# test.assert_equals(gap(2,100,110), [101, 103])
# test.assert_equals(gap(4,100,110), [103, 107])
# test.assert_equals(gap(6,100,110), None)
# test.assert_equals(gap(8,300,400), [359, 367])
# test.assert_equals(gap(10,300,400), [337, 347])
# test.assert_equals(gap(2,100,103), [101, 103])



def choose_best_sum(t, k, ls):
    sm = []
    for n in range(1, k):
        temp_arr = []
        if not sm:
            sm = ls[:]
        for i in range(len(sm)):
            for j in range(0+n, len(ls)):
                temp = sm[i] + ls[j]
                if temp <= t:
                    temp_arr.append(temp)
        sm = temp_arr[:]
    print(sm)

    same = 0
    for i in sm:
        if i == t:
            print(i)
            return i
        elif i > same:
            same = i

    return None if same == 0 else same


test.it("Bigger numbers")
# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# test.assert_equals(choose_best_sum(150, 2, xs), 150)
# test.assert_equals(choose_best_sum(230, 4, xs), 230)
# test.assert_equals(choose_best_sum(430, 5, xs), 430)
# test.assert_equals(choose_best_sum(430, 8, xs), None)

xs = [1,2,3,4,5,6]
test.assert_equals(choose_best_sum(100, 6, xs), 5)

