# Lab 01: Câu trả lời thảo luận

## Câu hỏi nhanh: cấu hình `--global` lưu ở đâu? Khác gì `--local`?
- `--global` lưu ở `~/.gitconfig` (máy này: `C:/Users/Admin/.gitconfig`), áp dụng cho mọi repo của user.
- `--local` lưu ở `.git/config` của từng repo, chỉ áp dụng cho repo đó và được ưu tiên hơn `--global` khi trùng khóa.
- Ngoài ra còn `--system` (cho cả máy), ưu tiên thấp nhất.

## 1. Vì sao dùng `git mv`?
Dùng `git mv` thay vì lệnh `mv` của hệ điều hành giúp Git nhận diện ngay lập tức đây là hành động đổi tên/di chuyển tệp (rename) thay vì báo xóa tệp cũ và thêm tệp mới (untracked). Điều này giúp bảo toàn lịch sử commit của tệp.

## 2. `release/lab01` có phải baseline không?
Có. Nhánh `release/lab01` đóng vai trò là một baseline, đánh dấu một trạng thái đã được thống nhất, hoàn chỉnh và đóng băng để nộp bài/phát hành. Không ai được thay đổi trực tiếp trên nhánh này nữa.

## 3. Vì sao không commit thẳng master dù làm một mình?
Để tuân thủ đúng luồng làm việc (workflow) quản lý cấu hình và kiểm soát thay đổi. Mọi thay đổi phải được cô lập trên nhánh riêng và đi qua quy trình kiểm duyệt (Pull Request) để tạo thói quen, đảm bảo chất lượng mã nguồn và khả năng hoàn tác dễ dàng.
