import sys
import sqlite3
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QBasicTimer


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.orientation = 1
        self.object = None
        self.score = 0
        self.x = 400
        self.y = 300
        self.x_2 = 410
        self.y_2 = 300
        self.x_3 = 420
        self.y_3 = 300
        self.x_4 = 430
        self.y_4 = 300
        self.x_5 = 440
        self.y_5 = 300
        self.x_6 = 450
        self.y_6 = 300
        self.x_7 = 460
        self.y_7 = 300
        self.x_8 = 470
        self.y_8 = 300
        self.x_9 = 480
        self.y_9 = 300
        self.x_10 = 490
        self.y_10 = 300
        self.x_11 = 500
        self.y_11 = 300
        self.x_12 = 510
        self.y_12 = 300
        self.x_13 = 520
        self.y_13 = 300
        self.x_14 = 530
        self.y_14 = 300
        self.x_15 = 540
        self.y_15 = 300
        self.x_16 = 550
        self.y_16 = 300
        self.food_x = None
        self.food_y = None
        self.get_food_x()
        self.get_food_y()
        self.timer = QBasicTimer()
        self.update_time = 125
        self.start_timer()
        self.flag = True

    def start_timer(self):
        self.timer.start(self.update_time, self)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.snake_move()
            self.snake_outside()
            self.snake_death()
            self.replay()
            self.update()

    def replay(self):
        if self.flag is False:
            self.orientation = 1
            self.score = 0
            self.x = 400
            self.y = 300
            self.x_2 = 410
            self.y_2 = 300
            self.x_3 = 420
            self.y_3 = 300
            self.x_4 = 430
            self.y_4 = 300
            self.x_5 = 440
            self.y_5 = 300
            self.x_6 = 450
            self.y_6 = 300
            self.x_7 = 460
            self.y_7 = 300
            self.x_8 = 470
            self.y_8 = 300
            self.x_9 = 480
            self.y_9 = 300
            self.x_10 = 490
            self.y_10 = 300
            self.x_11 = 500
            self.y_11 = 300
            self.x_12 = 510
            self.y_12 = 300
            self.x_13 = 520
            self.y_13 = 300
            self.x_14 = 530
            self.y_14 = 300
            self.x_15 = 540
            self.y_15 = 300
            self.x_16 = 550
            self.y_16 = 300
            self.get_food_x()
            self.get_food_y()
            self.flag = True

    def get_food_x(self):
        self.food_x = random.randint(5, 780)
        self.food_x = self.food_x // 10 * 10

    def get_food_y(self):
        self.food_y = random.randint(100, 570)
        self.food_y = self.food_y // 10 * 10

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            if self.orientation != 3:
                self.orientation = 1
        if event.key() == Qt.Key_Down:
            if self.orientation != 4:
                self.orientation = 2
        if event.key() == Qt.Key_Right:
            if self.orientation != 1:
                self.orientation = 3
        if event.key() == Qt.Key_Up:
            if self.orientation != 2:
                self.orientation = 4

    def paintEvent(self, event):
        if self.flag:
            self.object = QPainter()
            self.object.begin(self)
            self.draw_back()
            self.draw_food()
            self.eating_food()
            self.draw_snake()
            self.draw_game_board()
            self.object.end()

    def draw_back(self):
        self.object.setBrush(QColor(255, 255, 255))
        self.object.drawRect(0, 0, 800, 600)

    def draw_food(self):
        self.object.setBrush(QColor(255, 0, 0))
        self.object.drawRect(self.food_x, self.food_y, 10, 10)

    def draw_game_board(self):
        self.object.drawLine(10, 100, 790, 100)
        self.object.drawLine(10, 100, 10, 580)
        self.object.drawLine(10, 580, 790, 580)
        self.object.drawLine(790, 100, 790, 580)

    def draw_snake(self):
        self.object.setBrush(QColor(0, 100, 0))
        self.object.drawRect(self.x, self.y, 10, 10)
        self.object.setBrush(QColor(0, 255, 0))
        self.object.drawRect(self.x_2, self.y_2, 10, 10)
        self.object.setBrush(QColor(0, 150, 0))
        self.object.drawRect(self.x_3, self.y_3, 10, 10)
        self.object.setBrush(QColor(0, 255, 0))
        self.object.drawRect(self.x_4, self.y_4, 10, 10)
        self.object.setBrush(QColor(0, 150, 0))
        self.object.drawRect(self.x_5, self.y_5, 10, 10)
        self.object.setBrush(QColor(0, 255, 0))
        self.object.drawRect(self.x_6, self.y_6, 10, 10)
        self.object.setBrush(QColor(0, 150, 0))
        self.object.drawRect(self.x_7, self.y_7, 10, 10)
        self.object.setBrush(QColor(0, 255, 0))
        self.object.drawRect(self.x_8, self.y_8, 10, 10)
        self.object.setBrush(QColor(0, 150, 0))
        self.object.drawRect(self.x_9, self.y_9, 10, 10)
        self.object.setBrush(QColor(0, 255, 0))
        self.object.drawRect(self.x_10, self.y_10, 10, 10)
        self.object.setBrush(QColor(0, 150, 0))
        self.object.drawRect(self.x_11, self.y_11, 10, 10)
        self.object.setBrush(QColor(0, 255, 0))
        self.object.drawRect(self.x_12, self.y_12, 10, 10)
        self.object.setBrush(QColor(0, 150, 0))
        self.object.drawRect(self.x_13, self.y_13, 10, 10)
        self.object.setBrush(QColor(0, 255, 0))
        self.object.drawRect(self.x_14, self.y_14, 10, 10)
        self.object.setBrush(QColor(0, 150, 0))
        self.object.drawRect(self.x_15, self.y_15, 10, 10)
        self.object.setBrush(QColor(0, 255, 0))
        self.object.drawRect(self.x_16, self.y_16, 10, 10)

    def snake_move(self):
        if self.orientation == 1:
            self.x_16 = self.x_15
            self.x_15 = self.x_14
            self.x_14 = self.x_13
            self.x_13 = self.x_12
            self.x_12 = self.x_11
            self.x_11 = self.x_10
            self.x_10 = self.x_9
            self.x_9 = self.x_8
            self.x_8 = self.x_7
            self.x_7 = self.x_6
            self.x_6 = self.x_5
            self.x_5 = self.x_4
            self.x_4 = self.x_3
            self.x_3 = self.x_2
            self.x_2 = self.x
            self.y_16 = self.y_15
            self.y_15 = self.y_14
            self.y_14 = self.y_13
            self.y_13 = self.y_12
            self.y_12 = self.y_11
            self.y_11 = self.y_10
            self.y_10 = self.y_9
            self.y_9 = self.y_8
            self.y_8 = self.y_7
            self.y_7 = self.y_6
            self.y_6 = self.y_5
            self.y_5 = self.y_4
            self.y_4 = self.y_3
            self.y_3 = self.y_2
            self.y_2 = self.y
            self.x = self.x - 10
        if self.orientation == 2:
            self.x_16 = self.x_15
            self.x_15 = self.x_14
            self.x_14 = self.x_13
            self.x_13 = self.x_12
            self.x_12 = self.x_11
            self.x_11 = self.x_10
            self.x_10 = self.x_9
            self.x_9 = self.x_8
            self.x_8 = self.x_7
            self.x_7 = self.x_6
            self.x_6 = self.x_5
            self.x_5 = self.x_4
            self.x_4 = self.x_3
            self.x_3 = self.x_2
            self.x_2 = self.x
            self.y_16 = self.y_15
            self.y_15 = self.y_14
            self.y_14 = self.y_13
            self.y_13 = self.y_12
            self.y_12 = self.y_11
            self.y_11 = self.y_10
            self.y_10 = self.y_9
            self.y_9 = self.y_8
            self.y_8 = self.y_7
            self.y_7 = self.y_6
            self.y_6 = self.y_5
            self.y_5 = self.y_4
            self.y_4 = self.y_3
            self.y_3 = self.y_2
            self.y_2 = self.y
            self.y = self.y + 10
        if self.orientation == 3:
            self.x_16 = self.x_15
            self.x_15 = self.x_14
            self.x_14 = self.x_13
            self.x_13 = self.x_12
            self.x_12 = self.x_11
            self.x_11 = self.x_10
            self.x_10 = self.x_9
            self.x_9 = self.x_8
            self.x_8 = self.x_7
            self.x_7 = self.x_6
            self.x_6 = self.x_5
            self.x_5 = self.x_4
            self.x_4 = self.x_3
            self.x_3 = self.x_2
            self.x_2 = self.x
            self.y_16 = self.y_15
            self.y_15 = self.y_14
            self.y_14 = self.y_13
            self.y_13 = self.y_12
            self.y_12 = self.y_11
            self.y_11 = self.y_10
            self.y_10 = self.y_9
            self.y_9 = self.y_8
            self.y_8 = self.y_7
            self.y_7 = self.y_6
            self.y_6 = self.y_5
            self.y_5 = self.y_4
            self.y_4 = self.y_3
            self.y_3 = self.y_2
            self.y_2 = self.y
            self.x = self.x + 10
        if self.orientation == 4:
            self.x_16 = self.x_15
            self.x_15 = self.x_14
            self.x_14 = self.x_13
            self.x_13 = self.x_12
            self.x_12 = self.x_11
            self.x_11 = self.x_10
            self.x_10 = self.x_9
            self.x_9 = self.x_8
            self.x_8 = self.x_7
            self.x_7 = self.x_6
            self.x_6 = self.x_5
            self.x_5 = self.x_4
            self.x_4 = self.x_3
            self.x_3 = self.x_2
            self.x_2 = self.x
            self.y_16 = self.y_15
            self.y_15 = self.y_14
            self.y_14 = self.y_13
            self.y_13 = self.y_12
            self.y_12 = self.y_11
            self.y_11 = self.y_10
            self.y_10 = self.y_9
            self.y_9 = self.y_8
            self.y_8 = self.y_7
            self.y_7 = self.y_6
            self.y_6 = self.y_5
            self.y_5 = self.y_4
            self.y_4 = self.y_3
            self.y_3 = self.y_2
            self.y_2 = self.y
            self.y = self.y - 10

    def snake_outside(self):
        if self.x == 0 or self.x == 790 or self.y == 90 or self.y == 580:
            self.flag = False
            self.get_result()

    def snake_death(self):
        if self.x == self.x_5 and self.y == self.y_5 or self.x == self.x_6 and self.y == self.y_6 or \
                self.x == self.x_7 and self.y == self.y_7 or self.x == self.x_8 and self.y == self.y_8 \
                or self.x == self.x_9 and self.y == self.y_9 or self.x == self.x_10 and self.y == self.y_10 or \
                self.x == self.x_11 and self.y == self.y_11 or self.x == self.x_12 and self.y == self.y_12 or \
                self.x == self.x_13 and self.y == self.y_13 or self.x == self.x_14 and self.y == self.y_14 or \
                self.x == self.x_15 and self.y == self.y_15 or self.x == self.x_16 and self.y == self.y_16:
            self.flag = False
            self.get_result()

    def eating_food(self):
        if self.x == self.food_x and self.y == self.food_y:
            self.get_food_x()
            self.get_food_y()
            self.score = self.score + 10

    def get_result(self):
        con = sqlite3.connect("project.db")
        cur = con.cursor()
        cur.execute("""UPDATE snake
        SET value = {}
        WHERE name = 'Счёт'""".format(self.score))
        cur.execute("""UPDATE snake
        SET value = {}
        WHERE name = 'Полследняя позиция головы x'""".format(self.x))
        cur.execute("""UPDATE snake
        SET value = {}
        WHERE name = 'Полследняя позиция головы y'""".format(self.y))
        cur.execute("""UPDATE snake
        SET value = {}
        WHERE name = 'Последняя позиция еды x'""".format(self.food_x))
        cur.execute("""UPDATE snake
        SET value = {}
        WHERE name = 'Последняя позиция еды y'""".format(self.food_y))
        con.commit()
        con.close()

    def initUI(self):
        self.setGeometry(300, 50, 800, 600)
        self.setWindowTitle('Змейка')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec())
