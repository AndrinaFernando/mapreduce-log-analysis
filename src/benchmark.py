from pathlib import Path
from main import run_analysis

def main():
    data_dir = "../data"
    output_path = Path("../output/benchmark.txt")
    lines = ["Workers\tExecutionSeconds"]

    for workers in (1, 2, 4):
        _, result, elapsed = run_analysis(data_dir, workers)
        line = f"{workers}\t{elapsed:.6f}"
        print(line)
        lines.append(line)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Saved benchmark to {output_path}")

if __name__ == "__main__":
    main()
