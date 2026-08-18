def count_freq():
    name = input("Enter a string: ")
    character = input("Enter character: ")
    count = 0

    for i in name:
        if i == character:
            count += 1

    print(count)

count_freq()