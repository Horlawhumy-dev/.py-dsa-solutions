from operator import le
from new_stack import Stack


string = "Hello World! How are you doing?"

reversed_string = ""


def reverse_string(string, reversed_str) -> str:
    """
    @params: string to be reversed, empty string container
    @returns: reversed string result using stack data structure
    Time Complexity: O(n)
    Space complexity: O(n)
    """
    stack = Stack()
    splitted_str = string.split(" ")

    count = 0

    assert stack.size() == count #loop invariant

    for el in splitted_str:
        assert stack.size() == count
        stack.push(el)
        count += 1
        assert stack.size() == count


    for i in range(stack.size()):
        reversed_str = reversed_str + " " + stack.pop()

    return reversed_str

print(reverse_string(string, reversed_string))