# RED Skeleton — AAA 골격만

Dual Track **Logic 또는 UI** 검증용 AAA 골격 테스트 1개를 `tests/` 에만 추가한다.

## 필수 선언 (응답 첫 줄)
Phase: red | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}

## Dual Track · BCE
| Track | BCE | 테스트 파일 |
|-------|-----|-------------|
| logic | Entity / Control | `tests/test_convert.py` |
| ui | Boundary | `tests/test_main.py` |

## 자율 실행
- 추가 입력·질문 없이 즉시 수행한다.
- 미커버 Track·케이스 1건의 골격을 스스로 작성한다 (Logic 우선).

## 절차
1. Track·BCE·미커버 케이스 1건을 고른다.
2. 해당 테스트 파일에 `# Arrange` / `# Act` / `# Assert` 골격 1개를 추가한다.
3. Assert 는 `pytest.fail("RED skeleton")` 또는 `# TODO` 만 둔다.
4. pytest 로 FAIL 을 확인한다.

## pytest
    pytest tests/test_convert.py tests/test_main.py -v

## 보고 형식
- Track / BCE / 테스트 함수명
- pytest 결과: FAIL (이유 한 줄)
- 변경 파일: `tests/` 만

## 금지
- `src/`·`UnitConverter.py` 수정
- 완전한 assert (→ `/tdd-red`)
- assert 완화 / skip / xfail
- 한 번에 여러 케이스·양 Track
