# Void OS — Development Workflow

## Context Priority

This is a standalone Android app project. When working on void-os:
- Load this CLAUDE.md (project-specific), not kb/ context
- Reference the design spec in kb/projects/void/project.md only for architecture questions
- Keep context lean—prefer git history over file reads

## Token Discipline

- **No whole-file reads.** Use `Read` with `offset`/`limit` for large files.
- **Commit before major changes.** A 50-line feature is a commit; it's not wasted history.
- **Git is your context.** Use `git log --oneline -20` or `git diff` instead of re-reading code.
- **Handoff protocol:** `/handoff` before leaving → writes to `handoff.md`. `/pickup` on return.
- If a task will be expensive (multiple large files, deep archaeology), flag it upfront.

## Git Flow

- **Branches:** Feature branches for work (`feat/radial-menu`, `fix/color-bug`, `refactor/kb-layer`).
- **Commits:** One logical change per commit. Format: `component: brief summary`
  - Examples: `radial-menu: add touch detection`, `capture: wire submit button`, `core: add journal reader`
- **Push early:** Commit and push after meaningful progress. No long-lived branches.
- **PRs:** Even solo work gets a PR. Squash + merge to main. PR description captures the why.
- **Main branch:** Deploy-ready. APK builds cleanly, no known bugs.

## Proactive Commits

I will suggest commits when appropriate and do them with a heads-up:
> "Good. Going to commit this: 'radial-menu: add touch-down detection and segment animation'"

You can:
- Approve: I commit and push
- Hold: Say "wait" and I'll bundle more before committing
- Reject: "Don't commit that yet" and I'll revert or modify

## Task Tracking

- **GitHub Issues** for features and bugs (persistent across sessions)
- **Labels:** `bug`, `feature`, `blocked`, `help-wanted`
- **Milestones:** `M1` through `M6` (one per issue, aligns with project.md phases)
- **TaskCreate:** Only during active session work for sub-tasks
- **Status:** Closed issues = shipped + tested on device

## Code Style

[TBD: type hints? docstrings? line length? — decide when M1 is done]

## Testing Strategy

[TBD: manual on-device? unit tests? integration tests? — decide after first APK build]

## Reference

- **Design spec:** `~/kb/projects/void/project.md` (philosophy, milestones, interaction model)
- **Core logic:** `~/kb/projects/life-os/core-scripts/` (inbox, capture, kb_utils patterns)
- **lo system paths:** `~/kb/` structure; void-os uses same files
