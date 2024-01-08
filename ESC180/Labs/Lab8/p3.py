def get_word_counts():
    words = open("Labs/Lab8/text.txt", encoding="latin-1").read().split()

    word_counts = {}
    for word in words:
        if word in word_counts.keys():
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

def top10(L):
    return sorted(L)[:-10]

def most_frequent_words(n):
    word_counts = get_word_counts()
    L = sorted(word_counts.items(), key=lambda item: item[1])

    ret = []
    count = 1
    while count < len(L) and count <= n:
        ret.append(L[-count])
        count += 1
    
    return ret

print(most_frequent_words(10))