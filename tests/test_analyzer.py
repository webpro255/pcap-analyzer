# tests/test_analyzer.py

import unittest
import os
from pcap_analyzer.utils import read_pcap_file
from pcap_analyzer.detection import DetectionEngine

class TestPcapAnalyzer(unittest.TestCase):
    def test_detect_suspicious_activities(self):
        # Check if the sample pcap file exists
        pcap_file = 'tests/test_pcap_files/sample.pcap'
        self.assertTrue(os.path.exists(pcap_file), f"PCAP file not found: {pcap_file}")

        # Read the pcap file
        packets = read_pcap_file(pcap_file)
        
        # Run detection
        detections = DetectionEngine.detect_suspicious_activities(packets)
        
        # Assert that detections is a list
        self.assertIsInstance(detections, list)
        
        # You can add more assertions based on expected results
        # For example, if you know how many detections should be found
        # self.assertEqual(len(detections), expected_number_of_detections)

if __name__ == '__main__':
    unittest.main()
