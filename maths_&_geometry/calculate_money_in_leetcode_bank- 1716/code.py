
# brute force approch
def totalMoney(n: int) -> int:
        day = 0
        deposit = 0
        total = 0

        while  day < n:
            total += deposit
            deposit +=1
            day +=1
            if day % 7 == 0:
                deposit = 1 + day // 7

        return total

# efficent math approch 
def totalMoney(n: int) -> int:
        total = 0
        week = n // 7
        leftover = n % 7
        
        for i in range(week):
            total += 28 + (7*i)
        for j in range(leftover):
            total += j + (week + 1)

        return total