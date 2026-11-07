# Changelog

Định dạng theo Keep a Changelog, đánh số phiên bản theo Semantic Versioning.

## [1.1.0] - 2026-11-07

### Added
- Cart.sort_by_title(), Cart.sort_by_cost()
- search_by_category() tìm đĩa theo thể loại
### Fixed
- search_by_title không phân biệt hoa thường (bản vá 1.0.1, issue #22)

## [1.0.1] - 2026-11-07
### Fixed
- search_by_title không phân biệt hoa thường (issue #22)
## [1.0.0] - 2026-11-07
### Added
- Gói aims với DigitalVideoDisc và Cart
- Cart.print_cart() hiển thị chi tiết giỏ hàng
- search_by_title() tìm đĩa theo tiêu đề
- Cart.total_cost_with_discount() tính tổng sau giảm giá, kiểm tra phần trăm hợp lệ
- Unit test (unittest) cho Cart và giảm giá
- Mẫu mô tả Pull Request

### Fixed
- Giỏ hàng nhận đĩa thứ 21 (#<N>)
