word1 = "leetcode"
word2 = "etco"
average = ""
longest = word1 if len(word1) > len(word2) else word2
shortest = word1 if len(word1) < len(word2) else word2
for i in range(len(longest)):
    if average + longest[i] in shortest:
        average += longest[i]
print(len(longest) - len(average) * 2 + len(shortest))