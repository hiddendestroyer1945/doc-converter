#!/bin/bash

# --- Professional Dependency Installer ---

# 1. Check if the user is running with sudo/root
if [ "$EUID" -ne 0 ]; then 
  echo "Please run as root (use sudo ./install_deps.sh)"
  exit
fi

echo "--- Starting Environment Setup for Doc-Converter ---"

# 2. Update package lists
echo "[1/3] Updating system package lists..."
apt-get update -y > /dev/null

# 3. Install Pandoc and Poppler-Utils
# Pandoc: The conversion engine
# Poppler-utils: Handles PDF processing
echo "[2/3] Installing Pandoc and Poppler-Utils..."
apt-get install -y pandoc poppler-utils

# 4. Check if Python3 is installed
if command -v python3 &>/dev/null; then
    echo "[3/3] Python3 is already installed."
else
    echo "[3/3] Python3 not found. Installing..."
    apt-get install -y python3
fi

echo "------------------------------------------------"
echo "✅ Setup Complete!"
echo "You can now run: python3 doc-converter.py"
echo "------------------------------------------------"