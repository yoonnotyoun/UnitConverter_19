# Golden Master — 레거시 기준 대조

Boundary 레거시(`UnitConverter.py`)와 Control 목표(`convert()`)를 golden master 로 대조한다. 코드 변경 없음.

## 필수 선언 (응답 첫 줄)
Phase: green | Target: {convert|main} | Track: {logic|ui} | BCE: {Control|Boundary}

## Dual Track · BCE
| BCE | golden master | 목표 |
|-----|---------------|------|
| Boundary | `UnitConverter.py` `main()` 현행 출력 | PRD CLI §3 |
| Control | `convert()` dict 계약 | `.cursorrules` |

## 자율 실행
- 추가 입력·질문 없이 즉시 수행한다.
- 레거시·계약·갭 대조표와 샘플 3~5건을 스스로 작성한다.

## 절차
1. Boundary: `main()` 입·출력 흐름 추출.
2. Control: `convert()` pass/fail 계약과 대조.
3. 입력→legacy vs 목표 표, 갭(음수·줄 수·error.type·로직 위치) 정리.
4. Logic/UI Track 각 TC 반영 권고 1줄.

## SSOT
- Control: `.cursorrules` · PRD §3 `convert()`
- Boundary 참조: `UnitConverter.py` · PRD §9 갭

## 보고 형식
- golden master 샘플 표 (Boundary / Control)
- Track 별 갭·권고
- 변경 파일: 없음

## 금지
- `tests/`·`src/`·`UnitConverter.py` 수정
- 레거시를 SSOT 로 간주
- 사용자에게 샘플 선택 질문
