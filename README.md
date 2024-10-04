# Demo for cx_Freeze entry-points


```
git clone https://github.com/cluck/cx_Freeze_entry-points
cd cx_Freeze_entry-points

# Windows:
py -m venv venv
venv\Scripts\pip.exe install --editable .
venv\Scripts\cxfreeze build_exe --verbose

# Unix:
python3 -m venv venv
venv/bin/pip install --editable .
venv/bin/cxfreeze build_exe --verbose
```

Then compare the output:

Running native script:

```
$ venv/bin/python3 dummy.py
C:\> .\venv\Scripts\python.exe .\dummy.py
```

Output:
```
# Found group: console_scripts
  - EntryPoint(name='cxfreeze', value='cx_Freeze.cli:main', group='console_scripts')
  - EntryPoint(name='cxfreeze-quickstart', value='cx_Freeze.setupwriter:main', group='console_scripts')
  - EntryPoint(name='pip', value='pip._internal.cli.main:main', group='console_scripts')
  - EntryPoint(name='pip3', value='pip._internal.cli.main:main', group='console_scripts')
  - EntryPoint(name='pip3.10', value='pip._internal.cli.main:main', group='console_scripts')
# Found group: distutils.commands
# Found group: distutils.setup_keywords
# Found group: dummymod.plugins
  - EntryPoint(name='internal', value='dummymod.plugin:plugin_main', group='dummymod.plugins')
# Found group: egg_info.writers
# Found group: setuptools.finalize_distribution_options
TOTAL of console_scripts endpoints: 5
TOTAL of dummymod.plugins endpoints: 1
```

Running compiled script:
```
$ build-exe/dummy.exe
C:\> build-exe\dummy.exe
```

Output:

```
# Found group: console_scripts
  - EntryPoint(name='pip', value='pip._internal.cli.main:main', group='console_scripts')
  - EntryPoint(name='pip3', value='pip._internal.cli.main:main', group='console_scripts')
  - EntryPoint(name='pip3.10', value='pip._internal.cli.main:main', group='console_scripts')
TOTAL of console_scripts endpoints: 3
TOTAL of dummymod.plugins endpoints: 0
```

Tested on Linux and Windows to yield the same result.

Looking at build-exe/lib/library.zip reveals that not all of the *.dist-info directories contain the required entry_points.txt. Finding these files in the venv/ directory and inserting them manually into the library.zip makes the entry-points to be found and working.

This seems to be limited to packages for which both .egg-info exists in the development directory (editable) and *.dist-info in the venv directory.
