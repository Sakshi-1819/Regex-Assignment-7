#!/usr/bin/env python
# coding: utf-8

# # Q1. Given an array of size N containing only 0s,1s, and 2s;sort the array in ascending order.

# In[11]:


def intsort(list):
   for i in range(1,len(list)):
      j=i-1
      while j>=0 and list[j+1]<list[j]:
         list[j+1],list[j]=list[j],list[j+1]
         j-=1
   return list
print(intsort([0,2,1,2,0]))


# In[12]:


def intsort(list):
   for i in range(1,len(list)):
      j=i-1
      while j>=0 and list[j+1]<list[j]:
         list[j+1],list[j]=list[j],list[j+1]
         j-=1
   return list
print(intsort([0,1,0]))


# # Q2. Given an array, rotate the array by one position in clock-wise direction.

# In[13]:


def rotate(arr,n):
    x=arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1];
    arr[0] = x

arr=[1,2,3,4,5]
n = len(arr)
print("Given array is")
for i in range(0,n):
    print(arr[i],end=" ")
rotate(arr,n)

print("\nRotated array is")
for i in range(0,n):
    print(arr[i], end=" ")


# In[14]:


def rotate(arr,n):
    x=arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1];
    arr[0] = x

arr=[9,8,7,6,4,2,1,3]
n = len(arr)
print("Given array is")
for i in range(0,n):
    print(arr[i],end=" ")
rotate(arr,n)

print("\nRotated array is")
for i in range(0,n):
    print(arr[i], end=" ")


# # Q3. Implement next permutation which rearranges numbers into the lexicographically next greater permutation of numbers.

# In[15]:


class Solution(object):
   def nextPermutation(self, nums):
      found = False
      i = len(nums)-2
      while i >=0:
         if nums[i] < nums[i+1]:
            found =True
            break
         i-=1
      if not found:
         nums.sort()
      else:
         m = self.findMaxIndex(i+1,nums,nums[i])
         nums[i],nums[m] = nums[m],nums[i]
         nums[i+1:] = nums[i+1:][::-1]
      return nums
   def findMaxIndex(self,index,a,curr):
      ans = -1
      index = 0
      for i in range(index,len(a)):
         if a[i]>curr:
            if ans == -1:
               ans = curr
               index = i
            else:
               ans = min(ans,a[i])
               index = i
      return index
ob1 = Solution()
print(ob1.nextPermutation([1,2,3]))


# In[16]:


class Solution(object):
   def nextPermutation(self, nums):
      found = False
      i = len(nums)-2
      while i >=0:
         if nums[i] < nums[i+1]:
            found =True
            break
         i-=1
      if not found:
         nums.sort()
      else:
         m = self.findMaxIndex(i+1,nums,nums[i])
         nums[i],nums[m] = nums[m],nums[i]
         nums[i+1:] = nums[i+1:][::-1]
      return nums
   def findMaxIndex(self,index,a,curr):
      ans = -1
      index = 0
      for i in range(index,len(a)):
         if a[i]>curr:
            if ans == -1:
               ans = curr
               index = i
            else:
               ans = min(ans,a[i])
               index = i
      return index
ob1 = Solution()
print(ob1.nextPermutation([3,2,1]))


# # Q4. Given two arrays a[] and b[] of size n and n resp. The task is to find union between these two arrays.

# In[17]:


a1 = [5,3]
b2 = [1,2,3,4,5]
c1 = [1,2,3]
    
def doUnion( a, n, b, m, c, k):
     
    hs = set()
    for i in range(0, n):
        hs.add(a[i])

    for i in range(0, m):
        hs.add(b[i])

    for i in range(0, k):
        hs.add(c[i])

    return len(hs)
print(doUnion(a1,2,b2,5,c1,3))


# In[18]:


a1 = [6,2]
b2 = [85,25,1,32,54,6]
c1 = [85,2]

def doUnion( a, n, b, m, c, k):

    hs = set()

    for i in range(0, n):
        hs.add(a[i])

    for i in range(0, m):
        hs.add(b[i])

    for i in range(0, k):
        hs.add(c[i])

    return len(hs)
print(doUnion(a1,2,b2,6,c1,2))


# In[ ]:




