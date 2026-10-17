# Provenance ledger

Use exactly this format for every entry. Write each entry when the work is done, one entry per reviewable change.

```text
## Entry 01
artifact:  The dependency pin pytest==9.1.1 in the project's requirements file, and the pip install step that fails on it.
tool:      claude-opus-5-5, 2026-10-17, approx. 11:35–11:37 ET
prompts:   Pasted the pip error for pytest==9.1.1 with no other instruction.	prompts/2026-10-17_01_pip-pytest-error.txt
review:    The full pip error output. The offered versions stop at 8.4.2 with no 9.x at all.
            The pytest 9.1.1 package page on a PyPI mirror: released 2026-06-19, Requires-Python: >=3.10.
            The pytest 9.1.1 release notes, quoted in several Dependabot pull requests.
            CHANGED
            Nothing in the codebase. The output was advice only.
            Recommended running under Python 3.10 or newer, or pinning pytest==8.4.2 on Python 3.9, optionally with python_version environment markers.
            REJECTED
            "pytest 9.1.1 doesn't exist." Rejected because the release is published on PyPI.
            A stale private index as the primary cause. Kept as a fallback only. pip hides releases whose Requires-Python excludes the running interpreter, and a list ending at 8.4.2, the last 3.9-compatible release, matches that pattern.
checks:    WebSearch "pytest 9.1.1 release requires python"	pytest 9.1.1 confirmed, released 2026-06-19, requires Python >=3.10.
evidence:  Traces to the failing dependency install in the dev or test environment setup.
risk:      The local Python version was inferred from the error, not observed. If it is 3.10 or newer, the cause is likely a l agging mirror or proxy.
        If the project pins 8.4.2 to stay on 3.9, it diverges from environments running 9.1.1. Tests may pass on one and fail on the other.

For an experiment, add three fields:
dataset:   task set identifier and its commit SHA or version
result:    metric, N, and the result table or its file path
changed:   what you did differently as a result
```

Add your entries below this line, starting with Entry 1.

---

## Entry 01
artifact:  The dependency pin pytest==9.1.1 in the project's requirements file, and the pip install step that fails on it.
tool:      claude-opus-5-5, 2026-10-17, approx. 11:35–11:37 ET
prompts:   Pasted the pip error for pytest==9.1.1 with no other instruction.	prompts/2026-10-17_01_pip-pytest-error.txt
review:    The full pip error output. The offered versions stop at 8.4.2 with no 9.x at all.
            The pytest 9.1.1 package page on a PyPI mirror: released 2026-06-19, Requires-Python: >=3.10.
            The pytest 9.1.1 release notes, quoted in several Dependabot pull requests.
            CHANGED
            Nothing in the codebase. The output was advice only.
            Recommended running under Python 3.10 or newer, or pinning pytest==8.4.2 on Python 3.9, optionally with python_version environment markers.
            REJECTED
            "pytest 9.1.1 doesn't exist." Rejected because the release is published on PyPI.
            A stale private index as the primary cause. Kept as a fallback only. pip hides releases whose Requires-Python excludes the running interpreter, and a list ending at 8.4.2, the last 3.9-compatible release, matches that pattern.
checks:    WebSearch "pytest 9.1.1 release requires python"	pytest 9.1.1 confirmed, released 2026-06-19, requires Python >=3.10.
evidence:  Traces to the failing dependency install in the dev or test environment setup.
risk:      The local Python version was inferred from the error, not observed. If it is 3.10 or newer, the cause is likely a l agging mirror or proxy.
        If the project pins 8.4.2 to stay on 3.9, it diverges from environments running 9.1.1. Tests may pass on one and fail on the other.

## Entry 02

artifact : The origin remote configuration of the local Assignment-3 repository, stored in .git/config.
Tool: Claude-Sonnet 026-10-17, approx. 12:51–12:54 ET
Prompt: How to change the remote repo url
Review: No repository files, git output or remote URLs were shared
CHANGED
Nothing directly. The output was commands to run.
Recommended git remote -v to inspect, and git remote set-url origin <new-url> to change, followed by git remote -v to confirm and git push -u origin <branch> for a new empty repository.
Checks: git remote -v returned 
        origin  git@github.com:md685-njit/Assignment-3.git (fetch)
        origin  git@github.com:md685-njit/Assignment-3.git (push)
Evidence: git remote set-url origin https://github.com/ap3478/CS690-Assignment3.git
        git remote -v
        origin  https://github.com/ap3478/CS690-Assignment3.git (fetch)
        origin  https://github.com/ap3478/CS690-Assignment3.git (push)
Risk : Any previous commits may not have been successful or will need to be recomited to the new repo

# Entry 03

Artifact: pytest for the below 3 acceptance criteria. 

Tool: Claude Opus 026-10-17, approx. 1:51–12:54 ET
Prompt: I need help with creating pytest for the below 3 acceptance criteria. write exactly three pytest test functions and use the attached reservation.py file
**AC-1 (R-2: checked-in reservation stays active)**
- **Given** the lab's configured grace period is G minutes, a reservation starts at S, and a check-in was recorded at S + 2 minutes
- **When** the system evaluates the reservation's status at S + G + 10 minutes
- **Then** the status is Active (checked in), not Releasable or Released

**AC-2 (R-3: active staff hold blocks release)**
- **Given** the lab's configured grace period is G minutes, a reservation starts at S with no check-in, and staff recorded a hold ending at H = S + G + 10 minutes with the reason "student called: class running late"
- **When** the system evaluates the reservation's status at S + G + 5 minutes
- **Then** the status is Held, not Releasable, and the hold end time and reason are recorded on the reservation

**AC-3 (R-4: released but not-ready kit is not offered)**
- **Given** a reservation's status is Released and its kit is not marked ready for checkout
- **When** the system checks whether the kit may be offered to the waitlist
- **Then** the kit is not offered to the waitlist
Review: the AC-1/AC-2/AC-3 text, their expected results, and the R-2/R-3/R-4 traces;reference.py in full, to answer "does it change anything?" and to verify the tests. No external sources were consulted.
CHANGED Created tests/test_student_acceptance.py. The first version expressed AC-2 as a within-grace "held" case, because the README example showed no hold argument and a parameter name was not invented. After reference.py revealed staff_hold_until: int | None, AC-2 was rewritten as a genuine staff-hold test (evaluated 5 minutes past grace, held only because the hold runs to grace + 10), matching the Part-3 AC-2. For verification only: copied the user's reference.py into the working directory, created tests/, and installed pytest.
REJECTED
Inventing a hold-parameter name before reference.py was shared. Would guess the API; left AC-2 as a within-grace test instead.
Keeping the within-grace AC-2 permanently. Rejected once staff_hold_until was confirmed, since the staff-hold test matches Part-3 AC-2 and actually exercises the hold branch.
Hardcoding 15 or 20 as the grace value. Rejected; the value is unresolved (Q-1), so the tests use CONFIGURED_GRACE_MINUTES and reference it by offset.
Deriving expected values from the reference's logic. Rejected; each expected value was taken from the acceptance criterion.

Checks: python3 -m pytest tests/test_student_acceptance.py -v	3 passed in 0.02s — AC-1, AC-2, AC-3 all PASSED	pass
Run inside the Claude sandbox (Python 3.13.16, pytest 9.1.1) against the reference.py pasted in prompt 12. Re-run against the official graded module to confirm.

Evidence: Traces from each test through its requirement to interview evidence:
AC-1 → R-2 → E-4 (INT-01:P06, P17, P21)
AC-2 → R-3 → E-1 (INT-01:P04), E-4 (INT-01:P06, P17, P21)
AC-3 → R-4 → E-2 (INT-01:P13), E-3 (INT-01:P09, P13), E-5 (INT-01:P17, P21)
Open items left open, not settled by these tests: Q-1 (actual grace value / what students are told), Q-2 (how technicians signal a kit is ready). No test ID beyond AC-1/AC-2/AC-3 was assigned.

Risks:
