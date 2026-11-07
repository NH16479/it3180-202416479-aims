# Lab 03: Câu trả lời thảo luận

## 1. Merge base là gì?
Merge base là commit tổ tiên chung gần nhất của hai nhánh. Khi merge,
Git so sánh từng nhánh với merge base (merge ba bên): chỗ nào chỉ một
bên đổi thì lấy bên đó, chỗ cả hai bên đổi khác nhau (cùng dòng) thì
báo xung đột để người dùng quyết định. Nhờ vậy Git biết thay đổi nào
là của nhánh nào.

## 2. Vì sao master và release/* phải dùng revert?
master và release/* là lịch sử chung, nhiều người và nhiều bản sao
đã dựa vào. reset viết lại lịch sử (đổi SHA), buộc phải push --force
và làm lệch bản sao của người khác. revert thêm một commit đảo ngược,
không viết lại lịch sử, vẫn truy vết được cái gì đã bị hoàn tác và vì
sao, và đi qua PR nên có review. Với release/* (baseline), giữ nguyên
lịch sử còn là yêu cầu của quản lý cấu hình.
