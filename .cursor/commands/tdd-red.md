# TDD RED — 실패 테스트 먼저

Dual Track **Logic 또는 UI** 의 새 동작을 검증하는 실패 테스트를 `tests/` 에만 작성한다.

## 필수 선언 (응답 첫 줄)
Phase: red | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}

## Dual Track · BCE
| Track | BCE | Target | 테스트 | RED 금지 구현 |
|-------|-----|--------|--------|---------------|
| logic | Entity | 단위·비율·변환 규칙 | `tests/test_convert.py` | `src/` |
| logic | Control | `convert()` | `tests/test_convert.py` | `src/convert.py` |
| ui | Boundary | `main()` | `tests/test_main.py` | `UnitConverter.py` |

## 자율 실행
- 추가 입력·질문 없이 즉시 수행한다.
- 미커버 Track·케이스 1건의 **완전한 assert** 테스트를 스스로 작성한다 (Logic 우선).

## 절차
1. Track·BCE·입력·기대 출력(`status`/`lines`/`error` 또는 CLI 출력)을 확정한다.
2. 해당 테스트 파일에 AAA 테스트 1개를 추가한다.
3. pytest 로 FAIL 을 확인한다.
4. 통과시키려 하지 않는다. RED 는 실패가 목표다.

## pytest
    pytest tests/test_convert.py tests/test_main.py -v

## 보고 형식
- Track / BCE / 테스트 함수명
- 입력·기대 출력 요약
- pytest 결과: FAIL (이유 한 줄)
- 변경 파일: `tests/` 만

## 금지
- 해당 Track 구현 파일 수정 (logic→`src/`, ui→`UnitConverter.py`)
- assert 완화 / skip / xfail
- 한 번에 여러 케이스·양 Track
