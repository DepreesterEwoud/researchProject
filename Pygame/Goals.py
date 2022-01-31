import pygame

class Goal:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.isactiv = False
    
    def draw(self, win):
        pygame.draw.line(win, (0,255,0), (self.x1, self.y1), (self.x2, self.y2), 2)
        if self.isactiv:
            pygame.draw.line(win, (255,0,0), (self.x1, self.y1), (self.x2, self.y2), 2)

# the file of shame
def getGoals():
    goals = []

    goal1 = Goal(0,200,120,200)
    goal2 = Goal(0,100,120,150)
    goal2_5 = Goal(0,0,150,130)
    goal3 = Goal(120,0,170,120)
    goal3_5 = Goal(200,0,200,120)
    goal4 = Goal(270,0,270,110)
    goal4_5 = Goal(350,0,300,110)
    goal5 = Goal(410,30,340,140)
    goal5_5 = Goal(470,80,360,180)
    goal6 = Goal(470,150,360,240)
    goal6_5 = Goal(500,150,420,270)
    goal7 = Goal(530,150,500,270)
    goal7_5 = Goal(560,150,560,270)
    goal8 = Goal(640,150,630,270)
    goal9 = Goal(750,200,660,300)
    goal9_5 = Goal(790,280,660,330)
    goal10 = Goal(790,350,660,350)
    goal10_5 = Goal(790,430,660,380)
    goal11 = Goal(720,490,600,380)
    goal12 = Goal(580,490,580,380)
    goal13 = Goal(500,490,500,380)
    goal14 = Goal(420,490,420,380)
    goal15 = Goal(350,490,350,380)
    goal16 = Goal(280,490,280,380)
    goal17 = Goal(200,490,200,380)
    goal18 = Goal(120,490,160,380)
    goal19 = Goal(60,420,160,320)
    goal19_5 = Goal(30,340,160,300)
    goal20 = Goal(30,260,160,260)

    goals.append(goal1)
    goals.append(goal2)
    goals.append(goal2_5)
    goals.append(goal3)
    goals.append(goal3_5)
    goals.append(goal4)
    goals.append(goal4_5)
    goals.append(goal5)
    goals.append(goal5_5)
    goals.append(goal6)
    goals.append(goal6_5)
    goals.append(goal7)
    goals.append(goal7_5)
    goals.append(goal8)
    goals.append(goal9)
    goals.append(goal9_5)
    #goals.append(goal10_5)
    goals.append(goal10)
    goals.append(goal11)
    goals.append(goal12)
    goals.append(goal13)
    goals.append(goal14)
    goals.append(goal15)
    goals.append(goal16)
    goals.append(goal17)
    goals.append(goal18)
    goals.append(goal19)
    goals.append(goal19_5)
    goals.append(goal20)

    goals[len(goals)-1].isactiv = True

    return(goals)
