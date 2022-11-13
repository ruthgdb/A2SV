class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        answer = [word for word in words if word != '']
        answer.reverse()
        return ' '.join(answer)