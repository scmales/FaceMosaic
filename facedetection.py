import cv2
import os
def detector(inputPath, outputPath, size=32):
    img = cv_imread(inputPath)
    detector = cv2.CascadeClassifier('source/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        #cv2.rectangle(img, (x + 30, y + 30), (x + w - 30, y + h - 30), (255, 0, 0), 2)
        size = int(0.07*w)
        w = int(0.62*w)
        h = int(0.8*h)
        x = int(x+0.32*w)
        y = int(y+0.1*h)
        mosaic(img, x, y, w, h, size)
        #print(w, h)
    # cv2.namedWindow('img', 0)
    # cv2.resizeWindow("enhanced", 1024, 1536)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    _, imgName = os.path.split(inputPath)
    cv_imwrite(outputPath+'/'+imgName, img)  # 保存图像 也会遇到解析文件名的问题

def cv_imread(file_path):
    root_dir, file_name = os.path.split(file_path)
    pwd = os.getcwd()
    if root_dir:
        os.chdir(root_dir)
    cv_img = cv2.imread(file_name)
    os.chdir(pwd)
    return cv_img

def cv_imwrite(file_path, img):
    root_dir, filename = os.path.split(file_path)
    pwd = os.getcwd()
    if root_dir:
        os.chdir(root_dir)
    cv2.imwrite(filename, img)
    os.chdir(pwd)

def mosaic(img, x, y, w, h, size):
    h = h/size*size
    w = w/size*size
    for i in range(int(h/size)):
        for j in range(int(w/size)):
            for m in range(size):
                for n in range(size):
                    #img[y+i*size+m][x+j*size+n] = img[y+i*size][x+j*size]
                    img[y + i * size + m][x + j * size + n] = 1



if __name__ == '__main__':
    #path = sys.argv[1]
    #path = sys.argv[2]
    path = '2.JPG'
    detector(path, path)