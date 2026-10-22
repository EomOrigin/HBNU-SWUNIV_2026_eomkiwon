<div align="center">

# Ki-won Eom &nbsp;<sub>엄기원</sub>

Undergraduate student, Computer Engineering, Hanbat National University · Undergraduate researcher, AIM Lab

[Email](mailto:eomkiwon1528@gmail.com) &nbsp;/&nbsp; [GitHub](https://github.com/EomOrigin) &nbsp;/&nbsp; [Kaggle](https://www.kaggle.com/kiwoneom) &nbsp;/&nbsp; [DACON](https://dacon.io/myprofile/497780/home)

[한국어](README.md) | **English**

</div>

I am an undergraduate student in Computer Engineering at Hanbat National University and have been an undergraduate researcher in the AIM Lab since February 2024. I work on finding objects that are only a few pixels wide in satellite and aerial images, using both optical and SAR data. I have published two first-author papers in KCI-indexed journals, and I am preparing to submit SPOT-DETR, a co-first-author manuscript on tiny object detection.

<sub>Entry for the 2026 Portfolio Competition of the Department of Computer Engineering, Hanbat National University</sub>

## News

- **2026.10** &nbsp; Finished the SPOT-DETR manuscript; preparing to submit it.
- **2026.03** &nbsp; YOLO-Dos published in the Journal of IKEEE.
- **2025** &nbsp; ViT-based deepfake detection paper published in the Journal of Digital Forensics.
- **2025** &nbsp; 16th of 271 teams in the finals of the SW-Centered University AI Competition.
- **2024** &nbsp; Grand Prize, 6th AI SPARK Challenge (Korea R&D Special Zones).
- **2024.02** &nbsp; Joined the AIM Lab as an undergraduate researcher.

## Featured research

<a href="SPOT-DETR_EN.md"><img src="assets/figures/Fig1_concept.png" alt="Pipeline comparison between existing DETR-based detectors and SPOT-DETR"></a>

**[SPOT-DETR: Tiny object detection in aerial images using high-resolution feature refinement and off-grid candidate memory](SPOT-DETR_EN.md)**

Vehicles and people in aerial images are often only a few pixels wide. In DETR-based detectors they shrink to one or two feature-map cells and rarely line up with candidates that start at cell centers. SPOT-DETR handles both problems on one high-resolution path that starts from the stride-4 feature: SGS refines the feature, and ATOM generates off-grid candidates from it.

| | AI-TOD AP | AI-TOD-v2 AP | AP<sub>vt</sub> (v2) | Very tiny candidate recall |
|---|:---:|:---:|:---:|:---:|
| Baseline (SMWG-DETR) | 32.1 | 29.8 | 15.7 | 38.5% |
| **SPOT-DETR** | **37.6** | **33.3** | **20.8** | **67.1%** |

This is the highest AP on both datasets among the detectors we retrained under the same protocol. As co-first author, I defined the problem, implemented the model, ran the comparisons and wrote the manuscript. The method, full results, analysis and limitations are on the [project page](SPOT-DETR_EN.md).

## Publications

I mostly work on object detection and segmentation in remote sensing images. <sup>†</sup> denotes equal contribution.

<table>
<tr>
<td width="34%" valign="top"><a href="SPOT-DETR_EN.md"><img src="assets/thumbs/spot_detr.png" width="260" alt="SPOT-DETR"></a></td>
<td valign="top">
<a href="SPOT-DETR_EN.md"><b>SPOT-DETR: Tiny object detection in aerial images using high-resolution feature refinement and off-grid candidate memory</b></a><br>
<b>Ki-won Eom</b><sup>†</sup>, Cheoneum Park<sup>†</sup>, Eunkyung Kim, Haneol Jang<br>
<i>Manuscript in preparation</i>, 2026<br>
<a href="SPOT-DETR_EN.md">project page</a> / <a href="paper/SPOT_DETR_manuscript_20261022.pdf">manuscript</a>
<p>Feature refinement and off-grid candidate generation on one stride-4 path give the highest AP on AI-TOD and AI-TOD-v2 among the retrained detectors.</p>
</td>
</tr>
<tr>
<td width="34%" valign="top"><a href="https://doi.org/10.7471/ikeee.2026.30.1.171"><img src="assets/thumbs/yolo_dos.png" width="260" alt="YOLO-Dos"></a></td>
<td valign="top">
<a href="https://doi.org/10.7471/ikeee.2026.30.1.171"><b>YOLO-Dos: Improving YOLO-Based SAR Object Detection Performance via a Speckle Suppression Module</b></a><br>
<b>Ki-won Eom</b>, Eunkyung Kim, Haneol Jang<br>
<i>Journal of IKEEE</i>, 30(1):171–181, 2026 · KCI-indexed<br>
<a href="https://doi.org/10.7471/ikeee.2026.30.1.171">DOI</a> / <a href="https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003322680">KCI</a>
<p>Replacing the YOLOv8 input stem with a speckle suppression module (log transform, wavelet split, high-frequency attention) raises mAP@50:95 by 5.75 points and F1 by 3.21 points on HRSID.</p>
</td>
</tr>
<tr>
<td width="34%" valign="top"><a href="https://doi.org/10.22798/KDFS.2025.19.4.116"><img src="assets/thumbs/rwm_deepfake.png" width="260" alt="Region Weight Module"></a></td>
<td valign="top">
<a href="https://doi.org/10.22798/KDFS.2025.19.4.116"><b>ViT-based Deepfake Detection via Regional Emphasis Weights on Eyes, Nose, and Mouth</b></a><br>
<b>Ki-won Eom</b>, Dong-Su Kim, Tae-Woo Oh, Haneol Jang<br>
<i>Journal of Digital Forensics</i>, 19(4):116–131, 2025 · KCI-indexed<br>
<a href="https://doi.org/10.22798/KDFS.2025.19.4.116">DOI</a> / <a href="https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003243484">KCI</a> / <a href="https://github.com/EomOrigin/HBNU-SWUNIV_2025_eomkiwon">2025 portfolio</a>
<p>A Region Weight Module adds learnable weights for the eyes, nose and mouth at the ViT patch-embedding stage. On FaceForensics++ it improves ACER by 7.94% and AUC by about 3% over plain ViT.</p>
</td>
</tr>
</table>

## Honors

- **Grand Prize**, 6th AI SPARK Challenge (Korea R&D Special Zones), wildfire detection from multispectral satellite imagery, 2024 · [competition](https://aifactory.space/task/2723/overview)
- **16th of 271 teams**, finals of the SW-Centered University AI Competition, 2025 · [competition](https://dacon.io/competitions/official/236473/overview/description)
- **2nd of 13 teams** (2024) and **5th of 17 teams** (2025), preliminaries of the SW-Centered University AI Competition
- **2nd place**, cloud segmentation in satellite imagery, Kaggle challenge of the Hanbat National University AI course, 2025 · [competition](https://www.kaggle.com/competitions/clouds-segmentation-2025/overview)

## Experience and education

- **2024.02 – present** &nbsp; Undergraduate researcher, AIM Lab, Hanbat National University
- **2023.03 – present** &nbsp; B.S. student, Department of Computer Engineering, Hanbat National University

---

<sub>Layout adapted from [Jon Barron](https://jonbarron.info/)'s academic website.</sub>
