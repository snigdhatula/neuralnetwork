#!/usr/bin/env python
# coding: utf-8

# In[1]:


s_str=input()
if(len(s_str))>=2:
    s_str=s_str[2:]
s_str=s_str[::-1]
print(s_str)


# In[2]:


num1=int(input())
num2=int(input())
print("Addition: ",(num1+num2));
print("substraction: ",(num1-num2));
print("Multiplication: ",(num1*num2));
print("Division: ",(num1//num2));
print("Percentile: ",(num1%num2));


# In[3]:


input_str=input()
input_str=input_str.replace("python","pythons")
print(input_str)
        


# In[4]:


score=int(input("Enter your score to get grade out of 100"))
if score>=90 and score<=100:
    print("Your Grade is A")
elif score>=80 and score<=89:
     print("Your Grade is B")
elif score>=70 and score<=79:
     print("Your Grade is C")
elif score>=60 and score<=69:
     print("Your Grade is D")
else:
     print("Your Grade is F")


# In[ ]:




