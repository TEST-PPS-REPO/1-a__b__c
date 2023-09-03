inp = input()
spt = inp.split(' ')
assert len(spt) == 3, 'len(spt) = ' + str(len(spt))
for i in spt:
    ii = int(i)
    assert 0 <= ii <= 10