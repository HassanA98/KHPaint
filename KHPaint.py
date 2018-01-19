#Hassan Arshad
#Paint Program
#Theme: Kingdom Hearts
from pygame import *
from math import *
from random import *
from glob import *
screen = display.set_mode((1120,840))
font.init()
init()

sp= 1

background = image.load("Pic\khw.jpg")
background = transform.scale(background,(1120,840))
screen.blit(background,(0,0))

#Draw the top part of the program
p = image.load("Pic/kh.png")
screen.blit(p,(415,0))

p = image.load("Pic/kk.png")
screen.blit(p,(20,20))

p = image.load("Pic/kk1.png")
screen.blit(p,(750,20))

running = True

#draws the canvas
canvas = Rect(210,80,680,510)
draw.rect(screen,(255,255,255),canvas)



#draws color selecter
colorWheel = image.load("Pic/color.png")
colorWheelRect= screen.blit(colorWheel,(850,640))

draw.rect(screen,(255,255,255),[1020,815,100,25])

color = (0,0,0) # color variable
size = 1 #size variable
lines = [] #variable used by polygon tool to remeber coordinates
stamps = 0 #decides which page of stamps is shown
stamp = ""

#Default tool is pencil
tool = "pencil"


#-----------------------------------------
w1 = Rect(32,426,76,74)
w2 = Rect(109,426,76,74)
w3 = Rect(32,501,76,74)
w4 = Rect(109,501,76,74)

draw.rect(screen,color,w1)
draw.rect(screen,color,w2)
draw.rect(screen,color,w3)
draw.rect(screen,color,w4)

w1s = image.load("Pic/w1.jpg")
w1s = transform.scale(w1s,(76,74))
screen.blit(w1s,(32,426))

w2s = image.load("Pic/w2.png")
w2s = transform.scale(w2s,(76,74))
screen.blit(w2s,(109,426))

w3s = image.load("Pic/w3.jpg")
w3s = transform.scale(w3s,(76,74))
screen.blit(w3s,(32,501))

w4s = image.load("Pic/w4.jpg")
w4s = transform.scale(w4s,(76,74))
screen.blit(w4s,(109,501))
#-------------------------------------------

#-----------------------------------------
so1 = image.load("Sound/f.png")
so1Rect = screen.blit(so1,(950,110))

so2 = image.load("Sound/r.png")
so2Rect = screen.blit(so2,(950,210))

so3 = image.load("Sound/p.png")
so3Rect = screen.blit(so3,(950,310))

so4 = image.load("Sound/s.png")
so4Rect = screen.blit(so4,(950,410))
#-------------------------------------------


#helps with draw stamps
def drawStamp(path):
    stamp = image.load(path)
    stamp = transform.scale(stamp,(75,75))
    return stamp

def getName():
    ans = ""
    arialFont = font.SysFont("Calibri", 16)
    back = screen.copy()        
    textArea = Rect(400,300,200,25) 
    
    pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
    n = len(pics)
    choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
    draw.rect(screen,(0,0,0),choiceArea)        
    draw.rect(screen,(0,0,0),choiceArea,1)        
    for i in range(n):
        txtPic = arialFont.render(pics[i], True, (255,255,255)) 
        screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))
        
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       
                    
        txtPic = arialFont.render(ans, True, (255,255,255))   
        draw.rect(screen,(0,0,0),textArea)        
        draw.rect(screen,(0,0,0),textArea,2)           
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans

#Text tool function
def getText():
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Calibri", 25)
    back = screen.copy()
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                
                if e.key == K_BACKSPACE:    # remove last letter
                    scre = screen.copy()
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    scre = screen.copy()
                    ans += e.unicode       # add character to ans
                    
        txtPic = arialFont.render(ans, True, color)
        screen.blit(back,(0,0))
        screen.blit(txtPic,(startx,starty))
        
        display.flip()
        
    screen.blit(back,(0,0))    
    return ans

#redraws stamps in widndow if one is selected
def getStamp(stamps):
    if stamps == 0:
        draw.rect(screen,(100,100,255),[30,124,154,302])
        s1 = Rect(32,126,76,74)
        s2 = Rect(109,126,76,74)
        s3 = Rect(32,201,76,74)
        s4 = Rect(109,201,76,74)
        s5 = Rect(32,276,76,74)
        s6 = Rect(109,276,76,74)
        s7 = Rect(32,351,76,74)
        s8 = Rect(109,351,76,74)
        
        draw.rect(screen,(255,255,255),s1)
        draw.rect(screen,(255,255,255),s2)
        draw.rect(screen,(255,255,255),s3)
        draw.rect(screen,(255,255,255),s4)
        draw.rect(screen,(255,255,255),s5)
        draw.rect(screen,(255,255,255),s6)
        draw.rect(screen,(255,255,255),s7)
        draw.rect(screen,(255,255,255),s8)

        s = drawStamp(("Stamps/1.png"))
        screen.blit(s,(32,126))
        
        s = drawStamp("Stamps/2.png")
        screen.blit(s,(109,126))
        
        s = drawStamp("Stamps/3.png")
        screen.blit(s,(32,201))
        
        s = drawStamp("Stamps/4.png")
        screen.blit(s,(106,198))
        
        s = drawStamp("Stamps/5.png")
        screen.blit(s,(32,276))
        
        s = drawStamp("Stamps/6.png")
        screen.blit(s,(109,276))
        
        s = drawStamp("Stamps/7.png")
        screen.blit(s,(32,351))
        
        s = drawStamp("Stamps/8.png")
        screen.blit(s,(109,351))
    if stamps == 1:
        draw.rect(screen,(100,100,255),[30,124,154,302])
        s9 = (32,126,76,74)
        s10 = (109,126,76,74)
        s11 = (32,201,76,74)
        s12 = (109,201,76,74)
        s13 = (32,276,76,74)
        s14 = (109,276,76,74)

        draw.rect(screen,(255,255,255),s9)
        draw.rect(screen,(255,255,255),s10)
        draw.rect(screen,(255,255,255),s11)
        draw.rect(screen,(255,255,255),s12)
        draw.rect(screen,(255,255,255),s13)
        draw.rect(screen,(255,255,255),s14)
        
        s = drawStamp(("Stamps/9.png"))
        screen.blit(s,(32,126))
        
        s = drawStamp("Stamps/10.png")
        screen.blit(s,(109,126))
        
        s = drawStamp("Stamps/11.png")
        screen.blit(s,(32,201))
        
        s = drawStamp("Stamps/12.png")
        screen.blit(s,(109,201))

        s = drawStamp("Stamps/13.png")
        screen.blit(s,(32,276))
        
        s = drawStamp("Stamps/14.png")
        screen.blit(s,(109,276))
        #-------------------------------------------------------
        draw.rect(screen,(255,255,255),[32,351,76,74])
        draw.rect(screen,(255,255,255),[109,351,76,74])

#---------------------------------------------------
#draws the arrows on top of the stamps windows
draw.rect(screen,(255,11,11),[32,90,76,36])
draw.rect(screen,(255,11,11),[109,90,76,36])
aright = image.load("Pic/ArrowRight.png")
aright = transform.scale(aright,(74,34))
aleft = image.load("Pic/ArrowLeft.png")
aleft = transform.scale(aleft,(74,34))
arightRect = screen.blit(aright,(110,91))
aleftRect = screen.blit(aleft,(33,91))

draw.rect(screen,(0,0,0),[22,603,756,216])
toolp = image.load("Pic/khb1.png")
toolp = transform.scale(toolp,(736,196))
screen.blit(toolp,(32,613))
#------------------------------------------------

#------------------------------------------
#Loads the images for tools
save = image.load("Tools/Save.png")
save = transform.scale(save,(61,83))
saveRect= screen.blit(save,(36,617))

pencil = image.load("Tools/Pencil.png")
pencil = transform.scale(pencil,(61,83))
pencilRect= screen.blit(pencil,(147,617))

eraser = image.load("Tools/Eraser.png")
eraser = transform.scale(eraser,(61,81))
eraserRect = screen.blit(eraser,(258,617))

spray = image.load("Tools/Spray.png")
spray = transform.scale(spray,(61,81))
sprayRect = screen.blit(spray,(369,617))

fill = image.load("Tools/Fill.png")
fill = transform.scale(fill,(61,81))
fillRect = screen.blit(fill,(480,617))

brush = image.load("Tools/Brush.png")
brush = transform.scale(brush,(61,81))
brushRect = screen.blit(brush,(591,617))

polygon = image.load("Tools/Polygon.png")
polygon = transform.scale(polygon,(61,81))
polygonRect = screen.blit(polygon,(702,617))

load = image.load("Tools/Load.png")
load = transform.scale(load,(61,83))
loadRect= screen.blit(load,(36,720))

rec = image.load("Tools/Rec.png")
rec = transform.scale(rec,(61,81))
recRect = screen.blit(rec,(147,720))

elp = image.load("Tools/Elp.png")
elp = transform.scale(elp,(61,81))
elpRect = screen.blit(elp,(258,720))

text = image.load("Tools/Text.png")
text = transform.scale(text,(61,81))
textRect = screen.blit(text,(369,720))

pick = image.load("Tools/Pick.png")
pick = transform.scale(pick,(61,81))
pickRect = screen.blit(pick,(480,720))

line = image.load("Tools/Line.png")
line = transform.scale(line,(61,81))
lineRect = screen.blit(line,(591,720))

clean = image.load("Tools/Clean.png")
clean = transform.scale(clean,(61,81))
cleanRect = screen.blit(clean,(702,720))
#----------------------------------------------

#function to redraw the tools after selecting one 
def drawTools():
    save = image.load("Tools/Save.png")
    save = transform.scale(save,(61,83))
    saveRect= screen.blit(save,(36,617))

    pencil = image.load("Tools/Pencil.png")
    pencil = transform.scale(pencil,(61,83))
    pencilRect= screen.blit(pencil,(147,617))

    eraser = image.load("Tools/Eraser.png")
    eraser = transform.scale(eraser,(61,81))
    eraserRect = screen.blit(eraser,(258,617))

    spray = image.load("Tools/Spray.png")
    spray = transform.scale(spray,(61,81))
    sprayRect = screen.blit(spray,(369,617))

    fill = image.load("Tools/Fill.png")
    fill = transform.scale(fill,(61,81))
    fillRect = screen.blit(fill,(480,617))

    brush = image.load("Tools/Brush.png")
    brush = transform.scale(brush,(61,81))
    brushRect = screen.blit(brush,(591,617))

    polygon = image.load("Tools/Polygon.png")
    polygon = transform.scale(polygon,(61,81))
    polygonRect = screen.blit(polygon,(702,617))

    load = image.load("Tools/Load.png")
    load = transform.scale(load,(61,83))
    loadRect= screen.blit(load,(36,720))

    rec = image.load("Tools/Rec.png")
    rec = transform.scale(rec,(61,81))
    recRect = screen.blit(rec,(147,720))

    elp = image.load("Tools/Elp.png")
    elp = transform.scale(elp,(61,81))
    elpRect = screen.blit(elp,(258,720))

    text = image.load("Tools/Text.png")
    text = transform.scale(text,(61,81))
    textRect = screen.blit(text,(369,720))

    pick = image.load("Tools/Pick.png")
    pick = transform.scale(pick,(61,81))
    pickRect = screen.blit(pick,(480,720))

    line = image.load("Tools/Line.png")
    line = transform.scale(line,(61,81))
    lineRect = screen.blit(line,(591,720))

    clean = image.load("Tools/Clean.png")
    clean = transform.scale(clean,(61,81))
    cleanRect = screen.blit(clean,(702,720))

#draw 'highlighted' tool picture
def drawToolsA(path,xcor,ycor):
    i = image.load(path)
    i = transform.scale(i,(61,81))
    screen.blit(i,(xcor,ycor))


while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:     #Helps out with Rec tool
            if e.button == 1:
               copy = screen.copy()
               startx,starty = e.pos
            if e.button == 1 and so1Rect.collidepoint(mx,my):
                sp += 1
                if sp > 3:
                    sp = 1
            elif e.button == 1 and so2Rect.collidepoint(mx,my):
                sp -= 1
                if sp <= 0:
                    sp = 1
            elif e.button == 1 and so3Rect.collidepoint(mx,my):
                if sp == 1:
                    mixer.music.load("Sound/1.mp3")
                    mixer.music.play()
                if sp == 2:
                    mixer.music.load("Sound/2.mp3")
                    mixer.music.play()
                if sp == 3:
                    mixer.music.load("Sound/3.mp3")
                    mixer.music.play()
            elif e.button == 1 and so4Rect.collidepoint(mx,my):
                mixer.music.stop()
                
            if e.button == 1 and canvas.collidepoint(mx,my) and tool == "polygon":   #First half of polygon tool
                lines.append((mx,my))                                                #
                draw.circle(screen,color,(mx,my),int(size/2))                        #
            if e.button == 1 and plusRect.collidepoint(mx,my): #increases the size variable of tools
               size += 1
               if size > 5: #maximum size = 5
                   size = 5
            if e.button == 1 and minusRect.collidepoint(mx,my): #decreases the size variable of tools
               size -= 1
               if size <= 0: #minimum size = 1
                   size = 1
            if e.button == 1 and aleftRect.collidepoint(mx,my):   #Used to change display of stamps window
                stamp = ""
                stamps = 0
                getStamp(0)
            if e.button == 1 and arightRect.collidepoint(mx,my):
                stamp = ""
                stamps = 1
                getStamp(1)
    #------------------Your Code Here------------------
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    print(mx,my)
    if tool == "":
        drawTools()
    #--------------------------------------------------------
    if stamps == 0 and stamp == "":
        draw.rect(screen,(100,100,255),[30,124,154,302])
        s1 = Rect(32,126,76,74)
        s2 = Rect(109,126,76,74)
        s3 = Rect(32,201,76,74)
        s4 = Rect(109,201,76,74)
        s5 = Rect(32,276,76,74)
        s6 = Rect(109,276,76,74)
        s7 = Rect(32,351,76,74)
        s8 = Rect(109,351,76,74)
        
        draw.rect(screen,(255,255,255),s1)
        draw.rect(screen,(255,255,255),s2)
        draw.rect(screen,(255,255,255),s3)
        draw.rect(screen,(255,255,255),s4)
        draw.rect(screen,(255,255,255),s5)
        draw.rect(screen,(255,255,255),s6)
        draw.rect(screen,(255,255,255),s7)
        draw.rect(screen,(255,255,255),s8)

        s = drawStamp(("Stamps/1.png"))
        screen.blit(s,(32,126))
        
        s = drawStamp("Stamps/2.png")
        screen.blit(s,(109,126))
        
        s = drawStamp("Stamps/3.png")
        screen.blit(s,(32,201))
        
        s = drawStamp("Stamps/4.png")
        screen.blit(s,(106,198))
        
        s = drawStamp("Stamps/5.png")
        screen.blit(s,(32,276))
        
        s = drawStamp("Stamps/6.png")
        screen.blit(s,(109,276))
        
        s = drawStamp("Stamps/7.png")
        screen.blit(s,(32,351))
        
        s = drawStamp("Stamps/8.png")
        screen.blit(s,(109,351))
    if stamps == 1 and stamp == "":
        draw.rect(screen,(100,100,255),[30,124,154,302])
        s9 = Rect(32,126,76,74)
        s10 = Rect(109,126,76,74)
        s11 = Rect(32,201,76,74)
        s12 = Rect(109,201,76,74)
        s13 = Rect(32,276,76,74)
        s14 = Rect(109,276,76,74)

        draw.rect(screen,(255,255,255),s9)
        draw.rect(screen,(255,255,255),s10)
        draw.rect(screen,(255,255,255),s11)
        draw.rect(screen,(255,255,255),s12)
        draw.rect(screen,(255,255,255),s13)
        draw.rect(screen,(255,255,255),s14)
        
        s = drawStamp(("Stamps/9.png"))
        screen.blit(s,(32,126))
        
        s = drawStamp("Stamps/10.png")
        screen.blit(s,(109,126))
        
        s = drawStamp("Stamps/11.png")
        screen.blit(s,(32,201))
        
        s = drawStamp("Stamps/12.png")
        screen.blit(s,(109,201))

        s = drawStamp("Stamps/13.png")
        screen.blit(s,(32,276))
        
        s = drawStamp("Stamps/14.png")
        screen.blit(s,(109,276))
        #-------------------------------------------------------
        draw.rect(screen,(255,255,255),[32,351,76,74])
        draw.rect(screen,(255,255,255),[109,351,76,74])
    #--------------------------------------------------------

    #------------------------------------------------------------
    #This series of if statements decides which stamp is selected
    if mb[0] == 1 and stamps == 0 and s1.collidepoint(mx,my):
        tool = ""
        getStamp(0)
        stamp = "1"
        draw.rect(screen,(100,100,255),[32,126,76,74])
        s = drawStamp(("Stamps/1.png"))
        screen.blit(s,(32,126))
    if mb[0] == 1 and stamps == 0 and s2.collidepoint(mx,my):
        tool = ""
        getStamp(0)
        stamp = "2"
        draw.rect(screen,(100,100,255),[109,126,76,74])
        s = drawStamp(("Stamps/2.png"))
        screen.blit(s,(109,126))
    if mb[0] == 1 and stamps == 0 and  s3.collidepoint(mx,my):
        tool = ""
        getStamp(0)
        stamp = "3"
        draw.rect(screen,(100,100,255),[32,201,76,74])
        s = drawStamp(("Stamps/3.png"))
        screen.blit(s,(32,201))
    if mb[0] == 1 and stamps == 0 and s4.collidepoint(mx,my):
        tool = ""
        getStamp(0)
        stamp = "4"
        draw.rect(screen,(100,100,255),[109,201,76,74])
        s = drawStamp(("Stamps/4.png"))
        screen.blit(s,(106,198))
    if mb[0] == 1 and stamps == 0 and s5.collidepoint(mx,my):
        tool = ""
        getStamp(0)
        stamp = "5"
        draw.rect(screen,(100,100,255),[32,276,76,74])
        s = drawStamp(("Stamps/5.png"))
        screen.blit(s,(32,276))
    if mb[0] == 1 and stamps == 0 and s6.collidepoint(mx,my):
        tool = ""
        getStamp(0)
        stamp = "6"
        draw.rect(screen,(100,100,255),[109,276,76,74])
        s = drawStamp(("Stamps/6.png"))
        screen.blit(s,(109,276))
    if mb[0] == 1 and stamps == 0 and s7.collidepoint(mx,my):
        tool = ""
        getStamp(0)
        stamp = "7"
        draw.rect(screen,(100,100,255),[32,351,76,74])
        s = drawStamp(("Stamps/7.png"))
        screen.blit(s,(32,351))
    if mb[0] == 1 and stamps == 0 and s8.collidepoint(mx,my):
        tool = ""
        getStamp(0)
        stamp = "8"
        draw.rect(screen,(100,100,255),[109,351,76,74])
        s = drawStamp(("Stamps/8.png"))
        screen.blit(s,(109,351))
#--------------------------------------------------------------
    if mb[0] == 1 and stamps == 1 and s9.collidepoint(mx,my):
        tool = ""
        getStamp(1)
        stamp = "9"
        draw.rect(screen,(100,100,255),[32,126,76,74])
        s = drawStamp(("Stamps/9.png"))
        screen.blit(s,(32,126))
    if mb[0] == 1 and stamps == 1 and s10.collidepoint(mx,my):
        tool = ""
        getStamp(1)
        stamp = "10"
        draw.rect(screen,(100,100,255),[109,126,76,74])
        s = drawStamp(("Stamps/10.png"))
        screen.blit(s,(109,126))
    if mb[0] == 1 and stamps == 1 and s11.collidepoint(mx,my):
        tool = ""
        getStamp(1)
        stamp = "11"
        draw.rect(screen,(100,100,255),[32,201,76,74])
        s = drawStamp(("Stamps/11.png"))
        screen.blit(s,(32,201))
    if mb[0] == 1 and stamps == 1 and s12.collidepoint(mx,my):
        tool = ""
        getStamp(1)
        stamp = "12"
        draw.rect(screen,(100,100,255),[109,201,76,74])
        s = drawStamp(("Stamps/12.png"))
        screen.blit(s,(109,201))
    if mb[0] == 1 and stamps == 1 and s13.collidepoint(mx,my):
        tool = ""
        getStamp(1)
        stamp = "13"
        draw.rect(screen,(100,100,255),[32,276,76,74])
        s = drawStamp(("Stamps/13.png"))
        screen.blit(s,(32,276))
    if mb[0] == 1 and stamps == 1 and s14.collidepoint(mx,my):
        tool = ""
        getStamp(1)
        stamp = "14"
        draw.rect(screen,(100,100,255),[109,276,76,74])
        s = drawStamp(("Stamps/14.png"))
        screen.blit(s,(109,276))
    #------------------------------------------------------------



    #------------------------------------------------------------
    #These series of if statements detemines which tool the cursor is hovering over
    #It then tells what tool it is
    if pencilRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Pencil",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif eraserRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Eraser",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif sprayRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Spray Can",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif fillRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Paint",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif brushRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Brush Tool",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif polygonRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Polygon",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif recRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Rectangle",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif elpRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Ellipse",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif textRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Text Tool",True,(0,0,0))
        screen.blit(txtPic,(1026,820))

    elif pickRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Pick Tool",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif lineRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Line Tool",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif cleanRect.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 18)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("New Canvas",True,(0,0,0))
        screen.blit(txtPic,(1026,820))
        
    elif saveRect.collidepoint(mx,my): #the save function
        paintFont = font.SysFont("Calibri", 25)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Save",True,(0,0,0))
        screen.blit(txtPic,(1026,818))

    elif loadRect.collidepoint(mx,my): # the load function
        paintFont = font.SysFont("Calibri", 25)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Load",True,(0,0,0))
        screen.blit(txtPic,(1026,818))
    else:
        paintFont = font.SysFont("Calibri", 20)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render("Off Canvas",True,(0,0,0))
        screen.blit(txtPic,(1026,820))


        

    #------------------------------------------------------------
    #These series of if statements decides which tool is selected
    if mb[0]==1 and pencilRect.collidepoint(mx,my):
        tool = "pencil"
        stamp = ""
        drawTools()
        drawToolsA("Tools/PencilA.png",147,617)
    elif mb[0]==1 and eraserRect.collidepoint(mx,my):
        tool = "erase"
        stamp = ""
        drawTools()
        drawToolsA("Tools/EraserA.png",258,617)
    elif mb[0]==1 and sprayRect.collidepoint(mx,my):
        tool = "spray"
        stamp = ""
        drawTools()
        drawToolsA("Tools/SprayA.png",369,617)
    elif mb[0]==1 and fillRect.collidepoint(mx,my):
        tool = "fill"
        stamp = ""
        drawTools()
        drawToolsA("Tools/FillA.png",480,617)
    elif mb[0]==1 and brushRect.collidepoint(mx,my):
        tool = "brush"
        stamp = ""
        drawTools()
        drawToolsA("Tools/BrushA.png",591,617)
    elif mb[0]==1 and polygonRect.collidepoint(mx,my):
        tool = "polygon"
        stamp = ""
        drawTools()
        drawToolsA("Tools/PolygonA.png",702,617)
    elif mb[2]==1 and recRect.collidepoint(mx,my):
        tool = "rec1"
        stamp = ""
        drawTools()
        drawToolsA("Tools/RecB.png",147,720)
    elif mb[0]==1 and recRect.collidepoint(mx,my):
        tool = "rec2"
        stamp = ""
        drawTools()
        drawToolsA("Tools/RecA.png",147,720)
    elif mb[2]==1 and elpRect.collidepoint(mx,my):
        tool = "elp1"
        stamp = ""
        drawTools()
        drawToolsA("Tools/ElpB.png",258,720)
    elif mb[0]==1 and elpRect.collidepoint(mx,my):
        tool = "elp2"
        stamp = ""
        drawTools()
        drawToolsA("Tools/ElpA.png",258,720)
    elif mb[0]==1 and textRect.collidepoint(mx,my):
        tool = "text"
        stamp = ""
        drawTools()
        drawToolsA("Tools/TextA.png",369,720)
    elif mb[0]==1 and pickRect.collidepoint(mx,my):
        tool = "pick"
        stamp = ""
        drawTools()
        drawToolsA("Tools/PickA.png",480,720)
    elif mb[0]==1 and lineRect.collidepoint(mx,my):
        tool = "line"
        stamp = ""
        drawTools()
        drawToolsA("Tools/LineA.png",591,720)
    elif mb[0]==1 and cleanRect.collidepoint(mx,my):
        canvas = Rect(210,80,680,510)
        draw.rect(screen,(255,255,255),canvas)
        
    elif mb[0]==1 and saveRect.collidepoint(mx,my): #the save function
        name = getName()
        image.save(screen.subsurface(canvas),(name+".bmp"))

    elif mb[0]==1 and loadRect.collidepoint(mx,my): # the load function
        screen.set_clip(canvas)
        name = getName()
        imag = image.load(name)
        screen.blit(imag,(210,90))
        screen.set_clip(None)

    #-----------------------------------------
    if mb[0] == 1 and w1.collidepoint(mx,my):
        w1s = image.load("Pic/w1.jpg")
        w1s = transform.scale(w1s,(680,510))
        screen.blit(w1s,(210,80))

    elif mb[0] == 1 and w2.collidepoint(mx,my):
        w2s = image.load("Pic/w2.png")
        w2s = transform.scale(w2s,(680,510))
        screen.blit(w2s,(210,80))

    elif mb[0] == 1 and w3.collidepoint(mx,my):
        w3s = image.load("Pic/w3.jpg")
        w3s = transform.scale(w3s,(680,510))
        screen.blit(w3s,(210,80))

    elif mb[0] == 1 and w4.collidepoint(mx,my):
        w4s = image.load("Pic/w4.jpg")
        w4s = transform.scale(w4s,(680,510))
        screen.blit(w4s,(210,80))
#-------------------------------------------
        
    #------------------------------------------------------- The color wheel and the color displayer...
    draw.circle(screen,color,(935,740),95)
    draw.circle(screen,color,(850,638),45)
    draw.circle(screen,color,(1020,638),45)
    colorWheelRect= screen.blit(colorWheel,(850,655))
    #-------------------------------------------------------

    #---------------------------------------------------------
    #draws the plus and minus which increase or decrease teh size variable
    s = image.load("Pic/Minus.png")
    s = transform.scale(s,(75,75))
    minusRect = screen.blit(s,(812,600))
    s = image.load("Pic/Plus.png")
    s = transform.scale(s,(75,75))
    plusRect = screen.blit(s,(982,600))
    #-------------------------------------------------------

    #------------------coordinate box--------------------
    #draw the coordinate box in the bottom right which displays the coordinates of the mouse relative
    #to the canvas
    cx = str(mx-216)
    cy = str(my-28)
    if canvas.collidepoint(mx,my):
        paintFont = font.SysFont("Calibri", 25)
        draw.rect(screen,(255,255,255),[1020,815,100,25])
        txtPic = paintFont.render((cx + "," + cy), True, (0,0,0))
        screen.blit(txtPic,(1028,816))
    #----------------------------------------------------

    if mb[0] == 1 and canvas.collidepoint(mx,my):
        screen.set_clip(canvas)
    #------------------pencil tool-----------------------
        if tool == "pencil":
            draw.line(screen,color,(omx,omy),(mx,my),size)
    #----------------------------------------------------

    #------------------color pick tool-------------------
        elif tool == "pick":
            color = screen.get_at((mx,my))
            draw.rect(screen,color,(5,5,10,10)) 
    #----------------------------------------------------

    #---------------------fill tool----------------------
        elif tool == "fill":
            oldcol = screen.get_at((mx,my))
            listfill = [(mx,my)]
            if oldcol != color:
                while len(listfill) != 0:
                    x,y = listfill.pop() 
                    if canvas.collidepoint(mx,my) and screen.get_at((x,y)) == oldcol:     
                        screen.set_at((x,y),color)
                        listfill+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]           
    #----------------------------------------------------

    #---------------------text tool----------------------
        elif tool == "text":
            txt = getText()
            txtPic = paintFont.render(txt, True, color)
            screen.blit(txtPic,(startx,starty))
            
    #----------------------------------------------------
            
    #-----------------spray tool-------------------------
        elif tool == "spray":
            for i in range(0,size+20):
                x = mx+randint((-1*size*10),size*10)
                y = my+randint((-1*size*10),size*10)
                dist = hypot(mx-x,my-y)
                if dist <= (size*10):
                    screen.set_at((x,y),color)
    #----------------------------------------------------
                    
    #-----------------erase tool-------------------------
        elif tool == "erase":
            dist = hypot(omx-mx,omy-my)
            draw.circle(screen,(255,255,255),(mx,my),size*2)
            if dist != 0:
                sx = (mx-omx)/dist
                sy = (my-omy)/dist
                for i in range(int(dist)):
                    draw.circle(screen,(255,255,255),(int(omx),int(omy)),size*2)
                    omx += sx
                    omy += sy
    #----------------------------------------------------
                    
    #-----------------brush tool-------------------------
        elif tool == "brush":
            dist = hypot(omx-mx,omy-my)
            draw.circle(screen,color,(mx,my),size+5)
            if dist != 0:
                sx = (mx-omx)/dist
                sy = (my-omy)/dist
                for i in range(int(dist)):
                    draw.circle(screen,color,(int(omx),int(omy)),size+5)
                    omx += sx
                    omy += sy
    #----------------------------------------------------
                    
    #------------------rectangle tool--------------------
        elif tool == "rec1":  #filled rectangle
            screen.blit(copy,(0,0))
            rec = Rect(startx,starty,mx-startx,my-starty)
            draw.rect(screen,color,rec)
        elif tool == "rec2":  #un-filled rectangle
            screen.blit(copy,(0,0))
            rec = Rect(startx,starty,mx-startx,my-starty)
            draw.rect(screen,color,rec,size)
    #----------------------------------------------------
            
    #-------------------ellipse tool---------------------
        elif tool == "elp1": #filled ellipse
            screen.blit(copy,(0,0))
            rec = Rect(startx,starty,mx-startx,my-starty)
            rec.normalize()
            draw.ellipse(screen,color,rec,0)
        elif tool == "elp2": #unfilled ellipse
            screen.blit(copy,(0,0))
            rec = Rect(startx,starty,mx-startx,my-starty)
            rec.normalize()
            if abs(mx-startx) > size*2 and abs(my-starty) > size*2:
                draw.ellipse(screen,color,rec,size)
    #----------------------------------------------------
            
    #----------------------line tool---------------------
        elif tool == "line":
            screen.blit(copy,(0,0))
            draw.line(screen,color,(startx,starty),(mx,my), size)
    #----------------------------------------------------

    #-----------------------stamps-----------------------
        if stamp == "1":
            st = image.load("Stamps/1.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "2":
            st = image.load("Stamps/2.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "3":
            st = image.load("Stamps/3.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "4":
            st = image.load("Stamps/4.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "5":
            st = image.load("Stamps/5.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "6":
            st = image.load("Stamps/6.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "7":
            st = image.load("Stamps/7.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "8":
            st = image.load("Stamps/8.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "9":
            st = image.load("Stamps/9.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "10":
            st = image.load("Stamps/10.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "11":
            st = image.load("Stamps/11.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "12":
            st = image.load("Stamps/12.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "13":
            st = image.load("Stamps/13.png")
            screen.blit(st,(mx-75,my-75))
        elif stamp == "14":
            st = image.load("Stamps/14.png")
            screen.blit(st,(mx-75,my-75))
    #----------------------------------------------------
        screen.set_clip(None)

    #---------------------polygon tool-------------------
    if len(lines) > 2 and mb[2] == 1 and canvas.collidepoint(mx,my) and tool == "polygon":
        for i in range(len(lines)):
            if i +1 >= len(lines):
                draw.line(screen,color,lines[0],lines[-1],size)
                lines = []
                break
            draw.line(screen,color,lines[i],lines[i+1],size)
    #----------------------------------------------------
            
    #-----------------color wheel----------------------
    if mb[0]==1 and colorWheelRect.collidepoint(mx,my):
        color = screen.get_at((mx,my))       
    #--------------------------------------------------
    omx,omy = mx,my #stores the old x and y coordinates of the cursor
    display.flip()
quit()
