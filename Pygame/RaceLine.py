import pygame

class RaceLine:
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
def getRaceLines():
    goals = []
    
    line2 = RaceLine(65,230,90,350)
    line3 = RaceLine(90,350,120,400)
    line3_5 = RaceLine(120,400,180,440)
    line4 = RaceLine(180,440,280,450)
    line5 = RaceLine(280,450,325,450)
    line5_2 = RaceLine(325,450,400,450)
    line5_3 = RaceLine(400,450,500,450)
    line5_4 = RaceLine(500,450,580,450)
    line6 = RaceLine(580,450,660,430)
    line7 = RaceLine(660,430,700,410)
    line8 = RaceLine(700,410,715,390)
    line9 = RaceLine(715,390,730,350)
    line10 = RaceLine(730,350,725,310)
    line11 = RaceLine(725,310,700,270)
    line12 = RaceLine(700,270,665,250)
    line13 = RaceLine(665,250,600,230)
    line14 = RaceLine(600,230,510,210)
    line15 = RaceLine(510,210,460,190)
    line16 = RaceLine(460,190,380,123)
    line17 = RaceLine(380,123,320,70)
    line18 = RaceLine(320,70,230,40)
    line19 = RaceLine(230,40,150,55)
    line20 = RaceLine(150,55,110,70)
    line21 = RaceLine(110,70,80,105)
    line22 = RaceLine(80,105,65,150)
    line1 = RaceLine(65,150,65,230)
    

    #goals.append(line1)
    goals.append(line1)
    goals.append(line22)
    goals.append(line21)
    goals.append(line20)
    goals.append(line19)
    goals.append(line18)
    goals.append(line17)
    goals.append(line16)
    goals.append(line15)
    goals.append(line14)
    goals.append(line13)
    goals.append(line12)
    goals.append(line11)
    goals.append(line10)
    goals.append(line9)
    goals.append(line8)
    goals.append(line7)
    goals.append(line6)
    goals.append(line5_4)
    goals.append(line5_3)
    goals.append(line5_2)
    goals.append(line5)
    goals.append(line4)
    #goals.append(line3_5)
    #goals.append(line3)
    #goals.append(line2)
    

    goals[len(goals)-1].isactiv = True

    return(goals)
