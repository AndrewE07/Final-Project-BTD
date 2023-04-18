from graphics import *
from time import sleep as slp
win = GraphWin("MAP TEST", 1400, 766, autoflush=False)

m = Image(Point(600, 383), "MonkeyMeadows.png")
m.draw(win)

click = True
path = []
path.append(win.getMouse())

while click:
    if win.checkMouse() is not None:
        click = False
    cur = win.getCurrentMouseLocation()
    if (path[-1].getX() - 5 > cur.getX() or cur.getX() > path[-1].getX() + 5) or (path[-1].getY() - 5 > cur.getY() or cur.getY() > path[-1].getY() + 5):
        path.append(cur)
print(path)
# path = [Point(6.0, 318.0), Point(569.0, 307.0), Point(581.0, 285.0), Point(570.0, 147.0), Point(519.0, 136.0), Point(411.0, 147.0), Point(400.0, 165.0), Point(389.0, 194.0), Point(400.0, 383.0), Point(389.0, 525.0), Point(378.0, 565.0), Point(366.0, 586.0), Point(355.0, 597.0), Point(329.0, 608.0), Point(228.0, 597.0), Point(217.0, 585.0), Point(198.0, 573.0), Point(187.0, 561.0), Point(176.0, 474.0), Point(188.0, 456.0), Point(219.0, 444.0), Point(296.0, 433.0), Point(411.0, 444.0), Point(701.0, 433.0), Point(728.0, 422.0), Point(742.0, 410.0), Point(755.0, 394.0), Point(767.0, 264.0), Point(869.0, 275.0), Point(884.0, 286.0), Point(895.0, 306.0), Point(906.0, 372.0), Point(917.0, 429.0), Point(906.0, 505.0), Point(894.0, 537.0), Point(883.0, 558.0), Point(557.0, 569.0), Point(545.0, 592.0), Point(534.0, 656.0)]

for i in path:
    c = Image(i, "red_bloon_trans.png")
    c.draw(win)
    win.flush()
    slp(.1)
    c.undraw()
c = Image(Point(0, 0), "red_bloon_trans.png")
prevCurPos = None
mouseUnclick = False
while not False:
    curPos = None

    while mouseUnclick:
        win.update()
        curPos = win.getCurrentMouseLocation()
        print(curPos)
        if curPos is not prevCurPos and curPos is not None:
            c.undraw()
            c = Image(curPos, "red_bloon_trans.png")
            c.draw(win)
        slp(.00000001)

    prevCurPos = curPos


