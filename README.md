# simple-rss
Simple rss parser that let me read hacker news from the terminal
---

- Vibed it :(

## how to use
- `python main.py` retrieves the Best | HN RSS from hnrss.org/best and formats it into article paragraphs separated by new lines (for ease of read in vim, e.g. with '{' and '}')

- Optionally, alias it. `alias news='python <abs-path-to-this-dir>/main.py'`

- optionally, pipe into `vim` or `view` (vim read-only mode) or `less`
```shell
news | nvim -
news | view -
news | less
```
