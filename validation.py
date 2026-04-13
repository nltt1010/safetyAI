from ultralytics import YOLO
model = YOLO(r'G:\CV\safetyAI\runs\detect\train\weights\best.pt')

results = model.val(data='data.yaml')