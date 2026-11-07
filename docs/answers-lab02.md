# Lab 02: Câu trả lời thảo luận

## 1. Vì sao phải đồng bộ master trước khi gửi PR?
Nhánh được tạo từ một thời điểm cũ của master, trong khi master đã có
thêm thay đổi. Đồng bộ (merge/rebase master vào nhánh) giúp phát hiện sớm
xung đột và lỗi tích hợp ở nhánh của mình, kiểm thử được mã đã kết hợp
(ví dụ nhánh search-by-title chạy cùng print_cart), và reviewer duyệt đúng
thứ sẽ được tích hợp. Nhờ vậy PR sạch, ít rủi ro khi vào master.

## 2. Khi nào không được rebase?
Không rebase trên commit đã chia sẻ (đã push và người khác có thể đã dựa
vào), vì rebase viết lại lịch sử và tạo SHA mới, gây lệch lịch sử giữa
các bản sao. Cũng không rebase trên master hoặc release/*. Nhánh riêng
chưa ai dùng thì rebase an toàn (cần push --force-with-lease sau đó).

## 3. feature/* khác topic/* ra sao?
Cả hai đều tạo từ master và merge về master, khác nhau ở mục đích:
feature/* thêm một tính năng của sản phẩm (cart-print, search-by-title),
còn topic/* là một chủ đề không phải tính năng, như tài liệu hay cấu
hình (pr-template, use-case-diagram, readme-usage).

## Ghi chú: ba kiểu merge đã dùng
- Merge commit (PR cart-print): giữ đủ commit, lịch sử có nhánh rẽ,
  revert cả tính năng bằng 1 lệnh (-m 1).
- Squash (PR README): gộp thành 1 commit, lịch sử tuyến tính.
- Rebase (PR use case): giữ từng commit với SHA mới, lịch sử tuyến tính,
  revert cả tính năng phải revert nhiều commit.
