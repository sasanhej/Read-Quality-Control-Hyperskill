import gzip
files = [input(), input(), input()]
paramdict ={}
totalfinal = []
for _ in range(len(files)):
    file = gzip.open(files[_], 'rt')
    readslist = file.read().split('\n')[1::4]
    file.close()
    lengths = []
    GC = []
    GCper = []
    Ns = []
    Nsper = []
    for i in readslist:
        lengths.append(len(i))
        GC.append(i.count('C')+i.count('G'))
        GCper.append((i.count('C')+i.count('G'))/len(i)*100)
        Ns.append(i.count('N'))
        Nsper.append(i.count('N')/len(i)*100)
    GCmean = round((sum(GCper)/len(GCper)), 2)
    totalreads = len(readslist)
    avl = int(round((sum(lengths)/len(lengths)), 0))
    cntset = []
    repeats = len(readslist)-len(set(readslist))
    Nsreads = len([i for i in Ns if i > 0])
    Nsavg = round(sum(Nsper)/len(Nsper), 2)
    paramdict[_] = [totalreads, avl, repeats, Nsreads, GCmean, Nsavg]
    totalfinal.append(repeats+sum(Ns))
best = min(range(len(totalfinal)), key=lambda x: totalfinal[x])
totalreads, avl, repeats, Nsreads, GCmean, Nsavg = paramdict[best]
print(f'Reads in the file = {totalreads}:')
print(f'Reads sequence average length = {avl}\n')
print(f'Repeats = {repeats}')
print(f'Reads with Ns = {Nsreads}\n')
print(f'GC content average = {GCmean}%')
print(f'Ns per read sequence = {Nsavg}%')
