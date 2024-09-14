# tests/test_analyzer.py

import unittest
import os
from pcap_analyzer.utils import read_pcap_file
from pcap_analyzer.detection import DetectionEngine

class TestPcapAnalyzer(unittest.TestCase):
    def test_detect_suspicious_activities(self):
        pcap_file = os.path.join('tests', 'test_pcap_files', 'sample.pcapng')
        self.assertTrue(os.path.exists(pcap_file), f"PCAP file not found: {pcap_file}")
        
        try:
            packets = read_pcap_file(pcap_file)
            detections = DetectionEngine.detect_suspicious_activities(packets)
            self.assertIsInstance(detections, list)
        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

if __name__ == '__main__':
    unittest.main()
