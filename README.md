![badge](https://img.shields.io/badge/Python-white?logo=python) 
![badge](https://img.shields.io/badge/preset-red) 
[![badge](https://img.shields.io/badge/Package_manager-uv-8A2BE2)](https://docs.astral.sh/uv/) ![badge](https://img.shields.io/badge/Linter-Ruff-yellow)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Yoshida24/preset-python-uv)

# preset-python-uv-vscode

Preset for develop Python app by `uv`.

## Included
- Auto format on save by ruff
- Task runner by make
- Jupyter Notebook support
- Env support

## Usage

- Python: 3.12
- uv: 0.6.2
- OS and Device: M1 Macbook Air Sequoia 15.3.1

## Prerequest

Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
```

## Gettig Started
First of all, install VSCode recommended extensions. This includes Linter, Formatter, and so on. Recommendation settings is written on `.vscode/extensions.json`.

Install dependencies:

```bash
uv sync
```

To use environment variables in `.env` file, run below script to create `.env`

```bash
if [ ! -f .env ]; then
    cp .env.tmpl .env
    echo 'Info: .env file has successfully created. Please rewrite .env file'
else
    echo 'Info: Skip to create .env file. Because it is already exists.'
fi
```

Now you can run script:

```bash
# load environment variables from .env to your shell.
set -a && source ./.env && set +a
make run
```

```bash
  ____________
| Hello, Alan! |
  ============
            \
             \
               ^__^
               (oo)\_______
               (__)\       )\/\
                   ||----w |
                   ||     ||
```

> **Note**
>
> This project *does not* depends on `dotenv-python`. Instead, using below script.
> `set -a && source ./.env && set +a`

## Use Jupyter

In VSCode, `src/notebook.ipyenv` can be used with `.venv` automatically.

Serve Juyter server:

```bash
uv run --with jupyter jupyter lab
# Then automatically open http://localhost:8888/lab
```

## Cheat Sheet
Add dependencies:

```bash
uv add requests
```

Add dev dependencies:

```bash
uv add --dev ruff
```

Pin python version:

```bash
uv python pin 3.12
```

Update `uv`:

```bash
uv self update
```