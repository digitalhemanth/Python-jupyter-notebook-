def bubblesort(arry):
    for i in range(0, len(arry)-1):
        if arry[i] > arry[i+1]:
            arry[i] , arry[i+1] = arry[i+1], arry[i]
        
        
                        
arry = [2,8,4,1,-6]
print(bubblesort(arry))