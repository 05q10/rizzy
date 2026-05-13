words = {
    'unhappiness': [('un-', "bound"), ('happy', 'free'), ('-ness', "bound")],
    'replayed': [('re-', "bound"), ('play', "free"), ('-ed', "bound")],
     "international":[("inter-", "bound"), ("nation",  "free"), ("-al",    "bound")],
}

for word in words:

    print(word)

    for morpheme in words[word]:
        print(morpheme)

    print()