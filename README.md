# ScriptProfiler helps you track where your code is slow

It provides:

- Code lines that impact your code speed.
- Visualisation of slow code lines for quick fix.

# Setup

Python 3.9
Require matplotlib.pyplot, numpy

from speed_testpy import ScriptProfilerPy

ScriptProfilerPy().Profiler(filepath="your_py_file_totest_path", erase_line=True)

'If the program fails, try again with Profiler(filepath, erase_line=True)

**Your script will be executed as a standard python import**

# Output:

![ScriptProfilerPy](https://github.com/Lucas-BLP/ScriptProfilerPy/blob/master/code_profile_output.png)

# How it works:

Provide the python script path
The module will insert datetime() variable at each non-indented line.

- Your code is opened, read and duplicated
- New lines of code are inserted with timestamps
- A new file is created with the name extension "\_STP".

A python script "SpeedTestPy (STP)" file is created that is, your code + timestamps.

Add lines of code to keep track of execution time between each line of your code.
Add lines of code to plot the performance as a bar chart.

At the end the module execute your file.
Total time display is then, the time taken by your code to run entirely.

# License:

Copyright (c) 2021-2022 Lucas Boulé

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
