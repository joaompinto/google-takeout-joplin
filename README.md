# Import Google Keep notes to Joplin

1. Export your Google Keep notes to a folder using the Google Takeout Service
2. Install the Joping Desktop app and enable the Web Clipper Service

```sh
export JOPLIN_TOKEN=your_token # See the value on the Joplin Desktop app clipper config
python -m joplin_import "C:\Users\lamego\OneDrive\GoogleTakeout_8.7.2023\Keep"
```