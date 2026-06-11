# REFACTOR Smell — 코드 스멜 탐지 (ARRR R⑦)

**역할:** ARRR R단계(Refine ⑦) — 코드 스멜 탐지만, 수정·commit 금지.

## 필수 선언 (응답 첫 줄)
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI

## 전제
- `python -m pytest tests/ -v` 전부 PASS 확인. FAIL이면 중단·보고 (GREEN 먼저).

## 자율 실행
- 추가 입력·질문 없이 즉시 수행한다.
- `src/`, `UnitConverter.py`, `tests/` 를 Logic+UI · BCE 관점에서 검토한다.
- 스멜만 나열한다. **코드 수정·commit 금지.**

## 스멜 표
| 우선순위 | 스멜 | 설명 |
|----------|------|------|
| P0 | Long Method | 한 함수·메서드가 과도하게 길어 SRP·가독성 저하 |
| P0 | Duplicated Code | 동일·유사 로직 반복 |
| P0 | Mysterious Name | 의도 불명 변수·함수·상수명 |
| P1 | Magic Number | 의미 없는 리터럴 (비율·단위 등은 상수화 후보) |
| P1 | ECB 위반 | Entity·Control·Boundary 역할 침범·혼입 |
| P2 | Feature Envy | 타 객체 데이터를 과도하게 참조하는 메서드 |

## Change Budget (후보 제안 시 준수)
- 파일 ≤ 3
- 클래스 ≤ 1
- 메서드 ≤ 3

## 절차
1. pytest 전체 PASS 확인 (FAIL → 중단).
2. 위 스멜 표 기준으로 P0/P1/P2 분류·위치·영향 TC 기록.
3. Change Budget 내 `/refactor-safe` 후보 1~3개 제안.

## 출력
1. **스멜 표** — 우선순위 · 스멜 · 위치(파일·함수) · 영향 TC
2. **`/refactor-safe` 후보 1~3개** — Track · BCE · 스멜 · Change Budget 적합 여부

## 다음 안내
- **P0 1개만** 골라 `/refactor-safe` 실행.

## 금지
- `src/`·`tests/`·`UnitConverter.py` 코드 수정
- commit
- 사용자에게 Track·스멜 선택 질문
