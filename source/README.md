# Nhận dạng hoạt động từ PPG và ACC

Notebook [`notebooks/har_complete_pipeline.ipynb`](notebooks/har_complete_pipeline.ipynb) được rút gọn còn **48 cell, khoảng 520 dòng code**:

1. Tải 15 file PPG-DaLiA.
2. Tiền xử lý, chia Train/Validation/Test theo người.
3. E1–E6, chỉ **seed 42**.
4. Sáu confusion matrix trên Test S13–S15.

Các phần export, lượng tử hóa, benchmark CPU, sinh firmware, đo board và kiểm toán lặp lại đã bỏ khỏi notebook. Firmware, checkpoint, CSV và báo cáo cũ vẫn giữ nguyên ở thư mục riêng.

## Chạy

Python 3.11, mở notebook bằng VS Code/Jupyter và chọn đúng kernel:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.notebook.txt
```

`requirements.notebook.txt` chỉ cài thư viện dùng trong notebook gọn; không cần TensorFlow, Kaleido hay PlatformIO. `requirements.lock.txt` và `requirements.esp32.txt` vẫn giữ cho môi trường triển khai cũ.

- Mặc định `RETRAIN = False`: nạp checkpoint gốc nếu có; nếu thiếu model thì train model đó. Đọc CSV prediction đi kèm đúng checkpoint nếu có, nếu không thì suy luận lại.
- Đặt `RETRAIN = True` rồi chạy lại từ đầu để train cả sáu model và dự đoán lại. Kết quả mới lưu trong `artifacts/compact/run-.../`; không ghi đè `artifacts/models/` hoặc `artifacts/extension/`.
- Tiền xử lý một lần vào `artifacts/compact/data/`, những lần sau dùng cache. Tải ZIP khoảng 3,14 GB và giải nén khoảng 22 GB pickle; cần đủ đĩa và RAM để đọc một người (khoảng 1–2 GB pickle, RAM thực tế có thể cao hơn).
- Notebook có sẵn sáu hình được dựng lại từ CSV prediction Test gốc, không cần tải dataset để xem hình. Chạy lại toàn bộ vẫn cần dataset/cache. Dưới mỗi hình có nhãn nguồn kết quả.

Checkpoint phát hành trên GitHub Releases: xem [README repo](../README.md#restore-experiment-artifacts).

## Thiết kế

- Train S1–S10; Validation S11–S12; Test S13–S15. Không để cửa sổ của cùng một người rơi vào nhiều split.
- Cửa sổ 8 giây, bước 2 giây; bỏ nhãn chuyển tiếp 0 và cửa sổ có độ thuần nhãn dưới 80%.
- PPG 64 Hz hạ về 32 Hz bằng lọc chống aliasing; ACC giữ 32 Hz. Mean/std chỉ tính trên Train.
- E1: Random Forest, PPG+ACC, 38 đặc trưng.
- E2: CNN 1D, PPG+ACC.
- E3: CNN 2D STFT, PPG+ACC; E4: chỉ ACC; E5: chỉ PPG.
- E6: MultiKernel CNN 1D, Mixup α=0,2 khi train; causal EMA khi đánh giá. Bộ nhớ EMA reset khi đổi người hoặc có khoảng trống giữa các cửa sổ.
- Chọn checkpoint theo Macro F1 trung bình của S11/S12. E6 gốc đọc temperature/EMA đã chọn từ `selection.json`; E6 train mới giữ temperature 1 và chọn alpha trên Validation.

Code train E6 được viết lại theo cấu hình đã lưu. Seed cố định giúp kiểm soát ngẫu nhiên, nhưng không bảo đảm train lại ra đúng trọng số cũ giữa các thiết bị/phiên bản. Trong phát triển trước đây đã xem và xếp hạng một số ứng viên trên Test; đây là giới hạn của kết quả lịch sử.

## Kết quả Test seed 42 đi kèm notebook

Các số dưới đây tính lại từ CSV prediction gốc trên cùng **9.420 cửa sổ Test**, không phải lượt train mới hoặc phép đo mới trên ESP32. E6 có causal EMA, E1–E5 không có.

| Model | Accuracy (%) | Macro F1 (%) |
|---|---:|---:|
| E1 | 73,09 | 75,87 |
| E2 | 75,10 | 77,99 |
| E3 | 73,74 | 75,46 |
| E4 | 71,35 | 73,63 |
| E5 | 44,79 | 45,82 |
| E6 + EMA | 81,46 | 85,31 |

E2–E5 ở đây chỉ dùng seed 42, khác bảng trung bình ba seed trong báo cáo cũ.

## Type checking

Run these commands from `source/` using the notebook's Python interpreter:

```bash
python -m pip install -r requirements-dev.txt
python -m pyright
python check_types.py
```

`check_types.py` checks every code cell together in a temporary Python file and
maps diagnostics back to notebook cells. It never executes downloads, training or
evaluation, and leaves saved notebook outputs unchanged.

## Phần ESP32 giữ riêng

`firmware/esp32_baselines` chứa E1–E5/Q1; `firmware/esp32_har` chứa E6. Kết quả đo lịch sử nằm trong `results/` và báo cáo gốc. Phần này không còn chạy trong notebook gọn. Đã dùng ESP32-D0WDQ6, 240 MHz, không PSRAM; dữ liệu Test được replay qua USB, chưa phải cảm biến chạy trực tiếp.

Tác giả: Lương Nguyễn Thành Hưng — MSSV 23110111. Học phần Trí tuệ nhân tạo cho IoT; GVHD ThS. Hồ Nhựt Minh.
