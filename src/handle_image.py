import cv2
import numpy as np
import pandas as pd
import os

class ColorProcesser:
    def __init__(self) -> None:
        self.bw_output_path = "bw"
        self.list1 = []
        self.list2 = []
        pass

    def handleToBlackAndWhite(self,image_path):
        image = cv2.imread(image_path)
        # 将图像转换为灰度图像
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 定义阈值范围
        lower_threshold = 15
        upper_threshold = 200

        # 对图像进行滤波，保留特定范围内的像素值
        filtered_image = cv2.inRange(gray_image, lower_threshold, upper_threshold)

        if not os.path.exists(self.bw_output_path):
            os.makedirs(self.bw_output_path) 
        new_path = self.bw_output_path + "/" + image_path.split("/")[-1]
        cv2.imwrite(new_path, filtered_image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        pass

    def calBwRatio(self,image_path):
        image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        x,y= image.shape
        black = 0
        white = 0
        #遍历二值图，为0则black+1，否则white+1
        for i in range(x):
            for j in range(y):
                if image[i,j]==0:
                    black+=1
                else:
                    white+=1
        rate1 = white/(x*y)
        rate2 = black/(x*y)
        
        # self.list1.append(float(image_path.split("/")[-1].split(".png")[0].split("s")[0]))
        self.list2.append(rate2)
        #round()第二个值为保留几位有效小数。
        # print("白色占比:", round(rate1*100,2),'%')
        # print("黑色占比:", round(rate2*100,2),'%')

    def handleAll(self):
        # for file_name in os.listdir(os.getcwd()+"/cutout"):
        #     self.handleToBlackAndWhite("cutout/"+file_name)
        
        for file_name in os.listdir(os.getcwd()+"/bw"):
            self.list1.append(float(file_name.split(".png")[0].split("s")[0]))
        self.list1.sort()
        for i in self.list1:
            print("bw/"+str("%.3f"%i)+"s.png")
            self.calBwRatio("bw/"+str("%.3f"%i)+"s.png")
        
        cv2.destroyAllWindows()

        self.writeToCsv()

    def setBwOutputPath(self,bw_output_path):
        self.bw_output_path = bw_output_path
    
    def writeToCsv(self):
        dataframe = pd.DataFrame({'time':self.list1,'area':self.list2})

        #将DataFrame存储为csv,index表示是否显示行名，default=True
        dataframe.to_csv("test.csv",index=False,sep=',')

    def convert_to_float(string):
        try:
            number = float(string)
            formatted_number = "{:.3f}".format(number)
            return formatted_number
        except ValueError:
            return "Invalid input"