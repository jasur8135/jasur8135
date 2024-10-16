mem_names=[]
mem_ages=[]
mem_lastnames=[]
mem_phones=[]
def room_members():
    n=1
    while n<5:
        name=input(f'{n}-azoning ismini kiriting\n>>>')
        surname=input(f'{n}-azoning familiyasi kiriting\n>>>')
        age=int(input(f'{n}-azoning yoshini kiriting\n>>>'))
        phone=int(input(f'{n}-azoning telefon raqamini kiriting\n>>>'))
        mem_names.append(name.title())
        mem_ages.append(age)
        mem_lastnames.append(surname.title())
        mem_phones.append(phone)
        n=n+1
    print(mem_names)
    print(mem_lastnames)
    print(mem_ages)
    print(mem_phones)


def info_mem():
    mem_number=len(mem_names)
    mem_num=int(input(f'salom.Bu xonaning azolari haqida malumot beruvchi dastur,\nxonada {mem_number} azo bor.\nAzoning raqamini kiriting\n>>'))
    if True:
        index=mem_num-1
        print(mem_names[index])
        print(mem_lastnames[index])
        print(mem_ages[index])
        print(mem_phones[index])
        if mem_num==4:
            print(mem_names[index])
            print(mem_lastnames[index])
            print(mem_ages[index])
            print(mem_phones[index])
            break
    
room_members()
info_mem()
        

    
