# JAX Folder

This script was cobbled together as a result of https://twitter.com/sanchitgandhi99/status/1656665496463495168 and https://old.reddit.com/r/MachineLearning/comments/14xxg6i/d_what_is_the_most_efficient_version_of_openai/jrsbfps/.

This automatically takes a folder full of video files, extracts the audio, and then uses the Whisper JAX API to transcribe them and output SRT files.

I haven't tested this extensively yet but it seems to perform well enough. For me this is a replacement for using Const-Me/Whisper via Whisperer, as using this API is significantly faster.

Note: To make this file directly executable in Linux by calling main.py, uncomment the first line but leave one `#` so that it reads `#!/usr/bin/env python3`.