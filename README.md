  Dự án này vẫn còn là một dự án cá nhân nhỏ trong quá trình bản thân tôi tự học nên còn khá đơn giản
  Dự án SafetyAI là một hệ thống giám sát an toàn lao động toàn diện được thiết kế để giải quyết bài toán kiểm soát trang thiết bị bảo hộ trong môi trường công nghiệp. Mục tiêu cốt lõi của ứng dụng là sử dụng thị giác máy tính để nhận diện tự động các đối tượng bao gồm đầu người đầu trần và mũ bảo hiểm. Hệ thống không chỉ dừng lại ở việc xử lý dữ liệu hình ảnh mà còn tích hợp khả năng giám sát trực tiếp qua webcam mang lại giá trị thực hiện cao cho công tác quản lý an toàn tại công trường.

  Về khía cạnh dữ liệu mô hình được huấn luyện dựa trên bộ khung nhận diện vật thể YOLOv8 với ba lớp nhãn chính là head helmet và person. Qua quá trình thực nghiệm dữ liệu cho thấy sự tập trung cao độ vào việc phân biệt giữa các trạng thái an toàn và nguy cơ vi phạm. Các chỉ số đánh giá cho thấy mô hình đạt độ chính xác Precision và độ bao phủ Recall ở mức rất ấn tượng đối với hai nhãn quan trọng nhất là head và helmet giúp giảm thiểu tối đa tình trạng bỏ sót các trường hợp không đội mũ bảo hiểm.

  Để đảm bảo khả năng vận hành ổn định trên các thiết bị phần cứng phổ thông hệ thống đã được thử nghiệm kỹ lưỡng trên cấu hình chip xử lý Intel Core i5 thế hệ thứ 12. Điểm đặc biệt của dự án nằm ở việc tối ưu hóa mô hình thông qua định dạng ONNX giúp duy trì tốc độ suy luận ở mức khoảng ổn mỗi khung hình ngay cả khi không có sự hỗ trợ từ các chip đồ họa rời GPU.


<p align="center">
  <img width="390" height="195" alt="image" src="https://github.com/user-attachments/assets/bf7991ed-ff59-49be-828e-63fbd161f1fd">
</p>


  Kết quả trên phản ánh sự vượt trội về chỉ số mAP@50 khi cả hai lớp đối tượng chính đều đạt ngưỡng trên 0.96. Tuy nhiên hệ thống vẫn tồn tại một số hạn chế nhất định cần được cải thiện trong tương lai như sự mất cân bằng dữ liệu của nhãn person dẫn đến độ bao phủ thấp. Ngoài ra hiệu năng nhận diện trong các môi trường thiếu sáng hoặc có góc khuất phức tạp vẫn là một thách thức kỹ thuật đòi hỏi việc bổ sung thêm các kỹ thuật tăng cường dữ liệu Augmentation hoặc thu thập thêm mẫu thực tế.

  Nhìn chung SafetyAI là một minh chứng cho quy trình phát triển sản phẩm AI hoàn chỉnh từ khâu tiền xử lý dữ liệu huấn luyện mô hình đến triển khai giao diện web người dùng qua Flask. Ưu điểm lớn nhất của dự án là tính sẵn sàng trong việc tích hợp vào các hệ thống camera an ninh hiện có giúp chuyển đổi phương thức giám sát thủ công sang tự động hóa hoàn toàn. Đây là một nền tảng vững chắc để phát triển thêm các tính năng cao cấp hơn như cảnh báo qua âm thanh hoặc gửi thông báo vi phạm theo thời gian thực.

## Công nghệ và Công cụ sử dụng

* **Ngôn ngữ lập trình:** Python
* **Mô hình AI:** YOLOv8 (Ultralytics)
* **Web Framework:** Flask
* **Xử lý hình ảnh:** OpenCV
* **Định dạng tối ưu hóa:** ONNX / OpenVINO
* **Giao diện người dùng:** HTML5, CSS3, JavaScript

## Hướng dẫn chạy ứng dụng

1. **Clone dự án về máy**
    ```bash
    git clone https://github.com/nltt1010/safetyAI/
    ```
2. **Cài đặt thư viện:** 
   ```bash
   pip install -r requirements.txt
   ```
3. **Chạy app**
   ```bash
   python app.py
   ```
