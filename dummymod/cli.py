import sys
from importlib import metadata


def main():
    ep = metadata.entry_points()
    
    # Dump entry-point groups (console_scripts, etc.)
    for g in ep:
        print(f"# Group: {g}", file=sys.stderr)
        if g not in ('console_scripts', 'dummymod.plugins'):
            continue
        nr = 0
        for p in ep.select(group=g):
            nr += 1
            print(f"  - {p}")
        print(f"# TOTAL of {g} endpoints: " + str(nr))        
   