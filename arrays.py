
def sort_array(n,A):
    if n > len(A):
        return None

    output = ''
    for j in range(n,len(A)+1):
        output = output+ ' ' + str(j)
    for i in range(0,n):
        output = output+' '+str(A[i])
    return output

print(sort_array(5,[1,2,3,4,5,6]))


def find_kth_smallest_element(n,A):

    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[i]  > A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp

    return A[n-1]

print(find_kth_smallest_element(2,[1,3,4,5,8,2,6]))


def find_frequency_of_elements(A):
    output = set()
    for i in range(len(A)):
        count = 0
        for j in range(i,len(A)):
            if A[i] == A[j]:
                count = count + 1
        output.add((A[i],count))
    return output

print(find_frequency_of_elements(['a','v','b','n','a','b','a','c','v','f']))


def matrix_column_switch(A,m,n):
    for i in range(m):
        for j in range(n-1,-1,-1):
            print(A[i][j],end=' ')
        print('\n')


matrix_column_switch([[1, 2, 3],[4,5,6],[7,8,9]],3,3)



def maximum_height_given_2struct_array:
    pass
