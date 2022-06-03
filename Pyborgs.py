
from graphics import *
from buttonclass import *
from pyborgclass import *
from random import*
from audioplayer import*
import time

def main():

    win = GraphWin("Pyborgs", 700, 700)
    win.setCoords(0,0,100,100)
    win.setBackground("black")

    intro=Text(Point(50,80),"A new species called 'pyborgs' have been created in a lab to test conditions of different planets")
    intro2=Text(Point(50,78),"This program shows how they evolve in the ecosystems of different planets based on the planets")
    intro3=Text(Point(50,76),"mass (gravity), average tempurature, amount of water, light exposure, and most prominent color")
    intro4=Text(Point(50,76),"click anywhere to get started")
    intro.setTextColor("gold")
    intro2.setTextColor("gold")
    intro3.setTextColor("gold")
    intro.draw(win)
    intro2.draw(win)
    intro3.draw(win)

    win.getMouse()
    
    intro.undraw()
    intro2.undraw()
    intro3.undraw()

#simple graphics to introduce the user to the program

    def makeDNA(lst):

#creates new random DNA for a pyborg object
        
        for n in range(5):
            lst.append(str(randrange(10)))
        return lst
        
    py1=pyborg(makeDNA([]),randrange(2,6),randrange(10,15),win)
    py1.traits()
    py1.drawBorg()

    py2=pyborg(makeDNA([]),randrange(11,15),randrange(10,15),win)
    py2.traits()
    py2.drawBorg()

    py3=pyborg(makeDNA([]),randrange(21,25),randrange(10,15),win)
    py3.traits()
    py3.drawBorg()

    py4=pyborg(makeDNA([]),randrange(33,37),randrange(10,15),win)
    py4.traits()
    py4.drawBorg()

    py5=pyborg(makeDNA([]),randrange(44,48),randrange(10,15),win)
    py5.traits()
    py5.drawBorg()

    py6=pyborg(makeDNA([]),randrange(53,57),randrange(10,15),win)
    py6.traits()
    py6.drawBorg()

    py7=pyborg(makeDNA([]),randrange(62,66),randrange(10,15),win)
    py7.traits()
    py7.drawBorg()

    py8=pyborg(makeDNA([]),randrange(71,75),randrange(10,15),win)
    py8.traits()
    py8.drawBorg()

    py9=pyborg(makeDNA([]),randrange(80,84),randrange(10,15),win)
    py9.traits()
    py9.drawBorg()

    py10=pyborg(makeDNA([]),randrange(89,93),randrange(10,15),win)
    py10.traits()
    py10.drawBorg()

    borgs=[py1,py2,py3,py4,py5,py6,py7,py8,py9,py10]

#creating pyborg objects an adding them to a list

    planetName=''
    planetnames=['Earth','Zorbex','Tatooine','Sheen','Kamino']
    planets=[]
    p1=planet('none',win)
    for p in planetnames:
        p1=planet(p,win)
        planets.append(p1)
        
    descheight=100
    desc=Text(Point(0,0),'')

#a few variable and list initializations that will help later on

    def drawDesc(planets,descheight,desc,win):

#this function draws the description of each planet, is helpful to redraw on top of new graphics objects when the planet is changed
        
        for p in planets:
            descheight-=2.5
            desc=Text(Point(30,descheight),p.planetDesc()[0])
            descheight-=2.5
            desc2=Text(Point(23,descheight),p.planetDesc()[1])
            desc.setTextColor("purple")
            desc2.setTextColor("purple")
            desc.setStyle('bold')
            desc2.setStyle('bold')
            desc.draw(win)
            desc2.draw(win)

    drawDesc(planets,descheight,desc,win)

    planetEntry=Entry(Point(85,85),12)
    planetEntry.draw(win)

    entryPrompt1=Text(Point(80.5,97.5),"enter the name of a planet exactly as it's listed on the")
    entryPrompt2=Text(Point(80.5,96),"left side of the screen, then press go to travel there!")
    entryPrompt1.setSize(10)
    entryPrompt1.setStyle('bold')
    entryPrompt1.setFill('purple')
    entryPrompt1.draw(win)
    entryPrompt2.setSize(10)
    entryPrompt2.setStyle('bold')
    entryPrompt2.setFill('purple')
    entryPrompt2.draw(win)

    planetGo=Button(win,Point(85, 75),12,6,"GO")

    reproduceBtn=Button(win,Point(85, 65),12,6,"reproduce")

    rerrormsg=Text(Point(50,50),"reproduction cannot happen until a planet has been chosen!")
    rerrormsg.setTextColor("red")

    perrormsg=Text(Point(50,50),"there is no planet that matches the name you entered!")
    perrormsg.setTextColor("red")

    randomizeBtn=Button(win,Point(85, 55),12,6,"randomize")

    quitBtn=Button(win,Point(85, 45),12,6,"quit")

    scorelist=[]
    survivor=0
    survivorlist=[]

#some button objects, error messages, planet entry box, and some lists and variables to help later on

    def randomize(borgs):

#this function randomizes the borgs in the same way as when they are first initialized

        for b in borgs:
            b.changeDNA(makeDNA([]))
            b.undrawBorg()
            b.traits()
            b.drawBorg()

    def reproduce(borgs,cPlanet,scorelist,survivorlist):
        
#this function will run when the reprouce button is clicked, it takes the DNA
#from the top scoring pyborgs and uses it to generate new traits (the pyborg objects are recycled)
        
        DNAind0list=[]
        DNAind1list=[]
        DNAind2list=[]
        DNAind3list=[]
        DNAind4list=[]

#each of these lists will include the gene at a specific index of each of the 5 top scoring pyborgs

        DNAindlistlist=[DNAind0list,
                        DNAind1list,
                        DNAind2list,
                        DNAind3list,
                        DNAind4list]
        scorelist=[]
        survivorlist=[]
        for b in borgs:
            score=b.scoreBorg(cPlanet.getStats())
            scorelist.append(score)

#scoring each pyborg for fitness on the current planet
    
        for s in range(5):
            survivor=scorelist.index(max(scorelist))
            scorelist[survivor]=-100
            survivorlist.append(survivor)

#compiling the indexes of the highest scoring pyborgs
            
        for s in survivorlist:
            for l in DNAindlistlist:
                l.append(borgs[s].getDNA()[DNAindlistlist.index(l)])

#adding the genes from the top scoring pyborgs to the DNAind lists
                
        for b in borgs:
            DNAlist=[str(DNAind0list[randrange(5)]),str(DNAind1list[randrange(5)]),str(DNAind2list[randrange(5)]),
                     str(DNAind3list[randrange(5)]),str(DNAind4list[randrange(5)])]
            b.changeDNA(DNAlist)
            mutantnum=randrange(10)
            if mutantnum==9:
                mutindex=randrange(5)
                DNAlist[mutindex]=str(randrange(10))
                b.changeDNA(DNAlist)
            b.undrawBorg()
            b.traits()
            b.drawBorg()

#randomly choosing these genes from each list, and using them to create "new" pyborgs, also a 1 in 10 chance for mutation of a gene

    def gobtnclick(entry,planetnames,perrormsg,borgs,cPlanet,win):

#this function checks if there is a valid entry for a planet, then if there is changes the planet
        
        if entry not in planetnames:
            perrormsg.draw(win)
            time.sleep(3)
            perrormsg.undraw()

#error message for entry that doesn't match any planets
            
        else:
            nPlanet=planet(entry,win)
            win.setBackground(nPlanet.getBackground())
            for i in nPlanet.getLandscape():
                i.draw(win)
            for b in borgs:
                b.undrawBorg()
                b.drawBorg()
            return nPlanet

#new planet!

        
    pt=win.getMouse()
    pl=False
    cPlanet=planet('cPlanet',win)
    while not quitBtn.clicked(pt):
        if randomizeBtn.clicked(pt):
            randomize(borgs)
        if planetGo.clicked(pt):
            if planetEntry.getText() in planetnames:
                cPlanet.leaveLandscape()
            cPlanet=gobtnclick(planetEntry.getText(),planetnames,perrormsg,borgs,cPlanet,win)
            if planetEntry.getText() in planetnames:
                pl=True
                startSound('boing2.wav', asyncPlay=True, loop=False)
                drawDesc(planets,descheight,desc,win)
        elif reproduceBtn.clicked(pt):
            if pl==True:
                reproduce(borgs,cPlanet,scorelist,survivorlist)
            else:
                rerrormsg.draw(win)
                time.sleep(3)
                rerrormsg.undraw()
        pt=win.getMouse()
    win.close()
            
#add prompt, sound effect, and notes to code        
main()




