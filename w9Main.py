def countwords():
    word='sangmyung university'
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    
def lab9():
    countwords()
    
def main():
    lab9()

if __name__=="__main__":
    main()
