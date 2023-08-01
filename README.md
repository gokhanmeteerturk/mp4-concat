# MP4 File Concatenator

![MP4 File Concatenator](https://raw.githubusercontent.com/gokhanmeteerturk/mp4-concat/main/screenshot.png)

MP4 File Concatenator is a simple graphical application built using Python and Tkinter that allows you to merge multiple MP4 video files into a single output file. This tool uses FFmpeg for the actual merging process and provides an easy-to-use interface to arrange the order of the videos before merging.

## Features

- Select multiple MP4 video files from your computer.
- Arrange the order of the selected files using the "UP" and "DOWN" buttons.
- Merge the selected MP4 files into a single output file.
- Set the output file name and location.

## Prerequisites

Before using MP4 File Concatenator, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (3.6 or above)
- FFmpeg: You can download it from the official website or install it using package managers like Homebrew on macOS or Chocolatey on Windows.

## Use Compiled Executable (Optional)
If you prefer using the compiled executable file, you can find it in the `dist` directory. You can directly run `main.exe` without installing any dependencies.

Or you can compile it by using:

```
pyinstaller --onefile -i"favicon.ico" -w main.py --collect-data sv_ttk
```

## Installation

1. Clone this repository to your local machine or download the source code as a ZIP archive and extract it.

   ```bash
   git clone https://github.com/gokhanmeteerturk/mp4-concat.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mp4-concat
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the `main.py` script:

```bash
python main.py
```

The MP4 File Concatenator window will appear:

- Click on the "Browse Files" button to select MP4 video files that you want to merge. You can select multiple files by holding the Ctrl key while clicking.

- The selected files will be listed in the order they will be merged. You can rearrange the order by selecting a file and clicking the "UP" or "DOWN" buttons.

- After arranging the files, click the "Merge" button to start the merging process. A file dialog will appear to choose the destination and file name for the merged video. By default, the output file will have the ".mp4" extension.

- Once you choose the output file location and name, the application will use FFmpeg to concatenate the selected MP4 files into a single output file. The process may take some time, depending on the size and number of input files.

- After the merging process is complete, you will find the merged video file at the specified location.

## Contributing

Contributions to this project are welcome! If you find any bugs or have suggestions for new features, please open an issue on the [GitHub repository](https://github.com/gokhanmeteerturk/mp4-concat/issues). If you want to contribute code, feel free to create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

This project uses the following third-party libraries:

- [Tkinter](https://docs.python.org/3/library/tkinter.html): Python's standard GUI library for creating graphical user interfaces.
- [FFmpeg](https://www.ffmpeg.org/): A powerful multimedia framework that can handle audio, video, and other multimedia files.
- [pywinstyles](https://github.com/gokhanmeteerturk/pywinstyles): A Python package for applying custom styles to Tkinter applications.

---

By [Gökhan Mete Ertürk](https://github.com/gokhanmeteerturk)