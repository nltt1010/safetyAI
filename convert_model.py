from ultralytics import YOLO

model = YOLO(r'G:\CV\safetyAI\runs\detect\train\weights\best.pt')

# ONNX: Định dạng chung, chạy cực nhanh trên CPU.

# TFLite: Dùng cho ứng dụng Android/iOS.

# TensorRT: Nếu sau này bạn có GPU NVIDIA, cái này sẽ tăng tốc lên gấp 10 lần.

model.export(format='onnx')