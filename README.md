# OmniPath

OmniPath is a Python-based utility designed to efficiently manage and analyze data storage on Windows systems using advanced algorithms. It provides insights into the storage usage of various drives and offers suggestions for better data management.

## Features

- **Drive Detection**: Automatically detects fixed drives on the system.
- **Storage Analysis**: Provides detailed information on total, used, free space, and usage percentage for each drive.
- **Management Suggestions**: Offers recommendations for drives that exceed a specified usage threshold.

## Requirements

- Python 3.x
- psutil library

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the `psutil` library using pip:

   ```bash
   pip install psutil
   ```

3. Download the `omnipath.py` file to your local machine.

## Usage

Run the script using Python:

```bash
python omnipath.py
```

The program will output the storage analysis and provide management suggestions for each detected drive.

## Configuration

You can modify the threshold for storage management suggestions by changing the `threshold` parameter in the `manage_storage` method. The default value is 80% usage.

## Contributing

Contributions to OmniPath are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact [your-email@example.com].