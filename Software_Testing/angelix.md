[angelix](https://github.com/mechtaev/angelix) is what we want to try for our Software Testing class.

## Installation

Everything is ok before `make default`, it needs to download some files as shown in [Makefile](https://github.com/mechtaev/angelix/blob/master/Makefile).

First, the timeout is not so good for my Internet connection, so change Line#32 to set new timeout as you wish.

The `LLVM2_PATCH_URL` seems have connection limit, and `wget` just failed in make, I download it via browser and copy & paste it to the file.

## Suggestion when build

I failed to build when run `make default`, and `make` one by one successful.

## previous version of z3

The problem use old version of z3 (version 2.19) which is not so easy to download now.

[Stackoverflowed](http://stackoverflow.com/questions/39893529/previous-version-of-z3-for-windows) and only have an alternative of [version 2.15](https://polybox.ethz.ch/index.php/s/r9sTrXWKm5nwzsi)

Luckily, the author uoload [a copy of 2.19 at github](https://github.com/Z3Prover/bin/raw/master/legacy/z3-2.19.tar.gz) [after asking for it](https://github.com/Z3Prover/z3/issues/997).

## THEN

I still failed to run the tests (build ok).

At last, I choose to download the virtualbox image files, it's too big, I just wonder why not the author compress it first (9.x GB vs 2.8 GB). -.-

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

I download the original virtualbox image files and tried to find the explicit version of different modules:

The code base is `icse16`:

modules include `llvm-gcc llvm2 minisat stp klee-uclibc klee z3 clang bear runtime frontend maxsmt synthesis semfix`

build folder: BF
src folder: SF

* `llvm-gcc`:   BF
* `llvm2`:      BF
* `minisat`:    `20130925 version`(37dc6c67e2af263), BF
* `stp`:        `20151123 version`(3785148da15919d), BF
* `klee-uclibc`: `klee_0_9_29`, the same, BF
* `klee`: `20151124 version`(0b39b9276f5), SF
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

And also need to remove possible files in `/usr/bin`(minisat), `/usr/lib`(minisat), `/usr/local/bin`(stp), `usr/local/bin`(stp)


## PROCESS

After failed to recompile with the original files, I decide to try another one or just finish the project by using the virtualbox, but the author said he succeed in make a fresh install after some changes to the Makefile, well, ...


## Build in a very fresh new virtualenv

After comments to the author via email, he add the version of [`Bear`](https://github.com/rizsotto/Bear.git) to `2.1.4`.

And it seems that `STP` version is still not so right, change it to `2.1.2` by changing the Line#100 to `cd build && git clone --branch=2.1.2 $(STP_URL)`

And, you know what? It all build ok and tests are also ok! (Even at the first time, `make semfix` failed, but after poweroff and restart the virtual machine, it magically succeed)

## Conclusion

Building angelix seems take me for than two weeks and several late night. Mostly, I do my stuff and every ten or twenty or thirty minutes to look at the putty and hope build is OK. It can be really time consuming for some modules, i.e. stp, z3, clang, frontend.

## Lesson Learned

If I am going to make a big program, or more precisely, a complex program which need lots of other modules, I will try my best to make the code module versions as explicit as possible. So, I really appreciate the programming community's efforts on the version management in programming languages, like nodejs, python, java, scala and so on (note the absence of official C/C++ ones). But things will come really complex when the code base is a combination of many programming languages, like in angelix this time, there are C++, scala, perl and python. And to be honest, the author really did a hard job to make all the configurations much easier by the `activate` file to provide various environment variables and version number in `Makefile`. But the usage of `master` codebase is error prone, since the code will change and it makes no sense that the latter code is still suitable for our usage as today.

So, when I finally have chance to make a big and complex project, hopefully I will do slight better than the author of angelix and that's it.