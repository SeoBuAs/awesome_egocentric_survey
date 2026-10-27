---
name: arxiv-daily-scan
description: 에고센트릭 비디오 × 3D 비전 분야의 최근 arXiv 논문을 훑어, 기존 지형도(data/*.csv)에 없는 논문을 축별로 보고하고 새 축이 필요한지 제안만 한다. "오늘 arXiv 확인", "데일리 스캔", "새 논문 보고" 또는 매일 루틴이 호출할 때 사용. 저장소 파일은 수정하지 않는다.
---

# arXiv 데일리 스캔 (보고·제안 전용)

## 원칙

- **읽기 전용.** `data/*.csv`, `index.html`, `docs/` 등 저장소 파일을 수정·커밋·푸시하지 않는다. 노드 추가와 축 신설은 사용자가 승인한 뒤 별도로 한다.
- **확인한 것만 쓴다.** 제목·저자·arXiv ID·날짜는 검색 결과나 원문에서 본 것만 적는다. 초록을 직접 못 읽었으면 `검색 스니펫 기준`이라고 표시한다. 추측으로 ID를 만들지 않는다.
- 결과는 한국어로 쓴다.

## 절차

1. **현재 지형 파악**
   - `data/axes.csv`에서 축 목록(축 번호·이름·문제·목표)을 읽는다.
   - `data/nodes.csv`의 `arxiv` 열을 모아 이미 등록된 ID 집합을 만든다. `title`도 함께 봐서 ID 없는 노드와의 중복을 거른다.
   - 이 대화에 이전 데일리 보고가 있으면, 거기서 이미 보고한 ID도 제외한다.

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
