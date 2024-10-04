import sys
from importlib import metadata


def main():
    ep = metadata.entry_points()
    
    # Dump entry-point groups (console_scripts, etc.)
    for p in ep:
        print(f"# Group: {p}", file=sys.stderr)
        
    # Dump dummymod.plugins-specific entry-points
    nr = 0
    for p in ep.select(group='dummymod.plugins'):
        nr += 1
        print(f"- {p}")
    
    # Write total of dummymod.plugins entry-points found
    # We have one (1) entry_point in dummymod/plugin.py
    print("Endpoints: " + str(nr))
