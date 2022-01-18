# albert-uuid-gen

Extension for generating version 4 [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)s in [Albert launcher](https://albertlauncher.github.io/).

## Installation

1. Locate the `modules` directory in the Python extension data directory.

The data directories reside in the data directories of the application defined by Qt. Hence on linux the modules would be looked up in the following directories (in this order):

```
~/.local/share/albert/org.albert.extension.python/modules
/usr/local/share/albert/org.albert.extension.python/modules
/usr/share/albert/org.albert.extension.python/modules
```

(Note: Double-clicking on a module in the settings will open the directory in the file manager.)

2. Clone this repository into your `modules` directory.

```bash
cd /path/to/modules

git clone https://github.com/peterdb/albert-uuid-gen.git
```

3. Enable the extension in the settings under `Extensions > Python`.

## Usage

Generates 1 or more version 4 UUID(s).

Synopsis: `<trigger> [amount]`

Example: 
- `uuid`: generate 1 random UUID and copy to the clipboard.
- `uuid 42`: generate 42 random UUIDs and copy to the clipboard, the UUIDs will be separated by the newline-character.

## Contributing

If you have any questions, suggestions, or issues, please feel free to open an issue or pull request.
