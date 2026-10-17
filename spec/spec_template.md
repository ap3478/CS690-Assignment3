# Implementation-ready specification template

## Selected requirement

Requirement ID:Requirement ID: R-2 (checked-in reservations stay active)
Evidence trace:E-4 (INT-01:P17, INT-01:P21)

## Behavior and scope

Given a single reservation, this function returns its status at one moment in time. It covers exactly one rule: once a check-in has been recorded, the reservation stays active and is never reported as releasable or released, no matter how much time has passed since the start time or the configured grace period. It does not decide what a not-checked-in reservation's status should be.

## Typed interface or function signature

from typing import Literal

ReservationStatus = Literal[
    "reserved", "checked_in", "held", "releasable", "released"
]

def evaluate_reservation_status(
    current_status: ReservationStatus,
    checked_in: bool,
    minutes_since_start: int,
    grace_period_minutes: int,
    hold_until_minutes: int | None,
) -> ReservationStatus:
    """Return the reservation's status at the evaluated moment.

    This spec constrains only the checked_in == True branch (R-2).
    minutes_since_start and hold_until_minutes are both measured in
    minutes relative to the reservation start time, on the same clock.
    hold_until_minutes is None when no staff hold is recorded.
    Implementation is out of scope for this document.
    """
    ...

## Preconditions

1.grace_period_minutes is the lab's configured value, supplied by the caller as an int >= 0. The function must not read or assume a grace value of its own.
2.checked_in is True only if a check-in was actually recorded for this reservation; the caller does not pass True as a guess or default.
3.A reservation that has already been released is never passed with checked_in = True; a released kit cannot be retroactively marked checked in.
4.minutes_since_start and hold_until_minutes (when not None) are measured against the same clock and the same start time.


## Postconditions

1.If checked_in is True, the returned status is "checked_in", regardless of minutes_since_start, grace_period_minutes, or hold_until_minutes.
2.If checked_in is True, the function never returns "releasable" or "released".
3.The function is pure: it mutates no state and, for identical inputs, returns an identical result.


## Invariant


Once a reservation is checked in, check-in is absorbing with respect to time: across every later evaluation (every larger minutes_since_start), the status remains "checked_in" and is never downgraded to "releasable" or "released" by the passage of the grace period. This holds because the rule depends on the recorded check-in, not on the clock.


## Edge cases


1.checked_in = True exactly at minutes_since_start == grace_period_minutes (the grace boundary): the reservation is still "checked_in"; crossing the boundary does not release a checked-in reservation.
2.checked_in = True with a hold also present (hold_until_minutes is not None): the reservation remains active and must not be releasable; see open question 1 for the status label when both apply.
3.checked_in = True with grace_period_minutes == 0 (config set to zero): still "checked_in"; a zero grace period does not override a recorded check-in.
4.checked_in = True with minutes_since_start < 0 (evaluated before the start time, e.g. an early check-in): the function must still return "checked_in" and must not error; whether an early check-in is permitted is open question 2.


## Non-goal

This spec does not define the status of a reservation that has not checked in — the grace-period release rule (R-1) and the staff-hold rule (R-3) are specified separately and are out of scope here.

## Settled decisions

1A recorded check-in takes precedence over the grace period: it keeps the reservation active regardless of elapsed time (E-4).
The grace period is a caller-supplied configured value (grace_period_minutes), never hard-coded, even though it does not change the output in the checked-in branch (E-6).
The function is deterministic and side-effect free; status is computed from its inputs alone.


## Open questions the implementation agent may not answer

1.When a reservation is both checked in and under an active hold, which status label applies — "checked_in" or "held"? The outcome (active, not releasable) is settled by E-4; the label is not. The agent must not pick one silently. Owner: Media Lab manager.
2.May a check-in be recorded before the reservation start time (minutes_since_start < 0), and is such an early check-in valid? The interview does not say. Owner: Jordan Lee / Media Lab manager.
3.Can a check-in be reversed or cancelled once recorded (e.g., a student checks in and then leaves)? E-4 establishes that a check-in keeps a reservation active but says nothing about undoing one, so the agent must not invent a revert rule. Owner: Media Lab manager.

