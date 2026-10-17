"""Write exactly three pytest tests in this file.

TODO 1: Add one test derived from acceptance criterion AC-1.
TODO 2: Add one test derived from acceptance criterion AC-2.
TODO 3: Add one test derived from acceptance criterion AC-3.

Use only the public functions in ``reference``: reservation_disposition and
can_offer_to_waitlist. Do not edit the reference module. Call them with named
arguments, as in tests/test_reference_smoke.py.

Name each test so the acceptance criterion it checks is visible from the test
name or an adjacent comment, for example: def test_ac1_<what_it_checks>().

Put any policy value, such as the grace period, in a named constant marked as
a configured value, as in the at-risk example from the Week 5 lecture.
"""
"""Acceptance tests for INT-01 late-pickup requirements.

Each test corresponds to one acceptance criterion from requirements.md.
Expected results are taken from the acceptance criteria, not from reading
the reference implementation.

Only the two public functions are used, with named arguments:
    reservation_disposition(minutes_after_start=..., grace_minutes=...,
                            checked_in=..., staff_hold_until=...)
        -> Literal["active", "held", "releasable"]
    can_offer_to_waitlist(disposition=..., preparation_complete=...) -> bool

Mapping to the reference's three dispositions:
    "active"     -> a recorded check-in keeps the reservation active (R-2)
    "held"       -> an active staff hold (or the grace window) blocks release (R-3)
    "releasable" -> past grace with no check-in and no active hold (R-1)

The tests use offsets from CONFIGURED_GRACE_MINUTES, so they do not depend on
the specific grace value the lab chooses.
"""

from reference import can_offer_to_waitlist, reservation_disposition

# Configured value, set by the lab, not a fact established by the interview.
# The interview leaves the real grace period unresolved (Q-1: Jordan says 15,
# Priya was told 20), so this stands in as a configured setting. The tests
# reference it by offset and never assert that a particular number is correct.
CONFIGURED_GRACE_MINUTES = 15


def test_ac1_checked_in_reservation_stays_active_past_grace():
    """AC-1 (R-2): once checked in, a reservation stays active even past grace."""
    disposition = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES + 10,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=True,
    )
    # Expected from AC-1: "active" (checked in), never "releasable".
    assert disposition == "active"


def test_ac2_active_staff_hold_blocks_release():
    """AC-2 (R-3): an active staff hold keeps the reservation held past grace,
    instead of letting it become releasable."""
    # Evaluated 5 minutes *after* grace ends, so without the hold it would be
    # "releasable"; the hold (ending 10 minutes after grace) is what holds it.
    disposition = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES + 5,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=CONFIGURED_GRACE_MINUTES + 10,
    )
    # Expected from AC-2: "held", not "releasable".
    assert disposition == "held"


def test_ac3_releasable_but_not_prepared_is_not_offered():
    """AC-3 (R-4): a releasable kit that is not yet prepared must not be offered
    to the waitlist."""
    offered = can_offer_to_waitlist(
        disposition="releasable",
        preparation_complete=False,
    )
    # Expected from AC-3: not offered.
    assert offered is False