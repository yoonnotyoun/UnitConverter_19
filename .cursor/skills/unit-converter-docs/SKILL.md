---
name: unit-converter-docs
description: UnitConverter_19 문서·보고·Export. Report/Prompting 내보내기, PRD 추적, ARRR checklist. export·Report·Transcript·PRD·Mom Test·ARRR 실습 회고 시 사용.
---

# UnitConverter Docs

UnitConverter_19 문서·세션 아카이브 가이드. SSOT: `.cursorrules`, `docs/PRD.md`.

## Dual Track · BCE (TDD 실습)

| Track | BCE | 산출물 |
|-------|-----|--------|
| logic | Entity, Control | `src/convert.py`, `tests/test_convert.py` |
| ui | Boundary | `UnitConverter.py`, `tests/test_main.py` |

Report·Checklist 에 Track/BCE·Dual Track 진행 상태를 기록한다.

## Export 커맨드

`/export` — `Report/{NN}_{제목}_Report.md` + `Prompting/{NN}_Export_Transcript.md`

- **제목:** 현재 대화 주제 반영 (Mom Test 고정 금지)
- **번호:** 폴더별 `{NN}_` 최대값 +1
- **기존 `{NN}_*` 수정 금지**

## 템플릿

| 용도 | 경로 |
|------|------|
| Report | [templates/report-template.md](templates/report-template.md) |
| Transcript | [templates/transcript-template.md](templates/transcript-template.md) |
| ARRR Checklist | [templates/checklist-template.md](templates/checklist-template.md) |

## Report 제목 예

| 세션 | `{제목}` |
|------|----------|
| Mom Test | `MomTest` |
| PRD | `PRD` |
| TDD·ARRR·커맨드 | `TDD_ARRR` |
| Golden Master | `Golden_Master` |

파일명: `04_TDD_ARRR_Report.md`

## Report 본문 (최소)

1. 요약 — 산출물·결정
2. 배경·목표 — SSOT 참조
3. 산출물·변경 — 경로 표
4. 기술 내용 — 주제별
5. 결정·갭·다음 단계

## Transcript 규칙

- Turn 단위 User(요약) / Assistant(결과)
- Session Metadata 표 (turns, reports, code reviewed, key change)
- verbatim 전체 복붙 **금지**

## PRD 참조 포인트

| 섹션 | 용도 |
|------|------|
| §3 | Input/Output·`convert()` 계약 |
| §4·§5 | FR/NFR |
| §7 | TC 추적표 |
| §8 | 성공 기준 B/L/Q/M |
| §9 | `UnitConverter.py` 갭 |

## 문서 위치

| 종류 | 경로 |
|------|------|
| PRD | `docs/PRD.md` |
| Report | `Report/{NN}_{제목}_Report.md` |
| Transcript | `Prompting/{NN}_Export_Transcript.md` |
| 커맨드 | `.cursor/commands/*.md` |
| TDD 스킬 | `.cursor/skills/unit-converter-tdd/` |

## 자율 실행

`/export` 호출 시 **추가 입력·질문 없이** 현재 세션 주제·변경분만 반영해 내보낸다.

## 금지

- 기존 번호 파일 덮어쓰기
- 세션에 없는 내용 임의 추가
- 타 프로젝트·워크샵 예시 포함
