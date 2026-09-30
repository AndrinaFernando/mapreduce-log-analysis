from pathlib import Path
from multiprocessing import Pool
from time import perf_counter
import argparse

from mapper import map_file
from reducer import reduce_results

def run_analysis(data_dir: str, workers: int):
    files = sorted(str(p) for p in Path(data_dir).glob("*.log"))
    if not files:
        raise FileNotFoundError(f"No .log files found in {data_dir}")

    start = perf_counter()
    if workers == 1:
        partials = [map_file(path) for path in files]
    else:
        with Pool(processes=workers) as pool:
            partials = pool.map(map_file, files)
    combined = reduce_results(partials)
    elapsed = perf_counter() - start
    return files, combined, elapsed

def format_results(files, result, elapsed, workers):
    lines = []
    lines.append("===== MAPREDUCE SERVER LOG ANALYSIS =====")
    lines.append(f"Files processed: {len(files)}")
    lines.append(f"Workers used: {workers}")
    lines.append(f"Total valid requests: {result['total']}")
    lines.append(f"Invalid lines: {result['invalid_lines']}")
    lines.append("")
    lines.append("HTTP Methods:")
    for key, value in result["methods"].most_common():
        lines.append(f"  {key}: {value}")
    lines.append("")
    lines.append("Status Codes:")
    for key, value in sorted(result["statuses"].items()):
        lines.append(f"  {key}: {value}")
    lines.append("")
    lines.append("Top URLs:")
    for key, value in result["urls"].most_common(5):
        lines.append(f"  {key}: {value}")
    lines.append("")
    lines.append("Top IPs:")
    for key, value in result["ips"].most_common(5):
        lines.append(f"  {key}: {value}")
    lines.append("")
    lines.append(f"Execution time: {elapsed:.6f} seconds")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="MapReduce-style log analysis demo")
    parser.add_argument("--data", default="../data", help="Folder containing .log files")
    parser.add_argument("--workers", type=int, default=4, help="Number of worker processes")
    parser.add_argument("--output", default="../output/results.txt", help="Output text file")
    args = parser.parse_args()

    workers = max(1, args.workers)
    files, result, elapsed = run_analysis(args.data, workers)
    text = format_results(files, result, elapsed, workers)
    print(text)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
