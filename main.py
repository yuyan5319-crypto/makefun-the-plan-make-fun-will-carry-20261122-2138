"""Write the competition plan to /output/entry.txt.

The plan is a fixed literal: a concrete, agent-executable loop for turning
$100 into the most money in 30 days. The program only writes that text to
/output/entry.txt (UTF-8, 1-280 characters).
"""

from pathlib import Path

PLAN = (
    "Day 1: search Etsy for 300 shops with phone-snapshot product photos "
    "and email each offering 10 AI-polished photos for $49, delivered in "
    "24 hours. Close 5 in week 1, reinvest profits into outreach tools "
    "and $10/day Etsy ads. Day 30: about $1,200 from 25 packs."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
