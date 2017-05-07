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

At last, I choose to download the virtualbox image files, it's too big, I just wonder why not the author compress it first. -.-

```
Angelix VM request form
Thank you for your interest in Angelix!

Please download the following files:
https://s3-ap-southeast-1.amazonaws.com/angelix/angelix-icse16-v2.vbox
https://s3-ap-southeast-1.amazonaws.com/angelix/angelix-icse16-v2.vdi (9.7 GB)
https://s3-ap-southeast-1.amazonaws.com/angelix/md5sum.txt

Execute "md5sum -c md5sum.txt" to verify your download.

The image includes Ubuntu 14.04 64-bit with pre-installed Angelix.

**********************************************
*    The user/password are angelix/angelix.  *
**********************************************
```

![download_vm_files](download_vm_files.png)


## The original version of modules:

I download the original virtualbox image files and digest the explicit version of different modules:

The code base is `icse16`:

modules include `llvm-gcc llvm2 minisat stp klee-uclibc klee z3 clang bear runtime frontend maxsmt synthesis semfix`


build folder: BF
src folder: SF

* `llvm-gcc`:   BF
* `llvm2`:      BF
* `minisat`:    `20130925 version`(37dc6c67e2af263), BF
* `stp`:        `20151123 version`(3785148da15919d), BF
* `klee-uclibc`: `klee_0_9_29`, the same, BF
* `klee`: `20151124 version`(0b39b9276f5),newer than to version 1.1.0, SF
* `z3`: `20150215`(96f6bf70284156), BF
* `clang`:      BF
* `bear`: **`2.1.4`**, BF
* `runtime`:
* `frontend`:
* `maxsmt`: `20151013`(82ef25715e93d), build folder
* `synthesis`:
* `semfix`:


## to clean all old build

```
make clean-all
```

And also need to remove possible files in `/usr/bin`(not find yet), `/usr/lib`(minisat), `/usr/local/bin`(stp), `usr/local/bin`(stp)


## PROCESS

After failed to recompile with the original files, I decide to try another one or just finish the project by using the virtualbox, but the author said he succeed in make a fresh install after some changes to the Makefile, well, ...