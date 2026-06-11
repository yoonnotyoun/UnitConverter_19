# GREEN Minimal — 최소 구현

Dual Track **Logic 또는 UI** 의 실패 RED 테스트 1건을 통과시키는 최소 구현만 추가한다.

## 필수 선언 (응답 첫 줄)
Phase: green | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}

## Dual Track · BCE
| Track | BCE | 구현 위치 |
|-------|-----|-----------|
| logic | Entity / Control | `src/convert.py` (및 Entity 모듈) |
| ui | Boundary | `UnitConverter.py` — `main()` 만 |

## 자율 실행
- 추가 입력·질문 없이 즉시 수행한다.
- pytest 실패 목록에서 **Track 1건·TC 1건**만 통과시킨다 (해당 Track RED 우선).

## 절차
1. pytest 로 실패 TC·소속 Track 을 확인한다.
2. Track 에 맞는 파일에 **최소 코드**만 추가·수정한다.
3. Control(`convert()`)은 `print` 금지 — dict 만. Boundary(`main()`)는 `convert()` 호출·`print` 만.
4. pytest 로 해당 TC PASS + 동 Track 기존 PASS 유지.
5. 테스트 파일은 수정하지 않는다.

## pytest
    pytest tests/test_convert.py tests/test_main.py -v

## 보고 형식
- Track / BCE / 통과 TC
- 변경 요약 (한 줄)
- pytest 결과: N passed, M failed
- 변경 파일: Track 별 1개 (`src/` 또는 `UnitConverter.py`)

## 금지
- `tests/` 수정
- Boundary 에 변환·검증 로직 (→ Control)
- 양 Track·다중 TC 한꺼번에
- 사용자에게 구현 방향 질문
