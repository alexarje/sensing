# Week 4: Psychoacoustics

Psychoacoustics explores how humans perceive and interpret sound, bridging the gap between physical sound properties and subjective auditory experiences. Key topics include:

- **Pitch Perception**: How frequency relates to pitch perception and its variability among individuals.
- **Loudness**: The influence of sound intensity and duration on loudness perception.
- **Timbre**: Characteristics that differentiate sounds with the same pitch and loudness, such as a violin versus a flute.
- **Auditory Masking**: How certain sounds obscure or alter the perception of others.
- **Spatial Hearing**: The ability to localize sound sources in three-dimensional space.
- **Hearing Thresholds**: The limits of human hearing, from the quietest to the loudest perceivable sounds.

Psychoacoustics is vital in fields like audio engineering, music production, and hearing aid design, informing how sound is optimized for human listeners.

## Anatomy of the Ear

The human ear is a sophisticated organ responsible for detecting sound and maintaining balance. It consists of three main parts:

### Outer Ear
- **Components**: The **pinna** (visible part) and the **ear canal**.
- **Function**: Collects sound waves and directs them to the **eardrum**, causing vibrations.

![Outer Ear](https://upload.wikimedia.org/wikipedia/commons/4/40/Ear-anatomy-text-small-en.svg)  
*Image Source: [Wikipedia - Outer Ear](https://en.wikipedia.org/wiki/Outer_ear)*

### Middle Ear
- **Components**: Three tiny bones called the **ossicles** ([malleus](https://en.wikipedia.org/wiki/Malleus), [incus](https://en.wikipedia.org/wiki/Incus), and [stapes](https://en.wikipedia.org/wiki/Stapes)).
- **Function**: Amplifies eardrum vibrations and transmits them to the **oval window**.

![Middle Ear](https://upload.wikimedia.org/wikipedia/commons/4/4c/Middle_ear_anatomy.png)  
*Image Source: [Wikipedia - Middle Ear](https://en.wikipedia.org/wiki/Middle_ear)*

### Inner Ear
- **Components**: The **cochlea** ([cochlea](https://en.wikipedia.org/wiki/Cochlea)) and the **vestibular system** ([vestibular system](https://en.wikipedia.org/wiki/Vestibular_system)).
- **Function**: Converts mechanical vibrations into electrical signals via hair cells and maintains balance.

![Inner Ear](https://upload.wikimedia.org/wikipedia/commons/3/3e/Inner_ear_anatomy.png)  
*Image Source: [Wikipedia - Inner Ear](https://en.wikipedia.org/wiki/Inner_ear)*

---

## Psychoacoustics: A Detailed Breakdown

### Sensation

#### Auditory System
The auditory system processes sound through three main parts:
- **Outer Ear**: Collects sound waves. [Learn more](https://en.wikipedia.org/wiki/Outer_ear)
- **Middle Ear**: Amplifies sound vibrations. [Learn more](https://en.wikipedia.org/wiki/Middle_ear)
- **Inner Ear**: Converts vibrations into electrical signals. [Learn more](https://en.wikipedia.org/wiki/Inner_ear)

### Perception

#### Frequency
- **Infrasound**: Below 20 Hz. [Learn more](https://en.wikipedia.org/wiki/Infrasound)
- **Audible Sound**: 20 Hz to 20,000 Hz. [Learn more](https://en.wikipedia.org/wiki/Hearing_range)
- **Ultrasound**: Above 20,000 Hz. [Learn more](https://en.wikipedia.org/wiki/Ultrasound)

##### Instruments
- **Piano**: 32 Hz to 4186 Hz. [Learn more](https://en.wikipedia.org/wiki/Piano)
- **Saxophone**: Known for its rich tone. [Learn more](https://en.wikipedia.org/wiki/Saxophone)

##### Just Noticeable Differences (JND)
The smallest detectable frequency change. [Learn more](https://en.wikipedia.org/wiki/Just-noticeable_difference)

#### Loudness
- **Equal-Loudness Contours**: Show how loudness perception varies. [Learn more](https://en.wikipedia.org/wiki/Equal-loudness_contour)

The Fletcher-Munson curves, also known as equal-loudness contours, illustrate how human hearing sensitivity varies with frequency and loudness levels.

![Fletcher-Munson Curves](https://upload.wikimedia.org/wikipedia/commons/4/4c/Lindos1.svg)  
*Image Source: [Wikipedia - Equal-loudness contour](https://en.wikipedia.org/wiki/Equal-loudness_contour)*

- **Threshold of Hearing**: Quietest perceivable sound. [Learn more](https://en.wikipedia.org/wiki/Absolute_threshold_of_hearing)

![Threshold of Hearing](https://upload.wikimedia.org/wikipedia/commons/d/da/Average_click-evoked_waveforms_and_Average_hearing_thresholds_for_younger_and_older_adults.jpg)  
*Image Source: [Wikipedia - Hearing Thresholds](https://en.wikipedia.org/wiki/Absolute_threshold_of_hearing)*

#### Hysteresis
Hysteresis refers to the phenomenon where the response of a system depends not only on its current state but also on its past states. In psychoacoustics, this can manifest in auditory perception, where the perception of a sound may be influenced by previously heard sounds or stimuli. This concept is crucial in understanding how the auditory system adapts and reacts over time to varying acoustic environments.

![Hysteresis](https://upload.wikimedia.org/wikipedia/en/e/e2/Hysteresis.png)  
*Image Source: [Wikipedia - Hysteresis](https://en.wikipedia.org/wiki/Hysteresis)*

- **Threshold of Pain**: Sounds above 120 dB. [Learn more](https://en.wikipedia.org/wiki/Sound_pressure)

#### Time
- **Critical Bands**: Frequency ranges where masking occurs. [Learn more](https://en.wikipedia.org/wiki/Critical_band)
- **Temporal Masking**: One sound obscures another. [Learn more](https://en.wikipedia.org/wiki/Masking_(audio))

![Audio Masking Graph](https://upload.wikimedia.org/wikipedia/commons/e/eb/Audio_Mask_Graph.png)  
*Image Source: [Wikipedia - Audio Masking](https://en.wikipedia.org/wiki/Masking_(audio))*

#### Space
- **Spatial Hearing**: Localizing sound sources. [Learn more](https://en.wikipedia.org/wiki/Sound_localization)

### Cognition

#### The Brain
Processes auditory information via the cerebral cortex. [Learn more](https://en.wikipedia.org/wiki/Cerebral_cortex)

#### Auditory Cortex
Responsible for sound processing. [Learn more](https://en.wikipedia.org/wiki/Auditory_cortex)


### Filtering

```{exercise}
:label: Phase in production

Have you tried swapping the phase in a music track? Try [this phase cancellation](https://l2ork.music.vt.edu:3000/?url=VTWaves/Phase-Cancellation-Emscripten.pd) web experiment. 
```




### Audio Visualizations

- **Waveform**: A visual representation of amplitude over time. [Learn more](https://en.wikipedia.org/wiki/Waveform)
- **Spectrogram**: Displays frequency content over time. [Learn more](https://en.wikipedia.org/wiki/Spectrogram)
- **Log Mel Spectrogram**: Mimics human hearing by applying the Short-Time Fourier Transform (STFT), Mel band-pass filters, and a logarithmic transformation to represent audio on a decibel scale. Widely used in audio-related tasks for its perceptual relevance. [Learn more](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
- **MFCCs (Mel-Frequency Cepstral Coefficients)**: Extracts and compresses audio features by applying the Discrete Cosine Transform (DCT) to the Log Mel spectrum. Commonly used in speech processing, music classification, and music information retrieval. [Learn more](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
- **CQT (Constant-Q Transform)**: Uses a logarithmic frequency scale with exponentially spaced center frequencies and varying filter bandwidths. Ideal for musical note frequency extraction and analysis. [Learn more](https://en.wikipedia.org/wiki/Constant-Q_transform)


### Symbolic Representations

#### MIDI
MIDI (Musical Instrument Digital Interface) is a standard protocol for communicating musical performance data between electronic instruments and computers. It encodes information such as note pitch, velocity, duration, and control changes. [Learn more](https://en.wikipedia.org/wiki/MIDI)

#### ABC Notation
ABC Notation is a text-based music notation system that uses ASCII characters to represent musical scores. It is widely used for folk and traditional music due to its simplicity and compatibility with text-based tools. [Learn more](https://en.wikipedia.org/wiki/ABC_notation)

#### REMI
REMI (REvamped MIDI-derived events) is an enhanced representation of MIDI data designed to better capture musical rhythm and structure. It introduces features like Note Duration events, Bar and Position tokens, and Tempo events, making it suitable for music generation tasks. [Learn more](https://arxiv.org/abs/2002.00212)

#### MusicXML
MusicXML is an XML-based format for representing Western music notation. It encodes detailed musical elements such as notes, rests, articulations, and dynamics, making it ideal for sharing and analyzing sheet music. [Learn more](https://en.wikipedia.org/wiki/MusicXML)

#### Piano Roll
The Piano Roll is a visual representation of music, where time is displayed on the horizontal axis and pitch on the vertical axis. Notes are represented as rectangles, with their length indicating duration. It is commonly used in digital audio workstations (DAWs) for music editing and analysis. [Learn more](https://en.wikipedia.org/wiki/Piano_roll)

#### Note Graph
A Note Graph is a graph-based representation of musical scores, where nodes represent notes and edges capture relationships such as sequence, onset, and sustain. This approach provides a structured way to analyze and model complex musical relationships. [Learn more](https://arxiv.org/abs/2006.05417)


- **[Ideas Roadshow: Believing Your Ears - Auditory Illusions](https://ideasroadshow.com/items/believing-your-ears-auditory-illusions)**  
    *Diana Deutsch in conversation with Howard Burton* (2015), Open Agenda Publishing.



## Tools

- **PaulXStretcher**
- **SonicVisualiser**

---

## Citations

Use the following syntax for citations: `` {cite}`holdgraf_evidence_2014` ``.

```{bibliography}
```
