import sys
from importlib import metadata


def main():
    ep = metadata.entry_points()
    
    # Dump entry-point groups (console_scripts, etc.)
    totals = {'console_scripts': 0, 'dummymod.plugins': 0}
    for g in ep:
        print(f"# Found group: {g}", file=sys.stderr)
        if g not in totals:
            continue
        nr = 0
        for p in ep.select(group=g):
            nr += 1
            print(f"  - {p}")
        totals[g] = nr
    for g in totals:
        print(f"TOTAL of {g} endpoints: " + str(totals[g]))
   