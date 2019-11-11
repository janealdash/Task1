Write a function is_even that takes
in a number and returns True if it is even,otherwise False.

def is_even(a):
   if a % 2 == 0:
    return True
   else:
    return False

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(8) == True
    assert is_even(100) == True
    assert is_even(101) == False
    print("Your code is correct!")

test_is_even()

