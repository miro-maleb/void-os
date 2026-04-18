# Void OS

Mobile companion to lo/life-os. Anti-attention Android app with radial menu interface.

Black screen. Touch anywhere. Radial menu appears at your finger. Drag to select. Done.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Desktop Development

```bash
python main.py
```

## Building APK

```bash
buildozer init
buildozer android debug
```

See `project.md` in kb/projects/void for full spec and design philosophy.
