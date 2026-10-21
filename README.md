# Human Activity Recognition on ESP32

Classify eight daily activities from wrist PPG and accelerometer signals in
PPG-DaLiA, compare Random Forest and CNN models, and run inference on ESP32.

- [Pipeline, experiment design and results](source/README.md)
- [Compact notebook: download, preprocessing, E1–E6 seed 42, six test confusion matrices](source/notebooks/har_complete_pipeline.ipynb)
- [Measured ESP32 latency](source/results/esp32_latency_comparison.csv)
- [ESP32 firmware](source/firmware/)
- [Final report](LuongNguyenThanhHung_final.docx)
- [Presentation](LuongNguyenThanhHung_final.pptx)

Mean processing time on the same 1,000 recorded test windows was 88.35 ms
for E6 (multikernel 1D CNN) and 1,211.27 ms for E1 (Random Forest).
USB transfer and sensor acquisition are excluded. The test split contains
three participants; test results were inspected during development, as
documented in the report. These results are not a live sensor benchmark.

## Restore experiment artifacts

Checkpoints and generated experiment records are supplied as a release asset,
keeping the Git repository focused on code and the final reports. From the
repository root, with the GitHub CLI installed:

```bash
gh release download artifacts-v1 \
  --repo Hung0Toy2810/esp32-human-activity-recognition \
  --pattern esp32-artifacts.tar.gz
tar -xzf esp32-artifacts.tar.gz
rm esp32-artifacts.tar.gz
```

The archive restores `source/artifacts/` at the expected paths. Raw PPG-DaLiA
data is not included; the notebook downloads it separately.

Author: Luong Nguyen Thanh Hung.
