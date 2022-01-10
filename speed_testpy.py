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
            test
            plot_perfs
    '''

    def __init__(self, filepath=None, chart=None, indent=None):
        self.filepath = filepath
        self.chart = chart
        self.indent = None
        self.totaltime = None

        try:
            self.indent = len(sys.argv[1])
        except:
            if filepath is not None and isinstance(filepath, str):
                self.indent = self.checkFileIndent(filepath)

    def test():
        pass

    def eraseEmptyLines(self, filepath):
        with open(filepath, 'r') as f:
            contents = f.readlines()
            f.close()
            # Handle last line to prevent IndexError
            line_count = 0
            for line in contents:
                if line[:2] == "\n" or line.strip() == " ":
                    contents[line_count] = ""
                line_count += 1
        with open(filepath, 'w') as f:
            f.writelines(contents)
            f.close()

    def Profiler(self, filepath, erase_line=True):
        # Copy file example.txt into a new file called example_copy.txt
        pathname, extension = os.path.splitext(filepath)
        filetest_path = pathname + '_STP_test'
        filetest_path_ext = filetest_path + '.py'
        shutil.copy2(filepath, filetest_path_ext)

        if erase_line == True:
            self.eraseEmptyLines(filetest_path_ext)
        else:
            warnings.warn(
                "Empty lines not erased. If the module fail, please try again with: erase_line=True")

        with open(filetest_path_ext, 'r') as f:
            contents = f.readlines()
            f.close()
            line_number = 0
            indented_lines = []
            for line in contents:
                if re.match(r'^\s', line):
                    indented_lines.append(line_number)
                line_number += 1

        with open(filetest_path_ext, 'w') as f:
            for indent_line in range(line_number):
                if indent_line == 0:
                    contents[indent_line] += "\nfrom datetime import datetime\n"
                    contents[indent_line] += "import shutil\n"
                    contents[indent_line] += "from speed_testpy import ScriptProfilerPy\n"
                    contents[indent_line] += "import matplotlib.pyplot as plt\n"
                    contents[indent_line] += "from matplotlib.ticker import LinearLocator\n"
                    contents[indent_line] += "speed_test_restime = []\n"
                    contents[indent_line] += "speed_test_lines = []\n"
                    contents[indent_line] += "speedtest_startimefile = datetime.now()\n"
                    contents[indent_line] += "global speedtest_startime\n"
                    contents[indent_line] += "speedtest_startime = datetime.now()\n"
                    contents[indent_line] += "def STP_check(passed_line, speedtest_startime):\n"
                    contents[indent_line] += f"{self.indent*' '}speed_test_restime.append((datetime.now()-speedtest_startime).total_seconds())\n"
                    contents[indent_line] += f"{self.indent*' '}speed_test_lines.append(passed_line)\n"
                    contents[indent_line] += f"{self.indent*' '}speedtest_startime = datetime.now()\n"
                    continue

                elif not (((indent_line-1) in indented_lines) or (indent_line in indented_lines) or ((indent_line+1) in indented_lines)):
                    contents[indent_line] += f"STP_check({indent_line}, speedtest_startime)\n"
                    contents[indent_line] += f"speedtest_startime = datetime.now()\n"
                    # contents[indent_line] += "speed_test_restime.append((datetime.now()-speedtest_startime).total_seconds())\n"
                    # contents[indent_line] += f"speed_test_lines.append({indent_line})\n"
                    # contents[indent_line] += f"speedtest_startime = datetime.now()\n"

                if indent_line == max(range(line_number)):
                    contents[indent_line] += "\nplt.figure()\n"
                    contents[indent_line] += "x = speed_test_lines[::-1]\n"
                    contents[indent_line] += "restime = speed_test_restime[::-1]\n"
                    contents[indent_line] += "x_pos = [i for i, _ in enumerate(x)]\n"
                    contents[indent_line] += "plt.barh(x_pos, restime, color='green')\n"
                    contents[indent_line] += "timerun = np.round((speedtest_startime - speedtest_startimefile).total_seconds(),3)\n"
                    contents[indent_line] += "plt.ylabel('Code Lines')\n"
                    contents[indent_line] += "plt.yticks(fontsize=8)\n"
                    contents[
                        indent_line] += """plt.xlabel(f"Time (seconds), Script execution: {timerun}'s")\n"""
                    contents[indent_line] += "plt.title('Code profile')\n"
                    contents[indent_line] += "plt.yticks(x_pos, x)\n"
                    contents[indent_line] += "plt.show()\n"

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

    def check_indentation(self, filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()
            f.close()
            i = 0
            for line in lines:
                i += 1
                if re.match(r'^\s', line):
                    print("Indentation at line: " + str(i+1))

    def indentCount(self, txt_string=None):
        r''' Check indentation in a string with spaces (2 or 4)
            Returns None if more than 4 spaces are in left side of a string'''
        spaces = 0
        self.indent = None

        if not isinstance(txt_string, str):
            pass

        for i in range(len(txt_string)):
            if i == spaces and txt_string[i] == " ":
                spaces += 1
            if txt_string[i] == " " and txt_string[i+1] != " ":
                if spaces == 2:
                    self.indent = 2
                    break
                if spaces == 4:
                    self.indent = 4
                    break
                continue

        return self.indent

    def checkFileIndent(self, filepath):
        r''' Check indentation in a string with spaces (2 or 4)
            Returns None if more than 4 spaces are in left side of a string'''
        self.filepath = filepath
        self.indent = None
        try:
            self.indent = len(sys.argv[1])
        except:
            self.indent = None
            with open(filepath, "r") as f:
                contents = f.readlines()
                f.close()
                for line in contents:
                    if self.indent == None:
                        self.indent = self.indentCount(line)
            return self.indent
