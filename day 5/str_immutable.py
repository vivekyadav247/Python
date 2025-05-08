original_str = "Hello"

try:
    original_str[0] = "h"
except TypeError as e:
    print("Error:", e)
    print("Strings are immutable in Python.")
