def reverse(x):
    # Define the limits for a 32-bit signed integer
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Handle negative numbers by remembering the sign
    sign = 1 if x >= 0 else -1
    x = abs(x)

    # Initialize the result
    result = 0

    while x != 0:
        # Get the last digit of x
        last_digit = x % 10
        x = x // 10

        # Check for overflow
        if result > (INT_MAX - last_digit) // 10:
            return 0

        result = result * 10 + last_digit

    # Restore the original sign
    result *= sign

    # Check for overflow again after restoring the sign
    if result < INT_MIN or result > INT_MAX:
        return 0

    return result

# Example usage:
x = 123
print(reverse(x))  # Output: 321
