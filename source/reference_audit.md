# Đối chiếu nguồn của báo cáo HAR

Bản được soát: submission/LuongNguyenThanhHung_final.docx. Ngày 08/10/2026.

## Kiến thức và phạm vi dùng nguồn

Số trang dưới đây là số trang PDF đính kèm, tính cả bìa HAL. Mỗi mục tham khảo có đúng một PDF. Bản tác giả được ghi rõ, không gọi là PDF của nhà xuất bản.

| File PDF | Mục báo cáo | Vị trí trong nguồn | Nội dung dùng và giới hạn |
|---|---|---|---|
| 01_STFT_Allen_Rabiner_1977.pdf | 2.3 | pp. 1–2 | STFT: phân tích Fourier trên đoạn có cửa sổ. Hann 64, hop 4, dải 0–12 Hz và resize là cấu hình riêng. |
| 02_Random_Forests_Breiman_2001.pdf | 3.1 | pp. 1–3 | Random Forest và việc chọn ngẫu nhiên đặc trưng. 38 đặc trưng, 100 cây, class_weight và min_samples_leaf là cấu hình thí nghiệm. |
| 03_Temperature_Scaling_Guo_2017.pdf | 3.3 | p. 6, Eq. 9 | Chia logits cho một T dương trước softmax. Không dùng bài này làm nguồn cho EMA hay mức tăng Accuracy. |
| 04_Batch_Normalization_Ioffe_2015.pdf | 3.2 | pp. 3–4, Alg. 1–2 | BatchNorm khi huấn luyện/inference. Số kênh và thứ tự lớp lấy từ code của bài này. |
| 05_InceptionTime_Fawaz_2020.pdf | 3.3 | pp. 6–8, Fig. 1–2 | Ý tưởng nhiều nhánh, bottleneck và residual. Bài gốc dùng 10/20/40; E6 tự chọn 3/5/7 và bottleneck riêng từng nhánh. |
| 06_Integer_Quantization_Jacob_2018.pdf | 3.4 | p. 3, Eq. 1; p. 5, §3.2 | Quan hệ số thực–scale–zero-point và gộp BN. Q1 là PTQ; không nhận là đã thực hiện QAT của bài gốc. |
| 07_Adam_Kingma_Ba_2015.pdf | 3.2 | p. 2, Alg. 1 | Thuật toán Adam. Learning rate, weight decay, batch size, early stopping và scheduler lấy từ cấu hình thực nghiệm. |
| 08_Classification_Measures_Opitz_2024.pdf | 4.1 | pp. 4–6, §4.1–4.6 | Accuracy, P/R từng lớp, Macro F1 = trung bình F1 từng lớp (§4.4, Eq. 10), weighted F1 (§4.6). |
| 09_Deep_PPG_Reiss_2019.pdf | 2.1 | pp. 6–9, §2.2.1–2.2.4 | PPG-DaLiA, 15 người, hoạt động và BVP 64 Hz/ACC 32 Hz. Bài gốc ước lượng nhịp tim, không chứng minh kết quả HAR của báo cáo. |
| 10_Welch_PSD_1967.pdf | 3.1 | pp. 1–2 | PSD bằng trung bình modified periodogram. Hann 128, overlap 64 và các dải công suất là lựa chọn của pipeline. |
| 11_Mixup_Zhang_2018.pdf | 3.3 | pp. 2–3, §2 và Fig. 1 | Trộn đầu vào và nhãn cùng hệ số lambda. Alpha 0,2 và kết quả HAR là của thí nghiệm này. |

## Những chỗ đã sửa

- Bỏ câu gán kernel 3/5/7 cho InceptionTime. Nêu đúng phần tham khảo và phần tự cấu hình của E6.
- Sửa mô tả bottleneck: từng nhánh E6 có Conv 1×1 riêng; không mô tả thành một bottleneck chung.
- Nêu rõ Deep PPG làm bài toán nhịp tim; số liệu HAR và ESP32 là kết quả riêng.
- Dùng Opitz (2024) cho đúng công thức Macro F1. Không lấy F1 từ Precision macro và Recall macro.
- Giới hạn nguồn Guo ở temperature scaling, và nguồn Jacob ở scale/zero-point, gộp BN; không gán EMA hoặc PTQ của bài này cho quy trình khác trong nguồn.
- Nêu việc Test đã được xem/xếp hạng trong phát triển, dù checkpoint cuối khớp model thắng Validation. Không mô tả Test là dữ liệu chưa từng dùng.

## Đối chiếu với dữ liệu thí nghiệm

- 149 ô phân loại ở bảng tổng hợp, theo người, theo nhãn và lỗi cặp nhãn: tính lại từ dự đoán ESP32; khớp trong sai số làm tròn.
- 21 giá trị mean/median/P95: khớp results/esp32_latency_comparison.csv.
- 42 giá trị bộ nhớ: khớp results/esp32_memory_single_sample.csv.
- 46.763 cửa sổ giữ lại, 64.697 cửa sổ ban đầu và 17.934 cửa sổ loại do nhãn 0: khớp metadata xử lý. Tổng thời lượng và thời lượng không đếm chồng lấn cũng khớp.
- Tần số activity 4 Hz và mã 0–8 được kiểm tra ở readme/tệp đồng bộ của dataset; không suy từ EDA 4 Hz trong bài Deep PPG.
- E6: selection.json và validation_selection.csv ghi cùng model thắng Validation; ghi chú selection.json cũng thừa nhận đã có bảng xếp hạng Test trong phát triển. Bản ghi này không chứng minh Test hoàn toàn chưa từng được xem.

## Nguồn tải PDF và tình trạng bản thảo

Các URL sau dùng để kiểm tra tài liệu đã xuất bản; không thay cho file PDF đính kèm.
- **01_STFT_Allen_Rabiner_1977.pdf** — [A unified approach to short-time Fourier analysis and synthesis.](https://doi.org/10.1109/PROC.1977.10770)
- **02_Random_Forests_Breiman_2001.pdf** — [Random forests.](https://doi.org/10.1023/A:1010933404324) Author manuscript hosted by UC Berkeley.
- **03_Temperature_Scaling_Guo_2017.pdf** — [On calibration of modern neural networks.](https://proceedings.mlr.press/v70/guo17a.html)
- **04_Batch_Normalization_Ioffe_2015.pdf** — [Batch normalization: Accelerating deep network training by reducing internal covariate shift.](https://proceedings.mlr.press/v37/ioffe15.html)
- **05_InceptionTime_Fawaz_2020.pdf** — [InceptionTime: Finding AlexNet for time series classification.](https://doi.org/10.1007/s10618-020-00710-y) Author manuscript of the published article, deposited in HAL (hal-03181438).
- **06_Integer_Quantization_Jacob_2018.pdf** — [Quantization and training of neural networks for efficient integer-arithmetic-only inference.](https://openaccess.thecvf.com/content_cvpr_2018/html/Jacob_Quantization_and_Training_CVPR_2018_paper.html)
- **07_Adam_Kingma_Ba_2015.pdf** — [Adam: A method for stochastic optimization.](https://arxiv.org/abs/1412.6980) Published conference paper hosted on arXiv.
- **08_Classification_Measures_Opitz_2024.pdf** — [A closer look at classification evaluation metrics and a critical reflection of common evaluation practice.](https://doi.org/10.1162/tacl_a_00675)
- **09_Deep_PPG_Reiss_2019.pdf** — [Deep PPG: Large-scale heart rate estimation with convolutional neural networks.](https://doi.org/10.3390/s19143079)
- **10_Welch_PSD_1967.pdf** — [The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms.](https://doi.org/10.1109/TAU.1967.1161901)
- **11_Mixup_Zhang_2018.pdf** — [mixup: Beyond empirical risk minimization.](https://openreview.net/forum?id=r1Ddp1-Rb) Published conference paper hosted on arXiv.

Phân trang đã xem bằng bản render: 26 trang, 11 mục tham khảo trên trang 26. Mục lục đã cập nhật số trang và tiêu đề mục 6.3. Gói nộp chỉ có Word và 11 PDF; file đối chiếu này không nằm trong ZIP.
