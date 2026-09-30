# MapReduce-Based Server Log Analysis

A small local demonstration of the MapReduce programming model using Python multiprocessing.

## Software
- Python 3
- VS Code (recommended)
- No external Python packages required

## Optional: generate a larger test dataset
From the `src` folder:
```bash
python generate_logs.py
```

## Run the analysis
From the `src` folder:
```bash
python main.py --data ../data --workers 4 --output ../output/results.txt
```

## Compare different worker counts
```bash
python benchmark.py
```

This writes timing results to `output/benchmark.txt`.

## Main files
- `log_parser.py` - parses each log line
- `mapper.py` - maps each input file into partial counters
- `reducer.py` - combines partial results
- `main.py` - coordinates workers and writes results
- `generate_logs.py` - creates sample log data
- `benchmark.py` - compares 1, 2, and 4 workers
