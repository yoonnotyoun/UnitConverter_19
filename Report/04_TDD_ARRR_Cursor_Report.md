# Report — UnitConverter_19 TDD·ARRR Cursor 산출물

**프로젝트:** UnitConverter_19  
**일자:** 2026-06-11  
**주제:** Dual Track TDD · ARRR · BCE · Cursor Commands/Skills  
**대상:** `.cursor/commands/`, `.cursor/skills/`, `docs/PRD.md`  
**개정:** 04 — Cursor ARRR 실습 체계·Dual Track(Logic/UI)·BCE 반영 (03 Mom Test 대비)

---

## 1. 요약

UnitConverter_19 ARRR 실습용 Cursor **Commands 8종**·**Skills 2종**·**문서 템플릿 3종**을 구성했다. SSOT는 `.cursorrules`와 `docs/PRD.md`이다. 테스트 방식은 **Dual Track TDD**(Logic / UI)이며 **BCE**(Entity · Control · Boundary) 역할 분리를 커맨드 Phase 선언과 스킬에 명시했다. 구현·pytest·브랜치·commit 은 이번 세션 범위 밖이다.

---

## 2. 배경·목표

| 항목 | 내용 |
|------|------|
| 배경 | 03 보고서 `convert()` 계약·PRD 추적 확정 후, TDD 실습을 Cursor 슬래시 커맨드로 표준화 필요 |
| 목표 | RED→GREEN→REFACTOR·Export 를 `/슬래시` 만으로 자율 실행 (추가 입력·질문 금지) |
| SSOT | `.cursorrules`, `docs/PRD.md` |

---

## 3. 산출물·변경

| 산출물 | 경로 | 설명 |
|--------|------|------|
| PRD | `docs/PRD.md` | Mom Test 03·추적표·README 통합 PRD |
| TDD RED | `.cursor/commands/tdd-red.md` | Logic/UI Track 실패 TC 1건 |
| RED Test Plan | `.cursor/commands/red-test-plan.md` | Track·BCE·케이스 계획 (파일 변경 없음) |
| RED Skeleton | `.cursor/commands/red-skeleton.md` | AAA 골격만 |
| GREEN Minimal | `.cursor/commands/green-minimal.md` | Track별 최소 구현 |
| Golden Master | `.cursor/commands/golden-master.md` | Boundary↔Control 레거시 대조 |
| REFACTOR Smell | `.cursor/commands/refactor-smell.md` | BCE·Track 스멜 진단 |
| REFACTOR Safe | `.cursor/commands/refactor-safe.md` | BCE 경계 유지 리팩터 |
| Export | `.cursor/commands/export.md` | Report·Transcript (주제 동적 명명) |
| TDD Skill | `.cursor/skills/unit-converter-tdd/SKILL.md` | Dual Track · BCE · ARRR 흐름 |
| Docs Skill | `.cursor/skills/unit-converter-docs/SKILL.md` | Export·템플릿·PRD 참조 |
| Report 템플릿 | `.cursor/skills/unit-converter-docs/templates/report-template.md` | |
| Transcript 템플릿 | `.../templates/transcript-template.md` | |
| Checklist 템플릿 | `.../templates/checklist-template.md` | Logic/UI Track 분리 |

**미변경:** `Report/01~03_*`, `Prompting/01~03_*`, `src/`, `tests/`, `UnitConverter.py`

---

## 4. Dual Track TDD · BCE

| Track | BCE | Target | 테스트 | 구현 |
|-------|-----|--------|--------|------|
| **logic** | Entity | 단위·비율·순수 변환 | `tests/test_convert.py` | `src/` |
| **logic** | Control | `convert()` | `tests/test_convert.py` | `src/convert.py` |
| **ui** | Boundary | `main()` | `tests/test_main.py` | `UnitConverter.py` |

### Phase 선언 (TDD 커맨드 공통)

```
Phase: {red|green|refactor} | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}
```

### ARRR · 커맨드 매핑

| 단계 | 커맨드 | Track |
|------|--------|-------|
| Arrange | `/red-test-plan`, `/red-skeleton` | logic \| ui |
| Red | `/tdd-red` | logic \| ui |
| Green | `/green-minimal`, `/golden-master` | logic \| ui |
| Refactor | `/refactor-smell`, `/refactor-safe` | logic \| ui |
| Report | `/export` | archive |

### 자율 실행 규칙

- 슬래시 호출 시 **추가 입력·질문 없음**
- Logic 미완료 → Logic Track 우선, GREEN 후 UI Track
- RED: Track별 구현 파일 수정 금지 / GREEN: `tests/` 수정 금지
- 한 번에 1 Track · 1 케이스

### BCE 경계

| BCE | 할 일 | 금지 |
|-----|-------|------|
| Entity | meter/feet/yard, 비율 | I/O |
| Control | `convert()` → dict | print |
| Boundary | input, convert() 호출, print | 파싱·변환·검증 |

---

## 5. PRD (`docs/PRD.md`) 요약

- §1~2: Mom Test 배경·P0/P1 범위
- §3: Input/Output·`convert()` 계약 (error 4종: format/number/unit/negative)
- §4~6: FR/NFR/EXT · §7 추적표 · §8 성공 기준 B/L/Q/M
- §9: `UnitConverter.py` 갭 (음수·줄 수·print·TC 미구현)

> **SSOT 충돌:** 구현·TC는 `.cursorrules`(lines 3줄, error 3종) 우선. PRD §7은 TC 선정·추적용.

---

## 6. 결정·갭·다음 단계

| # | 항목 | 내용 |
|---|------|------|
| 1 | 결정 | Track = `logic` \| `ui` 만; BCE 를 Phase 선언 4번째 필드로 고정 |
| 2 | 결정 | Export Report 제목은 세션 주제 반영 (Mom Test 고정 금지) |
| 3 | 갭 | `tests/test_main.py`·UI Track TC·Logic GREEN 미착수 |
| 4 | 갭 | `.cursorrules` vs PRD (lines 2 vs 3, error 4 vs 3) — TC 작성 시 SSOT 우선순위 문서화만, 미통합 |
| 5 | 다음 | Logic Track FR-01 `/red-test-plan` → `/tdd-red` → `/green-minimal` 순 실습 |

---

*Report 04 — UnitConverter_19*
