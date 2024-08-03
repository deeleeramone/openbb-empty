# Empty OpenBB

Only the core OpenBB infrastructure is included (optional Charting, Jupyter Notebook).

The repository is intended to be cloned as a lightweight development environment. 
Alternatively, use `pip install` to install a core application shell with build and launch scripts.

## Installation

A Python environment needs to be created and activated. Use your preferred environment manager to create the Python environment.

### From Source

Clone the repository, and then from the root of the project, run:

```console
python openbb_empty/dev_install.py
```

Items within the "extensions/" folder will be installed by `dev_install.py`, but not by `poetry install`.

The "extras" listed in the PyPI section below are installable by adding the name - i.e, `dev_install.py notebook`

### PyPI

```console
pip install openbb-empty
```

Install with the charting library:

```console
pip install openbb-empty["charting"]
```

Add PyWry for Pythonic window creation.

```console
pip install openbb-empty["pywry"]
```

Add Jupyter Notebook.

```console
pip install openbb-empty["notebook"]
```

### Adding OpenBB Modules

Install data provider extensions individually, for example:

```console
pip install openbb-yfinance
```

Install the router paths independently:

```console
pip install openbb-equity openbb-derivatives
```

## Usage

With `dev_install.py`, the contents of the `/extensions` folder are installed in "editable" mode. Any changes will be reflected upon restarting the Python interpreter.

After installing a new provider or router path, rebuild the static assets:

```console
python -c "import openbb;openbb.build()"
```

### Python

Importing and operating are the same as with any other `openbb` installation; only here, there are no data providers or router paths included.
The `empty` paths are working starting points to replace with your code.

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

## Developing

Open the `/extensions` folder and examine the code to see how the pieces interact.
If your code changes are not being reflected after reloading the Python interpreter,
try rebuilding the assets:

```
import openbb
openbb.build()
```

Restart the session and try again.
