# Week 3: Acoustics


## Key Terms in Acoustics

Acoustics is the study of sound and its properties. The term originates from the Greek word **ἀκουστικός (akoustikos)**, meaning "of or for hearing, ready to hear." According to the **ANSI/ASA S1.1-2013** standard, acoustics can be defined as:

- (a) The science of sound, encompassing its production, transmission, and effects, both biological and psychological. [Learn more on Wikipedia](https://en.wikipedia.org/wiki/Acoustics)
- (b) The qualities of a room that determine its auditory characteristics. [Explore room acoustics on Wikipedia](https://en.wikipedia.org/wiki/Room_acoustics)

## Fundamental Concepts

### Fundamental Acoustics Terms

- **Vibrations**: Oscillatory motions of particles in a medium that generate sound waves. Vibrations can be periodic (regular) or aperiodic (irregular). [Evelyn Glennie: How to Truly Listen](https://www.ted.com/talks/evelyn_glennie_how_to_truly_listen?subtitle=en)

- **Sound waves**: Mechanical waves that propagate through a medium (such as air, water, or solids) due to particle vibrations. They can be longitudinal (particles move parallel to wave direction) or transverse (particles move perpendicular to wave direction).

- **Frequency**: The number of oscillations or cycles per second of a sound wave, measured in Hertz (Hz). Higher frequencies correspond to higher-pitched sounds.

- **Phase**: Describes the position of a point within a wave cycle, measured in degrees or radians. Phase differences between waves can lead to constructive or destructive interference.

- **Complex waves**: Sound waves composed of multiple frequencies combined together. These waves can be decomposed into simpler sinusoidal components using Fourier analysis.

- **Beating waves**: A phenomenon that occurs when two sound waves of slightly different frequencies interfere, creating a periodic variation in amplitude known as beats. [Glicol: Basic Connection](https://glicol.org/tour#basicconnection)

- **Time vs frequency domain**: Two ways of representing sound. The time domain shows how a signal changes over time, while the frequency domain represents the signal's frequency components, often visualized using the Fourier transform.

- **Sound pressure level (SPL)**: A measure of the pressure variation caused by a sound wave, expressed in decibels (dB). SPL decreases with distance according to the inverse-square law and follows the 3dB rule, where a 3dB increase doubles the perceived loudness.

- **Speed of sound**: The rate at which sound waves travel through a medium. It depends on the medium's properties, such as density and elasticity:
    - Air: 343 m/s
    - Water: 1481 m/s
    - Iron: 5120 m/s

### Digital Sound

- **Digitization**: The process of converting analog sound to digital using ADC (Analog-to-Digital Converter) and back using DAC (Digital-to-Analog Converter).
- **Sampling rate**: Defined by the sampling theorem and Nyquist frequency.
- **Bit rate**: The amount of data processed per second.
- **Containers**: Formats for storing digital audio.
- **Compression**: Reducing file size while maintaining quality.
- **Window size**: A parameter in digital signal processing.

## Electro-Acoustics

Electro-Acoustics" refers to the field of study and technology that deals with the conversion between electrical signals and sound waves. It encompasses the design, analysis, and application of devices that perform this conversion, such as microphones, loudspeakers, headphones, and hearing aids.

This field combines principles from acoustics (the science of sound) and electronics to create systems that enable sound recording, reproduction, and transmission.


### Microphones
Microphones are devices that convert sound waves into electrical signals. They are categorized based on their design and working principles:

Dynamic Microphones:

Use a diaphragm attached to a coil of wire, placed within a magnetic field.
Sound waves move the diaphragm, generating an electrical signal.
Durable and good for high sound pressure levels (e.g., live performances).
Condenser Microphones:

Use a diaphragm placed close to a charged backplate, forming a capacitor.
Sound waves change the distance between the diaphragm and backplate, altering the capacitance and creating an electrical signal.
Sensitive and ideal for studio recordings.
Contact Microphones:

Detect vibrations directly from solid surfaces rather than air.
Often use piezoelectric materials to convert vibrations into electrical signals.
Commonly used for instruments like violins or guitars.

### Speakers
Speakers are devices that convert electrical signals into sound waves. They are categorized based on their application and design:

Standard speakers used in audio systems.
Use a diaphragm (cone) driven by an electromagnet to produce sound.
Designed for a wide range of frequencies.
Headphones:

Miniature speakers worn on or in the ears.
Provide a personal listening experience by delivering sound directly to the listener.
Actuators:

Devices that create vibrations to produce sound in unconventional ways.
Often used in haptic feedback systems or to turn surfaces (like tables or windows) into speakers.

### Signal processing

Signal Processing: Often involves amplifying, filtering, or modifying the electrical signals to improve sound quality or adapt it for specific purposes.


### Instrument Acoustics

- **Frequency range**: The range of frequencies produced by instruments.
- **Organology**: The study of musical instruments and their classification.

### Room Acoustics

- **Room size and shape**: Influences sound behavior.
- **Modes**:
    - Standing waves: [Online Calculator](https://amcoustics.com/tools/amroc?l=300&w=500&h=300&r60=0.6)
    - Flutter echo
- **Materials**: Affect sound reflection, absorption, and diffusion.
- **Sound alterations**:
    - Reflection
    - Diffraction
    - Diffusion
    - Absorption
- **Reverberation**:
    - T60: The time it takes for sound to decay by 60 dB.





## Spatial audio


Here is a "note" directive:

```{Soundwalk}
We will do a soundwalk together
```



## Citations

the following syntax: `` {cite}`holdgraf_evidence_2014` `` 

Here is the bibliography


```{bibliography}
```
