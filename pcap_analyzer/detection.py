# pcap_analyzer/detection.py

from collections import defaultdict

class DetectionEngine:
    @staticmethod
    def detect_suspicious_activities(packets):
        detections = []
        syn_packets = defaultdict(int)
        port_scans = defaultdict(set)

        for packet in packets:
            try:
                if packet.transport_layer == 'TCP':
                    src_ip = packet.ip.src
                    dst_ip = packet.ip.dst
                    dst_port = int(packet.tcp.dstport)
                    flags = packet.tcp.flags

                    # Detect SYN Flood
                    if flags == '0x0002':  # SYN flag
                        syn_packets[src_ip] += 1

                    # Detect Port Scanning
                    port_scans[src_ip].add(dst_port)

            except AttributeError:
                # Non-IP packet
                continue

        # Analyze SYN counts for SYN Flood detection
        for ip, count in syn_packets.items():
            if count > 1000:
                detections.append(f"Potential SYN Flood detected from IP: {ip} (SYN packets: {count})")

        # Analyze port access patterns for Port Scan detection
        for ip, ports in port_scans.items():
            if len(ports) > 100:
                detections.append(f"Potential Port Scan detected from IP: {ip} (Ports accessed: {len(ports)})")

        return detections

