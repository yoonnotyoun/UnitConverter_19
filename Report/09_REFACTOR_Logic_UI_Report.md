# Report — UnitConverter_19 REFACTOR Logic · UI Boundary (ARRR R⑦)

**프로젝트:** UnitConverter_19  
**일자:** 2026-06-11  
**주제:** `/refactor-smell` · `/refactor-safe` 후보 A·B·C — Logic Control/Entity 분리 + Boundary `convert()` 위임  
**대상:** `src/convert.py`, `UnitConverter.py`, `README.md`  
**개정:** 09 — 08 Logic GREEN 대비 **REFACTOR 3건 완료·UI Boundary 선행 연동**

---

## 1. 요약

08 보고서 이후 Logic Track에서 `/refactor-smell`로 P0/P1 스멜을 식별하고 `/refactor-safe`를 3회 수행했다. 후보 A는 fail 응답 `_fail()` 헬퍼, 후보 B는 단위별 변환 `_lines_for_unit()` 추출, 후보 C는 `UnitConverter.py` `main()`이 `convert()`만 호출하도록 Boundary를 정리했다. `pytest tests/` **9 passed**, golden **UPDATE_GOLDEN 없이** 전 TC matched. `tests/test_main.py`는 미착수.

---

## 2. 배경·목표

| 항목 | 내용 |
|------|------|
| 배경 | 08에서 Logic GREEN·Golden 완료; `convert()` fail dict 4회 반복·3분기 변환·`main()` 이중 구현 갭 |
| 목표 | ARRR R⑦ Safe Refactor — 동작·계약·int[6] 불변, Change Budget 준수 |
| SSOT | `.cursorrules`, `docs/PRD.md` §9·§10, `src/constants.py` |

---

## 3. 산출물·변경

| 산출물 | 경로 | 설명 |
|--------|------|------|
| 스멜 분석 | (세션) `/refactor-smell` | P0 Duplicated Code·Long Method·ECB; 후보 A·B·C 제안 |
| fail 헬퍼 | `src/convert.py` — `_fail()` | format/number/negative/unit 4곳 보일러플레이트 제거 |
| 변환 헬퍼 | `src/convert.py` — `_lines_for_unit()` | meter/feet/yard 산술·줄 조립 Entity 분리 |
| Boundary 위임 | `UnitConverter.py` — `main()` | `input` → `convert()` → `lines`/`error.message` print |
| 진행 현황 | `README.md` | §2 REFACTOR·§3 UI Boundary 체크 반영 |
| Export | `Report/09_*`, `Prompting/09_*` | 본 보고서·트랜스크립트 |

---

## 4. 기술 내용

### `/refactor-smell` (Logic+UI)

| 우선순위 | 스멜 | 위치 |
|----------|------|------|
| P0 | Duplicated Code | fail dict 4회; meter/feet/yard 3분기 |
| P0 | Long Method | `convert()` 검증+변환+응답 혼재 |
| P1 | ECB 위반 | Control에 Entity 산술 인라인; Boundary 이중 구현 |

### `/refactor-safe` 실행 순서

| 후보 | Track | 변경 | pytest | golden |
|------|-------|------|--------|--------|
| C | UI (Boundary) | `main()` → `convert()` | 9 passed | matched |
| A | Logic (Control) | `_fail(type, message)` | 9 passed | matched |
| B | Logic (Entity) | `_lines_for_unit(unit, value)` | 9 passed | matched |

### `convert()` 구조 (after)

```
_fail()           — fail dict 조립 (Control)
_lines_for_unit() — round·변환 줄 (Entity)
convert()         — 파싱·검증·분기·pass 응답 (Control)
```

### CLI 동작 (PRD §9 정렬)

- pass: 입력 단위 제외 **2줄** (`convert().lines`)
- fail: `error["message"]` 1줄 (음수·미지원 단위 포함)

---

## 5. 결정·갭·다음 단계

| # | 항목 | 내용 |
|---|------|------|
| 1 | 결정 | REFACTOR는 스멜 1건·Change Budget 1회씩; golden diff 없음이 기본 목표 |
| 2 | 갭 | `tests/test_main.py` 미작성 — UI Track formal RED·Golden 없음 |
| 3 | 다음 | `/tdd-red` UI pass·fail stdout TC → `/green-minimal` 또는 golden-master UI |

---

*Report 09 — UnitConverter_19*
