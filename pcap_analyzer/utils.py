# pcap_analyzer/utils.py

import pyshark

def read_pcap_file(file_path):
    print(f"Reading pcap file: {file_path}")
    return pyshark.FileCapture(file_path)

def generate_report(detections, report_type='txt'):
    if report_type == 'txt':
        _generate_text_report(detections)
    elif report_type == 'html':
        _generate_html_report(detections)
    else:
        print("Unsupported report format.")

def _generate_text_report(detections):
    with open('reports/report.txt', 'w') as report_file:
        report_file.write("Suspicious Activity Report\n")
        report_file.write("=" * 30 + "\n")
        if detections:
            for detection in detections:
                report_file.write(f"{detection}\n")
        else:
            report_file.write("No suspicious activities detected.\n")
    print("Report generated at reports/report.txt")

def _generate_html_report(detections):
    html_content = "<html><head><title>Suspicious Activity Report</title></head><body>"
    html_content += "<h1>Suspicious Activity Report</h1><hr>"
    if detections:
        html_content += "<ul>"
        for detection in detections:
            html_content += f"<li>{detection}</li>"
        html_content += "</ul>"
    else:
        html_content += "<p>No suspicious activities detected.</p>"
    html_content += "</body></html>"

    with open('reports/report.html', 'w') as report_file:
        report_file.write(html_content)
    print("Report generated at reports/report.html")

