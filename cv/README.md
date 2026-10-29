# CV 원본

[CV](../CV.md) · [CV (English)](../CV_EN.md)

`cv_ko.json`과 `cv_en.json`이 CV의 원본입니다. 내용을 고친 뒤 아래 명령을 실행하면 `CV.md`, `CV_EN.md`와 PDF 두 개가 함께 다시 만들어집니다.

```bash
python3 scripts/build_cv.py
```

PyMuPDF와 나눔고딕(`NanumGothic-Regular.ttf`, `NanumGothic-Bold.ttf`)이 필요합니다. 글꼴은 `cv/fonts/`에 두며 저장소에는 올리지 않습니다.
