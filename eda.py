import cv2
import matplotlib.pyplot as plt
import pdb,os,shutil
import numpy as np

def save_img(path,minutes,seconds,base_path,name):
    vid_ca = cv2.VideoCapture(path)
    fps = vid_ca.get(cv2.CAP_PROP_FPS)
    # frame_id = int(fps*(minutes*60 + seconds))
    # vid_ca.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    t_msec = 1000*(minutes*60 + seconds  )
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

def get_vid_path(img_path):
    img_path = img_path.split('.')[0]
    folder = img_path.split('_')[0]
    vid_path = folder + '/' + img_path + '.MOV'
    return vid_path

def get_name_extention(path):
    path=path.split('/')
    s=path[-1]
    s = s.split('.')
    return s[0]

def action(folder_path, save_path, base_folder = '/Users/sagar/Desktop/AI Cap/sturdy-eureka/data/vid'):
    list_img_paths = os.listdir(folder_path)
    for img_path in list_img_paths:
        minu,sec = get_min_sec(img_path)
        name_extention = get_name_extention(img_path)
        save_dest = save_path+'/'+name_extention.split('_')[0]
        name = minu+'_'+sec+'_'+name_extention+'.png'
        minu,sec = eval(minu),eval(sec)
        vid_path = base_folder + '/' + get_vid_path(img_path)
        save_img(vid_path,minu,sec,save_dest,name)

def distribut_images(source_folder,defst_folder):
    list_files = os.listdir(source_folder)
    for file in list_files:
        # if np.random.uniform()<0.20:
        if file[-1]=='g':
            src=source_folder+'/'+file
            dest = defst_folder + '/' + file 
            shutil.move(src,dest)

def move_labels(img_folder,label_base_folder,move_label_folder):
    list_files = os.listdir(img_folder)
    for file in list_files:
        name = file.split('.')[0]
        name = name + '.txt'
        path = label_base_folder + "/" + name
        dest = move_label_folder +'/'+ name
        if os.path.exists(path):
            shutil.move(path , dest)

def read_vid_and_save_in_folder(vid_path,parent_folder = '/nfs/hpc/share/karkisa/AI cap/sturdy-eureka/yolo_training_data/test_data/210914'):
    vid_ca = cv2.VideoCapture(vid_path)
    extention = get_name_extention(vid_path)
    save_folder =parent_folder + '/' + extention
    os.mkdir(save_folder)
    count = 0
    time_skips = 3000             # fps is 29.9 .i.e almost 30
    while vid_ca.isOpened():
        count+=1
        t_msec = 1000*(count)
        vid_ca.set(cv2.CAP_PROP_POS_MSEC, t_msec)
        ret, frame = vid_ca.read()
        name = str(count)+'_'+ extention +'.png'
        if ret :

            cv2.imwrite(save_folder+'/'+name,frame)
            if count%60==0:
                print(count)

        else : break

def main(): 
    base_folder =  '/nfs/hpc/share/karkisa/AI_Cap/sturdy-eureka/yolo_training_data/vid/210831'
    save_folder =  '/nfs/hpc/share/karkisa/AI_Cap/sturdy-eureka/yolo_training_data/test_data/210831'
    list_p = os.listdir(base_folder)
    list_p = [os.path.join(base_folder,p) for p in list_p]
    
    for vid_path in list_p:
        read_vid_and_save_in_folder(vid_path,save_folder)
    
if __name__ == '__main__':
    main()