import pandas
import numpy
import matplotlib.pyplot as plt
import sys
import re
import shutil
import os
import warnings


class ScriptProfilerPy:
    r''' Allows to check performance of each block in a python file
        Main functions:
            Profiler
    '''

    def __init__(self, filepath=None, chart=None, indent=None):
        self.filepath = filepath
        self.chart = chart
        self.indent = None
        self.totaltime = None
        self.erasedlines = []

        if self.filepath is not None and isinstance(self.filepath, str):
            try:
                self.indent = len(sys.argv[1])
            except:
                self.indent = self.checkFileIndent()
        else:
            raise ValueError(
                "filepath should be complete path string to a valid py script")

    def test():
        pass

    def eraseEmptyLines(self, filetest_path_ext):
        with open(filetest_path_ext, 'r') as f:
            contents = f.readlines()
            f.close()
            # Handle last line to prevent IndexError

            for i, j in enumerate(contents):
                if j[:2] == "\n" or j.strip() == " ":
                    contents[i] = ""
                    self.erasedlines.append(i)

        with open(filetest_path_ext, 'w') as f:
            f.writelines(contents)
            f.close()

    def indexFirstMatch(self, matchvalue, matcharray):
        match_at = [i for i, j in enumerate(matcharray) if matchvalue <= j]
        if len(matcharray) == 0:
            return 0
        else:
            try:
                return match_at[0]
            except:
                return 0

    def Profiler(self):
        # Copy file example.txt into a new file called example_copy.txt
        pathname, extension = os.path.splitext(self.filepath)
        filetest_path = pathname + '_STP_test'
        filetest_path_ext = filetest_path + '.py'
        shutil.copy2(self.filepath, filetest_path_ext)

        self.eraseEmptyLines(filetest_path_ext)

        with open(filetest_path_ext, 'r') as f:
            contents = f.readlines()
            f.close()

            indented_lines = []
            for line_number, line in enumerate(contents):
                if re.match(r'^\s', line):
                    indented_lines.append(line_number)

        with open(filetest_path_ext, 'w') as f:
            for i, j in enumerate(contents):
                if i == 0:
                    contents[i] += "\nfrom datetime import datetime\n"
                    contents[i] += "import shutil\n"
                    contents[i] += "from speed_testpy import ScriptProfilerPy\n"
                    contents[i] += "import matplotlib.pyplot as plt\n"
                    contents[i] += "from matplotlib.ticker import LinearLocator\n"
                    contents[i] += "speed_test_restime = []\n"
                    contents[i] += "speed_test_lines = []\n"
                    contents[i] += "speedtest_startimefile = datetime.now()\n"
                    contents[i] += "global speedtest_startime\n"
                    contents[i] += "speedtest_startime = datetime.now()\n"
                    contents[i] += "def STP_check(passed_line, speedtest_startime):\n"
                    contents[i] += f"{self.indent*' '}speed_test_restime.append((datetime.now()-speedtest_startime).total_seconds())\n"
                    contents[i] += f"{self.indent*' '}speed_test_lines.append(passed_line)\n"
                    contents[i] += f"{self.indent*' '}speedtest_startime = datetime.now()\n"
                    continue

                elif not (((i-1) in indented_lines) or (i in indented_lines) or ((i+1) in indented_lines)):
                    contents[i] += f"STP_check({i+self.indexFirstMatch(i, self.erasedlines)}, speedtest_startime)\n"
                    contents[i] += f"speedtest_startime = datetime.now()\n"
                    # contents[i] += "speed_test_restime.append((datetime.now()-speedtest_startime).total_seconds())\n"
                    # contents[i] += f"speed_test_lines.append({i})\n"
                    # contents[i] += f"speedtest_startime = datetime.now()\n"

                if i == max(enumerate(contents))[0]:
                    contents[i] += "\nplt.figure()\n"
                    contents[i] += "x = speed_test_lines[::-1]\n"
                    contents[i] += "restime = speed_test_restime[::-1]\n"
                    contents[i] += "x_pos = [i for i, _ in enumerate(x)]\n"
                    contents[i] += "plt.barh(x_pos, restime, color='green')\n"
                    contents[i] += "timerun = np.round((speedtest_startime - speedtest_startimefile).total_seconds(),3)\n"
                    contents[i] += "plt.ylabel('Code Lines')\n"
                    contents[i] += "plt.yticks(fontsize=8)\n"
                    contents[i] += """plt.xlabel(f"Time (seconds), Script execution: {timerun}'s")\n"""
                    contents[i] += "plt.title('Code profile')\n"
                    contents[i] += "plt.yticks(x_pos, x)\n"
                    contents[i] += "plt.show()\n"

            f.writelines(contents)
            f.close()

        try:
            execute_file = __import__(filetest_path)
            import execute_file
            os.remove(filetest_path_ext)
        except:
            pass

    def plot_perfs():
        pass

    def check_indentation(self):
        with open(self.filepath, 'r') as f:
            contents = f.readlines()
            f.close()

            for i, j in enumerate(contents):
                if re.match(r'^\s', j):
                    print("Indentation at line: " + str(i+1))

    def indentCount(self, txt_string=None):
        r''' Check indentation in a string with spaces (2 or 4)
            Returns None if more than 4 spaces are in left side of a string'''
        spaces = 0
        self.indent = None

        if not isinstance(txt_string, str):
            pass

        for i, j in enumerate(txt_string):
            if i == spaces and j == " ":
                spaces += 1
            if j == " " and txt_string[i+1] != " ":
                if spaces == 2:
                    self.indent = 2
                    break
                if spaces == 4:
                    self.indent = 4
                    break
                continue

        return self.indent

    def checkFileIndent(self):
        r''' Check indentation in a string with spaces (2 or 4)
            Returns None if more than 4 spaces are in left side of a string'''
        self.indent = None
        try:
            self.indent = len(sys.argv[1])
        except:
            self.indent = None
            with open(self.filepath, "r") as f:
                contents = f.readlines()
                f.close()
                for line in contents:
                    if self.indent == None:
                        self.indent = self.indentCount(line)
            return self.indent
