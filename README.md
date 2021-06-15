# Pytest-Explicit
[![pypi version](https://img.shields.io/pypi/v/pytest-explicit)](https://pypi.org/project/pytest-explicit/)
[![python versions](https://img.shields.io/pypi/pyversions/pytest-explicit)](https://pypi.org/project/pytest-explicit/)
[![package state](https://img.shields.io/pypi/status/pytest-explicit)](https://pypi.org/project/pytest-explicit/)
[![pypi release](https://img.shields.io/github/workflow/status/taliamax/pytest-explicit/release)](https://github.com/taliamax/pytest-explicit/actions/workflows/release.yaml)
[![pypi downloads](https://img.shields.io/pypi/dm/pytest-explicit)](https://pypi.org/project/pytest-explicit/)
[![license](https://img.shields.io/pypi/l/pytest-explicit)](https://github.com/taliamax/pytest-explicit/blob/main/LICENSE)


## Some tests you just don't want to run

Hey, I get it. Sometimes we write tests, but we don't actually want to wait
for them to finish executing. Whether they're slow tests, they need some
dependencies you don't have, or they aren't related to the work you
do, there's some tests that just weren't meant to be run by devs in the age
of CI/CD platforms. That's where `pytest-explicit` comes in.


This plugin allows developers to specify test markers that should be ignored
by default when running `pytest`, but also quickly bypass this behaviour
for CI/CD. Just add a `--run-all` flag to your pytest command for your test
pipeline, and this plugin won't skip anything!

## Configuring

If all you want to do is skip slow tests by default, you can stop reading
now. Out-of-the-box, `pytest-explicit` will make any test marked `slow`
require you to pass the `--run-slow` (or `--run-all`) for them to take
up precious developer time.

Need more ignored tests? Just add the `explicit-only` option to your
pytest config file, and `pytest-explicit` will pick up the markers
specified and dynamically add `--run-<marker>` CLI options to pytest. Here's
a sample `setup.cfg` file below!

```ini
[tool:pytest]
markers =
    slow: Marks a slow test
    memory_intensive: Marks a test that needs at least 16 gb RAM to run
    smoke: Marks a test that gives early alert to the health of the app
testpaths = tests
explicit-only =
    slow
    memory_intensive
```

With this configuration file, any test marked with either `slow` or
`memory_intensive` won't run unless the appropriate CLI flags are passed!
