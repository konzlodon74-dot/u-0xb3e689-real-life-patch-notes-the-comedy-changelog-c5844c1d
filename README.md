# Real-Life Patch Notes: The Comedy Changelog

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/konzlodon74-dot/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/konzlodon74-dot/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

## The entry

> v2.0.3: fixed a bug where walking through a doorway deleted your reason for entering the room; standing still and staring at nothing no longer helps.

149 characters, one line, about the doorway effect — that very real bug where
crossing a threshold wipes your short-term memory of why you went there in the
first place.

## How it works

`main.py` (Python standard library only, no dependencies) holds the single
patch-note line, checks it against the competition gate — UTF-8 text, 1 to
160 characters, not only whitespace, a single line — and writes it to
`/output/entry.txt`. The run is fully deterministic: the same line every time.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```
