# REFACTOR Safe — 동작 유지 리팩터

**역할:** `/refactor-smell` 표에서 선택한 스멜 **1개만** Safe Refactor 실행.

## 필수 선언 (응답 첫 줄)
Phase: refactor | Layer: entity | Track: Logic

## 전제
- `/refactor-smell`에서 **P0 스멜 1건**이 확정되어 있다.
- `python -m pytest tests/ -v` 전부 PASS. FAIL이면 GREEN 먼저, 중단·보고.

## 원칙 (동작·계약 불변)
- **입출력·예외·int[6] 1-index** 변경 금지 (`convert()` dict → golden 직렬화 포맷 유지).
- **E001~E005 emit** 금지 — 에러 코드·`error` dict·`lines` 계약 변경 없음.
- **Change Budget** 준수 (파일 ≤ 3 · 클래스 ≤ 1 · 메서드 ≤ 3).
- **기능 추가·버그 수정** 금지 — 별도 GREEN 단계에서 수행.

## 자율 실행
- 추가 입력·질문 없이 즉시 수행한다.
- 확정된 스멜 **1건만** 리팩터. 다중 스멜·양 Track 동시 금지.

## 절차
1. pytest 전체 PASS 확인 (FAIL → 중단).
2. 확정 스멜 1건을 Change Budget 내에서 구조만 개선 (`src/` 중심, ECB 경계 유지).
3. 완료 후 검증:
   ```bash
   python -m pytest tests/ -v
   ```
   - golden 연결 TC는 **UPDATE_GOLDEN 없이** matched PASS 확인.

## golden diff 처리
| 구분 | 조치 |
|------|------|
| **의도적** (계약 변경이 아닌 직렬화·표현만) | ISS 문서화 + `UPDATE_GOLDEN=1`로 재캡처 |
| **비의도** (동작·계약 drift) | 즉시 롤백, 리팩터 재검토 |

- REFACTOR 기본 목표: golden diff **없음** (matched, UPDATE_GOLDEN 없음).

## 보고 형식
| 항목 | 내용 |
|------|------|
| 스멜 | `/refactor-smell`에서 선택한 P0 1건 |
| 변경 요약 | before → after (구조만) |
| pytest | N passed / failed |
| golden | matched `yes` / `no` (UPDATE_GOLDEN 사용 여부) |

## 금지
- `tests/` 수정 (golden diff 시 `UPDATE_GOLDEN=1` 재캡처만 허용, assert·TC 변경 금지)
- 입출력·예외·int[6]·E001~E005 변경
- 기능 추가·버그 수정 (GREEN 전용)
- Change Budget 초과·다중 스멜 동시
- commit (사용자 명시 요청 시만)
- 사용자에게 스멜·대상 선택 질문
