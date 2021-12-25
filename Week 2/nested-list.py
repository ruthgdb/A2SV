if __name__ == '__main__':
    students=[]
    studnames=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    results = [students[i][1] for i in range(len(students))]
    
    mini = min(results)
    for i in range(len(results)):
        if(min(results) == mini):
            results.remove(min(results))
    mini = min(results)
    for i in range(len(students)):
        if(mini == students[i][1]):
            studnames.append(students[i][0])
    studnames.sort()
    for i in studnames:
        print(i)
        
