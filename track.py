import cv2
from ultralytics import YOLO

model = YOLO(r'G:\CV\safetyAI\runs\detect\train\weights\best.pt')

ZONE_START = (100, 100) 
ZONE_END = (500, 400)

cap = cv2.VideoCapture(0) # Mở webcam

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # persist=True để nhớ ID
    results = model.track(frame, persist=True, conf=0.1, show=False)

    cv2.rectangle(frame, ZONE_START, ZONE_END, (0, 0, 255), 2)
    cv2.putText(frame, "RESTRICTED ZONE", (110, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy().astype(int)
        clss = results[0].boxes.cls.cpu().numpy().astype(int)

        for box, obj_id, cls in zip(boxes, ids, clss):
            x1, y1, x2, y2 = box
            center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
            
            in_zone = ZONE_START[0] < center_x < ZONE_END[0] and ZONE_START[1] < center_y < ZONE_END[1]
            
            label = model.names[cls]
            color = (0, 255, 0)

            if in_zone:
                if label == 'head': #trong vùng cấm mà là đầu trần
                    color = (0, 0, 255) # Đổi sang đỏ
                    cv2.putText(frame, f"ALARM: ID {obj_id} NO HELMET!", (50, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)


            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            cv2.putText(frame, f"ID {obj_id}: {label}", (int(x1), int(y1)-10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Safety Tracking Zone", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()