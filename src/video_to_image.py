import cv2
import os

class VideoToImage:
    def __init__(self,video_path,output_path) -> None:
        self.interval = 5
        self.video_path = video_path
        self.output_path = output_path
        if not os.path.exists(output_path):
            os.makedirs(output_path)             # 目标文件夹不存在，则创建
        self.cap = cv2.VideoCapture(video_path)    # 获取视频
        self.judge = self.cap.isOpened()                 # 判断是否能打开成功
        if(self.judge):
            print("打开成功！")
        else:
            print("打开失败！")
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)      # 帧率，视频每秒展示多少张图片
        self.dtime = self.interval / self.fps
        pass

    def setInterval(self,interval):
        self.interval = interval
        self.dtime = self.interval / self.fps

    def run(self):
        frames = 1                           # 用于统计所有帧数
        count = 1                            # 用于统计保存的图片数量
        time = 0

        while(self.judge):
            flag, frame = self.cap.read()         # 读取每一张图片 flag表示是否读取成功，frame是图片
            if not flag:
                print(flag)
                print("Process finished!")
                break
            else:
                if frames % self.interval == 0:         # 每隔2帧抽一张
                    imgname = str('%.3f'%time) + "s.png"
                    newPath = self.output_path + "/" + imgname
                    print(newPath)
                    # cv2.IMWRITE_PNG_COMPRESSION
                    cv2.imwrite(newPath, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])
                    count += 1
                    time += self.dtime
            frames += 1
        self.cap.release()
        print("共有 %d 张图片"%(count-1))