
# most efficient 
def lengthOfLastWord(s: str) -> int:
        s_stripped = s.strip()
        s_split = s_stripped.split(' ')
        x = int(len(str(s_split[-1])))
        return(x)
    
def lengthOfLastWord(s: str) -> int:
        """
	one shortcut
	"""
	# return len(s.split()[-1])
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c

def lengthOfLastWord_(s: str) -> int:
        i = len(s) -1
        isWord = True
        index = 0
        while isWord:
                if s[i] != " ":
                        index = i
                        isWord=False 
                if i == 0:
                        isWord=False 
                i-=1
        wordLen = 0
        wordFound = False
        while not wordFound:
                if index == 0:
                        wordFound=True
                if s[index] == " ":
                        wordFound = True
                else:
                        wordLen+=1
                index -=1
        return wordLen
lengthOfLastWord_("a")