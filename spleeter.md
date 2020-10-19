### Setup

* Had to change install from what was shown on spleeter repo via their spleeter-cpu.yaml file due to low memory on the AWS instance

```
conda create -n spleeter python=3.6
source activate spleeter
pip install --upgrade pip
pip install tensorflow==1.14.0 ffmpeg pandas==0.25.1 requests museval==0.3.0 musdb==0.3.1 norbert==0.2.1 spleeter ffmpeg-python
```
