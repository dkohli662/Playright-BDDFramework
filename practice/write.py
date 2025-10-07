# read the file and store the content in a list
# reverse the list
# write reversed list in a file

with open('text.txt', 'r') as file:
    content=file.readlines() # cat, dog, elephent,hen,mouse
    print(content)
    reversed(content) # mouse, Hen, elephnent, dog, cat
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


