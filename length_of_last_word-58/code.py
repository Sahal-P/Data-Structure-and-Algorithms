
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
	#	return len(s.split()[-1])
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c