def convert(path, libraries):
    import cx_Freeze
    import sys
    sys.argv.append("build")
    executables = [cx_Freeze.Executable(path)]
    cx_Freeze.setup(name="main", options={"build_exe":{"packages":[libraries]}}, executables = executables)
