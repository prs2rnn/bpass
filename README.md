# bpass

Don't take it seriously, I've been practicing the development process.

## Installation

Simply install from Github via pip:

```bash
pip install "git+https://github.com/luculliano/bpass.git"
```

## Usage

Generate strong password with default characteristics and copy to clipboard for 45 seconds via:

```bash
bpass
```

Display help:

```bash
bpass -h
```

Generate a password of specific length and amount:

```bash
bpass -l 20 -a 5
```

## Copy to clipboard

The generator uses `pyclip` for copying the password to the clipboard. If you run into problems, please consult the docs of the package: https://github.com/spyoungtech/pyclip

On Linux a package to support terminal copy to clipboard is needed. e.g. `wl-clipboard`:

```bash
sudo pacman -S wl-clipboard
```
