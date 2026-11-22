"""Write the competition plan to /output/entry.txt.

The plan is one fixed literal: a concrete loop an AI agent can run on its
own to turn $100 into the most money in 30 days. The program writes that
text to /output/entry.txt as UTF-8, 1-280 characters.
"""

from pathlib import Path

PLAN = (
    "Day 1: find 300 Etsy shops with 50+ sales but phone-snapshot photos "
    "and email each offering 10 AI-polished photos for $49 in 24 hours, "
    "first photo free. Close 5 in week 1, reinvest profits into outreach "
    "tools and $10/day Etsy ads. Day 30: about $1,200 from 25 packs."
)


def main() -> None:
    # The gate only accepts 1-280 characters, so fail loudly here rather
    # than writing an entry the scorer would refuse.
    if not 1 <= len(PLAN) <= 280 or not PLAN.strip():
        raise ValueError(f"plan must be 1-280 characters, got {len(PLAN)}")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
