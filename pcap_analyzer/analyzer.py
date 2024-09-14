# pcap_analyzer/analyzer.py

import argparse
from pcap_analyzer.detection import DetectionEngine
from pcap_analyzer.utils import read_pcap_file, generate_report

def main():
    parser = argparse.ArgumentParser(description='PCAP Analyzer')
    parser.add_argument('pcap_file', help='Path to the pcap file')
    parser.add_argument('--report', choices=['txt', 'html'], default='txt', help='Report format')
    args = parser.parse_args()

    packets = read_pcap_file(args.pcap_file)
    detections = DetectionEngine.detect_suspicious_activities(packets)
    generate_report(detections, report_type=args.report)

if __name__ == "__main__":
    main()

