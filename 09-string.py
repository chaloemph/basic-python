words = "hello world"
print(words)
print(words[2])
print(words[0:2])
print(len(words))
print(words.startswith("h"))
print(words.startswith("he"))
print(words.endswith("d"))
print(words.endswith("ld"))
print(words.find("h"))
print(words.replace("o", "Q"))
print(words.count("o"))
print(words.capitalize())
print(words.title())
print(words.upper())
print(words.lower())


print(words.split())

data = "one:two:three:four:five"
print(data.split(":"))
print(data.split(":",2))
