# Awesome Egocentric Survey — Egocentric Video × 3D Vision 연구 지형

1인칭(egocentric) 비디오와 3D 비전이 만나는 연구를 **축(axis)별로 분류**하고, 논문·데이터셋 사이의 관계(백본, 확장, 학습/평가 데이터, 비교 기준선 등)를 **인터랙티브 그래프**로 정리한 저장소입니다.

- **그래프 보기**: `index.html`을 브라우저로 열거나, GitHub Pages를 켜면 웹에서 바로 볼 수 있습니다.
- **목록으로 보기**: [축별 논문 목록](docs/papers.md) · [연결 목록](docs/edges.md) · [축별 목표와 과제](docs/axes.md) · [검토 대기](docs/review.md)
- **검토 대기 탭**: 페이지 상단의 `검토 대기` 탭(`index.html#review`)에서 arXiv 데일리 스캔이 찾은 미배치 논문을 봅니다.

## 현황

<!-- STATS:START -->
노드 **125**개 · 연결 **128**개 · 축 **11**개 · 축 사이 연결 **68**개 · 2026년 9월 이후 신규 **30**개

| 축 | 이름 | 노드 수 |
| --- | --- | --- |
| B | 기반 모델·데이터 | 9 |
| 1 | 에고 4D/동적 씬 재구성 | 14 |
| 2 | 3D 손·몸·물체 추적과 HOI | 20 |
| 1∩2 | world-grounded 통합 재구성 | 2 |
| 3 | 멀티뷰 에고 캡처·뉴럴 렌더링 | 10 |
| 4 | VLM/MLLM 에고 3D 공간추론 | 13 |
| 5 | 에고 비디오 → 로봇 학습 | 16 |
| 6 | 에고 월드 모델·제어 생성 | 14 |
| 7 | 지속형·스트리밍 에고 3D 메모리 | 7 |
| 8 | 데이터 생성 | 13 |
| 9 | 에고 시선·주의 예측 (2D→3D) | 7 |
<!-- STATS:END -->

## 축 구성

| 축 | 주제 |
| --- | --- |
| B | 기반 모델·데이터 (VGGT, MANO, HaMeR, Ego4D …) |
| 1 | 에고 4D/동적 씬 재구성 |
| 2 | 3D 손·몸·물체 추적과 HOI |
| 1∩2 | world-grounded 통합 재구성 |
| 3 | 멀티뷰 에고 캡처·뉴럴 렌더링 |
| 4 | VLM/MLLM 에고 3D 공간추론 |
| 5 | 에고 비디오 → 로봇 학습 |
| 6 | 에고 월드 모델·제어 생성 |
| 7 | 지속형·스트리밍 에고 3D 메모리 |
| 8 | 데이터 생성 |
| 9 | 에고 시선·주의 예측 (2D→3D) |

## 저장소 구조

```
.
├── index.html          # 인터랙티브 그래프 (D3, 데이터는 빌드 시 임베드)
├── data/
│   ├── nodes.csv       # 논문·데이터셋 (원본 데이터)
│   ├── edges.csv       # 노드 간 관계 (원본 데이터)
│   ├── axes.csv        # 축 정의: 문제·목표·과제·벤치마크·연결
│   ├── review.csv      # 검토 대기 논문 (arXiv 데일리 스캔이 추가)
│   └── graph.json      # 빌드 산출물 (CSV 3개를 합친 JSON)
├── docs/               # 빌드 산출물 (마크다운 표)
└── scripts/build.py    # 검증 + 생성 스크립트
```

**원본은 `data/*.csv` 네 개뿐입니다.** 나머지는 모두 빌드로 생성됩니다.

## 데이터 수정하는 법

1. `data/nodes.csv`, `data/edges.csv`, `data/axes.csv`를 수정합니다 (엑셀·구글시트·텍스트 편집기).
2. 빌드합니다 (Python 3 표준 라이브러리만 사용):
   ```bash
   python3 scripts/build.py          # 검증 후 index.html·docs·README 갱신
   python3 scripts/build.py --check  # 검증만
   ```
3. 커밋합니다.

### 필드 설명

**nodes.csv**

| 필드 | 설명 |
| --- | --- |
| `id` | 고유 ID (엣지에서 참조) |
| `label` / `title` | 그래프 표시 이름 / 정식 제목 |
| `date` | 공개 연월 (`YYYY-MM` 또는 `YYYY`) |
| `venue` | 게재처 |
| `arxiv` | arXiv ID (`2505.11709` 형식, 없으면 빈칸) |
| `axis` / `axis2` | 주 축 / 함께 걸친 축 (쉼표 구분) |
| `isNew` | 2026년 9월 이후 신규 여부 (`Y`/`N`) |
| `status` | 서지 검증 상태: `검증됨` · `2차 확인` · `원문 기준` · `미확인` |
| `note` | 메모 |

**edges.csv** — `source → target`은 "target이 source를 사용/참조함"을 뜻합니다.

| 필드 | 설명 |
| --- | --- |
| `rel` | `backbone` · `extends` · `trains_on` · `evaluates_on` · `compares` · `cross` · `cites` · `part_of` · `captures` · `produces` |
| `evidence` | 근거 수준: `원문` · `확인` · `추정` |
| `note` | 메모 |

**review.csv** — 지형도에 배치하기 전의 후보 논문. `status`는 `대기` · `보류` · `반영` · `제외` 중 하나이며 사용자가 바꿉니다. 지형도에 반영할 때는 `nodes.csv`에 행을 추가하고 여기 `status`를 `반영`으로 바꿉니다.

## GitHub Pages로 공개하기

Settings → Pages → Source: `Deploy from a branch`, Branch: `main` / `(root)` → 저장.
몇 분 뒤 `https://<사용자명>.github.io/<저장소명>/`에서 그래프가 열립니다.

## 주의사항

- `status`가 `검증됨`이 아닌 노드(특히 `미확인`)와 `evidence`가 `추정`인 엣지는 서지·관계가 원문으로 확인되지 않았습니다. 인용 전 원문을 확인하세요.
- 기업 발표(예: Ropedia W0, EgoXperience)의 "first", "SOTA" 주장은 독립 재현 전까지 자체 보고로 취급합니다.
- ICCV는 홀수 해에만 열립니다. 2026년 가을 학회는 ECCV 2026입니다.
