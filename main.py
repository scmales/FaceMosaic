import MainUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
import os
import facedetection

class MainCode(QMainWindow, MainUI.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        MainUI.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.toolButton_2.clicked.connect(self.on_selectImg)
        self.toolButton_3.clicked.connect(self.on_selectPath)
        self.pushButton.clicked.connect(self.on_save)

    def on_selectImg(self):
        self.imgPath, imgType = QFileDialog.getOpenFileName(self, '打开图片', r'./', " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        _ ,imgName = os.path.split(self.imgPath)  #分离出文件路径和文件名
        #(filename, extension) = os.path.splitext(imgName) #分离出文件名和后缀
        self.label_2.setText(imgName)


    def on_selectPath(self):
        self.saveDirectory = QFileDialog.getExistingDirectory(self, "选取文件夹", './')
        _, saveDirectory_s = os.path.split(self.saveDirectory)
        self.label_4 .setText(saveDirectory_s)

    def on_save(self):
        try:
            facedetection.detector(self.imgPath, self.saveDirectory)
        except AttributeError:
            return
        else:
            self.label_4.setText("保存成功！")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())
