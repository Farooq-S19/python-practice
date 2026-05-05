def funct(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}")
funct(a=1,b=3,c=10)