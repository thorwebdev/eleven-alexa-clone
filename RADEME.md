## Hotword detection

https://github.com/Ant-Brain/EfficientWord-Net

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

## ElevenLabs ConvAi

### Dependencies

```
pip install elevenlabs
pip install "elevenlabs[pyaudio]"
## Linux based system
sudo apt-get update
sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
```
