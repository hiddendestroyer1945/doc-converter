import os
import subprocess
import readline
import glob

# --- Tab Completion Setup ---
def completer(text, state):
    """Allows the user to use the TAB key to autocomplete file paths."""
    options = [x for x in glob.glob(text + '*') if os.path.exists(x)]
    return options[state] if state < len(options) else None

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

def main():
    print("--- Professional Linux Doc Converter ---")

    # 1. Get Source Path with Tab Completion
    source_path = input("Enter the source doc path: ").strip()
    
    if not os.path.exists(source_path):
        print(f"Error: File '{source_path}' not found.")
        return

    # 2. Get Formats
    # Note: Pandoc usually detects source format by extension, but we'll ask anyway.
    source_ext = input("Enter the source doc format (e.g., docx, pdf, txt): ").strip().lower()
    target_ext = input("Enter the target doc format (e.g., html, py, js): ").strip().lower()

    # 3. Setup Results Directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    results_dir = os.path.join(script_dir, "results")
    
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Prepare output filename
    base_name = os.path.basename(source_path)
    file_name_only = os.path.splitext(base_name)[0]
    output_path = os.path.join(results_dir, f"{file_name_only}.{target_ext}")

    # 4. The Conversion Logic
    print(f"\nConverting {base_name} to {target_ext}...")

    try:
        # Pandoc command: pandoc input.docx -o results/output.html
        # If converting FROM PDF, note that Pandoc works best with text-based formats.
        # For PDF to HTML, it's very reliable.
        subprocess.run(["pandoc", source_path, "-o", output_path], check=True)
        
        print("-" * 30)
        print(f"✅ Success!")
        print(f"Saved to: {output_path}")
        print("-" * 30)

    except subprocess.CalledProcessError:
        print("❌ Error: Conversion failed. Ensure Pandoc is installed.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()