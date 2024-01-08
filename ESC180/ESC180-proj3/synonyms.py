'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


def get_word_count(w0, w1, semantic_descriptor):
    curr = semantic_descriptor.get(w0, 0)
    if curr != 0:
        curr = curr.get(w1, 0)
    else:
        #without initializing w0 it return a key error when trying to access [w0][w1]
        semantic_descriptor[w0] = {}
        semantic_descriptor[w0][w1] = {}
    return curr

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    sum = 0
    for k in vec1:
        v1 = vec1.get(k)
        if k in vec2:
            v2 = vec2.get(k)
        else:
            v2 = 0
        sum += v1 * v2
    nom_v1 = norm(vec1)
    nom_v2 = norm(vec2)
    return sum/(nom_v1*nom_v2)

def build_semantic_descriptors(sentences):
    semantic_descriptor = {}
    for sentence in sentences:
        pairs = []
        sentence = list(set(sentence))
        for i in range(len(sentence)):
            w0 = sentence[i]
            for j in range(i + 1, len(sentence)):
                w1 = sentence[j]
                pairs.append((w0, w1))

        for pair in pairs:
            w0 = pair[0]
            w1 = pair[1]
            semantic_descriptor[w0][w1] = get_word_count(w0, w1, semantic_descriptor) + 1
            semantic_descriptor[w1][w0] = get_word_count(w1, w0, semantic_descriptor) + 1
            
    return semantic_descriptor

        
def build_semantic_descriptors_from_files(filenames):
    inp = []
    for file in filenames:
        text = open(file, "r", encoding="latin1").read().lower()
        text = text + " "
        text = text.replace("?", ".")
        text = text.replace("!", ".")
        punc = ["\n", ",", "-", "--", ":", ";"]
        for p in punc:
            text = text.replace(p, " ")
        text = text.split(". ")
        for sentence in text:
            inp.append(list(filter(None, sentence.split(" "))))
    
    return build_semantic_descriptors(inp)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    dic = {}
    for choice in choices:
        if choice not in semantic_descriptors or word not in semantic_descriptors:
            dic[choice] = -1
        else:
            dic[choice] = similarity_fn(semantic_descriptors.get(word), semantic_descriptors.get(choice))
    # print(dic)
    return max(dic, key=dic.get)

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    text = open(filename, "r", encoding="latin1").read().lower()
    text = text.split("\n")
    q = []
    for j in text:
        if j != "":
            q.append(j.split(" "))
    sol = []
    choices = []
    ans = []
    for question in q:
        choices.append(question[2:])
        sol.append(question[1])
    for i in range(len(choices)):
        ans.append(most_similar_word(q[i][0], choices[i], semantic_descriptors, similarity_fn))
    right_answer = 0
    total_question = 0
    for i in range(len(ans)):
        if ans[i] == sol[i]:
            right_answer += 1
        total_question += 1
    # print(sol)
    # print(ans)
    return (right_answer/total_question) * 100

def semantic_descriptor_test():
    test_semantic_discriptor = [["i", "am", "a", "sick", "man"],
    ["i", "am", "a", "spiteful", "man", "man"],
    ["i", "am", "an", "unattractive", "man"],
    ["i", "believe", "my", "liver", "is", "diseased"],
    ["however", "i", "know", "nothing", "at", "all", "about", "my",
    "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
    res = build_semantic_descriptors(test_semantic_discriptor)["man"]
    expected = sorted({'i': 3, 'am': 3, 'a': 2, 'sick': 1, 'spiteful': 1, 'an': 1, 'unattractive': 1})
    if res == expected:
        print("TEST PASSED")
    else:
        print(res, "does not match", expected)

# print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
semantic_descriptors = build_semantic_descriptors_from_files(["swan's_way.txt", "war_peace.txt"])
print(run_similarity_test("test.txt", semantic_descriptors, cosine_similarity))



