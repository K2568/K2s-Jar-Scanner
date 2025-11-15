# made by @K2568 on Github https://github.com/K2568/K2s-Jar-Scanner
import os
import zipfile

FILTER = ""  # set this to "" to print all embedded mods

def format_print(text):
    print(text.replace("-", "  -  "))

def scan_jar(jar_path):
    format_print(os.path.basename(jar_path))

    try:
        with zipfile.ZipFile(jar_path, 'r') as jar:
            entries = jar.namelist()
            found_files = []
            has_mccreator = any(name.startswith("net/mcreator/") for name in entries)

            for name in entries:
                if name.endswith(".jar"):
                    base = os.path.basename(name)
                    if base.startswith(FILTER):
                        if name.startswith("META-INF/jarjar/") or name.startswith("META-INF/jars/"):
                            found_files.append(base)

            if found_files:
                for file in found_files:
                    format_print(f"      {file}")
            else:
                format_print("      No embedded mods")

            if has_mccreator:
                format_print("      MCREATOR DETECTED")

    except zipfile.BadZipFile:
        format_print("  Not a valid jar/zip file")

    print()

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))

    for entry in os.listdir(root_dir):
        if entry.endswith(".jar"):
            scan_jar(os.path.join(root_dir, entry))

    print("Scan finished\nhttps://github.com/K2568/K2s-Jar-Scanner")


if __name__ == "__main__":
    main()