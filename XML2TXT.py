
import xml.etree.ElementTree as ET
import os
import shutil
import random
#root_path=os.path.abspath('...')#这里是以下内容的绝对地址
root_path = 'D:/MyDocument/Python_Demo/yolov5-5.0/ALL/Labels/'
def convert_annotation(image_id):
    classes=['vehicle', 'person', 'NonMotorVehicle']#标签名
    # in_file = open(root_path,'Annotations/%s.xml' % (image_id), encoding='UTF-8')

    in_file = open(root_path + '%s.xml' % (image_id), encoding='UTF-8')

    out_file = open(root_path + '%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    size_width = int(size.find('width').text)
    size_height = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = [float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),float(xmlbox.find('ymax').text)]
        # 标注越界修正
        if b[1] > size_width:
            b[1] = size_width
        if b[3] > size_height:
            b[3] = size_height
        txt_data=[((b[0]+b[1])/2.0-1)/size_width,((b[2]+b[3])/2.0-1)/size_height,(b[1]-b[0])/size_width,(b[3]-b[2])/size_height]
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in txt_data]) + '\n')   

img_path=os.path.join(root_path,'')
imglist=os.listdir(img_path)
# print(imglist)
for img_id in imglist:
    img_id=img_id[:-4]    
    convert_annotation(img_id)
