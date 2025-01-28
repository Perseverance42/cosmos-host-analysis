# Cosmos Hosts Analysis

This project is designed to analyze and visualize host data from JSON files, providing insights into geographical distribution and ISP information.

## Project Structure

- `host-analysis.py`: A script that processes JSON files containing host data, queries geolocation information, and saves the results to a CSV file.
- `visualize.ipynb`: A Jupyter Notebook that visualizes the data from the CSV file, including ISP distribution and host country distribution.
- `data/`: Directory containing JSON files with host data and the resulting CSV file.
- `requirements.txt`: Lists the Python dependencies required for this project.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
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

- The `addrsbook` JSON files in the `data/` directory are expected to be in CosmosSDKs addresbook format.
- The script will output a CSV file named `host-analysis_full.csv` in the same directory.

## Notes

- The script uses the `ip-api.com` service for geolocation data. Be mindful of the API's usage limits.
- Ensure that the JSON files are correctly formatted to avoid processing errors.

## License

This project is licensed under the MIT License. See the LICENSE file for more details. 