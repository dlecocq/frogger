Frogger Question
================
A frog may jump three spaces forward, or two spaces back, provided that a spot
is safe. The spot is safe if the character in the provided string at that spot
is '_'. The goal is to determine the fewest number of hops required to cross
the string.

For example, given this puzzle: `_X__XX_`, the frog makes the following jumps: `2X13XX4`.

Tests
=====
With `nose` installed, run tests with `make test`.
