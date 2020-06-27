import MainUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
import os
from faceMosaic import FaceMosaic

class MainWindow(QMainWindow, MainUI.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        MainUI.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.toolButton_1.clicked.connect(self.on_selectImgDir)
        self.toolButton_2.clicked.connect(self.on_selectImgFile)
        self.toolButton_3.clicked.connect(self.on_selectPath)
        self.pushButton.clicked.connect(self.on_save)
        self.imgDir = None
        self.imgPath = None
        self.saveDirectory = None

    def on_selectImgDir(self):
        self.imgDir = QFileDialog.getExistingDirectory(self, "选取文件夹", './')
        _, saveDirectory_s = os.path.split(self.imgDir)
        self.label_1.setText(saveDirectory_s)
        self.label_4.setText("未选择任何路径")

    def on_selectImgFile(self):
        self.imgPath, imgType = QFileDialog.getOpenFileName(self, '打开图片', r'./', " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        _ ,imgName = os.path.split(self.imgPath)  #分离出文件路径和文件名
        #(filename, extension) = os.path.splitext(imgName) #分离出文件名和后缀
        self.label_2.setText(imgName)
        self.label_4.setText("未选择任何路径")


    def on_selectPath(self):
        self.saveDirectory = QFileDialog.getExistingDirectory(self, "选取文件夹", './')
        _, saveDirectory_s = os.path.split(self.saveDirectory)
        self.label_4 .setText(saveDirectory_s)

    def on_save(self):

        model = FaceMosaic(self.imgDir, self.imgPath, self.saveDirectory)
        if model.flag_source == False:
            self.label_2.setText("加载模型失败!")
            self.label_1.setText("加载模型失败!")
        else:
            if model.flag_single == False:
                self.label_2.setText("未启用!")
            else:
                self.label_2.setText("保存成功!")

            if model.flag_multi == False:
                self.label_1.setText("未启用!")
            else:
                self.label_1.setText("保存成功!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainWindow()
    md.show()
    sys.exit(app.exec_())
