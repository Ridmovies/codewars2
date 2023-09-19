# import codewars_test as test

# def binary_array_to_number(arr):
#     return int(''.join(map(str, arr)), 2)
#
# print(binary_array_to_number([0,0,0,1]))


# def number(bus_stops):
#     res = 0
#     for i in bus_stops:
#         res += i[0] - i[1]
#     return res
#
# print(number([[10,0],[3,5],[5,8]]))


### Greatest common divisor (RECURSION)

# def mygcd(x, y):
#     if x % y == 0:
#         return y
#     return mygcd(y, x % y)
#
# print(mygcd(8, 4))



### Convert a linked list to a string (RECURSION)

# class Node():
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next
#
#     def __str__(self):
#         return f'data: {self.data} next: {self.next}'
#
#
# def stringify(list):
#     if list == None:
#         return 'None'
#
#     return f'{str(list.data)} -> {stringify(list.next)}'
#
# print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))


### The wheat/rice and chessboard problem

# def squares_needed(grains):
#
#     if grains < 2:
#         return grains
#     return 1 + squares_needed(grains // 2)
#
#
# print(squares_needed(70))


### Factorial Factory

# This function should return n!
# def factorial(n):
#     if n in range(0,2):
#         return 1
#     elif n <= 0:
#         return
#     return factorial(n-1) * n
#
#
# print(factorial(6))


### Reverser

# def reverse(n, acc=0):
#     if n == 0:
#         return acc
#     return reverse(n//10, acc*10 + n%10)
#
#
# print(reverse(1234))


### Recursion sum
# def rsum(lst):
#     if lst == []:
#         return 0
#     return rsum(lst[1:]) + lst[0]

#
# print(rsum([2,3,65]))


## Count elements
# def count_el(lst):
#     if lst == []:
#         return 0
#     return count_el(lst[1:]) + 1
#
# print(count_el([1,1,1,1,1]))


### max element in list

# def max_element(lst):
#     if len(lst) == 2:
#         return lst[0] if lst[0] > lst[1] else lst[1]
#     sub_max = max_element(lst[1:])
#     return lst[0] if lst[0] > sub_max else sub_max
#
#
# print(max_element([1,2,4,6,7,9,0,4]))

### Recursion find in dict

# d = {1: {'one': {'two': 2}}}
#
# def find_in_dict(d, key):
#     if key in d:
#         return d[key]
#     for k, v in d.items():
#         k = d.get(k)
#         if type(k) is dict:
#             return find_in_dict(k, key)
#
# print(find_in_dict(d, 'two'))


### Sum of a nested list
# def sum_nested(lst):
#     s = 0
#     for l in lst:
#         if type(l) == list:
#             s += sum_nested(l)
#         else:
#             s += l
#     return s
#
#
# test.assert_equals(sum_nested([]), 0)
# test.assert_equals(sum_nested([1, 2, [3], 4]), 10)


### Recursive Replication

# def replicate(times, number):
#     if times <= 0:
#         return []
#     return [number] + replicate(times - 1, number)
#
#
# test.describe("Basic tests")
# test.assert_equals(replicate(3,5), [5, 5, 5])
# test.assert_equals(replicate(5,1), [1, 1, 1, 1, 1])
# test.assert_equals(replicate(0,12), [])
# test.assert_equals(replicate(-1,12), [])
# test.assert_equals(replicate(8,0), [0, 0, 0, 0, 0, 0, 0, 0])


### Reduce My Fraction

# def gcd(a, b):
#     if not a % b:
#         return b
#     return gcd(b, a % b)
#
#
# def reduce_fraction(fraction):
#     return fraction[0] // gcd(*fraction), fraction[1] // gcd(*fraction)
#
#
# test.assert_equals(reduce_fraction((60, 20)), (3, 1))
# test.assert_equals(reduce_fraction((80, 120)), (2, 3))
# test.assert_equals(reduce_fraction((4, 2)), (2, 1))
# test.assert_equals(reduce_fraction((45, 120)), (3, 8))
# test.assert_equals(reduce_fraction((1000, 1)), (1000, 1))
# test.assert_equals(reduce_fraction((1, 1)), (1, 1))


### Sum squares of numbers in list that may contain more lists
# def sumsquares(l):
#     s = 0
#     for i in l:
#         if type(i) == list:
#             s += sumsquares(i)
#         else:
#             s += i ** 2
#     return s
#
# print(sumsquares([[1,2],3]))

### Set Reducer
# def set_reducer(inp):
#     if len(inp) == 1:
#         return inp[0]
#     arr = []
#     cnt = 1
#     for i in range(len(inp))[1:]:
#         if inp[i-1] != inp[i]:
#             arr.append(cnt)
#             cnt = 1
#         else:
#             cnt += 1
#     arr.append(cnt)
#     return set_reducer(arr)
#
#
# print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]))

### nova polynomial 1. add
# return the sum of the two polynomials p1 and p2.
# def poly_add(p1,p2):
#     if p1 == []:
#         return p2
#     if p2 == []:
#         return p1
#     return [p1[0] + p2[0]] + poly_add(p1[1:], p2[1:])
#
#
#
# test.describe("Add two polynomials")
#
# test.it("Should return the sum of polynomials")
# test.assert_equals(poly_add([1], [1]),  [2], "Two polynomial of order zero fail.")
# test.assert_equals(poly_add([1,2], [1]),  [2,2], "Mixed length polynomials fail.")
# test.assert_equals(poly_add([1,2,3,4], [4,3,2,1]), [5,5,5,5])
#
# test.it("Should handle empty list")
# test.assert_equals(poly_add([],[]), [])
# test.assert_equals(poly_add([1,2,3,4,5,6], []), [1,2,3,4,5,6])
# test.assert_equals(poly_add([], [1,2,3,4,5,6]), [1,2,3,4,5,6])


### Russian nesting dolls

# def smallest_doll_size(largest_doll):
#     doll = largest_doll()
#     if doll is None:
#         return largest_doll.size
#     return smallest_doll_size(doll)



#####################################################

# def mygcd(x, y):
#     if x % y == 0:
#         return y
#     return mygcd(y, x % y)
#
#
# test.assert_equals(mygcd(30, 12), 6)
# test.assert_equals(mygcd(36, 12), 12)
# test.assert_equals(mygcd(8, 9), 1)
# test.assert_equals(mygcd(1, 1), 1)



### Reverse words
# def reverse_words(text):
#     return ' '.join([x[::-1] for x in text.split(' ')])
#
# print(reverse_words("This is an example!"))
# print(reverse_words("double  spaces"))      # "elbuod  secaps"



# ### 7 kyu Find the divisors!
# def divisors(integer):
#     div = []
#     for i in range(2, integer):
#         if integer % i == 0:
#             div.append(i)
#     if div:
#         return div
#     else:
#         return f'{integer} is prime'
#
#
# print(divisors(15))
# print(divisors(13))


### 7 kyu Sum of the first nth term of Series
# def series_sum(n):
#     num = 0
#     a = 1
#     for x in range(1, n+1):
#         num += 1/a
#         a += 3
#     formatted_num = "{:.2f}".format(num)
#     return formatted_num
#
#
# print(series_sum(3))


### 7 kyu Remove the minimum
# def remove_smallest(numbers):
#     x = numbers[:]
#     if x:
#         x.remove(min(numbers))
#         return x
#     else:
#         return x
#
#
# print(remove_smallest([1,2,3,4,5]))


# 7 kyu Credit Card Mask
# return masked string
# def maskify(cc):
#     if len(cc) <= 4:
#         return cc
#     else:
#         return cc[-4:].rjust(len(cc), '#')
#
# print(maskify("4556364607935616"))


# def row_sum_odd_numbers(n):
#     return sum(range(n*(n-1)+1, n*(n+1), 2))
#
#
# print(row_sum_odd_numbers(3))


# def number(lines):
#     res = []
#     for i in range(len(lines)):
#         res.append(f'{i+1}: {lines[i]}')
#     return res
#
# print(number(["a", "b", "c"]))



# def min_max(lst):
#     return [min(lst), max(lst)]
#
#
# print(min_max([1,2,3,4,5]))


# def dont_give_me_five(start,end):
#     arr = []
#     for i in range(start, end+1):
#         if '5' not in str(i):
#             arr.append(i)
#     return len(arr)
#
# print(dont_give_me_five(1, 90))



# def stray(arr):
#     dic = {}
#
#     for i in arr:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1
#
#     for k, v in dic.items():
#         if v == 1:
#             return k
#
#
# print(stray([1, 1, 1, 1, 1, 1, 2]))


# def divisors(n):
#     # cnt = 1
#     # for i in range(1, n):
#     #     if not n % i:
#     #         cnt += 1
#     #
#     # return cnt
#
#     # return sum([True if n % i == 0 else False for i in range(1, n+1)])
#
#
# print(divisors(30))


# def calculate_years(principal, interest, tax, desired):
#     year = 0
#     while principal < desired:
#         principal += principal * interest - tax * (principal * interest)
#         year += 1
#
#     return year
#
#
# print(calculate_years(1000, 0.05, 0.18, 1000))


# def break_chocolate(n, m):
#     return 0 if n == 0 or m == 0 else n * m - 1
#
#
# print(break_chocolate(7, 0))


#
# def nb_dig(n, d):
#     cnt = 0
#     for k in range(n+1):
#         number = str(k * k)
#         cnt += number.count(str(d))
#
#     return cnt
# 
#
#
# print(nb_dig(5750, 0))