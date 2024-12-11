# Purpose

Generate a corpus of `rtlil` sources that make for good
reference material for compiler development.

The generated corpus should be 100% reproducible.

# Running

```bash
git clone --recursive git@github.com:ThePerfectComputer/rtlil-corpus.git
cd rtlil-corpus
nix-shell
```

The generated corpus should show up in `./corpus`.