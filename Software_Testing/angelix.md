[angelix](https://github.com/mechtaev/angelix) is what we want to try.

## Installation

Everything is ok before `make default`, it needs to download some files as shown in [Makefile](https://github.com/mechtaev/angelix/blob/master/Makefile).

First, it will download files again when stopped abnormally and the timeout is not so good for my Internet connection.

So change the Line 32 to add `-c` to `wget` for continue download and set new timeout as you wish.

The `LLVM2_PATCH_URL` seems have connection limit, and `wget` just failed when make, I download it via browser and copy & paste it to the file, since we already have `-c` flag open we can make things done.