# Export Transcript — UnitConverter_19 Mom Test Session

**Session ID:** 55baecc9-97be-47d2-af8f-d45c74bc7090  
**Exported:** 2026-06-11  
**Project:** UnitConverter_19

---

## Turn 1 — User

```
## Mom Test 워크북 — UnitConverter_19
### 페르소나:
### 인터뷰 답변 (과거 사실):
### 표면 문제 (금지 — 솔루션 섞인 문장):
### 진짜 문제 (한 문장):
```

## Turn 1 — Assistant

워크북 초안 제공 (인테리어 시공업 페르소나 예시). 저장소에는 Mom Test 인터뷰 기록 없음 확인. 워크샵용 예시 페르소나·과거 사실·표면/진짜 문제 템플릿 작성.

---

## Turn 2 — User

```
Mom test 인터뷰를 진행해.
너는 [페르소나: 이 코드베이스를 사용하는 실제 개발자 역할]
규칙:
- 코드를 이미 사용해 본 경험이 있는 것처럼 행동한다.
- 칭찬하거나 비판하지 말고 실제 사용 경험을 설명한다.
- 내가 기능 아이디어를 제안해도 평가하지 말고 현재의 불편함과 업무 흐름만 이야기한다.
- 답변은 과거 경험 기반으로 한다.
- "그 기능이 있으면 좋을 것 같다"보다 "현재는 어떻게 하고 있는지"를 우선한다.

내가 질문 시 각 질문에 아래와 같이 평가를 먼저 하고, 준수했을 시에만 대답해.
Mom test 준수/위반 표시
위반 질문은 왜 나쁜지, mom test 준수하도록 고친 버전 1줄 제안
```

## Turn 2 — Assistant

인터뷰 시작. 페르소나: README 요구사항 보며 `UnitConverter.py` 실행·수정한 백엔드 개발자. 질문 시 준수/위반 평가 → 개선 질문 → 답변 순서 안내.

---

## Turn 3 — User

```
최근 이 코드에서 가장 짜증났던 점은 뭐야?
```

## Turn 3 — Assistant

**Mom test: 준수** (약함)

**개선 질문:** README 요구사항 맞추려고 마지막으로 `UnitConverter.py` 실행·수정했을 때, 그때 어디서 시간이 걸렸어?

**답변 (페르소나):**
- 수요일: cubit 추가 시 `elif`·상수·출력 손수 추가
- 화요일: TC 6회 수동 실행·재입력, 소수 자릿수 대조
- 금요일: `feet:-1` README와 불일치 — TC 메모
- 현재: 1~2값은 스크립트, 여러 케이스는 엑셀

---

## Turn 4 — User

```
코드 탐색할 때 가장 자주 다시 확인하는 정보는 뭐야?
```

## Turn 4 — Assistant

**Mom test: 준수**

**개선 질문:** `UnitConverter.py` 열어 README랑 맞출 때, 마지막으로 어떤 숫자·규칙을 다시 찾아봤어?

**답변 (페르소나):**
- 변환 비율 `3.28084`, `1.09361` ↔ 코드 상수
- 지원 단위 이름 `meter`/`feet`/`yard`, `unit:value` 포맷
- README 기본 vs 추가 요구사항 구현 여부
- meter 기준 환산 흐름 (16~28줄)

---

## Turn 5 — User

```
마지막으로 새로운 단위를 추가했을 때 어떤 파일들을 수정했지?
```

## Turn 5 — Assistant

**Mom test: 준수**

**답변 (페르소나):**
- 수요일 cubit 시도 — 수정: `UnitConverter.py`만
- README는 참조만, 설정/테스트 파일 없음
- cubit 변경은 로컬 되돌림 또는 미커밋

---

## Turn 6 — User

```
입력 형식과 다른 걸 넣어서 불편했던 적은 없어?
```

## Turn 6 — Assistant

**Mom test: 준수 (약함)**

**개선 질문:** `unit:value` 형식이랑 다르게 넣어 막힌 마지막 경우, 뭐 넣었고 화면에 뭐가 나왔어?

**답변 (페르소나):**
- `2.5 meter` → Invalid format
- `meters:2.5` → Unknown unit
- `feet 8.2` → Invalid format
- `meter:abc` → Invalid number
- `meter:-1` → 출력됨 (README 갭)
- 현재: 실행 전 `meter:2.5` 형태로 미리 변환

---

## Turn 7 — User

```
동작 검증 시 불편한 점이 있다면 왜 불편하고 그게 시간을 얼마나 잡아먹는지 설명해줘
```

## Turn 7 — Assistant

**Mom test: 준수 (약함)**

**개선 질문:** 지난번 README/TC 맞추려고 실행 확인했을 때, 처음 켜서 마지막 케이스까지 몇 분 걸렸고 어디서 멈춰 있었어?

**답변 (페르소나):**
- 화요일 오후 TC 6케이스: **25~30분**
  - 수동 실행·재입력: 15~18분
  - 소수 자릿수: 5~7분
  - 오타: 3~5분
  - README 갭: 5분
- 엑셀 동일 케이스: 3~5분
- TC 파일 없음 — 검증 = 수동 실행 + 눈

---

## Turn 8 — User

```
이제 mom test를 종료하고 표면 문제 vs 진짜 문제를 정의해.
추가적으로 mom test 증거도 3줄 정도로 정리해줘.
```

## Turn 8 — Assistant

**표면 문제 (5건):** 설정 JSON, OCP 리팩터링, pytest, 자연스러운 CLI, JSON/CSV 출력 — 모두 솔루션 섞임

**진짜 문제:** README 기준 맞추기·검증 시 코드↔문서 반복 확인, CLI 수동 실행·재입력, 엑셀 눈 대조 → 재작업·25~30분/세션

**증거 3줄:**
1. 화요일 TC 6케이스 25~30분 vs 엑셀 3~5분
2. 수요일 cubit — `UnitConverter.py`만 수정
3. `feet:-1` README 불일치, README 체크리스트 반복 확인

---

## Turn 9 — User

```
진짜 문제 → R-G-I-O + 주제 1문장 + 성공 기준
```

## Turn 9 — Assistant

**주제:** README 기준 검증·확장 시 반복 수동 확인과 끊기는 CLI 흐름 → 재작업·시간 손실

**R-G-I-O:** Reality / Goal / Issue(5항) / Outcome 정리

**성공 기준 5항:** 검증 5분 이내, 재작업 감소, 단위 추가 한곳 정의, TC 자동 검증, README 갭 해소

---

## Turn 10 — User

```
Report 폴더에 보고서로보내고 Prompting 폴더에 Export Transcript해줘
두 폴더 다 파일 접두어는 01_ 로 시작하여 추가될 때마다 숫자 증가
```

## Turn 10 — Assistant

`Report/01_MomTest_Report.md`, `Prompting/01_Export_Transcript.md` 생성.

---

## Session Metadata

| Field | Value |
|-------|-------|
| Total turns | 10 |
| Interview questions | 5 |
| Persona | UnitConverter_19 개발자 |
| Code reviewed | `UnitConverter.py`, `README.md` |
| Mom test compliance | 5/5 준수 (3건 약함) |

---

*End of transcript*
