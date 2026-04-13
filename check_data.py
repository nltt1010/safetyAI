import cv2
import matplotlib.pyplot as plt
import os

def visualize_yolo(img_path, label_path, class_names):
    # Đọc ảnh
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, _ = image.shape
    
    # Đọc nhãn
    with open(label_path, 'r') as f:
        for line in f.readlines():
            cls, x, y, nw, nh = map(float, line.split())
            
            # Chuyển từ hệ [0, 1] về Pixel thực tế
            x_center, y_center = x * w, y * h
            width, height = nw * w, nh * h
            
            x1 = int(x_center - width / 2)
            y1 = int(y_center - height / 2)
            x2 = int(x_center + width / 2)
            y2 = int(y_center + height / 2)
            
            # Chọn màu cho từng lớp: 0:Red, 1:Green, 2:Blue
            colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
            color = colors[int(cls)] if int(cls) < len(colors) else (255, 255, 255)
            
            # Vẽ khung và tên lớp
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            cv2.putText(image, class_names[int(cls)], (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# --- THỬ NGHIỆM ---
CLASS_NAMES = ['head', 'helmet', 'person']
# Bạn hãy thay tên file ảnh/nhãn thực tế có trong máy bạn vào đây
IMG_FILE = "./data//train//images/000001_jpg.rf.fddb09e33a544e332617f8ceb53ee805.jpg"
LABEL_FILE = "./data/train/labels/000001_jpg.rf.fddb09e33a544e332617f8ceb53ee805.txt"

visualize_yolo(IMG_FILE, LABEL_FILE, CLASS_NAMES)