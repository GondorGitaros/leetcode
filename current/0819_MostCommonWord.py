def mostCommonWord(paragraph, banned):
    paragraph = paragraph.replace(",", " ")
    print(paragraph)
    for i in range(len(paragraph)):
        if paragraph[i] == " " and paragraph[i + 1] == " ":
            paragraph[i] == ""
    print(paragraph)
    paragraph = list(paragraph.replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace(";", "").lower().split(" "))
    paragraph = [i for i in paragraph if i not in banned]
    hm = {}
    for i in paragraph:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 0
    key_list = list(hm.keys())
    hmli = sorted(hm.values())
    couter = 0
    for i in hm:
        if hm[i] == hmli[-1]:
            return key_list[couter]
        couter += 1
        
    return hm

print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))