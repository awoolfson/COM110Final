from graphics import *
from planetclass import *
from random import *

class pyborg:

#the pyborg object represents each creature in the program

    def __init__(self, dna, x, y, window):
        self.win=window
        self.name=str(self)
        self.dna=dna
        self.ox=x
        self.oy=y
        self.x=x
        self.y=y
        
        self.head=Polygon(Point(0,0),Point(1,1))
        self.hair=Polygon(Point(0,0),Point(1,1))
        
        self.buildnum=0
        self.build=Polygon(Point(0,0),Point(1,1))
        
        self.eye1=Polygon(Point(0,0),Point(1,1))
        self.eye2=Polygon(Point(0,0),Point(1,1))
        
        self.feet=''
        self.foot1=Polygon(Point(0,0),Point(1,1))
        self.foot2=Polygon(Point(0,0),Point(1,1))
        self.score=0
        self.furry= False
        self.fur=Polygon(Point(0,0),Point(1,1))

        #setting coordinates and initializing objects and variables to be used for traits and scoring


    def traits(self):

    #this method decides the traits of each pyborg based on the DNA
        
        self.head=Polygon(Point(self.x+6.5,self.y+17.7),Point(self.x+5.5,self.y+19.8),Point(self.x+4.5,self.y+17.7),Point(self.x+3.5,self.y+19.8),
             Point(self.x+2.5,self.y+17.7),Point(self.x+1.5,self.y+19.8),Point(self.x+.5,self.y+17.7),
             Point(self.x,self.y+20),Point(self.x,self.y+16),Point(self.x+2,self.y+14),Point(self.x+3,self.y+13.5),
             Point(self.x+4,self.y+13.5),Point(self.x+5,self.y+14),Point(self.x+7,self.y+16),Point(self.x+7,self.y+20))
        self.head.setFill("purple")
        self.hair=Polygon(Point(self.x,self.y+20),Point(self.x+1,self.y+21.4),Point(self.x+2,self.y+22),Point(self.x+3,self.y+22.3),
             Point(self.x+4,self.y+22.3),Point(self.x+5,self.y+22),Point(self.x+6,self.y+21.4),Point(self.x+7,self.y+20),#width of hair is 7
             Point(self.x+6.5,self.y+17.7),Point(self.x+5.5,self.y+19.8),Point(self.x+4.5,self.y+17.7),Point(self.x+3.5,self.y+19.8),
             Point(self.x+2.5,self.y+17.7),Point(self.x+1.5,self.y+19.8),Point(self.x+.5,self.y+17.7))#length of hair is 4.6
        self.eye1=Circle(Point(self.x+1.5,self.y+17),.6)
        self.eye2=Circle(Point(self.x+5.5,self.y+17),.6)
        if int(self.dna[0]) < 2:
            self.hair.setFill('green')
            self.hairColor='green'
        elif 2 <= int(self.dna[0]) < 4:
            self.hair.setFill('gold')
            self.hairColor='gold'
        elif 4 <= int(self.dna[0]) < 6:
            self.hair.setFill('dark blue')
            self.hairColor='dark blue'
        elif 6 <= int(self.dna[0]) < 8:
            self.hair.setFill('blue')
            self.hairColor='blue'
        elif int(self.dna[0])==9:
            self.hair.setFill('tan')
            self.hairColor='tan'
        else:
            self.hair.setFill('red')
            self.hairColor='red'
        if int(self.dna[1]) < 3:
            self.buildnum=1
        elif 3 <= int(self.dna[1]) < 7:
            self.buildnum=2
        else:
            self.buildnum=3
        x=self.x
        y=self.y
        c=x+3.5
        n=self.buildnum
        self.build=Polygon(Point(c-.5,y+13.5),Point(c+.5,y+13.5),Point(c+n,y+12.5),Point(c+n*1.2,y+10),
                           Point(c+n*1.2,y+5),Point(c+n,y+2.5),Point(c+.5,y+1),Point(c-.5,y+1),Point(c-n,y+2.5),
                           Point(c-n*1.2,y+5),Point(c-n*1.2,y+10),Point(c-n,y+12.5))
        self.build.setFill('purple')
        if int(self.dna[2]) < 5:
            self.eye1.setFill('red')
            self.eye2.setFill('red')
        else:
            self.eye1.setFill('light blue')
            self.eye2.setFill('light blue')
        if int(self.dna[3]) < 5:
            self.feet='un'
            w=2
            wx=.3
        else:
            self.feet='webbed'
            w=3
            wx=0
        self.foot1=Polygon(Point(x+1.5,y+2),Point(x,y-2.5),Point(x+.75+wx,y-w+1),Point(x+1.5,y-2.5),
                           Point(x+2.25-wx,y-w+1),Point(x+3,y-2.5))
        self.foot1.setFill("purple")
        x+=4
        self.foot2=Polygon(Point(x+1.5,y+2),Point(x,y-2.5),Point(x+.75+wx,y-w+1),Point(x+1.5,y-2.5),
                           Point(x+2.25-wx,y-w+1),Point(x+3,y-2.5))
        self.foot2.setFill("purple")
        if int(self.dna[4]) < 5:
            self.furry= True
            x=self.x
            self.fur=Polygon(Point(c,y+7),Point(c-3.5,y+14.5),Point(c-2.5,y+13.5),Point(c-1.5,y+14.5),
                             Point(c-.85,y+13.5),Point(c+.85,y+13.5),Point(c+1.5,y+14.5),Point(c+2.5,y+13.5),
                             Point(c+3.5,y+14.5))
            self.fur.setFill(self.hairColor)
        else:
            self.furry= False
            self.fur=Polygon(Point(0,0))

            
    def drawBorg(self):  
        self.fur.draw(self.win)
        self.build.draw(self.win)
        self.head.draw(self.win)
        self.hair.draw(self.win)
        self.eye1.draw(self.win)
        self.eye2.draw(self.win)
        self.foot1.draw(self.win)
        self.foot2.draw(self.win)

    def undrawBorg(self):
        self.fur.undraw()
        self.build.undraw()
        self.head.undraw()
        self.hair.undraw()
        self.eye1.undraw()
        self.eye2.undraw()
        self.foot1.undraw()
        self.foot2.undraw()
        self.x+=randrange(-2,2)
        self.y+=randrange(-3,3)
        if (self.ox-self.x)>3:
            self.x=self.ox
        if (self.oy-self.y)>5 or self.y>20:
            self.y=self.oy
    #these methods draw and undraw the pyborg objects, the undraw has a few conditionals to keep them from floating into the air or hiding behind eachother
            

    def getScore(self):
        return self.score

    def getDNA(self):
        return self.dna

    def changeDNA(self,dnaList):
        self.dna=''.join(dnaList)
        return self.dna

    #these methods get different attributes of the object
        
    def scoreBorg(self,pstats):

    #this method scores the pyborgs for fitness based off of the attributes of the planet they are on, and their traits
        
        self.score=0
        if pstats[0]>=20: #mass
            if self.buildnum==3:
                self.score-=15
            elif self.buildnum==2:
                self.score-=5
            else:
                self.score+=15                
        elif 20>pstats[0]>=10:
            if self.buildnum==3:
                self.score-=10
            elif self.buildnum==2:
                self.score=self.score
            else:
                self.score+=10               
        elif 10>pstats[0]>=4:
            if self.buildnum==3:
                self.score+=5
            elif self.buildnum==2:
                self.score+=10
            else:
                self.score-=5                
        else:
            if self.buildnum==3:
                self.score+=10
            elif self.buildnum==2:
                self.score+=5
            else:
                self.score-=10
                
        if pstats[1]>=90: #water
            if self.feet=='un':
                self.score-=10
            else:
                self.score+=15               
        elif 90>pstats[1]>=70:
            if self.feet=='un':
                self.score-=5
            else:
                self.score+=10            
        elif 70>pstats[1]>=40:
            self.score=self.score
        else:
            if self.feet=='un':
                self.score+=5
            else:
                self.score-=10

        if pstats[2]==3: #light
            if int(self.dna[2])<5: #red eyes
                self.score-=5
            else:
                self.score+=10
        elif pstats[2]==2:
            if int(self.dna[2])<5:
                self.score+=5
            else:
                self.score=self.score
        elif pstats[2]==1:
            if int(self.dna[2])<5:
                self.score+=10
            else:
                self.score=self.score

        if pstats[3]==self.hairColor: #color
            self.score+=15
        else:
            self.score-=5

        if 70>pstats[4]>50:
            if self.furry==True:
                self.score-=5
        elif pstats[4]>70:
            if self.furry==True:
                self.score-=10
            else:
                self.score+=5
        elif 50>pstats[4]>30:
            if self.furry==True:
                self.score+=10
        elif 30>pstats[4]:
            if self.furry==True:
                self.score+=15
            else:
                self.score-=5
        return self.score




    





        

