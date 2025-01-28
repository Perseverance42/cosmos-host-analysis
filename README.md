# Cosmos Hosts Analysis

This project analyzes and visualizes host data from JSON files, providing insights into geographical distribution and ISP information.

## Project Structure

- `host-analysis.py`: Script that processes JSON host data, queries geolocation information, and saves results to a CSV file
- `visualize.ipynb`: Jupyter Notebook for generating visualizations (ISP distribution and geo heatmap)
- `data/`: Directory containing:
  - Input JSON files (Cosmos SDK address book format)
  - Output `host-analysis.csv` with processed data
- `requirements.txt`: Python dependencies list

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Perseverance42/cosmos-host-analysis.git
   cd cosmos-hosts-analysis
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the analysis script**:
   Execute the `host-analysis.py` script to process the JSON files and generate a CSV file with geolocation data.
   ```bash
   python host-analysis.py
   ```

2. **Visualize the data**:
   Open the `visualize.ipynb` notebook in Jupyter to generate visualizations of the data.
   ```bash
   jupyter notebook visualize.ipynb
   ```

## Data

- The `addrbook` JSON files in the `data/` directory are expected to be in CosmosSDKs addresbook format.
- The scipt tries to parse all `*.json` files in the data directory, so addrbooks from multiple hosts can be processed at once.
- The script will output a CSV file named `host-analysis.csv` in the same directory.

## Notes

- The script uses the `ip-api.com` service for geolocation data. Be mindful of the API's usage limits.
- Ensure that the JSON files are correctly formatted to avoid processing errors.
- A cutoff date can be specified in `host-analysis.py`, only hosts that had succesful connections after the cutoff will be processed.

## License

This project is licensed under the MIT License.