# REFACTOR Smell — 코드 냄새 진단

Dual Track **Logic/UI** · BCE 관점에서 스멜만 진단한다. 수정 없음.

## 필수 선언 (응답 첫 줄)
Phase: refactor | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}

## Dual Track · BCE
| Track | BCE | 진단 대상 | 흔한 스멜 |
|-------|-----|-----------|-----------|
| logic | Entity | 단위·비율 | 매직넘버, 하드코딩 단위 |
| logic | Control | `convert()` | God function, Boundary 로직 혼입 |
| ui | Boundary | `main()` | 변환·검증 로직, `convert()` 미사용 |

## 자율 실행
- 추가 입력·질문 없이 즉시 수행한다.
- Track·BCE 별 스멜 1~5건을 스스로 나열한다 (SRP·OCP·BCE 경계 위반 우선).

## 절차
1. `src/convert.py`, `UnitConverter.py` 를 Track·BCE·NFR-01·NFR-02 관점에서 검토한다.
2. 스멜별 위치·위반 BCE·영향 TC 를 적는다.
3. `/refactor-safe` 후보를 Track·BCE·우선순위와 함께 제안한다.

## 보고 형식
- Track / BCE / 스멜 목록
- `/refactor-safe` 권고 1건
- 변경 파일: 없음

## 금지
- `tests/`·구현 파일 수정
- BCE 경계 무시한 대개편만 제안
- 사용자에게 Track·스멜 선택 질문
