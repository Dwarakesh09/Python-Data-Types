# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wMbGmDwRtUB-e6fCVzk0CwLdeeMiYypP
"""

def trace_data_types(data_item):
  #print the original data item
  print("Original Data Item:",data_item)

  #use buit-in function and trace the type
  result = None

  if isinstance(data_item,int):
    result = data_item+10
    print("Type:int")
  elif isinstance(data_item,float):
    result = data_item*2
    print("Type:float")
  elif isinstance(data_item,str):
    result = data_item.upper()
    print("Type:str")
  elif isinstance(data_item,list):
    result = len(data_item)
    print("Type:list")
  elif isinstance(data_item,dict):
    result = list(data_item.key())
    print("Type:dict")
  else:
    print("Type:Unknown")

    #print the result after applying built-in function
    print("Result after applying built-in function:",result)
    print()

    #Test the program with different data types
    trace_data_types(5)
    trace_data_types(3.14)
    trace_data_types("hellow")
    trace_data_types([1,2,3,4])
    trace_data_types({"a":1,"b":2,"c":3,})
    trace_data_types(True)#This will fall into the "Unknown" category
