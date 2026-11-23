# Conditional statements
# Keywords: if, elif, else

marks = int(input("Enter your score: "))

if marks >= 90:
    print("Grade A - Excellent!")
elif marks >= 80:
    print("Grade B - Nice work!")
elif marks >= 70:
    print("Grade C - Not bad!")
else:
    print("Needs improvement...")

print()
status_code = int(input("Enter status code: "))

if status_code == 200:
    print("> Success")
elif status_code == 404:
    print("> Not Found")
elif status_code >= 500:
    print("> Server side error")
else:
    print("> Check Application server")
