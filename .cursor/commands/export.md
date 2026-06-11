# Export — 세션 보고서·트랜스크립트 내보내기

현재 세션 내용을 `Report/` 보고서와 `Prompting/` Export Transcript 로 내보낸다.

## 필수 선언 (응답 첫 줄)
Phase: export | Target: session | Track: archive

## 절차
1. `Report/`·`Prompting/` 의 기존 `{NN}_` 접두어 최대값을 확인하고, 다음 번호 `NN+1` 을 정한다.
2. 현재 대화의 **주제·산출물**을 파악하고 Report 제목(파일명)을 정한다.
3. 이번 세션(또는 직전 export 이후) 대화에서 **추가·변경된 내용만** 정리한다.
4. `Report/{NN+1}_{제목}_Report.md` 를 **새로 생성**한다.
5. `Prompting/{NN+1}_Export_Transcript.md` 를 **새로 생성**한다 (Turn 단위 User/Assistant 요약).
6. 기존 `{NN}_*` 파일은 **수정하지 않는다**.

## 파일 규칙
    Report/{NN}_{제목}_Report.md
    Prompting/{NN}_Export_Transcript.md
    NN = 01, 02, 03 … (폴더별 독립 증가, 직전 export 대비 +1)

## Report 제목 (현재 대화 반영)
- Mom Test 세션이면 → `MomTest_Report`
- PRD 작성이면 → `PRD_Report`
- TDD·커맨드 작업이면 → `TDD_Command_Report` 등
- `{제목}` = 이번 대화 핵심 주제를 PascalCase·언더스코어로 (예: `04_PRD_Report.md`)
- Mom Test 고정 **금지** — 세션 주제에 맞게 매번 새로 짓는다

## Report 내용
- 헤더: 프로젝트, 일자, 주제, 대상 파일, 개정 요약(직전 대비)
- 본문: **이번 세션에서 다룬 내용** (산출물·결정·변경 사항)
- 외부 워크샵 예시·타 프로젝트 내용 **제외**, UnitConverter_19 한정

## Export Transcript 내용
- 헤더: Session ID, Prior Transcript, Exported, Project
- 본문: `## Turn N — User` / `## Turn N — Assistant` (User 는 원문 요약, Assistant 는 수행·결과 요약)
- 말미: Session Metadata 표 (turns, prior/new report, code reviewed, key change)
- `*End of transcript*`

## 보고 형식
- 생성 파일 2개 경로 (Report 제목 포함)
- Report 주제·반영 범위 (한 줄 요약)
- Transcript Turn 범위 (예: Turn 18~21)
- 변경·미변경 파일 목록

## 금지
- 기존 `Report/{NN}_*` · `Prompting/{NN}_*` 수정·덮어쓰기
- Mom Test 등 **고정 제목**으로 Report 명명
- 세션에 없는 내용 임의 추가
- Transcript 전체 대화 verbatim 복붙 (요약만)
