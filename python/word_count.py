# Reads a text file, normalizes and counts word occurrences, then prints the three most frequent words.

'''
The cat sat on the mat. The cat saw the dog,
and the dog ran. The cat, the cat, the dog and the bird.
A bird sat near the cat while the dog slept.

'''

def main():
    # TODO: read python/word_count_input.txt, tally each lowercased word
    # (strip surrounding punctuation), and print the top 3.
    with open("/word_count_input.txt", "r") as f :
      dic = f.read().lower()
      dic = dic.split()
      dic = list(map(lambda x : x.strip('.,'), dic))

      freqDict = dict.fromkeys(set(dic), 0)
      for word in dic :
        freqDict[word] +=1
      freqDict = dict(sorted(freqDict.items(), key= lambda item : item[1], reverse = True))
      
      print(list(freqDict.items())[:3])

if __name__ == "__main__":
    main()