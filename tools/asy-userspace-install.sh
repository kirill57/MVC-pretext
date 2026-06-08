#!/usr/bin/env bash
# Install Asymptote into ~/.local WITHOUT root, for Linux build/CI sandboxes
# where TeX Live is already present but `asy` is not (e.g. this project's
# ephemeral build sandbox). On a normal machine, just install Asymptote the
# usual way (it ships with TeX Live) instead of using this.
set -euo pipefail
WORK="$(mktemp -d)"; cd "$WORK"
PKGS="asymptote libglew2.2 libgsl27 libgslcblas0 libsigsegv2 freeglut3 libtirpc3 libgc1 libboost-filesystem1.74.0"
apt-get download $PKGS
for d in *.deb; do dpkg-deb -x "$d" ext; done
mkdir -p "$HOME/.local/bin" "$HOME/.local/lib" "$HOME/.local/share"
cp -f ext/usr/bin/asy "$HOME/.local/bin/asy"
cp -rf ext/usr/share/asymptote "$HOME/.local/share/asymptote"
find ext/usr/lib -name '*.so*' -exec cp -f {} "$HOME/.local/lib/" \;
# Persist env for interactive shells
if ! grep -q ASYMPTOTE_DIR "$HOME/.bashrc" 2>/dev/null; then
  {
    echo ''
    echo '# --- Asymptote (user-space install) ---'
    echo 'export PATH="$HOME/.local/bin:$PATH"'
    echo 'export LD_LIBRARY_PATH="$HOME/.local/lib:$LD_LIBRARY_PATH"'
    echo 'export ASYMPTOTE_DIR="$HOME/.local/share/asymptote"'
  } >> "$HOME/.bashrc"
fi
export PATH="$HOME/.local/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/.local/lib:${LD_LIBRARY_PATH:-}"
export ASYMPTOTE_DIR="$HOME/.local/share/asymptote"
echo "Installed: $(asy --version 2>&1 | head -1)"
rm -rf "$WORK"
