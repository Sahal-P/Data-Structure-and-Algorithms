from collections import defaultdict


def Counter(chars):
    char_map = defaultdict(int)
    for s in chars:
        if s in char_map:
            char_map[s] += 1
        else:
            char_map[s] = 1
    return char_map


def countCharacters(words, chars):
    char_map = Counter(chars)
    total_count = 0

    for i in words:
        charCount: dict = Counter(i)
        isCharGood = True
        for key, count in charCount.items():
            print(key, count)
            if key not in char_map or count > char_map[key]:
                isCharGood = False
                break

        if isCharGood:
            total_count += len(i)
    return count


words = ["cat", "bt", "hat", "tree"]
words1 = [
    "dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
    "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb",
    "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl",
    "boygirdlggnh",
    "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
    "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
    "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
    "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
    "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
    "oxgaskztzroxuntiwlfyufddl",
    "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
    "qnagrpfzlyrouolqquytwnwnsqnmuzphne",
    "eeilfdaookieawrrbvtnqfzcricvhpiv",
    "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
    "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
    "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
    "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo",
    "teyygdmmyadppuopvqdodaczob",
    "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
    "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs",
]

chars = "atach"
chars1 = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"



# efficiant sollution


def countCharacters_e(words, chars) -> int:
    count = 0
    for word in words:
        for letter in word:
            # print(chars.count(letter), letter) it returns the count of signle letter in chars eg: 1:c, 2:a
            if chars.count(letter) < word.count(letter):
                break
        else:
            count += len(word)
    return count

countCharacters_e(words, chars)