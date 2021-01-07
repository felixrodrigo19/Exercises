def list_stats(lists):
  mean = sum(lists)/len(lists)
  listss = sorted(lists)
  x = (len(listss)-1)//2
  if (len(listss) % 2):
    median= listss[x]
  else:
    median= (listss[x]+listss[x+1])/2
    
  return median,mean
  


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)
