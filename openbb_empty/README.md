# Empty OpenBB

This is an empty OpenBB container with provider, router, and OBBject extension shells.

Only the OpenBB infrastructure is included (+ Charting), and a Jupyter Notebook server with IPython kernel.

## Installation

A Python environment must first be created and activated. Use your preferred environment manager to create the Python environment.

### From Source

From the root of the project, run:

Clone the repository, and then from the root of the project, run:

```console
python openbb_empty/dev_install.py
```

### Additional Modules

Extensions within the "extensions/" folder will be installed by `dev_setup.py`, but not by `poetry install`.

Install data provider extensions individually, for example:

```console
pip install openbb-yfinance
```

Install the router paths independently:

```console
pip install openbb-equity openbb-derivatives
```

## Usage

With `setup.py`, the package are all installed in "editable" mode. Any changes to the "empty" extensions code, in the "extensions" folder, will be reflected upon restarting the Python interpreter.

After installing a new provider or router path, rebuild the static assets:

```console
python -c "import openbb;openbb.build()"
```

### Python

Importing and operating are the same as with any other `openbb` installation; only here, there are no data providers or router paths included.

```python
from openbb import obb

obb.empty.hello()
```

Use, `obb.reference`, to get a map of all installed paths and extensions.

### API

Launch the Fast API server by opening a Terminal command line and activating the environment where the package is installed, then enter:

```console
openbb-api
```

### Developing

Open the `empty` extension folders and examine the code to see how the pieces interact.
If your code changes are not being reflected after reloading the Python interpreter,
try rebuilding the assets:

```
import openbb
openbb.build()
```

Restart the session and try again.