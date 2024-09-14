![GitHub license](https://img.shields.io/github/license/webpro255/pcap-analyzer)
![GitHub issues](https://img.shields.io/github/issues/webpro255/pcap-analyzer)
![Build Status](https://github.com/webpro255/pcap-analyzer/actions/workflows/python-app.yml/badge.svg)

# PCAP Analyzer

A Python tool to analyze pcap files for suspicious or malicious network activities.

## Features

- **Packet Parsing:** Reads and interprets pcap files using PyShark.
- **Protocol Analysis:** Analyzes TCP/IP packets for signs of suspicious behavior.
- **Detection Engine:** Identifies potential SYN Floods and Port Scans.
- **Reporting:** Generates reports in text or HTML format.
- **Extensibility:** Modular design allows for adding more detection rules.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Clone the Repository

```bash
git clone https://github.com/webpro255/pcap-analyzer.git
cd pcap-analyzer
```
### Install Dependencies

```
pip3 install -r requirements.txt
```
### Usage
```
python3 pcap_analyzer/analyzer.py <path_to_pcap_file> --report <report_format>

```
- `<path_to_pcap_file>`: Path to the pcap file you want to analyze.
- `--report`: (Optional) Report format (`txt` or `html`). Default is `txt`.
### Example

```
python3 pcap_analyzer/analyzer.py tests/test_pcap_files/sample.pcap --report html
```

### Testing
Run unit tests using:
```
python -m unittest discover tests
```
### Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
