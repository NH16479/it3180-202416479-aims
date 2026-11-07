# Lab 04: Câu trả lời thảo luận

## 1. Vì sao chuẩn bị phát hành trên master trước, không sửa trên nhánh release?
Mọi thay đổi (đổi số phiên bản, CHANGELOG) phải đi qua PR vào master để có
review và truy vết, và master luôn là dòng phát triển chính. Nếu sửa trực
tiếp trên release/* thì master không có thay đổi đó (lệch nhau), và nhánh
release không được phép nhận commit ngoài quy trình vì nó là baseline
đóng băng. Chuẩn bị trên master rồi mới tách nhánh release nên release
luôn là một tập con của lịch sử master.

## 2. Vì sao release/* không merge vào master? So sánh với GitFlow
Release flow của học phần đi từ master ra release/*: master tiếp tục phát
triển, release/* chỉ nhận bản sửa lỗi (hotfix) rồi lan truyền sang master
bằng cherry-pick, nên không cần merge ngược. Release không chứa gì mà
master chưa có, tính năng mới chỉ nằm trên master. GitFlow thì có nhánh
develop và main, nhánh release/hotfix merge về cả hai, nhiều nhánh dài
hạn hơn, phù hợp phát hành định kỳ nhiều môi trường. Release flow đơn
giản hơn, ít nhánh dài hạn, hợp với nộp bài theo tuần và nhiều bản chạy
song song.

## 3. Vì sao lên 1.0.0 mà không phải 0.4.0?
Theo Semantic Versioning, 0.y.z là giai đoạn đầu, API chưa ổn định
(Lab 01 đến Lab 03 là v0.1.0 đến v0.3.0). Đến Lab 04 sản phẩm có đủ
tính năng cốt lõi, có test, quy trình phát hành và CHANGELOG, được coi là
bản phát hành đầu tiên ổn định để giao cho người dùng, nên đánh 1.0.0
để báo hiệu từ đây tuân thủ SemVer đầy đủ (MAJOR cho thay đổi phá vỡ
tương thích, MINOR cho tính năng mới, PATCH cho sửa lỗi).
