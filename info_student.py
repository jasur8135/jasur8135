names=[]
surnames=[]
ages=[]
phones=[]
homes=[]

def info_studens():
    n=int(input('Studentlar sonini kiriting\n>>>'))
    while True:
        names.append(input('enter your name\n>>>').title())
        surnames.append(input('enter your surname\n>>>').title())
        ages.append(int(input('enter your age\n>>>')))
        phones.append(int(input('enter your phone\n>>>')))
        homes.append(input('enter your region\n>>>').title())
        if len(names)==n:
            break
    m=0
    for g in names:
        print(names[m],'',surnames[m],'',ages[m],'',phones[m],'',homes[m])
        m=m+1

info_studens()
