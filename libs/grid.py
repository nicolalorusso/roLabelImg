#!/usr/bin/env python3.7
#
# roLabelImgNiL
# Copyright: Rhea System SA 2020
# Author: nicola
#
from PyQt5.QtGui import QPen, QColor, QPainterPath


class Grid(object):
    def __init__(self, step=500):
        self.step = step
        self.size = None
        self.color = QColor(255, 255, 255)
        self.stroke = 1

    def setSize(self, size):
        self.size = size

    def paint(self, painter):
        # exit if size is not set
        if not self.size:
            return

        pen = QPen(self.color)
        pen.setWidth(self.stroke)
        painter.setPen(pen)

        for x in range(0, self.size.width(), self.step):
            line_path = QPainterPath()
            line_path.moveTo(x, 0)
            line_path.lineTo(x, self.size.height())
            painter.drawPath(line_path)

        for y in range(0, self.size.height(), self.step):
            line_path = QPainterPath()
            line_path.moveTo(0, y)
            line_path.lineTo(self.size.width(), y)
            painter.drawPath(line_path)



