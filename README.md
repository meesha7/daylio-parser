[![ci-badge][]][ci-link] [![docs-badge][]][docs-link]
[![py-versions-badge][]][pypi-link] [![pypi-badge][]][pypi-link]

# daylio-parser

A Python module to parse Daylio CSV exports

## TODO

- [x] Parse CSV into entries (parser.py)
- [x] Implement MoodConfig (config.py) to allow multiple moods
    - [x] Plus a default config for clean Daylio installs
- [ ] Stats
    - [ ] Mood stability algorithm
    - [x] Average moods by day
    - [x] Average mood by activity
    - [ ] Find mood periods -- aka periods of moods meeting certain criteria
    - [ ] Generate data for tag clouds (i.e. find most used words in notes)
- [ ] Prepare data for plotting
    - [x] Splitting entries into bands
    - [ ] Interpolating data for smooth charts
    - [ ] Calculating rolling mean
- [ ] Re-export data into other formats
    - [ ] JSON

[ci-link]: https://github.com/meesha7/daylio-parser/actions/workflows/check.yml
[ci-badge]: https://img.shields.io/github/workflow/status/meesha7/daylio-parser/Check/master
[docs-link]: https://daylio-parser.readthedocs.io/en/latest/
[docs-badge]: https://img.shields.io/readthedocs/daylio-parser/latest
[py-versions-badge]: https://img.shields.io/pypi/pyversions/daylio-parser
[pypi-link]: https://pypi.org/project/daylio-parser/
[pypi-badge]: https://img.shields.io/pypi/v/daylio-parser
