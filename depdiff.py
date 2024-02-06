import sys


try:
    deps_a_filename = sys.argv[1]
    deps_b_filename = sys.argv[2]
except IndexError:
    print("Usage: python depdiff.py <filename> <filename>")
    sys.exit(1)


def parse_deps(filename):
    deps = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                for depver in line.split(','):
                    if depver.startswith('-e'):
                        continue
                    dep, ver = depver.split('==')
                    deps[dep] = ver
    return deps


deps_a = parse_deps(deps_a_filename)
deps_b = parse_deps(deps_b_filename)

for dep, ver in deps_a.items():
    if dep in deps_b and deps_b[dep] != ver:
        print(f'Version mismatch A vs B: {dep}=={ver} vs. {dep}=={deps_b[dep]}')
    if dep not in deps_b:
        print(f'Extra dep in A: {dep}=={ver}')

for dep, ver in deps_b.items():
    if dep not in deps_a:
        print(f'Extra dep in B: {dep}=={ver}')
