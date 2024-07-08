from pathlib import WindowsPath as wp

title = "Zach的笔记"

list_name_exclude = [
    "index.md",
    "readme.md",
]

path_out = wp("index.md")

list_files = list(wp("").glob("*.md"))

with open(path_out, "w", encoding="utf-8") as f:
    f.write(f"# {title}\n\n")

    for i in list_files:
        if not i.name.lower() in list_name_exclude:
            f.write(f"[{i.stem}]({i})\n\n")
