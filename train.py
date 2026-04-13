from ultralytics import YOLO
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_yaml_path = os.path.join(current_dir, "data.yaml")

model = YOLO('yolov8s.pt')

# Chạy train
results = model.train(
    data=data_yaml_path,
    epochs=5,
    imgsz=640,
    batch=16,
    device='cpu'
)

# # Model	Tham số (Params)	T
# # YOLOv8n (Nano)	3.2M		
# # YOLOv8s (Small)	11.2M		
# # YOLOv8m/l/x	>25M	
# model = YOLO('yolov8s.pt') 

# # 2. Bắt đầu huấn luyện
# results = model.train(
#     data='data.yaml',      # Đường dẫn file config 
#     epochs=5,             # Số vòng lặp 
#     imgsz=640,             # Kích thước ảnh đầu vào 
#     batch=16,              
#     name='safetyAI', # Tên dự án để lưu kết quả
    
#     # Các tham số Augmentation
#     mosaic=1.0,            # 100% ảnh train sẽ áp dụng Mosaic
#     mixup=0.1,             # 10% ảnh train áp dụng Mixup
#     degrees=10.0,          # Xoay ngẫu nhiên 10 độ
#     flipud=0.0,            # Lật ngược ảnh (thường không dùng vì người không đứng ngược)
#     fliplr=0.5             # Lật trái phải 50%
# )