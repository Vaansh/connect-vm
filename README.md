# Connect VM

A simple Python script to launch my vm at work with AppleScript.

## Usage

Add this function to your `.bashrc`

```bash
# login to vm
function vm() {
  cd /Users/temp/projects/open-vm                             # sample directory
  echo "opening vm..."
  python -u "/Users/temp/projects/open-vm/src/main.py"        # sample path
}
```
to use `vm` to launch or run it directly

## License
[MIT](https://github.com/Vaansh/connect-vm/blob/main/LICENSE)
