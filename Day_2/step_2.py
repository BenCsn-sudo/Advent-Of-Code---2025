with open('input.txt', 'r', encoding='utf-8') as fichier:
    instructions = fichier.read().split(',')

res = 0

def search(chaine):
    i = 1
    for e in range(1, int(len(chaine)/2)+1, i):
        i += 1
        if chaine[:e] == chaine[e:(e*2)]:
            if e == 0:
                e = 1
            for l in range(e, len(chaine), e):
                if chaine[:e] == chaine[l:l+e]:
                    if l == len(chaine)-e:
                        return True
                else:
                    break
    return False

for ele in instructions:
    Ids = ele.split('-')
    start = int(Ids[0])
    end = int(Ids[1])
    for i in range(start, end):
        i = str(i)
        if search(i):
            res += int(i)
        

print("Le mot de passe est: ", res)
