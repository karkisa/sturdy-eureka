import cv2
import matplotlib.pyplot as plt
import pdb,os

def save_img(path,minutes,seconds,base_path,name):
    vid_ca = cv2.VideoCapture(path)
    fps = vid_ca.get(cv2.CAP_PROP_FPS)
    # frame_id = int(fps*(minutes*60 + seconds))
    # vid_ca.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    t_msec = 1000*(minutes*60 + seconds)
    vid_ca.set(cv2.CAP_PROP_POS_MSEC, t_msec)
    _,frame = vid_ca.read()
    cv2.imwrite(base_path+'/'+name,frame)

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

def get_significant_diigts(string):
    if string[0]=='0':
        return string[1]
    return string

def get_min_sec(path):
    path = path.split('.')
    time_seg = path[1]
    time_seg = time_seg.split('_')
    minutes =  time_seg[2]
    seconds = time_seg[3]
    minutes, seconds = get_significant_diigts(minutes),get_significant_diigts(seconds)
    return minutes, seconds

def get_paths():
    paths = []
    paths.append('/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/220813/220813_I2F_S4_U3_DJI0008.MOV')
    paths.append('/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/220813/220813_I2F_S4_U3_DJI0009.MOV')
    paths.append( '/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/220813/220813_I2F_S4_U3_DJI0010.MOV')
    return paths

def get_vid_path(img_path,paths):
    img_path = img_path.split('.')[0]
    if img_path[-1]=='8':
        return paths[0]
    if img_path[-1]=='9':
        return paths[1]
    else : return paths[2]

def get_name_extention(path):
    path=path.split('/')
    s=path[-1]
    s = s.split('.')
    return s[0]

def get_action(folder_path,save_path):
    list_img_paths = os.listdir(folder_path)
    for img_path in list_img_paths:
        minu,sec = get_min_sec(img_path)
        name_extention = get_name_extention(img_path)
        name = minu+'_'+sec+'_'+name_extention+'.png'
        minu,sec = eval(minu),eval(sec)
        vid_path = get_vid_path(img_path,get_paths())
        save_img(vid_path,minu,sec,save_path,name)
        
        # pdb.set_trace()



def main():
    # path = '/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/210716/210716_I2O_S5_U2_DJI0006.MOV'
    # base_path = '/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/images_2/'
    # minutes = 2
    # seconds = 43
    # path_2 = '/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/Pacman/220813_I2F_S4_U3_DJI0008.MOV_00_03_28_vlc00002.png'
    # name = str(minutes)+'_'+str(seconds)+'_220813'
    # minu,sec = get_min_sec(path_2)
    # minu,sec = eval(minu),eval(sec)
    folder_path = '/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/Pacman'
    save_path = '/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/save_path'

    get_action(folder_path,save_path)
    

if __name__ == '__main__':
    main()