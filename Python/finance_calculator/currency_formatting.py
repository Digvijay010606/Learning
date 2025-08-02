def format_currency(num):
    num_str = str(num)
    rev = num_str[::-1]   # Reverse the string
    result = ""

    for i in range(len(rev)):
        if i != 0 and i % 3 == 0:
            result += ","
        result += rev[i]

    return result[::-1]  # Reverse back to normal