# String methods

name = "Bruce Wayne"

print(name.upper()) # Converts to all uppercase
print(name.lower()) # Converts to all lowercase
print(name.title()) # Converts the first character of each word in the string to uppercase
print(name.replace("Bruce", "Brucie")) # Replaces a substring with another substring
print(name.split()) # Splits the string into a list of words
print(name.startswith("Bruce")) # Checks if the string starts with a specific substring
print(name.endswith("Wayne")) # Checks if the string ends with a specific substring

print(name.find("Wayne")) # Returns the index of the first occurence of the substring
print(name.count("a")) # Counts the number of occurrences of a substring in the string
print(name.isalpha()) # Checks if all characters in the string are alphabetic
print(name.isdigit()) # Checks if all characters in the string are numbers
print(name.isalnum()) # Checks if all characters in the string are alphanumeric
