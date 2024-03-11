import cv2
import os

class cutoutImageManger:
      def __init__(self,output_path) -> None:
            self.output_path = output_path
            if not os.path.exists(self.output_path):
                os.makedirs(self.output_path) 
            pass
      
      def setClipCoordinate(self,x0,x1,y0,y1):
           self.x0 = x0
           self.x1 = x1
           self.y0 = y0
           self.y1 = y1
           pass
      
      def cut(self,imgae_path):
            img = cv2.imread(imgae_path)
            cropped = img[self.y0:self.y1, self.x0:self.x1]  # 裁剪坐标为400:1060, 550:1150
            newImageName = self.output_path + "/" + imgae_path.split("/")[-1]
            cv2.imwrite(newImageName, cropped)
