from flask import Flask, render_template, request
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
# Đảm bảo các thư mục cần thiết tồn tại khi khởi động
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_RESULTS_DIR = os.path.join(BASE_DIR, 'static', 'results')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('static/results', exist_ok=True)
os.makedirs('static/css', exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model
model = YOLO("./runs/detect/train/weights/best.pt")

@app.route('/', methods=['GET', 'POST'])
def index():
    processed_img = None
    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename != '':
            filename = file.filename
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)
            
            # CHỈNH SỬA TẠI ĐÂY:
            # project="static" và name="results" kết hợp với exist_ok=True 
            # để YOLO lưu thẳng vào static/results/filename.jpg
            model.predict(
                source=input_path, 
                save=True, 
                project=os.path.join(BASE_DIR, 'static'),
                name="results", 
                exist_ok=True
            )
            
            # Ép tên file hiển thị đúng
            processed_img = filename 
            
    return render_template('index.html', processed_img=processed_img)

def gen_frames():
    # 0 là ID của webcam mặc định
    camera = cv2.VideoCapture(0)
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Chạy YOLO trên từng khung hình (frame)
            # stream=True giúp tối ưu bộ nhớ khi chạy video
            results = model.track(frame, persist=True, stream=True)
            
            for r in results:
                annotated_frame = r.plot() # Vẽ khung và nhãn lên frame

            # Mã hóa frame thành định dạng JPEG để gửi qua Web
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame_bytes = buffer.tobytes()
            
            # Trả về dữ liệu theo định dạng multipart
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Trả về phản hồi video stream
    from flask import Response
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)