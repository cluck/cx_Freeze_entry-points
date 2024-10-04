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
# Group: console_scripts
# Group: distutils.commands
# Group: distutils.setup_keywords
# Group: dummymod.plugins
# Group: egg_info.writers
# Group: setuptools.finalize_distribution_options
- EntryPoint(name='internal', value='dummymod.plugin:plugin_main', group='dummymod.plugins')
Endpoints: 1
```

Running compiled script:
```
$ build-exe/dummy.exe
C:\> build-exe\dummy.exe
```

Output:

```
Endpoints: 0
```

Tested on Linux and Windows to yield the same result.

Looking at build-exe/lib/library.zip reveals that none of the *.dist-info directories contains required entry_points.txt.
Finding these files in the venv/ directory and inserting them manually into the library.zip makes the entry-points to be found and working.
