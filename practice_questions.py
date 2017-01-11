'''
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

PSUEDOCODE:
- Set initial conditions for comparison: 
  Buy on first minute yesterday and sell second minute, calculate the profit, 
  set local minima (when to buy) as first price point
- From minute 1 onwards:
  If the current stock price yields a greater max profit as a point of sale
   update the max profit, the sell time to current mibute, buy time as min minute
  If the current stock price is less than the local stock price minima
   update the local minima (purchase time) to the current minute

Current implementation:
   0(n) for time; loop through list only once
   O(1) for space
'''

def get_max_profit(stock_prices_yesterday):
   buy, min = 0, 0
   sell = 1
   max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

   for minute in xrange(1, len(stock_prices_yesterday)):
      if (stock_prices_yesterday[minute] - stock_prices_yesterday[min]) > max_profit:
         max_profit = stock_prices_yesterday[minute] - stock_prices_yesterday[min]
         sell = minute
         buy = min
      if stock_prices_yesterday[min] > stock_prices_yesterday[minute]:
         min = minute
   print("buy at {} sell at {} max profit at {}".format(buy, sell, max_profit))
   return max_profit

# print(get_max_profit([5, 4, 6 ,7 ,6 ,3 ,2, 5]) == 3)
# print(get_max_profit([10, 7, 5, 8, 11, 9]) == 6)
# print(get_max_profit([119, 110, 15, 10, 5, 4]) == -1)

'''
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:
  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

No division!

'''

def get_products_of_all_ints_except_at_index(arr):
   # new_arr = []
   # for indx in xrange(0,len(arr)):
   #    temp = 1
   #    for indx_two in xrange(0, len(arr)):
   #       if indx_two != indx:
   #          # print indx, arr[indx_two]
   #          temp *= arr[indx_two]
   #          # print temp
   #    new_arr.append(temp)
   # return new_arr


   # new_arr = [None] * len(arr)
   # left, right, temp = 1, -1, 1
   # for indx in xrange(0,len(arr)):
   #    if indx == len(arr) - 1:
   #       print "yay"
   #       new_arr[right] = arr[-1]
   #    else:
   #       print "nay"
   #       print right, indx
   #       new_arr[right] = arr[indx]

   #    right += 1

   before_arr = [1] * len(arr)
   after_arr = [1] * len(arr)
   for indx in xrange(0,len(arr)-1):
      before_arr[indx + 1] = before_arr[indx] * arr[indx] 
   for indx in xrange(-1, -len(arr), -1): 
      after_arr[indx - 1] = after_arr[indx] * arr[indx] 
   print after_arr
   return before_arr, after_arr

print get_products_of_all_ints_except_at_index([3, 1, 2, 5, 6, 4])#([1,7,3,4]) #== [84, 12, 28, 21]
# print get_products_of_all_ints_except_at_index([0,7,3,4]) #== [84, 0, 0, 0]

def shuffle(deck_cards):
   import random

   N = len(deck_cards)

   while N > 0:
      random_indx = random.rand(N)
      if random_indx != N:
         temp = deck_cards[random_indx]
         deck_cards[random_indx] = deck_cards[N]
         deck_cards[N] = temp
      N -= 1

   return deck_cards

# Practice Problems
'''
https://www.hackerrank.com/contests/the-coding-be-ing/challenges/anagram-finder
'''

def get_char_freqs(word):
  char_freq = {}
  for char in list(word):
    if char_freq.get(char):
      char_freq[char] += 1
    else:
      char_freq[char] = 1   
  return char_freq

def filter_words(user_words):
  groupings = {}

  for word in user_words:
    char_freq = get_char_freqs(word)
    char_freq_str = ''
    for item in sorted(char_freq.items()):
      char_freq_str += ''.join(str(i) for i in item)
    if groupings.get(char_freq_str):
      groupings[char_freq_str].append(word)
    else:
      groupings[char_freq_str] = [word]

  groupings = dict(sorted(groupings.items()))

  final_words = []
  
  for char_freq, words in groupings.items():
    final_words.append(''.join(sorted(words[0])))

  return final_words

'''
TODO: Care only about removing any anagrams that the user may put in later.
Want to return input strings in same order minus these anagrams.

my_words = ['abba','baa','aaaa','bbbaaa','baba','aba','aababb']
output = ['aabb', 'aab', 'aaaa', 'aaabbb']  # TODO: ORDER MATTERS

answer = filter_words(my_words)  # ['aaaa', 'aabb', 'aaabbb', 'aab']

print(answer)
print(answer == output)
'''

# Find all anagrams given a word and list of words

def get_char_freqs(word):
  char_freq = {}
  for char in list(word): # Big O(n)
    if char_freq.get(char):
      char_freq[char] += 1
    else:
      char_freq[char] = 1   
  return char_freq

def get_arangrams(word, words):
  '''
  Performance is Big O(n**2)
  '''
  input_char_freq = get_char_freqs(word)
  anagrams = []
  for new_word in words: # Big O(n)
    if len(word) != len(new_word):
      next
    char_freq = get_char_freqs(word)
    if input_char_freq == char_freq:
      anagrams.append(new_word)

  return anagrams


# Find if a word is a palindrome

def is_palindrome(word):
  '''
  Big O(log n), we are doing log n comparisons
  '''
  if len(word) == 1:
    return

  mid = len(word) // 2
  for num_comparions in range(0, mid):
    if word[0] == word[-1]:
      is_palindrome(word[1:-2]) 
    else:
      return False

  return True

# print(is_palindrome('racecar'))
# print(is_palindrome('moon'))
# print(is_palindrome('mama'))
# print(is_palindrome('evilolive'))
# print(is_palindrome('boob'))

# Flatten an array

def flatten(my_list):
  flattened = []
  for val in my_list:
    if isinstance(val, list):
      flattened += flatten(val)
    else:
      flattened.append(val)

  return flattened

# print(flatten([1,[2,3], None, [[4,3,2]]]) == [1,2,3,None,4,3,2])

# Permutation of Parentheses
# Print all possible n pairs of balanced parentheses.
# For example, when n is 2, the function should print “(())” and “()()”. 
# When n is 3, we should get “((()))”, “(()())”, “(())()”, “()(())”, “()()()”.
# Read - http://algorithms.tutorialhorizon.com/generate-all-valid-parenthesis-strings-of-length-2n-of-given-n/
# http://stackoverflow.com/questions/3172179/valid-permutation-of-parenthesis

# Reverse Polish Notation
# http://danishmujeeb.com/blog/2014/12/parsing-reverse-polish-notation-in-python/

import operator
def reverse_polish(my_input):
  input_list = my_input.strip().split()
  total = [input_list.pop(0)]
  math_symbols = { '+': operator.add, '-': operator.sub, '/': operator.sub, '/': operator.truediv, '*': operator.mul }

  for val in input_list:
    if val.isdigit():
      total.append(val)
    else:
      temp = math_symbols[val](int(total.pop(-2)) , int(total.pop(-1)))
      total.append(temp)
  return total[0]


# print(reverse_polish('3 2 +') == 5)
# print(reverse_polish('3 2 + 1 -') == 4)
# print(reverse_polish('3 2 * 11 -') == -5)


