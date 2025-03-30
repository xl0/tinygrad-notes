import sys
import traceback
import linecache

def print_last_frame_context(exception: Exception, num_lines=2):
    # Get the last frame from the traceback
    tb = traceback.extract_tb(sys.exc_info()[2])
    last_frame = tb[-1]

    # Unpack frame info
    filename, lineno, funcname, line = last_frame

    # Print location info
    print(f"{type(exception).__name__}: {" ".join(exception.args)}")
    print(f"in {filename}:{lineno} in {funcname}()")

    # Get surrounding lines
    start = max(lineno - num_lines, 1)
    end = lineno + num_lines

    # Print code context
    print("\nCode context:")
    for i in range(start, end + 1):
        line = linecache.getline(filename, i).rstrip()
        prefix = "--->" if i == lineno else "    "
        print(f"{prefix} {i:4d} {line}")