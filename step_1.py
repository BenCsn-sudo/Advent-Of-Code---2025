# Lecture du fichier
with open('input.txt', 'r', encoding='utf-8') as fichier:
    data = fichier.read().split('\n')

fresh_range = []
Id = []

mode_ajout = False
res = 0

for i in range(len(data)):

    if data[i] == '':
        mode_ajout = True
    else:
        if not mode_ajout:
            fresh_range.append(data[i])
        else:
            Id.append(data[i])


for ele in Id:

    for ran in fresh_range:

        intervalle = ran.split('-')
        mini = intervalle[0]
        maxi = intervalle[1]

        if int(ele) >= int(mini) and int(ele) <= int(maxi):
            res += 1
            break

print(res)