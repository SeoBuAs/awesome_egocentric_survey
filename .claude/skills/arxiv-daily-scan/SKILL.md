---
name: arxiv-daily-scan
description: 에고센트릭 비디오 × 3D 비전 분야의 최근 arXiv 논문을 훑어, 기존 지형도(data/*.csv)에 없는 논문을 축별로 보고하고 새 축이 필요한지 제안만 한다. 찾은 논문은 data/review.csv(검토 대기)에만 추가한다. "오늘 arXiv 확인", "데일리 스캔", "새 논문 보고" 또는 매일 루틴이 호출할 때 사용.
---

# arXiv 데일리 스캔 (보고·제안 + 검토 대기 목록 갱신)

## 원칙

- **쓰기는 `data/review.csv` 한 곳뿐.** 찾은 논문은 지형도에 배치하지 않고 검토 대기 목록에만 넣는다. `nodes.csv`·`edges.csv`·`axes.csv`, `index.html`의 코드, 스킬 파일은 수정하지 않는다. 노드 추가와 축 신설은 사용자가 승인한 뒤 별도로 한다.
- `review.csv`에 이미 있는 행(상태가 보류·반영·제외인 것 포함)은 고치거나 지우지 않는다. 상태는 사용자가 정한다.
- **확인한 것만 쓴다.** 제목·저자·arXiv ID·날짜는 검색 결과나 원문에서 본 것만 적는다. 초록을 직접 못 읽었으면 `검색 스니펫 기준`이라고 표시한다. 추측으로 ID를 만들지 않는다.
- 결과는 한국어로 쓴다.

## 절차

1. **현재 지형 파악**
   - `data/axes.csv`에서 축 목록(축 번호·이름·문제·목표)을 읽는다.
   - `data/nodes.csv`의 `arxiv` 열을 모아 이미 등록된 ID 집합을 만든다. `title`도 함께 봐서 ID 없는 노드와의 중복을 거른다.
   - `data/review.csv`의 `arxiv` 열도 제외 목록에 넣는다(이미 검토 대기 중이거나 사용자가 처리한 논문).

2. **검색** (WebSearch, 가능하면 arxiv.org 직접 조회)
   - 기간: 최근 1~3일. arXiv ID의 앞 4자리(YYMM)가 이번 달 또는 지난달인 것만 후보로 둔다.
   - 질의는 축마다 1개 이상 + 범용 질의 몇 개. 예시:
     - 범용: `arXiv egocentric 3D`, `egocentric video reconstruction arXiv`, `first-person video 4D`
     - 축 B/1: `egocentric feed-forward 4D reconstruction`, `streaming VGGT egocentric`, `dynamic gaussian splatting egocentric`
     - 축 2: `egocentric 3D hand pose world space`, `hand-object interaction reconstruction egocentric`
     - 축 3: `multi-view egocentric dataset Aria`
     - 축 4: `egocentric spatial reasoning VLM benchmark`
     - 축 5: `egocentric human video robot learning VLA`
     - 축 6: `egocentric world model video generation hand control`
     - 축 7: `egocentric 3D memory long video object`
     - 축 8: `synthetic egocentric data generation`
     - 축 9: `egocentric gaze forecasting 3D`
     - 축이 새로 생겼으면 그 축의 질의도 추가한다.
   - arxiv.org 접속이 막혀 있으면 WebSearch 결과만 쓰고, 보고서 첫 줄에 그 사실을 적는다.

3. **분류**
   - 각 후보를 기존 축 하나(주 축)와 선택적인 보조 축에 배정한다.
   - 기존 노드와의 관계(백본·확장·비교·데이터)가 보이면 `source → target (rel)` 형태로 적는다. 근거가 초록 수준이면 `추정`이라고 표시한다.
   - 어느 축에도 잘 맞지 않는 논문은 "미분류"로 따로 모은다.

4. **새 축 판단** (제안만)
   - 아래 조건을 **모두** 만족할 때만 새 축을 제안한다.
     - 미분류 논문(오늘 것 + 이 대화의 이전 보고 누적)이 3편 이상이다.
     - 기존 축의 `problem`/`goal`로 설명되지 않는 공통 문제가 있다.
     - 기존 축 하나를 쪼개는 편이 나으면, 새 축 대신 "축 X 분할"로 제안한다.
   - 조건을 못 채우면 "새 축 제안 없음"이라고 쓰고, 후보 주제가 있으면 "관찰 중"으로 남긴다.

## 검토 대기 목록 갱신

보고서를 쓴 뒤, 신규 후보를 `data/review.csv` 끝에 행으로 추가한다.

| 열 | 값 |
| --- | --- |
| `arxiv` | `2610.12345` 형식. ID를 확인 못 한 논문은 넣지 말고 보고서에만 적는다 |
| `title` | 정식 제목 |
| `found` | 오늘 날짜 `YYYY-MM-DD` (한국시간) |
| `axis_guess` / `axis2_guess` | 잠정 주 축 / 보조 축(쉼표 구분). 모르면 빈칸 |
| `status` | 항상 `대기` |
| `note` | 확인 수준(`검색 스니펫 기준`, `초록 확인` 등)과 한 줄 메모 |

그다음:

1. `python3 scripts/build.py`로 검증·빌드한다. 실패하면 행을 고쳐 다시 빌드하고, 그래도 안 되면 커밋하지 말고 보고서에 오류를 적는다.
2. 바뀐 파일(`data/review.csv`, `data/graph.json`, `index.html`, `docs/review.md`)만 커밋한다. 메시지: `Review queue: YYYY-MM-DD 스캔 N편`.
3. `git push origin main`. 거절되면 `git pull --rebase origin main` 후 다시 빌드·푸시한다.
4. 신규 후보가 0편이면 커밋하지 않는다.

페이지의 **검토 대기** 탭(`index.html#review`)에 이 목록이 나타난다.

## 보고 형식

```
# arXiv 데일리 · YYYY-MM-DD

검색 범위: (기간, 질의 수, arxiv.org 직접 조회 가능 여부)

## 요약
- 신규 후보 N편 (축별: B a, 1 b, 2 c, …) / 미분류 m편
- 오늘 꼭 볼 것 1~3편과 그 이유 한 줄씩

## 축별 신규 논문
### 축 X · 이름
| arXiv | 제목 | 날짜 | 한 줄 요약 | 기존 노드와의 관계 | 확인 수준 |

## 미분류
(같은 표)

## 새 축 제안
- 제안 / 제안 없음 / 관찰 중
- 제안이면: 축 이름, 핵심 문제, 목표, 근거 논문(3편 이상), 기존 축과의 경계, 연결될 축

## 반영하려면
사용자가 승인하면 추가할 nodes.csv / edges.csv 행 초안 (CSV 그대로)
```

신규 후보가 0편이면 요약에 그렇게 쓰고 짧게 끝낸다.

## 알림

PushNotification 도구가 있으면 보고를 마친 뒤 "arXiv 데일리: 신규 N편, 새 축 제안 있음/없음" 한 줄로 알린다.
