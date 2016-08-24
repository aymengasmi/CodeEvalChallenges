import sys 
import itertools

with open(sys.argv[1], 'r') as test_cases:
  for line in test_cases:
      line = line.rstrip('\n')  
      stuff = sorted(line)
        
      irts = [''.join(item) for item in itertools.permutations(stuff, len(stuff))]
       

      for x in irts:  
          if irts.index(x) == len(irts)-1:  sys.stdout.write(x)
          else :
              sys.stdout.write(x)
              sys.stdout.write(",")
      print 