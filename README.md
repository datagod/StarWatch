# Pi-Star Log Watcher

A real-time log monitoring tool for Pi-Star systems. This script watches a specified directory for changes to log files and displays new entries as they occur. Each file is printed in a distinct color to help visually distinguish between multiple sources of logs. This tool is especially useful for Raspberry Pi-based ham radio setups running Pi-Star.

---

## 📌 Features

- ✅ **Real-Time Monitoring** — Watches a directory for log file updates using `watchdog`.
- ✅ **Colorized Output** — Each log file gets a unique color using `colorama`, making it easy to identify where messages are coming from.
- ✅ **Clean Output Format** — Aligns file names for consistent, readable output.
- ✅ **Auto-Tail Behavior** — Reads only the newly appended lines, like `tail -f`.
- ✅ **Simple to Use** — Just run the script and observe logs as they happen.
- ✅ **Keyboard Interrupt Support** — Stop watching any time using `Ctrl+C`.

---

## 📂 Use Case

This tool is ideal for amateur radio operators or system administrators monitoring Pi-Star logs, such as:

- `DStarRepeater.log`
- `DMRGateway.log`
- `YSFGateway.log`
- `MMDVM-*.log`

You can point it at any log directory, not just `/var/log/pi-star`.

---

## 👨‍💻 Author

**William McEvoy**
**ChatGPT 4o**
---

## 🧰 Requirements

This script is written in Python 3 and requires the following libraries:

| Package   | Purpose                   | Installation Command          |
|-----------|---------------------------|-------------------------------|
| `watchdog`| File system monitoring    | `pip install watchdog`        |
| `colorama`| Terminal color support    | `pip install colorama`        |

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/pi-star-log-watcher.git
cd pi-star-log-watcher
```

### Step 2: Install Python Packages

Make sure you’re in a virtual environment or have root permissions:

```bash
pip install watchdog colorama
```

---

## ▶️ Usage

1. **Edit the script** to point to your desired log folder. For Pi-Star, the default is:

```python
log_directory = "/var/log/pi-star"
```

2. **Run the script**:

```bash
python3 log_watcher.py
```

3. You’ll see a banner, then live updates from the logs, like:

```
DMRGateway.log    : Starting DMR Gateway service...
DStarRepeater.log : Connected to reflector...
```

Press `Ctrl+C` to exit at any time.

---

## 🖥️ Screenshot (Example Output)

```
 ____  _              __        __    _       _
/ ___|| |_ __ _ _ __  \ \      / /_ _| |_ ___| |__
\___ \| __/ _` | '__|  \ \ /\ / / _` | __/ __| '_ \
 ___) | || (_| | |      \ V  V / (_| | || (__| | | |
|____/ \__\__,_|_|       \_/\_/ \__,_|\__\___|_| |_|

An AI generated tool to watch your pi-star log directory

DMRGateway.log     : [2025-03-22 17:34:01] Received transmission from ...
YSFGateway.log     : [2025-03-22 17:34:02] Linking to reflector ...
```

---

## 🛠️ Customization

- To monitor a different folder, update the `log_directory` variable.
- To support subdirectories, set `recursive=True` in the observer (not recommended for large trees).
- You can change the color rotation order or add more colors in the `self.colors` list.

---

## 🧪 Testing

For testing purposes, create a dummy folder and simulate log updates:

```bash
mkdir /tmp/test-logs
echo "Starting up..." > /tmp/test-logs/sample.log
python3 log_watcher.py  # Then in another terminal:
echo "New log entry..." >> /tmp/test-logs/sample.log
```

---

## ⚠️ Limitations

- Does not detect newly created log files after the script starts.
- Reads entire files on start to determine position; can be adjusted to truncate old files if needed.
- Intended for local log directories; remote or network drives may have latency.

---

## 📜 License

MIT License – see [`LICENSE`](LICENSE) for details.

---

## 🙏 Acknowledgements

- [Watchdog](https://pypi.org/project/watchdog/) by Ben Hoyt and contributors  
- [Colorama](https://pypi.org/project/colorama/) by Jonathan Hartley

---

## 📬 Feedback

Feel free to submit issues or pull requests. Contributions are welcome!
