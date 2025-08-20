import sys
import socket
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit,
    QTabWidget, QLineEdit, QLabel, QProgressBar, QMessageBox, QHBoxLayout
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal

# ---------------- Modules ----------------
from modules.ping_module import run_ping
from modules.nmap_module import run_nmap_scan
from modules.whois_module import run_whois
from modules.http_headers_module import fetch_http_headers
from modules.dns_lookup_module import run_dns_lookup
from modules.port_scanner_module import run_port_scan
from modules.subdomain_module import run_subdomain_scan
from modules.save_results_module import save_results

# ---------------- Worker Thread ----------------
class WorkerThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, func, target):
        super().__init__()
        self.func = func
        self.target = target

    def run(self):
        try:
            result = self.func(self.target)
        except Exception as e:
            result = f"[ERROR] {str(e)}"
        self.finished.emit(result)

# ---------------- Main GUI ----------------
class WebAttackGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Attack GUI")
        self.resize(800, 600)
        self.threads = []  # keep running threads references

        self.tabs = QTabWidget()

        # Add tabs
        self.tabs.addTab(self.create_tab("Ping", run_ping, "assets/ping.png"), QIcon("assets/ping.png"), "Ping")
        self.tabs.addTab(self.create_tab("Nmap", run_nmap_scan, "assets/nmap.png"), QIcon("assets/nmap.png"), "Nmap")
        self.tabs.addTab(self.create_tab("Whois", run_whois, "assets/whois.png"), QIcon("assets/whois.png"), "Whois")
        self.tabs.addTab(self.create_tab("HTTP Headers", fetch_http_headers, "assets/headers.png"), QIcon("assets/headers.png"), "HTTP Headers")
        self.tabs.addTab(self.create_tab("DNS Lookup", run_dns_lookup, "assets/dns.png"), QIcon("assets/dns.png"), "DNS Lookup")
        self.tabs.addTab(self.create_tab("Port Scanner", run_port_scan, "assets/port.png"), QIcon("assets/port.png"), "Port Scanner")
        self.tabs.addTab(self.create_tab("Subdomain Scan", run_subdomain_scan, "assets/subdomain.png"), QIcon("assets/subdomain.png"), "Subdomain Scan")

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

        # Dark theme
        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; color: #ffffff; font-family: Consolas; font-size: 12px; }
            QPushButton { background-color: #007acc; color: white; padding: 6px; border-radius: 4px; }
            QPushButton:hover { background-color: #005f99; }
            QLineEdit { background-color: #2d2d2d; color: #ffffff; border: 1px solid #555; }
            QTextEdit { background-color: #2d2d2d; color: #00ff00; }
        """)

    # ---------------- Tab Creation ----------------
    def create_tab(self, label, func, icon_path):
        tab = QWidget()
        layout = QVBoxLayout()

        # Input field
        layout.addWidget(QLabel(f"Enter target for {label}:"))
        target_input = QLineEdit()
        layout.addWidget(target_input)

        # Output box
        output_box = QTextEdit()
        output_box.setReadOnly(True)
        layout.addWidget(output_box)

        # Progress bar
        progress = QProgressBar()
        progress.setValue(0)
        layout.addWidget(progress)

        # Buttons
        button_layout = QHBoxLayout()
        btn_run = QPushButton(f" Run {label}")
        btn_run.setIcon(QIcon(icon_path))
        btn_save = QPushButton(" Save Results")
        btn_clear = QPushButton(" Clear Output")
        button_layout.addWidget(btn_run)
        button_layout.addWidget(btn_save)
        button_layout.addWidget(btn_clear)
        layout.addLayout(button_layout)

        # ---------------- Run Scan ----------------
        def start_scan():
            if not target_input.text().strip():
                QMessageBox.warning(self, "Warning", "Please enter a target.")
                return
            progress.setValue(30)
            thread = WorkerThread(func, target_input.text())
            self.threads.append(thread)  # avoid GC
            thread.finished.connect(lambda result: self.display_result(result, output_box, progress))
            thread.start()

        btn_run.clicked.connect(start_scan)

        # ---------------- Save Results ----------------
        def save_output():
            content = output_box.toPlainText()
            if not content.strip():
                QMessageBox.warning(self, "Warning", "No results to save.")
                return
            file_path = save_results(label.lower(), content)
            QMessageBox.information(self, "Saved", f"Results saved to: {file_path}")

        btn_save.clicked.connect(save_output)

        # ---------------- Clear Output ----------------
        def clear_output():
            output_box.clear()
            progress.setValue(0)

        btn_clear.clicked.connect(clear_output)

        tab.setLayout(layout)
        return tab

    # ---------------- Display Results ----------------
    def display_result(self, result, output_box, progress):
        output_box.setPlainText(result)
        progress.setValue(100)

    # ---------------- Graceful Exit ----------------
    def closeEvent(self, event):
        for thread in self.threads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        event.accept()

# ---------------- Run App ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebAttackGUI()
    window.show()
    sys.exit(app.exec_())
