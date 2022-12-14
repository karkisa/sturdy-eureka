import torch
import cv2
import matplotlib.pyplot as plt
import pdb

def save_img(path,minutes,seconds,base_path,name):
    vid_ca = cv2.VideoCapture(path)
    fps = vid_ca.get(cv2.CAP_PROP_FPS)
    print(fps)
    frame_id = int(fps*(minutes*60 + seconds))
    vid_ca.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    _,frame = vid_ca.read()
    cv2.imwrite(base_path+name+'.png',frame)

def read_vid(path):
    vid_ca = cv2.VideoCapture(path)
    count = 0
    time_skips = 3000             # fps is 29.9 .i.e almost 30
    while vid_ca.isOpened():
        vid_ca.set(cv2.CAP_PROP_POS_MSEC,(count*time_skips))
        count+=1
        ret, frame = vid_ca.read()
        plt.imshow( frame)
        plt.show()
        count+=2

def main():

    path = '/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/210716_I2O_S5_U2_DJI0006.MOV'
    base_path = '/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/empty/'
    minutes = 5
    seconds = 23
    name = '1'

    save_img(path, minutes, seconds, base_path, name)
    # read_vid(path)

if __name__ == '__main__':
    main()