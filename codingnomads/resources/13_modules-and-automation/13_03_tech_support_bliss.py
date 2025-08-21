# Use the built-in `platform` module to print out the following info:
import platform
placeholder = "hello world"

print(f"{'Platform:':>10} {platform.platform()}",)  #macOS-15.6-arm64-arm-64bit - the platform
print(f"{'Compiler:':>10} {platform.python_compiler()}",)  #Clang 14.0.6 - the Python compiler
print(f"{'Python:':>10} {platform.python_version()}",)  #3.12.4 - the Python version
print(f"{'System:':>10} {platform.system()}",)  #Darwin - the system
print(f"{'Release:':>10} {platform.release()}",)  #24.6.0 - the release
print(f"{'System:':>10} {platform.processor()}",)  #arm - the processor