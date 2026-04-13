Dự án SafetyAI là một hệ thống giám sát an toàn lao động toàn diện được thiết kế để giải quyết bài toán kiểm soát trang thiết bị bảo hộ trong môi trường công nghiệp. Mục tiêu cốt lõi của ứng dụng là sử dụng thị giác máy tính để nhận diện tự động các đối tượng bao gồm đầu người đầu trần và mũ bảo hiểm. Hệ thống không chỉ dừng lại ở việc xử lý dữ liệu hình ảnh mà còn tích hợp khả năng giám sát trực tiếp qua webcam mang lại giá trị thực hiện cao cho công tác quản lý an toàn tại công trường.

Về khía cạnh dữ liệu mô hình được huấn luyện dựa trên bộ khung nhận diện vật thể YOLOv8 với ba lớp nhãn chính là head helmet và person. Qua quá trình thực nghiệm dữ liệu cho thấy sự tập trung cao độ vào việc phân biệt giữa các trạng thái an toàn và nguy cơ vi phạm. Các chỉ số đánh giá cho thấy mô hình đạt độ chính xác Precision và độ bao phủ Recall ở mức rất ấn tượng đối với hai nhãn quan trọng nhất là head và helmet giúp giảm thiểu tối đa tình trạng bỏ sót các trường hợp không đội mũ bảo hiểm.

Để đảm bảo khả năng vận hành ổn định trên các thiết bị phần cứng phổ thông hệ thống đã được thử nghiệm kỹ lưỡng trên cấu hình chip xử lý Intel Core i5 thế hệ thứ 12. Điểm đặc biệt của dự án nằm ở việc tối ưu hóa mô hình thông qua định dạng ONNX giúp duy trì tốc độ suy luận Inference ở mức khoảng 170ms mỗi khung hình ngay cả khi không có sự hỗ trợ từ các chip đồ họa rời GPU. Điều này chứng minh tính linh hoạt và khả năng triển khai rộng rãi của ứng dụng trên nhiều hạ tầng máy tính khác nhau.

______________________________________________
|   Class    | Precision |  Recall  | mAP@50 |     
|____________|___________|__________|________|
|    head    |   0.930   |   0.940  |  0.969 | 
|   helmet   |   0.963   |   0.936  |  0.983 |  
|   person   |   1.000   |   0.000  |  0.025 | 
|____________|___________|__________|________|
|   Average  |   0.964   |   0.625  |  0.659 |     
|____________|___________|__________|________|

Kết quả trên phản ánh sự vượt trội về chỉ số mAP@50 khi cả hai lớp đối tượng chính đều đạt ngưỡng trên 0.96. Tuy nhiên hệ thống vẫn tồn tại một số hạn chế nhất định cần được cải thiện trong tương lai như sự mất cân bằng dữ liệu của nhãn person dẫn đến độ bao phủ thấp. Ngoài ra hiệu năng nhận diện trong các môi trường thiếu sáng hoặc có góc khuất phức tạp vẫn là một thách thức kỹ thuật đòi hỏi việc bổ sung thêm các kỹ thuật tăng cường dữ liệu Augmentation hoặc thu thập thêm mẫu thực tế.

Nhìn chung SafetyAI là một minh chứng cho quy trình phát triển sản phẩm AI hoàn chỉnh từ khâu tiền xử lý dữ liệu huấn luyện mô hình đến triển khai giao diện web người dùng qua Flask. Ưu điểm lớn nhất của dự án là tính sẵn sàng trong việc tích hợp vào các hệ thống camera an ninh hiện có giúp chuyển đổi phương thức giám sát thủ công sang tự động hóa hoàn toàn. Đây là một nền tảng vững chắc để phát triển thêm các tính năng cao cấp hơn như cảnh báo qua âm thanh hoặc gửi thông báo vi phạm theo thời gian thực.