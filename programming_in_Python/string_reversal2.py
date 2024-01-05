def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

str = "Felix"
print(string_reverse(str))
"""
The program defines a function string_reverse that takes a string str as an argument.

In the function, there's a base case: if the length of the string is 0 (empty string), it returns the string as is.

If the length of the string is not 0 (non-empty string), the function enters the recursive case. It reverses the substring starting from the second character (str[1:]) by making a recursive call to string_reverse. It then concatenates this reversed substring with the first character of the original string (str[0]).

The recursion continues until the base case is reached, at which point the reversed string is gradually built up.

The program then defines a string str with the value "Felix."

Finally, it prints the result of calling string_reverse on the input string "Felix," which effectively reverses the string. In this case, the output would be "xileF."
"""