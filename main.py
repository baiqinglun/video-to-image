from src.video_to_image import VideoToImage
from src.cut_out_image import CutoutImageManger
from src.handle_image import ColorProcesser
from src.draw_curve import DrawManger
import os

def main():
    # 视频转图片
    # v = VideoToImage(video_path="video.mp4",output_path="out")
    # v.run()

    # 图片切割
    # cutManger = CutoutImageManger(output_path="cutout")
    # cutManger.setClipCoordinate(x0=550,x1=1150,y0=400,y1=1060) # 正常裁剪
    # cutManger.setClipCoordinate(x0=550,x1=1150,y0=400,y1=970) # 灰度处理裁剪
    # cutManger.cutAll()

    # colorProcesser = ColorProcesser()
    # colorProcesser.handleAll()


    drawManger = DrawManger("test.csv")
    drawManger.draw()

if __name__== "__main__" :
    main()