s = "catsanddog"
words = ["cat", "cats", "and", "dog"]


def wordbreak(s, words, c = "", current = "", i=0):
    if(i == len(s)):
        print(current)
        return
    print(current)
    
    check = [word.startswith(c) for word in words]
    if(not any(check)):
        print("grave",current)
        return 
          
    if(c in words):
        print("palabra",c) 
        
    wordbreak(s, words, c + s[i] + " ", current + s[i] + " ", i+1)
    wordbreak(s, words, c + s[i] + " ", current + s[i], i+1)
    
wordbreak(s, words)
