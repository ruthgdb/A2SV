class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        places = {3: "Billion", 2: "Million", 1: "Thousand"}
        
        tens = {0: "", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        
        tens_alt = {0: "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen", 6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}
        
        ones = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        
        def findWord(curr):
            currWord = []
            
            for i in range(3):
                if i == 0:
                    if curr[0] != '0':
                        currWord.append(ones[int(curr[0])] + " Hundred")
                elif i == 1:
                    if curr[1] == '1':
                        currWord.append(tens_alt[int(curr[2])])
                        break
                    if curr[1] != '0':
                        currWord.append(tens[int(curr[1])])
                else:
                    if curr[2] != '0':
                        currWord.append(ones[int(curr[2])])
            
            return " ".join(currWord)
        
        num = str(num)
        words = []
        remaining = len(num) % 3
        if remaining > 0:
            num = "0" * (3 - remaining) + num
            
        partitions = []
        
        for i in range(0, len(num), 3):
            partitions.append(num[i: i + 3])
            
        for i, curr in enumerate(partitions):
            word = findWord(curr)
            placeIdx = len(partitions) - i - 1
            
            if word:
                words.append(word)
        
                if placeIdx in places:
                    words.append(places[placeIdx])
            
        return " ".join(words)