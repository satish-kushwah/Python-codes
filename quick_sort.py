def partition(A,p,r):
	print('partion',p+1,r+1)
	i=p-1
	for j in range(p,r):
		if A[j]<A[r]:
			i=i+1
			A[i],A[j]=A[j],A[i]
	i=i+1
	A[i],A[r]=A[r],A[i]
	return(i)

def quick_sort(A,p,r):
	print('quick_sort',p+1,r+1)
	if p<r:
		q=partition(A,p,r)
		quick_sort(A,p,q-1)
		quick_sort(A,q+1,r)

infile=input('enter file name to sort: ')
oufile=input('enter file name to store sorted data: ')
import time
start = time.time()
fp=open(infile)
randintlist=fp.readlines()
randint=[]
for i in range(len(randintlist)):
	randint.append(int(randintlist[i]))

quick_sort(randint,0,len(randint)-1)
fout=open(oufile,'w')
for i in range(len(randint)):
	fout.write(str(randint[i])+'\n')
end = time.time()
print(end - start)