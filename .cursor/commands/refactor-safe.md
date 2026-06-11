# REFACTOR Safe — 동작 유지 리팩터

Dual Track **Logic 또는 UI** 에서 pytest PASS 유지하며 BCE 경계를 지키고 구조만 개선한다.

## 필수 선언 (응답 첫 줄)
Phase: refactor | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}

## Dual Track · BCE
| Track | BCE | 리팩터 대상 |
|-------|-----|-------------|
| logic | Entity / Control | `src/` |
| ui | Boundary | `UnitConverter.py` `main()` |

## 자율 실행
- 추가 입력·질문 없이 즉시 수행한다.
- `/refactor-smell` 스멜 **1건**만 해당 Track·BCE 에 안전하게 적용한다.

## 절차
1. 해당 Track pytest 전체 PASS 확인 (FAIL → GREEN 먼저, 중단·보고).
2. 스멜 1건만 리팩터. **BCE 경계 유지** (Boundary→Control 로직 이전 금지).
3. 공개 API·동작·계약 변경 금지.
4. pytest 재확인.

## pytest
    pytest tests/test_convert.py tests/test_main.py -v

## 보고 형식
- Track / BCE / 스멜
- 변경 요약 (before → after)
- pytest: all passed (해당 Track)
- 변경 파일: Track 별 1개

## 금지
- `tests/` 수정
- BCE 역할 침범 (Boundary 에 Entity·Control 로직)
- 양 Track·다중 스멜 동시
- 사용자에게 대상 질문
