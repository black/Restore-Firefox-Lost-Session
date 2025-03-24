import json
import os
import subprocess
import webbrowser
import time


def find_firefox():
    """Find the Firefox browser executable."""
    possible_paths = [
        "C:\\Program Files\\Mozilla Firefox\\firefox.exe",  # Windows
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def extract_urls_in_order(data):
    """Extract URLs while maintaining their order in the JSON file."""
    url_list = []

    def recursive_extract(item):
        if isinstance(item, dict):
            if "entries" in item and isinstance(item["entries"], list):
                for entry in item["entries"]:
                    if isinstance(entry, dict) and "url" in entry and isinstance(entry["url"], str):
                        url_list.append(entry["url"])
            for value in item.values():
                recursive_extract(value)
        elif isinstance(item, list):
            for element in item:
                recursive_extract(element)

    recursive_extract(data)
    return url_list

def open_links_in_firefox(urls):
    """Open URLs in Firefox tabs in the given order."""
    firefox_path = find_firefox()

    if not urls:
        print("No valid URLs found.")
        return

    if firefox_path:
        print(f"Opening {len(urls)} URLs in Firefox tabs...")

        # Open the first URL normally to create a window if needed
        subprocess.Popen([firefox_path, urls[0]])
        time.sleep(5)  # Give Firefox a moment to open
        i = 0
        # Open subsequent URLs in new tabs
        for url in urls[1:]:
            subprocess.Popen([firefox_path, "-new-tab", url])
            if i<10:
                i=i+1
                print(i)
            else:
                i=0
                time.sleep(30)
                print(i)
    else:
        print("Firefox not found. Opening URLs in the default browser...")
        webbrowser.open(urls[0])
        for url in urls[1:]:
            webbrowser.open_new_tab(url)

def open_links(json_file):
    """Read a JSON file, extract URLs, and open them in Firefox tabs in order."""
    time.sleep(2)
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        urls = extract_urls_in_order(data)
        open_links_in_firefox(urls)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    json_file = "test.json"  # Change this to your JSON file path
    open_links(json_file)
