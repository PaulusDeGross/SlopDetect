import os
import urllib.request

os.makedirs("./data/raw", exist_ok=True)

urls = [
    "https://dataset.raid-bench.xyz/train.csv",
    "https://dataset.raid-bench.xyz/test.csv",
    "https://dataset.raid-bench.xyz/extra.csv",
    "https://dataset.raid-bench.xyz/train_none.csv",
    "https://dataset.raid-bench.xyz/test_none.csv",
    "https://dataset.raid-bench.xyz/extra_none.csv",
]

print("Downloading RAID Dataset...")

for url in urls:
    filename = url.split('/')[-1]
    output_path = os.path.join("./data/raw", filename)
    if not os.path.exists(output_path):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, output_path)
    else:
        print(f"Skipping {filename}, already exists.")