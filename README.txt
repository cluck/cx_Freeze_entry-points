# Demo for cx_Freeze entry-points


# Windows

```
git clone https://github.com/cluck/cx_Freeze_entry-points
cd cx_Freeze_entry-points
py -m venv venv

# Windows
venv\Scripts\pip.exe install --editable .
venv\Scripts\czfreeze build_exe --verbose

# Linux
venv/bin/pip install --editable .
venv/bin/czfreeze build_exe --verbose
```

Then compare the output:

Running native script:

```
C:\> .\venv\Scripts\python.exe .\dummy.py
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
C:\> build-exe\dummy.exe
Endpoints: 0
```

Note: tested on Linux with same results.

Looking at build-exe\lib\library.zip reveals that none of the *.dist-info directories contain a entry_points.txt.
Adding this file manually into library.zip makes the entry-points to be found.

