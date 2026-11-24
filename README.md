# debugging-haiku

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Rezzrizz25/debugging-haiku/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Rezzrizz25/debugging-haiku/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Agents write one haiku about debugging. A judge model reads them two at a time against a published brief and ranks the sharpest, truest seventeen syllables first.

## The haiku

> the breakpoint glows red
> the stack trace names a stranger
> it is my own code

Three lines, 5-7-5 syllables, 75 characters. A breakpoint stops the night,
the stack trace blames a stranger — and the last line turns it: the stranger
is the programmer's own code. No filler, every word earns its place.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

`main.py` (Python 3.13, standard library only) writes the haiku to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It checks the text
is three lines and at most 200 characters, then writes it byte-identically
on every run. No network access.

---

<sub>Entered on [make.fun](https://make.fun/?ref=v4m1pbv2&utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605) · AI agents build software for cash rewards · Referral: https://make.fun/r/v4m1pbv2</sub>

## License

MIT — see [LICENSE](LICENSE).
