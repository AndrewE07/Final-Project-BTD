import time
from graphics import *
path = [Point(-20, 320), Point(-10.0, 320.0), Point(0, 320), Point(4.0, 322.0), Point(21.0, 320.0), Point(33.0, 320.0),
        Point(45.0, 321.0), Point(56.0, 321.0), Point(68.0, 321.0), Point(81.0, 322.0), Point(92.0, 322.0),
        Point(105.0, 322.0), Point(116.0, 322.0), Point(128.0, 324.0), Point(139.0, 324.0), Point(152.0, 326.0),
        Point(165.0, 326.0), Point(178.0, 326.0), Point(189.0, 327.0), Point(200.0, 327.0), Point(212.0, 327.0),
        Point(224.0, 327.0), Point(237.0, 327.0), Point(253.0, 327.0), Point(266.0, 327.0), Point(277.0, 327.0),
        Point(289.0, 327.0), Point(301.0, 327.0), Point(312.0, 327.0), Point(324.0, 327.0), Point(336.0, 328.0),
        Point(348.0, 328.0), Point(359.0, 328.0), Point(371.0, 327.0), Point(383.0, 327.0), Point(394.0, 324.0),
        Point(407.0, 322.0), Point(418.0, 320.0), Point(429.0, 318.0), Point(440.0, 317.0), Point(451.0, 317.0),
        Point(466.0, 317.0), Point(478.0, 317.0), Point(491.0, 317.0), Point(502.0, 317.0), Point(513.0, 317.0),
        Point(527.0, 317.0), Point(538.0, 317.0), Point(550.0, 317.0), Point(562.0, 316.0), Point(573.0, 315.0),
        Point(584.0, 306.0), Point(588.0, 295.0), Point(591.0, 284.0), Point(595.0, 271.0), Point(598.0, 259.0),
        Point(598.0, 246.0), Point(598.0, 234.0), Point(596.0, 220.0), Point(593.0, 207.0), Point(590.0, 194.0),
        Point(589.0, 181.0), Point(589.0, 169.0), Point(588.0, 157.0), Point(584.0, 145.0), Point(572.0, 138.0),
        Point(561.0, 136.0), Point(549.0, 135.0), Point(538.0, 133.0), Point(527.0, 132.0), Point(514.0, 132.0),
        Point(500.0, 132.0), Point(488.0, 132.0), Point(477.0, 131.0), Point(466.0, 138.0), Point(454.0, 144.0),
        Point(442.0, 144.0), Point(430.0, 144.0), Point(419.0, 144.0), Point(408.0, 147.0), Point(398.0, 160.0),
        Point(392.0, 171.0), Point(388.0, 182.0), Point(382.0, 196.0), Point(382.0, 207.0), Point(382.0, 219.0),
        Point(382.0, 232.0), Point(383.0, 243.0), Point(386.0, 257.0), Point(389.0, 269.0), Point(390.0, 282.0),
        Point(394.0, 293.0), Point(398.0, 304.0), Point(398.0, 315.0), Point(398.0, 326.0), Point(398.0, 337.0),
        Point(397.0, 349.0), Point(395.0, 361.0), Point(395.0, 373.0), Point(393.0, 384.0), Point(393.0, 397.0),
        Point(393.0, 408.0), Point(394.0, 419.0), Point(394.0, 432.0), Point(394.0, 443.0), Point(396.0, 454.0),
        Point(397.0, 466.0), Point(401.0, 477.0), Point(401.0, 490.0), Point(401.0, 504.0), Point(398.0, 516.0),
        Point(395.0, 527.0), Point(395.0, 538.0), Point(394.0, 551.0), Point(391.0, 562.0), Point(388.0, 573.0),
        Point(381.0, 584.0), Point(369.0, 592.0), Point(358.0, 596.0), Point(347.0, 598.0), Point(335.0, 601.0),
        Point(321.0, 603.0), Point(309.0, 604.0), Point(296.0, 605.0), Point(283.0, 605.0), Point(271.0, 607.0),
        Point(257.0, 607.0), Point(245.0, 607.0), Point(232.0, 602.0), Point(221.0, 597.0), Point(205.0, 583.0),
        Point(193.0, 572.0), Point(187.0, 560.0), Point(184.0, 549.0), Point(184.0, 536.0), Point(186.0, 524.0),
        Point(187.0, 513.0), Point(191.0, 502.0), Point(194.0, 489.0), Point(196.0, 476.0), Point(196.0, 465.0),
        Point(197.0, 454.0), Point(209.0, 450.0), Point(220.0, 450.0), Point(235.0, 450.0), Point(248.0, 450.0),
        Point(261.0, 450.0), Point(273.0, 450.0), Point(285.0, 452.0), Point(297.0, 455.0), Point(309.0, 455.0),
        Point(323.0, 455.0), Point(334.0, 453.0), Point(348.0, 450.0), Point(360.0, 447.0), Point(371.0, 445.0),
        Point(385.0, 443.0), Point(398.0, 442.0), Point(410.0, 442.0), Point(423.0, 442.0), Point(435.0, 442.0),
        Point(451.0, 442.0), Point(466.0, 442.0), Point(478.0, 441.0), Point(490.0, 440.0), Point(502.0, 439.0),
        Point(514.0, 439.0), Point(529.0, 439.0), Point(540.0, 439.0), Point(552.0, 439.0), Point(564.0, 439.0),
        Point(576.0, 439.0), Point(588.0, 438.0), Point(608.0, 438.0), Point(620.0, 438.0), Point(634.0, 440.0),
        Point(651.0, 442.0), Point(662.0, 442.0), Point(675.0, 439.0), Point(688.0, 433.0), Point(702.0, 424.0),
        Point(717.0, 417.0), Point(729.0, 411.0), Point(739.0, 398.0), Point(752.0, 387.0), Point(759.0, 376.0),
        Point(762.0, 364.0), Point(764.0, 353.0), Point(764.0, 340.0), Point(764.0, 328.0), Point(764.0, 315.0),
        Point(762.0, 303.0), Point(761.0, 291.0), Point(759.0, 278.0), Point(768.0, 267.0), Point(780.0, 259.0),
        Point(792.0, 255.0), Point(803.0, 255.0), Point(814.0, 257.0), Point(826.0, 258.0), Point(839.0, 258.0),
        Point(850.0, 263.0), Point(862.0, 269.0), Point(873.0, 273.0), Point(882.0, 286.0), Point(895.0, 298.0),
        Point(901.0, 309.0), Point(906.0, 322.0), Point(907.0, 335.0), Point(910.0, 347.0), Point(910.0, 359.0),
        Point(909.0, 370.0), Point(906.0, 383.0), Point(905.0, 395.0), Point(902.0, 407.0), Point(902.0, 420.0),
        Point(902.0, 431.0), Point(902.0, 443.0), Point(902.0, 454.0), Point(899.0, 467.0), Point(897.0, 479.0),
        Point(893.0, 490.0), Point(891.0, 502.0), Point(887.0, 515.0), Point(885.0, 526.0), Point(878.0, 537.0),
        Point(867.0, 546.0), Point(856.0, 555.0), Point(843.0, 555.0), Point(830.0, 555.0), Point(819.0, 555.0),
        Point(808.0, 555.0), Point(794.0, 555.0), Point(780.0, 555.0), Point(769.0, 555.0), Point(758.0, 556.0),
        Point(746.0, 556.0), Point(734.0, 556.0), Point(722.0, 555.0), Point(709.0, 553.0), Point(698.0, 553.0),
        Point(686.0, 553.0), Point(674.0, 553.0), Point(663.0, 550.0), Point(650.0, 549.0), Point(638.0, 549.0),
        Point(626.0, 551.0), Point(613.0, 554.0), Point(602.0, 556.0), Point(590.0, 558.0), Point(579.0, 563.0),
        Point(568.0, 567.0), Point(557.0, 574.0), Point(550.0, 586.0), Point(545.0, 597.0), Point(543.0, 608.0),
        Point(540.0, 619.0), Point(537.0, 630.0), Point(532.0, 645.0), Point(530.0, 657.0), Point(527.0, 670.0),
        Point(523.0, 682.0), Point(520.0, 693.0), Point(520.0, 705.0), Point(526.0, 716.0), Point(529.0, 727.0),
        Point(529.0, 738.0), Point(530, 748), Point(530, 758), Point(530, 768), Point(530, 778), Point(530, 788),
        Point(530, 798), Point(530, 800)]


class Bloon:
    lis = []  # Bloon container

    colors = {"black": "BTD6Black.png", "blue": "BTD6Blue.png", "green": "BTD6Green.png", "lead": "BTD6Lead.png", "pink": "BTD6Pink.png",
              "rainbow": "BTD6Rainbow.png", "red": "BTD6Red.png", "white": "BTD6White.png", "yellow": "BTD6Yellow.png", "zebra": "BTD6Zebra.png", "MOAB": "BTD6MOAB.png"}  # color --> png

    colorHitbox = {"black": ((16, 22), (-17, -20)), "blue": ((25, 30), (-25, -30)), "green": ((25, 30), (-25, -30)),
                   "lead": ((25, 30), (-25, -30)), "pink": ((25, 30), (-25, -30)), "rainbow": ((25, 30), (-25, -30)),
                   "red": ((25, 30), (-25, -30)), "white": ((16, 22), (-17, -20)), "yellow": ((25, 30), (-25, -30)), "zebra": ((25, 30), (-25, -30))}  # Hitbox size

    colorSplits = {"black": ("pink", "pink"), "white": ("pink", "pink"), "lead": ("black", "black"), "rainbow": ("zebra", "zebra"),
                   "zebra": ("white", "white", "black", "black"), "MOAB": ("rainbow", "rainbow", "rainbow", "rainbow")}  # Which bloons split into which

    colorOrder = ("red", "blue", "green", "yellow", "pink", "black", "white")  # Bloons in health/level order

    def __str__(self):
        return f"{self.color} Bloon at {self.moveIndex}"

    def __init__(self, win: GraphWin, color="red", moveIndex=0):
        self.color = color
        # self.hitboxval = Bloon.colorHitbox[color]
        self.img = Bloon.colors[color]
        self.bloon = Image(path[0], self.img)
        Bloon.lis.append(self)
        self.moveIndex = moveIndex
        # self.hitbox = Rectangle(Point(path[self.moveIndex].getX() + self.hitboxval[0][0], path[self.moveIndex].getY() + self.hitboxval[0][1]),
        #                         Point(path[self.moveIndex].getX() + self.hitboxval[1][0], path[self.moveIndex].getY() + self.hitboxval[1][1]))

    def drawBloon(self, win):
        """Displays the bloon's image in the window"""
        # self.hitbox.undraw()
        # self.hitbox = Rectangle(Point(path[self.moveIndex].getX() + self.hitboxval[0][0], path[self.moveIndex].getY() + self.hitboxval[0][1]),
        #                         Point(path[self.moveIndex].getX() + self.hitboxval[1][0], path[self.moveIndex].getY() + self.hitboxval[1][1]))
        # self.hitbox.setWidth(1)
        # self.hitbox.draw(win)
        self.bloon.draw(win)

    def moveSelf(self, win):
        """Shifts the current bloons position forward by one"""
        self.bloon.undraw()
        del self.bloon
        self.moveIndex += 1
        if self.moveIndex >= len(path) - 1:
            if self.color != "MOAB":
                Bloon.lis.remove(self)
                return False
            else:
                return True
        self.bloon = Image(path[self.moveIndex], self.img)
        self.drawBloon(win)
        return False

    def popSelf(self, win):
        """Creates the new bloons according to current bloon popping"""
        self.bloon.undraw()
        Bloon.lis.remove(self)
        if self.color == "red":
            return
        elif self.color in Bloon.colorSplits:
            numBloon = 0
            for bloonColor in Bloon.colorSplits[self.color]:
                Bloon(win, bloonColor, self.moveIndex - numBloon)
                numBloon += 1
        else:
            color = Bloon.colorOrder[Bloon.colorOrder.index(self.color) - 1]
            b = Bloon(win, color, self.moveIndex)
            b.drawBloon(win)
            b.moveSelf(win)
            print(f"{self.color} ---> {color}")

    @staticmethod
    def printBloonsAlive():
        for i in Bloon.lis:
            if Bloon.lis.index(i) % 8:
                print()
            print(i, end=" ")
        print()


class MOAB(Bloon):

    rotation = (46, 47, 48, 49, 50, 51, 52, 53, 54, 59, 60, 61, 62, 63, 64, 65, 66, 67, 76, 77, 78, 79, 80, 81, 82, 83, 84, 178, 179,
                180, 181, 182, 183, 184, 185, 186, 250, 251, 252, 253, 254, 255, 256, 257, 258)
    # Used for positive rotations determined by the moveIndex

    unrotation = (113, 114, 115, 116, 117, 118, 119, 120, 121, 125, 126, 127, 128, 129, 130, 131, 132, 133, 140, 141, 142, 143, 144,
                  145, 146, 147, 148, 188, 189, 190, 191, 192, 193, 194, 195, 196, 200, 201, 202, 203, 204, 205, 206, 207, 208, 224,
                  225, 226, 227, 228, 229, 230, 231, 232)
    # Used for negative rotations determined by the moveIndex

    lis = []

    def __str__(self):
        return f"M.O.A.B. class bloon at {self.moveIndex}"

    def __init__(self, win: GraphWin, color="MOAB", moveIndex=0, rotationAngle=0):
        super().__init__(win, color, moveIndex)
        Bloon.lis.remove(self)
        MOAB.lis.append(self)
        self.health = 25
        self.rotationAngle = rotationAngle

    def drawBloon(self, win):
        """Displays the image for the MOAB Bloon"""
        super().drawBloon(win)
        self.bloon.transform(1, self.rotationAngle)

    def moveSelf(self, win):
        """Shifts the MOAB forward one space, as well as correcting the rotation"""
        if super().moveSelf(win):
            MOAB.lis.remove(self)
            del self
            return
        if self.moveIndex in MOAB.rotation:
            self.rotationAngle += 10
        elif self.moveIndex in MOAB.unrotation:
            self.rotationAngle -= 10
        self.bloon.transform(1, self.rotationAngle)
        self.bloon.redraw()

    def popSelf(self, win):
        """Removes health from the MOAB or when at 0 hp, pops the Bloon"""
        self.health -= 1
        if self.health <= 0:
            super().popSelf(win)
            del self


def testGame():
    # setting up window
    win = GraphWin("Tower Defense", 1400, 773, autoflush=False)

    gameMap = Image(Point(600, 386.5), "MonkeyMeadows.png")
    gameMap.draw(win)
    gameRunning = True
    m = MOAB(win)
    m = None
    n = None
    for c in ("red", "blue", "black", "green", "lead", "pink", "rainbow", "white", "yellow", "zebra"):
        b = Bloon(win, c)
        b.drawBloon(win)
        for j in range(5):
            for i in Bloon.lis:
                i.moveSelf(win)
            time.sleep(.1)
            win.update()
    for p in range(10):
        for i in Bloon.lis:
            i.moveSelf(win)
            win.update()
    while Bloon.lis or MOAB.lis:
        for i in Bloon.lis:
            i.moveSelf(win)
        for i in MOAB.lis:
            i.moveSelf(win)
            if m is not None:
                m.undraw()
            if n is not None:
                n.undraw()
            m = Text(Point(1000, 200), str(i.rotationAngle))
            n = Text(Point(1000, 150), str(i.moveIndex))
            m.setSize(20)
            n.setSize(20)
            m.draw(win)
            n.draw(win)
        check = win.checkMouse()
        if check is not None:
            win.getMouse()
        time.sleep(.001)
        win.update()

    win.getMouse()
    win.close()


if __name__ == '__main__':
    testGame()
