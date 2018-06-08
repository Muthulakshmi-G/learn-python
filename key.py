



def parrot(voltage,state=' a stiff',action='voom',type='norwegian blue'):
    print("--this parrot wouldnot",action,end='')
    print("if u put",voltage,"volts through it")
    print("lovely plumage,the",type)
    print("it is",state,"!")


parrot(1000)
parrot(voltage=1000)
parrot(voltage=100000,action='voooom')


def painting(colors,brush="12 brushes",pencil=3,sheet="long size"):
    print("i have 3 colors which are",colors)
    print("\nthe brushes i have ",brush)
    print("\ni have {} type of pencils,".format(pencil))
    print("\n{} is enough to draw tree".format(sheet))

painting('red')
painting('blue','10 brushee','4')

parrot(110)



def cheeseshop(kind,*arguments,**keywords):
    print("--do u have any",kind,"?")
    print("im sorry,we are all out of")
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw,":",keywords[kw])


cheeseshop("burger","it is very runny","it is really very,very funny",shopkeeper="paul",client="john",sketch="cheese shop sketch")

