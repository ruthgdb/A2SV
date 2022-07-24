class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        count_s = Counter(secret)
        count_g = Counter(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                count_s[secret[i]] -= 1
                count_g[guess[i]] -= 1
        for i in count_s.keys():
            if i in count_g.keys() and count_g[i] > 0:
                cow += min(count_s[i],count_g[i])
        return "{}A{}B".format(bull,cow)
        