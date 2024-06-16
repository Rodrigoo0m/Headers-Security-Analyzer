
# HTTP Headers Security Analyzer

A Python script to analyze HTTP response headers from web servers to identify relevant security information.

## Features

- Checks for common security headers:
  - Content-Security-Policy
  - Strict-Transport-Security
  - X-Content-Type-Options
  - X-Frame-Options
  - X-XSS-Protection
  - Referrer-Policy
- Provides a clear output indicating whether each header is present and its value.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/http-headers-security-analyzer.git
   ```

2. Navigate to the project directory:
   ```sh
   cd http-headers-security-analyzer
   ```

3. Install the required library:
   ```sh
   pip install requests
   ```

## Usage

1. Run the script:
   ```sh
   python analyze_http_headers.py
   ```

2. Enter the URL you want to analyze when prompted:
   ```sh
   Enter the URL to analyze: https://example.com
   ```

3. View the analysis results:
   ```sh
   Analyzing security headers for https://example.com

   Content-Security-Policy: Not present
   Strict-Transport-Security: Not present
   X-Content-Type-Options: Not present
   X-Frame-Options: DENY
   X-XSS-Protection: 1; mode=block
   Referrer-Policy: Not present
   ```

## Example Output

```sh
Analyzing security headers for https://example.com

Content-Security-Policy: Not present
Strict-Transport-Security: Not present
X-Content-Type-Options: Not present
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Referrer-Policy: Not present
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
