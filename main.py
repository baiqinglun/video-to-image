from video_to_image import VideoToImage
from cut_out_image import cutoutImageManger
import os

def main():
    # 视频转图片
    v = VideoToImage(video_path="video.mp4",output_path="out")
    v.run()

    # 图片切割
    cutManger = cutoutImageManger(output_path="cutout")
    cutManger.setClipCoordinate(x0=550,x1=1150,y0=400,y1=1060)
    for file_name in os.listdir(os.getcwd()+"/out"):
        cutManger.cut("out/"+file_name)
        print(file_name+"完成")

if __name__== "__main__" :
    main()