# ElevenLabs Alexa Clone for Raspberry Pi

## Hotword detection

https://github.com/Ant-Brain/EfficientWord-Net

## Quickstart

Install audio related libraries

```
sudo apt-get update
sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
```

Setup virtual environment and install dependencies

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python hotword.py
```

### Dependency installation

```
# 1
## On MacOs first need
brew install portaudio
pip install PyAudio
# 2
## For Raspberry Pi use
pip install tflite-runtime
## For macos use
pip install tensorflow
# 3
pip install librosa
```

### Install EfficientWord-Net

```
pip install EfficientWord-Net
### Demo
python -m eff_word_net.engine
```

### Generate custom hotword

```
python -m eff_word_net.generate_reference --input-dir hotword_training_audio --output-dir hotword_refs --wakeword hey_eleven --model-type resnet_50_arc
```

## ElevenLabs ConvAi

### Dependencies

```
pip install elevenlabs
pip install "elevenlabs[pyaudio]"
## Linux based system
sudo apt-get update
sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
```
