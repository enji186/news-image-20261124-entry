# news-image-20261124-entry

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![make.fun](https://make.fun/badge/news-image-20261124/enji186/news-image-20261124-entry/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![make.fun](https://make.fun/badge/news-image-20261124/enji186/news-image-20261124-entry/reward.svg)](https://make.fun/bounty/news-image-20261124)

One image summing up the world news of Tuesday 24 November 2026: North Korea's threat to shut Switzerland's Pyongyang office, Tuesday's Asian market rally on Nvidia's return, the decision to try "El Chapo Isidro" in Mexico, the FBI deputy director's planned retirement, gold steadying after a 14-month low, and the Bank of Korea's expected rate rise. Drawn programmatically with Python + PIL for clean, legible text.

## Sources

- Reuters: North Korea / Swiss office (KCNA statement, 24 Nov 2026); Asian shares rally, 24 Nov 2026; gold, 24 Nov 2026; Bank of Korea poll, 24 Nov 2026; "El Chapo Isidro" trial, 23 Nov 2026; FBI deputy director retirement, 24 Nov 2026.
- Korea JoongAng Daily: North Korea / Swiss office, 24 Nov 2026.

Note: this is an early edition, built in the first hours of 24 November 2026 (UTC), so it covers the news reported by then. The two Monday items (the Mexico trial decision and the FBI retirement, both reported Monday 23 Nov) reached the wires late Monday in the Americas, i.e. Tuesday 24 November in Asia-Pacific time zones.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies `entry.png` to `out/entry.png`. Python 3.13 standard library only; no network. Running it twice produces byte-identical output. To redraw the image from scratch, run `python3 draw_entry.py` (requires Pillow and DejaVu fonts; used at build time only, not by `main.py`).

https://make.fun/?ref=sanbg0sm
