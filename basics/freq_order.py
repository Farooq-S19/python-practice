def txt_chg(txt):
    dit={}
    for i in txt:
        if i in dit:
            dit[i]+=1
        else:
            dit[i]=1
    return dit
print(txt_chg("hellosirgoodhell"))