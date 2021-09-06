from setuptools import setup

setup(
    name="duckypad",
    py_modules=[
        "autogui",
        "check_update",
        "ds_syntax_check",
        "duck_objs",
        "duckypad_config",
        "hid_op",
    ],
    install_requires=["appdirs", "hidapi"],
    scripts=["build_linux.py", "build_mac.py", "build_windows.py"],
    entry_points="""
    [console_scripts]
    duckypad_config=duckypad_config:main
  """,
)
