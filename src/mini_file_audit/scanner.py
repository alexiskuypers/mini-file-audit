from pathlib import Path

def scan_folder (
    folder: Path, recursive: bool = False, 
    extensions: list[str] | None = None, 
    include_hidden: bool = False, 
    max_size: int | None = None
)-> list[Path] : 
    files = [] 
    if recursive: 
        items = folder.rglob("*")
    else :
        items = folder.iterdir()    
    for path in items:
        if not path.is_file() :
            continue
        if not include_hidden and path.name.startswith("."):
            continue
        if extensions is not None and path.suffix not in extensions : 
            continue
        try : 
            if max_size is not None and path.stat().st_size > max_size:
                continue
        except OSError: 
            continue
        files.append(path)
    return sorted(files)