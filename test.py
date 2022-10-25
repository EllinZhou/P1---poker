###########################################
# Why testing
# If you want to write solid, bug-free code, you need to write tests that catch errors before you send your code out. You may think that writing tests is boring or unnecessary, but they can actually save you a lot of time down the road with debugging, so it’s always worth it to write tests.
###########################################
# Unit testing
# Unit tests are tests that focus on one very small piece of your code and be able to show that it is correct.

# In Python, there are a number of different tools that you can use to create tests. We’ll be using the unittest module which is built into Python.
###########################################
# unittest
# All you have to do to get started is to create a new python file, call it something relevant (PokerTests.py for example), import unittest, and extend unittest.TestCase in your testing class. That’s it! You’ve just created a place where you can write unit tests.

# The key to writing unittest test cases is to call to assertEqual() to check for an expected result; assertTrue() or assertFalse() to verify a condition.

import unittest

def plusOne(x):
    return x + 1

# a suite of tests
class plusOneTest(unittest.TestCase):
    def test(self):
        self.assertEqual(plusOne(3), 4) # actual value first and expected value second

###########################################
# Best practices: Test As You Code
# - It's good practice to create a piece of code, and then write the tests for it. It'll save you a ton of time with debugging the project.
# - What can be some of the problems that occur if you try to write your unit tests weeks or months after you finish writing the code you're testing?

###########################################
# Practice together
# Practice writing these different functions and their unit tests

# Function 1: append_y
# - input: lst (list of strings)
# - output: A new list where each string has a 'y' appended to each value
# - ex: append_y(['hello', 'there' , 'mister']) => ['helloy' , 'therey', 'mistery']

def append_y(lst):
    # write code here
    new_list = []
    for word in lst:
      new_list.append(word + "y")
    return new_list


# Function 2: sum_list
# - inputs: lst (list of ints)
# - output: The sum of all the values in lst
# - ex: sum_list([1, 4, 5) => 10

def sum_list(x):
    # write code here
    return sum(x)

# Function 3: string_equals
# - inputs: str1, str2 (strings)
# - outputs:
  #   True if str1 and str2 are the same
  #   False otherwise
# - ex: string_equals('apple', 'apple') => True

def sting_equals(str1, str2):
    # write code here
    if str1 == str2:
      return (True)
    return (False)

class PracticeTest(unittest.TestCase):
    def test_append_y(self):
        #write a test for fun1
        self.assertEqual(append_y(['hello','there' ,'mister']),['helloy' , 'therey', 'mistery'])

    def test_sum_list(self):
        #write a test for fun2
       self.assertEqual(sum_list([1,2,3,4,5,6]), 21)

    def test_string_equals(self):
        #write a test for fun3
        self.assertEqual(sting_equals("Apple", "Apple"), True)
        self.assertEqual(sting_equals("Apple", "Banana"), False)


# Activity 1
# You started writing this program a few days ago and now you want to test it. Assume at first that multi() runs correctly and returns str, multipled 3 times. Write tests for multi_reverse(). Once those tests are written, identify what is causing them to fail.

# returns a string with str multiplied count number of times
# multi('ho', 3) => 'hohoho'
def multi(str, count):
  return str * count

# good practice: document
def multi_reverse(str):
  multiplied = multi(str, 3)
  newstr = ''
  for i in range(len(multiplied)-1, -1, -1):
    newstr += multiplied[i]
  return newstr

class MyTest2(unittest.TestCase):
    def test_multi_reverse(self):
      #write tests here
      self.assertEqual(multi_reverse('ho'), "ohohoh")


if __name__ == '__main__':
     unittest.main(argv=['first-arg-is-ignored'], exit=False)