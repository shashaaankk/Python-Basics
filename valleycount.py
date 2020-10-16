'''
An avid hiker keeps meticulous records of their hikes. During the last hike that
 took exactly "STEPS" steps, for every step it was noted if it was an uphill,"U"
 , or a downhill,"D" step.Hikes always start and end at sea level, and each step
  up or down represents a  unit change in altitude. We define the following terms:
A mountain is a sequence of consecutive steps above sea level, starting with a
step up from sea level and ending with a step down to sea level.A valley is a
sequence of consecutive steps below sea level, starting with a step down from
sea level and ending with a step up to sea level.
Sample Input
8
UDDDUDUU
Sample Output
1
'''
def countingValleys(steps, path):
    sealevel=0
    valley=0
    for step in path:
      if(step =="U"):
            sealevel+=1
      elif(step==" "):
          continue
      else:
         sealevel-=1
      if step == "U" and sealevel==0:
        valley+=1
        continue

    return valley
if __name__ == '__main__':

    steps = int(input().strip())

    path = input().strip()

    result = countingValleys(steps, path)

    print(result)
