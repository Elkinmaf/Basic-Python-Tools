def possible_tag(word):
    if word.startswith("<") and word.endswith(">"):
        print(word, "could maybe an HTML tag")
    else:
        print(word, "is definitely not an HTML tag (but might contain one)")