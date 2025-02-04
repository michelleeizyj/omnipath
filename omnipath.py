import os
import psutil

class OmniPath:
    def __init__(self):
        self.drives = self.get_drives()

    def get_drives(self):
        partitions = psutil.disk_partitions()
        return [partition.device for partition in partitions if "fixed" in partition.opts]

    def analyze_storage(self):
        analysis_results = {}
        for drive in self.drives:
            usage = psutil.disk_usage(drive)
            analysis_results[drive] = {
                "total": self.convert_size(usage.total),
                "used": self.convert_size(usage.used),
                "free": self.convert_size(usage.free),
                "percent": usage.percent,
            }
        return analysis_results

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_name[i]}"

    def manage_storage(self, threshold=80):
        actions = {}
        analysis_results = self.analyze_storage()
        for drive, stats in analysis_results.items():
            if stats['percent'] > threshold:
                actions[drive] = "Consider cleaning up this drive."
            else:
                actions[drive] = "Usage is within acceptable limits."
        return actions

    def display_results(self):
        analysis = self.analyze_storage()
        management = self.manage_storage()

        print("Storage Analysis:")
        for drive, stats in analysis.items():
            print(f"Drive {drive}:")
            for key, value in stats.items():
                print(f"  {key.capitalize()}: {value}")
            print(f"  Action: {management[drive]}")
            print()

if __name__ == "__main__":
    omni_path = OmniPath()
    omni_path.display_results()