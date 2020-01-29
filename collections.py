from collections import deque 

#Counting_elements
def frog_river_one(x,a):
    
    for i in range(len(a)):
        if a[i] == x:
            return i+1
    
    
#print(frog_river_one(5,[1,4,5,8,9]))
  

def check_permutation(A):
    output=True
    for i in range(1,len(A)+1):
        if i not in A:
            print(i, A)
            output = False
        print(i, A)
    return output
    
#print(check_permutation([1,1,2]))


def find_first_sorted_array_to_have_sum_n(A,n):
    output=0
    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[i] + A[j] == n:
                print(A[i],A[j])
                output = min(output , j-i)
    return output

#print(find_first_sorted_array_to_have_sum_n([1,2,3,4],5))



# def linked_list_has_a_loop():


##Basic implement linkedlist


class Node:
    def __init__(self,data):
        self.data = data
        self.nextLink = None
        
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.nextLink
    
    def detectLoop(self):
        s = set()
        temp = self.head
        while(temp): 
            if(temp in s):
                return True
            s.add(temp)
            temp = temp.nextLink
        return False
        

# l1 = LinkedList()

# first = Node(123)
# second = Node(456)
# third = Node(789)

# l1.head = first
# l1.head.nextLink = second
# second.nextLink = third

# print(l1.detectLoop())


# l1.printLinkedList()



##Basic implement Stack

class Stack:
    
    def __init__(self):
        self.data = [-1]
    
    def push(self,value):
        self.data = self.data + [value]
    
    def pop(self):
            data_dup = self.data 
            self.data = []
            for i in range(len(data_dup)-1):
                self.data = self.data + [data_dup[i]]
            if self.data is None:
                self.data = [-1]
        




s1 = Stack()
s1.push(890)
print(s1.data)
s1.push(891)
print(s1.data)
s1.push(892)
print(s1.data)
s1.pop()
print(s1.data)
s1.pop()
print(s1.data)
s1.pop()
print(s1.data)


##Python stack implementation using list append and pop


def stack_and_queue_demo():
    stack = []
    stack.append(1)
    stack.append(5)
    stack.append(8)

    stack.pop()

    print(stack)
    
    q= deque()
    q.append(90)
    q.append(78)
    q.popleft()
    print(q)

stack_and_queue_demo()







# Your previous Java content is preserved below:
# 
# import java.io.*;
# import java.util.*;
# 
# /*
#  * To execute Java, please define "static void main" on a class
#  * named Solution.
#  *
#  * If you need more classes, simply define them inline.
#  */
# 
# class Solution {
#   public static void main(String[] args) {
#     ArrayList<String> strings = new ArrayList<String>();
#     strings.add("Hello, World!");
#     strings.add("Welcome to CoderPad.");
#     strings.add("This pad is running Java " + Runtime.version().feature());
# 
#     for (String string : strings) {
#       System.out.println(string);
#     }
#   }
# }
# 
# 
# /* 
# Your previous Python 3 content is preserved below:
# 
#     
# def print_days_as_list():
#     days = ['Monday','Tuesday']
#     days += ['Wednesday']
#     for day in days:
#         print(day)
# 
# print_days_as_list()
# 
# 
# 
# def reverse_an_array(a):
#     
#     for i in range(0,len(a)//2):
#         k = len(a)-i-1
#         a[k],a[i] = a[i],a[k]
#     return a
# 
# print(reverse_an_array([5,6,7,8]))
# 
# 
# 
#  */

