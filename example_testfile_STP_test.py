import pandas as pd

from datetime import datetime
import shutil
from speed_testpy import ScriptProfilerPy
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
speed_test_restime = []
speed_test_lines = []
speedtest_startimefile = datetime.now()
global speedtest_startime
speedtest_startime = datetime.now()
def STP_check(passed_line, speedtest_startime):
    speed_test_restime.append((datetime.now()-speedtest_startime).total_seconds())
    speed_test_lines.append(passed_line)
    speedtest_startime = datetime.now()
import numpy as np
STP_check(1, speedtest_startime)
speedtest_startime = datetime.now()
import matplotlib.pyplot as plt
STP_check(2, speedtest_startime)
speedtest_startime = datetime.now()
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range("1/1/2000", periods=1000))
ts
ts = np.exp(ts.cumsum())
STP_check(6, speedtest_startime)
speedtest_startime = datetime.now()
df = pd.DataFrame(np.random.randn(1000, 4),
                  index=ts.index, columns=list("ABCD"))
df
df.head()
STP_check(10, speedtest_startime)
speedtest_startime = datetime.now()
df.head()
STP_check(11, speedtest_startime)
speedtest_startime = datetime.now()
for i in df.index:
    df.tail()
df.head()
df.head()
STP_check(16, speedtest_startime)
speedtest_startime = datetime.now()
df.tail()
STP_check(17, speedtest_startime)
speedtest_startime = datetime.now()
for i in df.index:
    
    df.tail()
df.tail()
df.tail()
STP_check(24, speedtest_startime)
speedtest_startime = datetime.now()
for i in df.index:
    df.tail()

plt.figure()
x = speed_test_lines[::-1]
restime = speed_test_restime[::-1]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, restime, color='green')
timerun = np.round((speedtest_startime - speedtest_startimefile).total_seconds(),3)
plt.ylabel('Code Lines')
plt.yticks(fontsize=8)
plt.xlabel(f"Time (seconds), Script execution: {timerun}'s")
plt.title('Code profile')
plt.yticks(x_pos, x)
plt.show()
