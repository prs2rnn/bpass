# bpass

Don't take it seriously, I've been practicing the development process.

## Installation

Simply install from Github via pip:

```bash
pip install "git+https://github.com/luculliano/bpass.git"
```

## Usage

Generate strong password with default characteristics via:

```bash
bpass
```

Display help:

```bash
bpass -h
```

Generate a password of specific length, amount and copy it:

```bash
bpass -l 20 -a 5 -c
```

## Copy to clipboard

The generator uses `pyclip` for copying the password to the clipboard. If you run into problems, please consult the docs of the package: https://github.com/spyoungtech/pyclip

On Linux a package to support terminal copy to clipboard is needed. e.g. `wl-clipboard`:

```bash
sudo pacman -S wl-clipboard
```
