# MeloTTS Wrapper

A user-friendly wrapper for the [MeloTTS](https://github.com/myshell-ai/MeloTTS) high-quality multi-lingual text-to-speech library by MyShell.ai. 

This wrapper simplifies installation, provides a clean API, and enhances the user experience while using the powerful MeloTTS library.

## Features

- **Multiple Languages**: Support for English (multiple accents), Spanish, French, Chinese, Japanese, and Korean
- **Fast Performance**: Optimized for CPU real-time inference
- **Easy Installation**: Simple one-command installation that handles all dependencies
- **User-friendly API**: Clean Python interface for easy integration in your projects
- **Web Interface**: Built-in web UI for interactive text-to-speech generation
- **CLI Tool**: Command-line tool for quick text-to-speech conversion

## Supported Languages

| Language | Accents/Variants |
|----------|------------------|
| English  | US, British, Indian, Australian, Default |
| Spanish  | Default |
| French   | Default |
| Chinese  | Default (supports mixed Chinese and English) |
| Japanese | Default |
| Korean   | Default |

## Installation

### Quick Install

```bash
pip install melotts-wrapper
```

The wrapper will handle the installation of MeloTTS and all its dependencies.

### Development Install

```bash
git clone https://github.com/ThuGie/MeloTTS-Wrapper.git
cd MeloTTS-Wrapper
pip install -e .
```

## Usage

### Python API

```python
from melotts_wrapper import TextToSpeech

# Initialize TTS engine
tts = TextToSpeech()

# Generate speech with default settings (English-US)
tts.generate("Hello, this is a test of the MeloTTS wrapper.", output_file="output.wav")

# Generate speech in Spanish
tts.generate("Hola, esta es una prueba del wrapper de MeloTTS.", 
             language="ES", 
             output_file="spanish.wav")

# Generate speech with British accent
tts.generate("Hello, this is a test with a British accent.", 
             language="EN", 
             accent="EN-BR", 
             output_file="british.wav")

# Adjust speech speed (0.5 = slower, 2.0 = faster)
tts.generate("This is a fast speech sample.", 
             speed=1.5, 
             output_file="fast.wav")

# Generate speech without saving to file (returns audio data)
audio_data = tts.generate("This returns the audio data without saving to file.")
```

### Command Line Interface

The wrapper provides a simple command-line interface:

```bash
# Basic usage
melotts-wrapper "Hello, this is a test" output.wav

# Specify language
melotts-wrapper "Bonjour, c'est un test" output.wav --language FR

# Specify accent (for English)
melotts-wrapper "Hello with British accent" output.wav --language EN --accent EN-BR

# Adjust speed
melotts-wrapper "This is faster" output.wav --speed 1.5

# Read from file
melotts-wrapper input.txt output.wav --file
```

### Web UI

Launch the web interface with:

```bash
melotts-web
```

Then open your browser at http://localhost:8888 to access the web UI.

## Advanced Usage

### Customizing TTS Parameters

```python
from melotts_wrapper import TextToSpeech

tts = TextToSpeech()

# Fine-tune synthesis parameters
tts.generate("This uses custom synthesis parameters.",
             output_file="custom_params.wav",
             sdp_ratio=0.3,  # Attention control
             noise_scale=0.5,  # Variation in speech
             noise_scale_w=0.7)  # Variation in prosody
```

### Batch Processing

```python
from melotts_wrapper import TextToSpeech

tts = TextToSpeech()

# Process multiple texts
texts = [
    "First sample sentence.",
    "Second sample sentence.",
    "Third sample sentence."
]

# Generate all with same settings
tts.batch_generate(texts, 
                   output_dir="batch_output",
                   language="EN",
                   accent="EN-US")
```

## API Reference

### TextToSpeech Class

Main class for text-to-speech functionality.

```python
TextToSpeech(models_dir=None, device="auto")
```

- **models_dir**: Optional directory for storing models (default: ~/.melotts_wrapper)
- **device**: Compute device - "cpu", "cuda", "mps", or "auto" (default: "auto")

#### Methods

**generate**
```python
generate(text, language="EN", accent=None, speed=1.0, output_file=None, 
         sdp_ratio=0.2, noise_scale=0.6, noise_scale_w=0.8)
```

- **text**: Text to convert to speech
- **language**: Language code - "EN", "ES", "FR", "ZH", "JP", "KR" (default: "EN")
- **accent**: Speaker accent - "EN-Default", "EN-US", "EN-BR", "EN_INDIA", "EN-AU" (default: None)
- **speed**: Speech speed multiplier (default: 1.0)
- **output_file**: Path to save audio file (default: None, returns audio data)
- **sdp_ratio**: Attention control parameter (default: 0.2)
- **noise_scale**: Variation in speech parameter (default: 0.6)
- **noise_scale_w**: Variation in prosody parameter (default: 0.8)

**batch_generate**
```python
batch_generate(texts, output_dir, language="EN", accent=None, speed=1.0,
               sdp_ratio=0.2, noise_scale=0.6, noise_scale_w=0.8)
```

- **texts**: List of texts to convert to speech
- **output_dir**: Directory to save audio files
- **language**: Language code (default: "EN")
- **accent**: Speaker accent (default: None)
- **speed**: Speech speed multiplier (default: 1.0)
- **sdp_ratio**: Attention control parameter (default: 0.2)
- **noise_scale**: Variation in speech parameter (default: 0.6)
- **noise_scale_w**: Variation in prosody parameter (default: 0.8)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [MeloTTS](https://github.com/myshell-ai/MeloTTS) - The original TTS library by MyShell.ai
- The authors of MeloTTS: Wenliang Zhao, Xumin Yu, and Zengyi Qin
