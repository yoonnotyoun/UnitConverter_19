# RED Test Plan — 다음 케이스 선정

Dual Track TDD **Logic 또는 UI** 트랙에서 RED 전 **테스트 1건** 계획만 수립한다. 코드·파일 변경 없음.

## 필수 선언 (응답 첫 줄)
Phase: red | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}

## Dual Track · BCE
| Track | BCE | Target | 테스트 | 구현 |
|-------|-----|--------|--------|------|
| logic | Entity | 단위·비율·순수 변환 | `tests/test_convert.py` | `src/` (Entity) |
| logic | Control | `convert()` 오케스트레이션 | `tests/test_convert.py` | `src/convert.py` |
| ui | Boundary | `main()` 입·출력 | `tests/test_main.py` | `UnitConverter.py` |

## 자율 실행
- 추가 입력·질문 없이 즉시 수행한다.
- 미커버 FR/NFR·트랙 상태를 읽고 **Track 1개·BCE 1개·케이스 1건**을 스스로 고른다.
- Logic 미완료 시 Logic 우선, Logic GREEN 후 UI.

## 절차
1. `tests/`, `docs/PRD.md` §4·§7, `.cursorrules` 로 Track·미커버 1건을 고른다.
2. Track 에 맞는 Target·BCE·입력·기대 출력을 확정한다.
3. 테스트 함수명(안)과 AAA 개요를 작성한다.
4. 파일은 변경하지 않는다. 계획만 보고한다.

## 보고 형식
- Track / BCE / Target
- FR/NFR ID, 입력·기대 출력
- 제안 테스트 함수명·파일
- 선정 이유 (한 줄)
- 변경 파일: 없음

## 금지
- `tests/`·`src/`·`UnitConverter.py` 수정
- 한 번에 여러 케이스·양 Track 동시
- 사용자에게 Track·케이스 선택 질문
