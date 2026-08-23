"""Small, dependency-free example of rule-guarded assistant routing."""

from __future__ import annotations

import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Decision:
    route: str
    answer: str
    next_step: str


def route_question(question: str) -> Decision:
    text = question.lower()
    low_oxygen = any(term in text for term in ("low oxygen", "low-oxygen", "dissolved oxygen"))
    direct_control = any(term in text for term in ("turn on", "start the aerator", "control the device"))

    if low_oxygen and direct_control:
        return Decision(
            route="field_incident_with_authorization_gate",
            answer=(
                "I can prepare a Pond 12 response task, but I cannot claim that a device was "
                "controlled without an authorized operator confirmation."
            ),
            next_step="Verify the device and dissolved oxygen, then record the authorized action and a retest.",
        )

    if low_oxygen:
        return Decision(
            route="field_incident_triage",
            answer=(
                "Prioritize aeration, pause or reduce feeding, verify the device and dissolved oxygen, "
                "and schedule a thirty-minute retest."
            ),
            next_step="Assign the response to an operator and keep the evidence trail attached to the task.",
        )

    return Decision(
        route="general_assistant",
        answer="I need the operating context before making a domain recommendation.",
        next_step="Provide the pond, observation, time, and requested decision.",
    )


def main() -> None:
    question = " ".join(sys.argv[1:]).strip() or "What should we do first for persistent low oxygen in Pond 12?"
    decision = route_question(question)
    print(f"Route: {decision.route}")
    print(f"Recommendation: {decision.answer}")
    print(f"Next step: {decision.next_step}")


if __name__ == "__main__":
    main()

