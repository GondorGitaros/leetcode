def mostCommonWord(paragraph, banned):
      paragraph = paragraph.replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace(";", "")
      paragraph = paragraph.lower()
      paragraph = list(paragraph.split(" "))
      paragraph = [i for i in paragraph if i not in banned]
      hm = {}
      for i in paragraph:
        if i in hm:
          hm[i] += 1
        else:
          hm[i] = 0
      return hm
      
print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))