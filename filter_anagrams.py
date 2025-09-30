def filter_anagrams(word, words):
    d = {i: word.count(i) for i in word}
    return [i for i in words if {j: i.count(j) for j in i} == d]


word = "abba"
anagrams = ["aabb", "abcd", "bbaa", "dada"]
print(filter_anagrams(word, anagrams))
print(filter_anagrams("отсечка", ["сеточка", "стоечка", "тесачок", "чесотка"]))
print(
    filter_anagrams(
        "tommarvoloriddle",
        ["iamlordvoldemort", "iamdevolremort", "mortmortmortmort", "remortvolremort"],
    )
)
print(filter_anagrams("стекло", []))
