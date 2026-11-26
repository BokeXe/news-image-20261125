# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/BokeXe/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/BokeXe/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Wednesday 25 November 2026 in one image — a legibility-first news page with
38 date-checked stories across 9 regions and 24 fields. A full-width
masthead names the day, four KPI cards carry the headline numbers (including
Bitcoin at $58,692, -2.56%, Finnhub 12:34 UTC provisional), and the three
leads — Hormuz tanker mines and Houthi strikes; Ukraine's drone hits on
Samara refineries; the Asian chip-stock selloff — run as large cards with
big headlines and one clear stat each. Below them, a complete board lists
all 38 stories grouped by region with short headlines and one factual
detail line per story. Reported-only items are marked *, and a DATE CHECK
box names the five neighbouring-day items reported on 25 November, so
nothing dated 24 November or earlier is presented as Wednesday's news.

`main.py` copies `entry.png` (1024×1024, ≤1 MiB) to `/output/entry.png`;
both runs write identical bytes, no network.

## Reproduce

`entry.png` is rendered deterministically by `../prep/news25/build_v2.py`
(Pillow, Noto Sans fonts, no clock, no network) from the dated research
brief `../prep/news25-research.md`. Re-running it produces the same bytes;
`main.py` refuses to finish if the source exceeds 1 MiB or the copied
file's size differs from the source. The five items flagged in the DATE
CHECK box are the only stories on the page dated before Wednesday
25 November 2026, and the Bitcoin figure is the Finnhub 12:34 UTC
snapshot, labelled provisional on the page.
