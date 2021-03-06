from psychopy import visual, core, gui, event, data
from random import sample
from itertools import product, chain,  islice
from  csvtest import  cue_order, CSIs, ProbeTypes, ProbeType2s, CSI2s,  cat1, cat2, sz, thisIndex
from setstim import downs, ups, color,col_a, col_b, pos
FEEDBACK = []
sz = []#setsize, determine how many squares need to present
ProbeType2 = []
CSI2 = []
ProbeTypes = []
CSI = []
cue = []
thisN = []
thisIndex = []
col_a =[]# col_a -> top 4 squares
color = []
col_b = []#col_b -> down 4 squares
ups = []#top 4 positions
pos = []#all position
downs = []#down 4 position
cat1 =[]
cat2 = []
cue_order = []
FEEDBACK = []
expInfo = {'ID': '', 'age': '', 'gender': ['Male', 'Female'], 'block': ''}
# dlg = gui.DlgFromDict(dictionary=expInfo, title='VWM Task', order=['ID', 'age', 'block'])
# if dlg.OK:
#    toFile('lastParams.pickle', expInfo)  # save params to file for next time
# else:
#    core.quit()  # the user hit "cancel" so exit
WIN = visual.Window((1366, 800), color="grey", units="pix", fullscr=False)
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=40,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',
                            color='white')
FIX = visual.TextStim(WIN, text='+', height=120, color='white', pos=(0, 0))
FEEDBACK_O = visual.TextStim(
    WIN, pos=(0, 4), height=30, text='CORRECT!', color='white')
FEEDBACK_X = visual.TextStim(
    WIN, pos=(0, 4), height=30, text='INCORRECT!', color='white')
phase = visual.TextStim(win=WIN, text='Practice block.\nPress the "Space" key to continue.', pos=(0, 6), height=0.8)
instr = visual.TextStim(win=WIN,text='Remmber position and color,\nif color belong same frame, press "Left",otherwise color belong diifent frame, press"Right".\n Press "space" to continue.', pos=(0, 4), height=0.8)
practice = visual.TextStim(win=WIN,text='This is the practice block.\n''Make judgment if color appear belong same frame.Press "Left",/n color appears in different frame, please press "Right".''Now press the "Space" key to start practice block.', pos=(0, -2), height=0.8)
col_new = []
COLORS = [(0, 230, 115),(255, 128, 0), (128, 0, 128), (0, 100, 0), (139, 69, 19) ,(255, 182, 193), (222, 184, 135), (255, 140, 0), (0, 102, 102), (107, 142, 35) ,(0, 128, 128)]
def process(downs, ups, color, cue_order, CSI, ProbeType, ProbeType2, CSI2, col_a, col_b, pos, cat1, cat2, thisIndex,COLORS):
    global ans, rt,res,display_color
    col_new = list(set(COLORS) - set(color))
    learningPhase(color, pos, downs, ups, cue_order)
    core.wait(1)  # wait for 5000ms and erase them all]
    testingPhase(CSI, cat1, ProbeType, CSI2, cat2, ProbeType2, color, col_a, col_b, COLORS)

#process(downs, ups, color, cue_order, CSI, ProbeType, ProbeType2, CSI2, col_a, col_b, pos, cat1, cat2, thisIndex,COLORS)
    # FIX.draw()
    # WIN.flip()
    # core.wait(.5)

for i in range(5):
    process(sz = sz[i],downs = downs[i], ups = ups[i], color = color[i], cue_order = cue_order[i], CSI = CSIs[i], ProbeType = ProbeTypes[i], ProbeType2 = ProbeType2s[i], CSI2 = CSI2s[i], col_a = col_a[i], col_b = col_b[i], pos = pos[i], cat1 = cat1[i], cat2 = cat2[i],thisIndex = thisIndex[i])
    print color[i],pos[i]

def save_resp(ans, rt, display_color, ProbeType, CSI, FEEDBACK, thisIndex, sz):
    dataFile = open("%s.csv"%(expInfo['ID']+'_'+expInfo['age']+'_'+expInfo['block']), 'a')
    rt = str(rt)
    ans = str(ans)
    CSI = str(CSI)
    ProbeType = str(ProbeType)
    sz = str(sz)
    FEEDBACK = str(FEEDBACK)
    display_color = str(display_color)
    thisIndex = str(thisIndex)
    dataFile.write(ans + ','+ rt +',' +display_color +','+ ProbeType +','+ CSI +','+ FEEDBACK +',' +thisIndex +','+ sz+'\n')
def get_ans(ans,res):
    if res == 0 and ans == ['left']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res == 1 and ans == ['right']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res == 2 and ans == ['right']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res == 0 and ans == ['right']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res == 1 and ans == ['left']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res == 2 and ans == ['left']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif ans == ['left''right'] and ans == ['right''left']:
        FEEDBACK.append('p')
    return FEEDBACK

def drawStimulus(color, pos, downs, ups, cue_order):
    drawLearningColors(color, pos,sz)
    drawLearningCues(downs, ups, cue_order)


def drawLearningColors(color, pos,sz):
    squares = []
    for i in range(2*sz):
        squ = visual.Rect(WIN, size=[100, 100], lineColor=None,fillColorSpace='rgb255')#,colorSpace = 'rgb255')
        squares.append(squ)
    for idx, squ in enumerate(squares):
        #print color[idx]
        squ.setFillColor(color[idx],'rgb255')
        squ.setPos(pos[idx])
        squ.draw()


def drawLearningCues(downs, ups, cue_order):  # make frame need seperately $ Lin: Failed to comprehence.
    if cue_order == 0:
        drawDiamondCue(positions=downs)
        drawCircleCue(positions=ups)
    else:
        drawDiamondCue(positions=ups)
        drawCircleCue(positions=downs)


def drawDiamondCue(positions):
    diam = []
    for j in range(len(positions)):
        dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
        diam.append(dim)
    for idx, dim in enumerate(diam):
        dim.setPos(positions[idx])
        dim.draw()


def drawCircleCue(positions):
    circle = []
    for j in range(len(positions)):
        cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
        circle.append(cir)
    for idx, cir in enumerate(circle):
        cir.setPos(positions[idx])
        cir.draw()


def drawTestingCue(CSI, cue):
    if cue == 0:
        cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
        cir.setPos([0, 0])
        cir.draw()
    elif cue == 1:
        dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
        dim.setPos([0, 0])
        dim.draw()
    WIN.flip()
    core.wait(CSI)


#put cue to cat1 or cat2 determine frame shape
def drawProbe(col_new, cue, res, col_a, col_b):
    squ = visual.Rect(WIN, size=[100, 100], lineColor=None, pos=[0, 0],fillColorSpace='rgb255')
    squ.setFillColor(display_color)#colorSpace = 'rgb255')
    squ.draw()
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['left', 'right'])
    t2 = core.getTime()
    return (ans, t2 - t1)

def getProbeColor(col_new, cue, ProbeType, col_a, col_b):
    col_positive = []
    col_intrusion = []
    if cue == 1:  # diamond circle
        col_positive = sample(col_b,1)[0]
        col_intrusion =  sample(col_a,1)[0]
    elif cue == 0:  # circle diamond
        col_positive = sample(col_a,1)[0]
        col_intrusion = sample(col_b,1)[0]
        if res == 0:
            display_color = col_positive
        elif res == 1:
            display_color = col_intrusion
        elif res == 2:
            display_color = sample(col_new,1)[0]


def showInstr():  # show instruction on screen
    instr.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])


def learningPhase(color, pos, downs, ups, cue_order):
    drawStimulus(color, pos, downs, ups, cue_order)
    WIN.flip()
    core.wait(5)


def recognitionPhase(CSI, cat1, ProbeType,col_new, col_a, col_b):
    cue = cat1
    drawTestingCue(CSI, cue)
    res=ProbeType
    display_color = getProbeColor(col_new, cat1, ProbeType, col_a, col_b)
    (ans, rt) = drawProbe(cat1, res, col_a, col_new, col_b)
    FEEDBACK = get_ans(ans,ProbeType)
    WIN.flip()
    core.wait(.8)
    FEEDBACK.pop()
    return ans, rt,display_color

def recognitionPhase2(CSI2, cat2, ProbeType2,col_new, col_a, col_b):
    FEEDBACK.pop()
    cue = cat2
    drawTestingCue(CSI2, cat2)
    res=ProbeType2
    display_color2 = getProbeColor(col_new, cat2, ProbeType2, col_a, col_b)
    (ans2, rt2) = drawProbe(cat2, ProbeType2, col_a, col_new, col_b)
    FEEDBACK = get_ans(ans,ProbeType2)
    WIN.flip()
    core.wait(.8)
    return ans2, rt2, display_color2


def testingPhase(CSI, cat1, ProbeType, CSI2, cat2, ProbeType2, color, col_a, col_b, col_new):
    recognitionPhase(CSI, cat1, ProbeType,col_new, col_a, col_b)
    save_resp(ans, rt, display_color, ProbeType, CSI,FEEDBACK, thisIndex, sz)
    recognitionPhase2(CSI2, cat2, ProbeType2,col_new, col_a, col_b)
    save_resp(ans2, rt, display_color2, ProbeType2, CSI2, FEEDBACK2, thisIndex, sz)



