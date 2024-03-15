def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_special_records(records):
    special_records = []
    for record in records:
        if is_palindrome(record):
            special_records.append(record)
    return special_records

# Example: Let's say we have these record numbers
records = [123, 121, 345, 454, 567, 676]
print(find_special_records(records))