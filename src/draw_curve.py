import matplotlib.pyplot as plt
import pandas as pd

class DrawManger:
    def __init__(self,csv_path) -> None:
        self.csv_path = csv_path

    def draw(self):
        path_data_x = pd.read_csv(self.csv_path, header=1, usecols=[0])
        path_data_y = pd.read_csv(self.csv_path, header=1, usecols=[1])
        print(path_data_x)
        plt.plot(path_data_x,path_data_y,'-',color = 'r',label="flame area")#s-:方形
        plt.xlabel("time")#横坐标名字
        plt.ylabel("ratio")#纵坐标名字
        plt.legend(loc = "best")#图例
        plt.savefig(self.csv_path.split(".")[0]+".png")
        plt.show()