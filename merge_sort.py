# creats 2 temporary arrays better available in C++ codes
def merge(A,p,q,r):
	n1=q-p+1
	n2=r-q
	L=[]; R=[]
	for i in range(p,q+1):
		L.append(A[i])
	#L.append(99999999)
	for i in range(q+1,r+1):
		R.append(A[i])
	#R.append(99999999)
	i=0;j=0
	for k in range(p,r+1):
		if i==n1:
			for l in range(k,r+1):
				A[l]=R[j]; j+=1
			break
		elif j==n2:
			for l in range(k,r+1):
				A[l]=L[i]; i+=1
			break
		elif L[i]<=R[j]:
			A[k]=L[i]; i+=1
		else:
			A[k]=R[j]; j+=1

def merge_sort(A,p,r):
	if p<r:
		q=int((p+r)/2)
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		merge(A,p,q,r)

infile=input('enter file name to sort: ')
oufile=input('enter file name to store sorted data: ')
import time
start = time.time()
fp=open(infile)
randintlist=fp.readlines()
randint=[]
for i in range(len(randintlist)):
	randint.append(int(randintlist[i]))

merge_sort(randint,0,len(randint)-1)
fout=open(oufile,'w')
for i in range(len(randint)):
	fout.write(str(randint[i])+'\n')
end = time.time()
print(end - start)