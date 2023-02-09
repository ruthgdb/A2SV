class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06', "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
        
        date = date.split(' ')
        date[1] = month[date[1]]
        date[0] = date[0][:-2] if len(date[0][:-2]) == 2 else '0' + date[0][:-2]
        date.reverse()
        return '-'.join(date)