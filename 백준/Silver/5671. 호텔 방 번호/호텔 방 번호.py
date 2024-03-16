
while True:
    try:
        n,m=input().split()
        hotel=list(range(int(n),int(m)+1))
        ans=[]
       
        for item in hotel:
            d={'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            flag=True
            for s in str(item):
                if s in d.keys():
                    d[s] += 1
            
            for v in d.values():
                if v >= 2 :
                    flag=False
            
            if flag:
                ans.append(item)
        
        print(len(ans))
                
    except EOFError:
        break
    