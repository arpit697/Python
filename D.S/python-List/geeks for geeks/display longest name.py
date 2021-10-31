def longname(l):
    longest = ""
    for i in range(len(l)):
        if len(l[i]) > len(longest):
            longest = l[i]
    print(longest)

l =["Geek", "Geeks", "Geeksfor","GeeksforGeek", "GeeksforGeeks"]
longname(l)