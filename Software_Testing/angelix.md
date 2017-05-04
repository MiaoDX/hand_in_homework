[angelix](https://github.com/mechtaev/angelix) is what we want to try.

## Installation

Everything is ok before `make default`, it needs to download some files as shown in [Makefile](https://github.com/mechtaev/angelix/blob/master/Makefile).

First, it will download files again when stopped abnormally and the timeout is not so good for my Internet connection.

So change the Line 32 to add `-c` to `wget` for continue download and set new timeout as you wish.

The `LLVM2_PATCH_URL` seems have connection limit, and `wget` just failed when make, I download it via browser and copy & paste it to the file, since we already have `-c` flag open we can make things done.

## Suggestion when build

I failed to build when run `make default`, and `make` one by one successful.

## previous version of z3

The problem use old version of z3 (version 2.19) which is not so easy to download now.

[Stackoverflowed](http://stackoverflow.com/questions/39893529/previous-version-of-z3-for-windows) and only have an alternative of [version 2.15](https://polybox.ethz.ch/index.php/s/r9sTrXWKm5nwzsi)

Luckily, the author uoload [a copy of 2.19 at github](https://github.com/Z3Prover/bin/raw/master/legacy/z3-2.19.tar.gz).

## TODO

I still failed to run the tests (build ok).