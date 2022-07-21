# Chapter 10 Excercises
# 10.2 Regular Expressions extract () brackets
import re
text='this is a (test) string how (fun)'
extracted=re.findall(r'\(.*?\)',text)
print(extracted)