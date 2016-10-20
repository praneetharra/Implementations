a = 'abcbbbbcccbdddadacb'

maps = {}

first_point = 0
second_point = 0
end_point = 0

two_set = []

for i in a:
    if i not in two_set:
        two_set.append(i)
    if len(two_set)==2:
        break

first_point, end_point = a.index(two_set[0]), a.index(two_set[1])

for i in range(len(a)):
    if a[i] in two_set:
        end_point = i
        if a[i] != a[second_point]:
            second_point = i
    else:
        maps[len(a[first_point:end_point+1])] = a[first_point:end_point+1]
        first_point = second_point
        two_set = [a[second_point],a[i]]
        second_point = i
        end_point = i
        
maps[len(a[first_point:end_point+1])] = a[first_point:end_point+1]
