#####
#### Experiments with pattern programs in python3 #########

def print_days_as_list():
    days = ['Monday','Tuesday']
    for day in days:
        print(day)

# print_days_as_list()

def print_days_as_dictionary():
    
    days = {'mon': 'Monday', 'tue': 'Tuesday'}
    for day in days:
        print(day, 'stands for', days[day])

#print_days_as_dictionary()

    
def find_first_2_digits_to_form_the_sum(a,n):
    length = len(a)
    for i in range(0,length):
        for j in range(i,length):
          if a[i] + a[j] == n:
                return (a[i],a[j])
                
    
#print(find_first_2_digits_to_form_the_sum([1,2,3,4],6)) 

def string_reverse(s):
    s=s[::-1]
    print(s)


# string_reverse('abcdfg')

def patterns_simple_left_alligned(n):
    output=''
    for i in range(1,n+1):
        for j in range(i):
           output=output+'* '
        output=output+'\n'
        
    return output
        
print(patterns_simple_left_alligned(4))


def patterns_simple_left_alligned_with_numbers(n):
    output=''
    for i in range(1,n+1):
        output=output+str(i)+' '
        for j in range(i):
           output=output+'* '
        output=output+'\n'
        
    return output
        
print(patterns_simple_left_alligned_with_numbers(4))


def patterns_simple_left_alligned_reverse(n):
    output=''
    for i in range(0,n):
        for j in range(n-i):
           output=output+'* '
        output=output+'\n'
        
    return output
        
print(patterns_simple_left_alligned_reverse(4))

def patterns_simple_left_alligned_reverse_with_numbers(n):
    output=''
    for i in range(0,n):
        output=output+str(n-i)
        for j in range(n-i):
           output=output+'* '
        output=output+'\n'
        
    return output
        
print(patterns_simple_left_alligned_reverse_with_numbers(10))


def patterns_simple_left_alligned_reverse_with_numbers_skipping_2_stars(n):
    output=''
    for i in range(0,n+1):
        
        if(i%2 ==0):
            output=output+str(n-i)
            for j in range(n-i):
                output=output+'* '
            output=output+'\n'
        
    return output
        
print(patterns_simple_left_alligned_reverse_with_numbers_skipping_2_stars(10))


def different_patterns_with_spaces(n):
    output=''
    for i in range(1,n+1):
        
            for j in range(n-i):
                output=output+'* '
            for k in range(i):
                output=output+str(n-k)
                output=output+' '
            output=output+'\n'
        
    return output
        
print(different_patterns_with_spaces(9))



def different_patterns_with_skipping_2_starts_without_if(n):
    output=''
    for i in range(1,n+1):
            for j in range(n-2*i):
                output=output+'* '
            
            output=output+'\n'
        
    return output
        
print(different_patterns_with_skipping_2_starts_without_if(10))


