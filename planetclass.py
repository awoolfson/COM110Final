from graphics import *

class planet:

#this class is used to simulate different planet's environments for the pyborg species in the pyborgs program
    
    def __init__(self,name,window):
        self.win=window
        self.name=name
        self.mass=0
        self.temp=0
        self.water=0
        self.light=0
        self.color='' #planet stats for scoring pyborgs^
        self.landscape=[]
        self.background='black'
        self.l0,self.l1,self.l2,self.l3,self.l4=Polygon(Point(0,0),Point(1,1)),Polygon(Point(0,0),Point(1,1)),Polygon(Point(0,0),Point(1,1)),Polygon(Point(0,0),Point(1,1)),Polygon(Point(0,0),Point(1,1))
        if name=='Earth': #all of the attributes of earth being used follow
            self.water=70 #% surface covered in water
            self.mass=5.972 #x10^24 kg
            self.temp=65 #f
            self.light=2 #non shaded land areas,scored in abundance from 1-3, also could be influenced
                         #by other factors like number of suns
            self.color='green' #common color on land
            #earth is designed to be untouched by human civilizaton here, but
            #in it's current geological state
            self.background='light blue' #color of the sky
            self.l0,self.l1,self.l2,self.l3=Rectangle(Point(0,0),Point(100,25)),Circle(Point(70,70),5),Circle(Point(20,50),30),Rectangle(Point(0,25),Point(50,80))#graphics objects for planet
            self.landscape=[self.l0,self.l1,self.l2,self.l3]
            self.landscape[0].setFill(self.color)
            self.landscape[1].setFill('gold')
            self.landscape[2].setFill('blue')
            self.landscape[3].setFill('light blue')
            self.landscape[3].setOutline('light blue')
            
        if name=='Zorbex':
            self.water=90 
            self.mass=3.22
            self.temp=40
            self.light=3
            self.color='blue'
            self.background='SlateBlue1'
            self.l0,self.l1,self.l2,self.l3,self.l4=Rectangle(Point(0,0),Point(100,25)),Circle(Point(70,70),7),Circle(Point(20,10),5),Circle(Point(65,10),7),Circle(Point(40,15),7)
            self.landscape=[self.l0,self.l1,self.l2,self.l3,self.l4]
            self.landscape[0].setFill(self.color)
            self.landscape[1].setFill('gold')
            self.landscape[2].setFill('light blue')
            self.landscape[3].setFill('light blue')
            self.landscape[4].setFill('light blue')

        if name=='Tatooine':
            self.water=0
            self.mass=5.471
            self.temp=90
            self.light=3
            self.color='gold'
            self.background='sky blue'
            self.l0,self.l1,self.l2=Rectangle(Point(0,0),Point(100,25)),Circle(Point(70,70),5),Circle(Point(55,55),5)
            self.landscape=[self.l0,self.l1,self.l2]
            self.landscape[0].setFill(self.color)
            self.landscape[1].setFill('sienna1')
            self.landscape[2].setFill('sienna1')

        if name=='Sheen':
            self.water=50
            self.mass=2.11
            self.temp=70
            self.light=2
            self.color='tan'
            self.background='sky blue'
            self.l0,self.l1=Rectangle(Point(0,0),Point(100,25)),Circle(Point(70,70),5)
            self.landscape=[self.l0,self.l1]
            self.landscape[0].setFill(self.color)
            self.landscape[1].setFill('gold')

        if name=='Kamino':
            self.water=100
            self.mass=12.548
            self.temp=50
            self.light=1
            self.color='dark blue'
            self.background='dark slate gray'
            self.l0,self.l1,self.l2,self.l3=Rectangle(Point(0,0),Point(100,25)),Circle(Point(70,70),5),Circle(Point(55,55),5),Circle(Point(50,70),5)
            self.landscape=[self.l0,self.l1,self.l2,self.l3]
            self.landscape[0].setFill(self.color)
            self.landscape[1].setFill('light blue')
            self.landscape[2].setFill('light blue')
            self.landscape[3].setFill('light blue')

    def leaveLandscape(self):
        
        #gets rid of graphics objects from previous planet after traveling
        
        self.l0.undraw()
        self.l1.undraw()
        self.l2.undraw()
        self.l3.undraw()
        self.l4.undraw()

    def planetDesc(self):
        
        #allows for efficient writing of descriptions in window without making each individual text object
        
        if self.light==1:
            light='low'
        elif self.light==2:
            light='medium'
        else:
            light='high'
        planetDesc=str(self.name+': % surface water: '+str(self.water)+'%, mass: '+str(self.mass)+'x10^24 kg, tempurature: '+str(self.temp)+' F')
        planetDesc2=str('light exposure: '+light+', most prominent color: '+self.color)
        return [planetDesc,planetDesc2]

    def getLandscape(self):
        return self.landscape

    def getBackground(self):
        return self.background

    def getName(self):
        return self.name

    def getWater(self):
        return self.water

    def getTemp(self):
        return self.temp

    def getMass(self):
        return self.mass

    def getLight(self):
        return self.light

    def getColor(self):
        return self.color

    def getStats(self):
        return [self.getMass(),self.getWater(),self.getLight(),self.getColor(),self.getTemp()]

    #each of these return a different attribute of a planet, getStats is used for
        
    
