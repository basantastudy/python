# write a program that uses string methods to alter each string so that .startswith("be") returns True for all of them.

# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = " bEautiful"

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

print(string1.lower().strip().startswith("be"))
print(string2.lower().strip().startswith("be"))
print(string3.lower().strip().startswith("be"))
print(string4.lower().strip().startswith("be"))