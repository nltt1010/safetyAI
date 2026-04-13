from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2 

model = YOLO('./runs/detect/train/weights/best.pt')

results = model.predict(source="./data/val/images/005300_jpg.rf.1670526983a03ed2ccc2ff28c90e0040.jpg", conf=0.08, iou=0.1)

for r in results:
    # Lấy danh sách các class_id được detect trong ảnh
    detected_classes = r.boxes.cls.tolist()
    

    has_anything = len(detected_classes) > 0 # Có bất kỳ vật thể nào được tìm thấy
    has_person = 2.0 in detected_classes
    has_helmet = 1.0 in detected_classes
    has_head = 0.0 in detected_classes

    print(f"--- Kết quả kiểm tra ---")
    # Nếu thấy mũ, thấy đầu HOẶC thấy thân người thì coi như có người
    if has_person or has_head or has_helmet:
        if has_helmet:
            print("Trạng thái: AN TOÀN - Có đội mũ bảo hiểm.")
        else:
            print("CẢNH BÁO: VI PHẠM - Phát hiện đầu trần không có mũ!")
    else:
        print("Trạng thái: Khu vực trống.")

for r in results:
    # r.plot() sẽ trả về một mảng numpy (Bgr) của ảnh đã được vẽ box
    im_array = r.plot()  
    
    # Chuyển đổi từ BGR (OpenCV) sang RGB (Matplotlib) để hiển thị đúng màu
    im_rgb = cv2.cvtColor(im_array, cv2.COLOR_BGR2RGB)
    
    # Hiển thị ảnh
    plt.imshow(im_rgb)
    plt.axis('off') # Ẩn các trục tọa độ
    plt.show()