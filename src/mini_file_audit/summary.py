from pathlib import Path
from collections import Counter

NO_EXTENSION = "no_extension"

def summarize_extensions(files: list[Path])-> dict[str,object]:
    files_by_extension = Counter(
        path.suffix or NO_EXTENSION
        for path in files
    )
    sorted_files_by_extension = dict(
        sorted(
            files_by_extension.items(),
            key=lambda item: (-item[1],item[0])
        )
    )
    extension_count = sum(1 for extension in sorted_files_by_extension if extension != NO_EXTENSION)

    return {
        "extension_count":extension_count,
        "files_by_extension":sorted_files_by_extension,
    }
        
def summarize_sizes (files: list[Path])-> dict[str, object]: 
    total_files = len(files)
    total_size_bytes = sum(path.stat().st_size for path in files)
    
    if total_files > 0:
        average_file_size_bytes = total_size_bytes / total_files
    else : 
        average_file_size_bytes = 0
    if files: 
        largest_path = max(files, key= lambda path: path.stat().st_size)
        largest_file = {
            "name": largest_path.name,
            "path": str(largest_path),
            "size_bytes": largest_path.stat().st_size
        }
        smallest_path = min(files, key= lambda path : path.stat().st_size)
        smallest_file = {
            "name": smallest_path.name,
            "path": str(smallest_path),
            "size_bytes": smallest_path.stat().st_size
        }
    else :
        largest_file = None
        smallest_file = None
    
    empty_files_count = sum(1 for path in files if path.stat().st_size == 0)

    return {
        "total_files": total_files,
        "total_size_bytes": total_size_bytes,
        "average_file_size_bytes": average_file_size_bytes,
        "largest_file": largest_file,
        "smallest_file": smallest_file,
        "empty_files_count": empty_files_count,
    }

def build_summary(
        files: list[Path], 
        recursive: bool, 
        csv_output: Path, 
        json_output: Path
)-> dict [str, object]:
    csv_report_path = str(csv_output)
    summary_report_path = str(json_output)
    sizes_data = summarize_sizes(files)
    extensions_data = summarize_extensions(files)
    summary = {
        **sizes_data,
        **extensions_data,
        "recursive": recursive,
        "csv_report_path": csv_report_path,
        "summary_report_path": summary_report_path,
    }
    return summary