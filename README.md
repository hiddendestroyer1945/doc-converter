Professional Document Converter

A powerful, Python-based CLI tool designed for Linux environments that converts documents across multiple formats using the industry-standard Pandoc engine.
📝 Description

The Professional Document Converter is a lightweight wrapper for Pandoc and Poppler-Utils. It allows users to convert files like PDF, DOCX, and TXT into web-ready formats (HTML) or code-ready formats (Python, JavaScript, CSS) with a simple, interactive interface featuring tab-completion for file paths.
✨ Features

    Interactive Path Completion: Use the TAB key to find files easily.

    Automated Directory Management: Converted files are automatically organized into a results/ folder.

    Wide Format Support: Handles PDF, DOCX, TXT, HTML, PY, JS, SH, and more.

    Linux Optimized: Designed to run efficiently on any Debian/Ubuntu-based distribution.

🚀 Benefits

    Zero Cost: Uses 100% open-source tools.

    Privacy: All conversions happen locally on your machine; no data is sent to the cloud.

    Efficiency: Faster than opening heavy GUI applications like Microsoft Word or Adobe Acrobat.

🛠 Requirements

    Operating System: Linux (Ubuntu/Debian recommended)

    System Tools: Pandoc, Poppler-utils

    Language: Python 3.x

⚙️ Installation & Setup

Follow these steps to set up the environment from scratch.
1. Update OS and Install Core Dependencies

Open your terminal and run:
Bash

sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git pandoc poppler-utils

2. Clone the Repository
Bash

git clone https://github.com/your-username/doc-converter.git
cd doc-converter

3. Virtual Environment (venv) Setup

It is best practice to keep your Python environment isolated:
Bash

# Create the environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate

4. Execute Installer & Requirements

Ensure the setup script is executable and run it to verify all system engines are ready:
Bash

chmod +x install_deps.sh
./install_deps.sh

# Install any Python dependencies
pip install -r requirements.txt

📖 Using the Program
Example Conversion

    Run the program:
    Bash

    python3 doc-converter.py

    Input Example:

        Source path: Documents/report.docx (Press TAB to autocomplete!)

        Source format: docx

        Target format: html

The result will be available at: results/report.html
Deactivation

Once you are finished, you can exit the virtual environment:
Bash

deactivate

⚖️ License

This project is licensed under the MIT License - free for personal and commercial use.
👤 Author

hiddendestroyer Professional Beginner Programmer & Linux Enthusias