# GEO1000 - Assignment 2
# Authors: Leonardo Melo	
# Studentnumbers: 4690923

#===== Recursive function call
def cdrec(n, deposit, apr, periods):
   if n==0:
        return deposit
   else:
        temp=cdrec(n-1,deposit,apr,periods)
        res=(1.0+(apr/100.0/periods))*temp
        return res


#===== iterative function 
def cditer(n, deposit, apr, periods):
    result=[]
    i=0
    while i<=n:
        if i==0:
            temp=deposit
        else:
            temp=(1.0+(apr/100.0/periods))*result[i-1]
        result.append(temp)
        i+=1  
    return result[i-1]   


def test():
    print cdrec(20,1000,5,12)
    print cditer(20,1000,5,2)

if __name__ == "__main__":
    test()
