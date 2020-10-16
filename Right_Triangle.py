sideOne=int(input("Enter a positive integer: "))
sideTwo=int(input("Enter a positive integer: "))
sideThree=int(input("Enter a positive integer: "))
try:
    if sideOne<=0 or sideTwo<=0 or sideThree<=0:
       print("INVALID INPUT")
except:
     if sideOne>sideTwo and sideOne>sideThree:
        hyp=sideOne
        otherSide1=sideTwo
        otherSide2=sideThree
     elif sideTwo>sideOne and sideTwo>sideThree:
        hyp=sideTwo
        otherSide1=sideOne
        otherSide2=sideThree
     else:
        hyp=sideThree
        otherSide1=sideOne
        otherSide2=sideTwo
     if (hyp*hyp)==(otherSide1*otherSide1)+(otherSide2*otherSide2):
        print("RIGHT ANGLED TRIANGLE")
     else:
        print("NOT A RIGHT ANGLED TRIANGLE")
