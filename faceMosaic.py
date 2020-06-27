import cv2
import os

class FaceMosaic():
    def __init__(self, inputDir, inputFileName, outputDir):
        super(FaceMosaic, self).__init__()
        self.flag_source = True
        self.flag_single = True
        self.flag_multi = True
        self.detector(inputDir, inputFileName, outputDir)

    def detector(self, inputDir, inputFileName, outputDir, size=32):
        try:
            detector = cv2.CascadeClassifier('source/haarcascade_frontalface_default.xml')
        except:
            self.flag_source = False
            return
        # handle an image and save
        try:
            self.handleImg(inputFileName, detector, outputDir)
        except:
            self.flag_single = False
            print("未开启单文件处理")

        # handle directory and save
        try:
            for root, dirs, filenames in os.walk(inputDir):
                for filename in filenames:
                    filePath = os.path.join(root, filename)
                    self.handleImg(filePath, detector, outputDir)
        except:
            self.flag_multi = False
            print("未开启多文件处理")

    def handleImg(self, filePath, detector, outDir):
        img = cv2.imread(filePath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            # cv2.rectangle(img, (x + 30, y + 30), (x + w - 30, y + h - 30), (255, 0, 0), 2)
            size = int(0.07 * w)
            w = int(0.62 * w)
            h = int(0.8 * h)
            x = int(x + 0.32 * w)
            y = int(y + 0.1 * h)
            self.mosaic(img, x, y, w, h, size)
            # print(w, h)
        # cv2.imshow('img', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        _, imgName = os.path.split(filePath)  # 解析图片源名字
        cv2.imwrite(os.path.join(outDir, imgName), img)


    def mosaic(self, img, x, y, w, h, size):
        h = h/size*size
        w = w/size*size
        for i in range(int(h/size)):
            for j in range(int(w/size)):
                for m in range(size):
                    for n in range(size):
                        #img[y+i*size+m][x+j*size+n] = img[y+i*size][x+j*size]
                        img[y + i * size + m][x + j * size + n] = 1
