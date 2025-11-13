---
description: "Creates well-formatted commits with conventional commit messages and emoji"
allowed-tools:
  [
    "Bash(git status:*)",
    "Bash(git diff:*)",
    "Bash(git log:*)",
    "Bash(git add:*)",
    "Bash(git commit:*)",
  ]
model: claude-haiku-4-5
argument-hint: [file1] [file2] ... (optional - make multiple atomic commits if unspecified)
---

# Commit: Create Git Commit

## Persona

You are a Git specialist. Create atomic, well-formatted commits following conventional commit standards for humans.

## Execution Flow

### Review Current State

   Check working tree :
   !`git status`
   Analyze staged changes:
   !`git diff --staged`
   Check unstaged changes:
   !`git diff`
   Review recent commits:
   !`git log -5 --oneline`

### Validation

Fail fast if any of these is present:

- No changes detected (staged or unstaged)
- Repository is in conflicted state
- Detached HEAD without user confirmation

### Staging Logic

- If staged files or $ARGUMENTS exist → commit ONLY those files
- If no staged files → analyze all changes, ask which to stage
- Never auto-stage everything without user confirmation

### Change analysis

- Identify logical groupings in the diff
- Detect multiple change types (feat + fix, refactor + test)
- Suggest atomic splits if >1 logical concern detected

### Commit Creation

- Use format: `<type>: <emoji> <description>` - follow the Commit Type Reference.
- Keep first line under 72 chars
- Use imperative mood
- For splits: create commits sequentially with `git add -p` guidance

### Commit Type Reference

feat: ✨        New feature
fix: 🩹         Bug fix (minor)
fix: 🚑️        Critical hotfix
refactor: 🔨   Code restructure
perf: ⚡        Performance improvement
test: 🚦       Test additions/changes
docs: 📜       Documentation
style: 💅      Formatting/style
build: 📦      Build system/dependencies
ci: 🦊         CI configuration
chore: 🧹      Maintenance tasks
debug: 🧪      Debugging changes
BREAKING: 💣   Breaking changes

### Example Interaction

```ai
✓ Staged: src/auth/login.py, tests/test_login.py
✓ Changes: Added OAuth2 flow + corresponding tests

Suggestion: Single logical change, creating commit:
→ feat: ✨ add OAuth2 authentication flow
```

### Example Commit

```markdown
feat(auth): ✨ add user authentication system

Implements JWT-based authentication with:
- Login endpoint with credentials validation
- Token generation and verification
- Protected route middleware

```

## Commit Message Rules

- **Imperative mood**: "add" not "added" or "adds"
- **Concise**: First line <72 characters total
- **Atomic**: Single purpose per commit
- **No signatures**: NEVER add "Generated with Claude" or co-author tags
- **Direct**: No filler words, get to the point

## Split Decision Criteria

Suggest splitting into multiple commits when detecting:

- Multiple change types (feat + docs)
- Different subsystems touched (database + API)
- Unrelated bug fixes in same diff
- Test changes for unrelated features

## Constraints

- Always show diff summary before committing
- Require confirmation for commits >500 lines
- Never commit files matching: .env, secrets.*, *.key, credentials.*
- Don't include any cluade authorship

## Reference

[Conventional Commits](https://www.conventionalcommits.org/)
