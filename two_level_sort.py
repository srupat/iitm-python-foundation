def two_level_sort(scores):
    x=[]
    for i in scores:
        x.append(i[1])
    x.sort()
    #x madhe jya index la to score asel tithe ha score takaycha    
    for i in range(len(x)):
        for j in range(len(scores)):
            if scores[j][1]==x[i]:
                temp=scores[i]
                scores[i]=scores[j]
                scores[j]=temp    
            
    for i in range(len(scores)-1):
        if scores[i][1]==scores[i+1][1]:
            if scores[i][0]>scores[i+1][0]:
                temp=scores[i]
                scores[i]=scores[i+1]
                scores[i+1]=temp
    return scores        
        
#print(two_level_sort([('srujan',97),('vedashree',81),('umesh',88),('shreya',81),('atharva',88)]))