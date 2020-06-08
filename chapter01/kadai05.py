text = "I am an NLPer"
def word_n_gram(text, N):
    words = text.split()
    result = []
    for it, c in enemerate(words):
        if it + N > len(words):
            return result
        result.append(words[it: it+N])

print(word_n_gram(text, N=2))

print(word_n_gram(text, N=3))
