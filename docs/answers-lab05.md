# Lab 05: Câu trả lời thảo luận

## 1. Ưu, nhược điểm của upstream first so với release first?
Release first (mô hình của học phần): hotfix tạo từ release/*, sửa và phát
hành bản vá ngay, rồi cherry-pick về master. Ưu: bản vá ra nhanh, đúng
bản đã phát hành, cô lập khỏi tính năng mới. Nhược: dễ quên đưa bản sửa
về master hoặc sang các release khác, nên cần bước kiểm toán.
Upstream first (Release Flow của Microsoft): sửa trên master trước, rồi
cherry-pick sang release/*. Ưu: master luôn có bản sửa, không bao giờ
quên và không có hồi quy khi release tiếp theo. Nhược: bản vá phát hành
chậm hơn vì phải qua master (có thể bị ảnh hưởng bởi mã mới chưa ổn định),
còn khi master đã đi xa thì cherry-pick về release dễ xung đột.

## 2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?
- git log --all --grep "cherry picked from commit <FIX_SHA>" chỉ ra 1
  bản cherry-pick thay vì 2.
- Vòng lặp kiểm tra hành vi in 0 thay vì 1 cho v1.1.0.
- git cherry -v origin/master origin/release/lab05 và git log
  --oneline release/lab05..master giúp so sánh commit hai nhánh còn
  thiếu gì.
- Vì bản sửa chưa có, git tag --contains cũng không liệt kê v1.1.0.

## Ghi chú: vì sao phải merge commit cho hotfix vào release/lab04
Cherry-pick -x và git tag --contains cần FIX_SHA còn nguyên trong lịch sử.
Squash hoặc rebase tạo commit mới (SHA khác) nên mất khả năng truy vết.
