# Repository Test Script

A basic Python test script which can be used to verify the repository and a Bazel installation. The test script imports some modules from [the repository's dependency tree](https://github.com/jaylamb/jdl_bench/blob/main/requirements_lock.txt) and does some very basic things with them.

## Execution
To run the test script, use the following command:
```bash
bazel run repository_test:test_script
```

The output should resemble:
```
Starting local Bazel server and connecting to it...
INFO: Analyzed target //repository_test:test_script (52 packages loaded, 6443 targets configured).
INFO: Found 1 target...
Target //repository_test:test_script up-to-date:
  bazel-bin/repository_test/test_script
INFO: Elapsed time: 8.950s, Critical Path: 1.46s
INFO: 4 processes: 4 internal.
INFO: Build completed successfully, 4 total actions
INFO: Running command line: bazel-bin/repository_test/test_script
INFO:__main__:Repository / Dependency Test Started:

INFO:__main__:Testing sys
INFO:__main__:3.10.6 (main, Aug  2 2022, 18:26:10) [Clang 14.0.3 ]
INFO:__main__:Testing requests
INFO:__main__:<function head at 0x7f99070ab370>
INFO:__main__:Testing pandas
INFO:__main__:Test DataFrame:
   hw_column
0     hello
1     world
INFO:__main__:Testing numpy
INFO:__main__:Test Dataset: [1, 2, 3, 4, 5], Mean: 3.0
```
