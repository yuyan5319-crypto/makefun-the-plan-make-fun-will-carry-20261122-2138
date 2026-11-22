# Polished Pixels — The $100-to-$1,200 Etsy Photo Plan

The brief asks for a plan an AI agent can carry out itself to turn $100
into the most money in 30 days. This entry sells a fast, concrete service
instead of chasing a viral hit: $49 packs of AI-polished product photos for
Etsy sellers with 50+ sales whose listings still use phone snapshots —
buyers who already earn online, are easy to find by searching Etsy, and
pay for a 24-hour deliverable with no meetings and no luck involved. The
first photo is free, which is what gets the reply where plain cold
outreach gets ignored.

## The plan

> Day 1: find 300 Etsy shops with 50+ sales but phone-snapshot photos and
> email each offering 10 AI-polished photos for $49 in 24 hours, first
> photo free. Close 5 in week 1, reinvest profits into outreach tools and
> $10/day Etsy ads. Day 30: about $1,200 from 25 packs.

## Run

```sh
python3 main.py
```

`main.py` runs on Python 3.13 with the standard library only — no
dependencies, no network. It writes the plan text to `/output/entry.txt`
(UTF-8, 266 characters, inside the 1–280 limit).

## License

MIT — see `LICENSE`.
