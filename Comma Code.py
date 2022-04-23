# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma
# and a space, with and inserted before the last item. Should work with any list value passed to it

# Normally, I would use the .join() to convert, but it only works on lists that contain the same elements.
# I choose to use map, even though it wasn't covered in the book, because I had previously used it in my studies.

def empty_list_check(check_list):
    if not check_list:
        return "This is an empty list."
    else:
        return list_to_string(check_list)


def list_to_string(spam_list):
    return ", ".join(map(str, spam_list[:-1])) + ", and " + str(spam_list[-1])


spam = ['apples', "bananas", "tofu", "cats"]
no_list = []

print(empty_list_check(spam))
print(empty_list_check(no_list))
