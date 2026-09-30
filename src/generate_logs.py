from pathlib import Path
import random

METHODS = ["GET", "GET", "GET", "POST", "PUT", "DELETE"]
URLS = ["/home", "/products", "/login", "/profile", "/cart", "/search", "/checkout"]
STATUSES = [200, 200, 200, 200, 201, 204, 400, 401, 404, 500]

def main():
    out_dir = Path("../data")
    out_dir.mkdir(parents=True, exist_ok=True)
    random.seed(42)

    files = 4
    lines_per_file = 25000

    for file_no in range(1, files + 1):
        path = out_dir / f"server{file_no}.log"
        with path.open("w", encoding="utf-8") as f:
            for i in range(lines_per_file):
                ip = f"192.168.{file_no}.{(i % 250) + 1}"
                method = random.choice(METHODS)
                url = random.choice(URLS)
                status = random.choice(STATUSES)
                f.write(f"{ip} {method} {url} {status}\n")
        print(f"Created {path} with {lines_per_file} lines")

    print(f"Done. Total requests generated: {files * lines_per_file}")

if __name__ == "__main__":
    main()
