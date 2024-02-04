# JAX Folder

This script was cobbled together as a result of https://twitter.com/sanchitgandhi99/status/1656665496463495168 and https://old.reddit.com/r/MachineLearning/comments/14xxg6i/d_what_is_the_most_efficient_version_of_openai/jrsbfps/.

This automatically takes a folder full of video files, extracts the audio, and then uses the Whisper JAX API to transcribe them and output SRT files.

I haven't tested this extensively yet but it seems to perform well enough. For me this is a replacement for using Const-Me/Whisper via Whisperer, as using this API is significantly faster.

Note: To make this file directly executable in Linux by calling main.py, uncomment the first line but leave one `#` so that it reads `#!/usr/bin/env python3`.

## Single EXE for Windows

There is a [release EXE](https://github.com/sanujar/JAXFolder/releases/latest) available. If FFMPEG is present in path or in the same folder, executing this EXE will automatically transcribe all video files in the same folder.

### Building with PyInstaller

I have a pre-generated `main.spec` file in the repo, so you can run `pyinstaller main.spec`.

To build the spec file yourself, [these steps](https://github.com/pyinstaller/pyinstaller/issues/8108#issuecomment-1815298117) need to be followed:

1. Run `pyi-makespec --collect-data=gradio_client --collect-data=gradio --onefile main.py`
2. Add the following to the analysis section of main.spec generated:
  ```a = Analysis(
    ...
    module_collection_mode={
        'gradio': 'py',  # Collect gradio package as source .py files
    },
  )```
3. Run `pyinstaller main.spec`.
