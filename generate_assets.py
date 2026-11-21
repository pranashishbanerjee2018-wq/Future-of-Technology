"""
generate_assets.py - Procedural Scientific Audio Synthesizer
Synthesizes professional original soundscapes and sound effects using pure Python (wave & math / numpy):
  1. lab_ambience.wav - Subtle futuristic laboratory drone & harmonics (looped)
  2. cinematic_music.wav - Soft, inspiring cinematic scientific progression (165s length)
  3. scene_transition.wav - Smooth sci-fi whoosh and harmonic sweep
  4. ui_click.wav - Clean futuristic tactile interface click
  5. calc_complete.wav - Dual-tone harmonic crystal chime for numerical calculation
"""

import os
import wave
import struct
import math
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, 'static', 'audio')
os.makedirs(AUDIO_DIR, exist_ok=True)

SAMPLE_RATE = 44100

def write_wav(filename, samples, sample_rate=SAMPLE_RATE):
    """Write float array in [-1.0, 1.0] to 16-bit PCM WAV."""
    path = os.path.join(AUDIO_DIR, filename)
    # Clip and convert to 16-bit integers
    samples = np.clip(samples, -0.98, 0.98)
    int_samples = (samples * 32767).astype(np.int16)
    
    with wave.open(path, 'w') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(int_samples.tobytes())
    print(f"[AUDIO] Generated: {path} ({len(samples)/sample_rate:.1f}s)")

def generate_lab_ambience(duration=20.0):
    """Generate subtle futuristic research lab drone with low harmonic hum."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    # 55Hz (A1) fundamental + 110Hz subharmonic + 165Hz subtle third harmonic
    hum = (0.28 * np.sin(2 * np.pi * 55.0 * t) +
           0.18 * np.sin(2 * np.pi * 110.0 * t) +
           0.08 * np.sin(2 * np.pi * 165.0 * t + 0.5) +
           0.04 * np.sin(2 * np.pi * 220.0 * t + 1.2))
    
    # Slow LFO filter modulation (0.15 Hz and 0.08 Hz)
    lfo1 = 0.5 + 0.5 * np.sin(2 * np.pi * 0.12 * t)
    lfo2 = 0.5 + 0.5 * np.sin(2 * np.pi * 0.07 * t + 1.0)
    
    # Ultra-subtle electronic airflow / white noise filtered
    noise = np.random.normal(0, 0.02, len(t))
    
    # Subtle server pulse every 4 seconds
    pulse = 0.03 * np.sin(2 * np.pi * 880 * t) * np.exp(-((t % 4.0) / 0.15)**2)
    
    audio = (hum * (0.8 + 0.2 * lfo1) + noise * lfo2 + pulse) * 0.25
    
    # Loop-friendly window fade in / out
    fade_len = int(SAMPLE_RATE * 1.5)
    fade = np.ones(len(audio))
    fade[:fade_len] = np.linspace(0, 1, fade_len)
    fade[-fade_len:] = np.linspace(1, 0, fade_len)
    audio = audio * fade
    
    write_wav('lab_ambience.wav', audio)

def generate_cinematic_music(duration=170.0):
    """
    Generate 170-second soft, inspiring, contemplative cinematic score for scientific presentation.
    Harmonic progression: C minor -> Ab major -> Eb major -> Bb major (Aeolian mode)
    Soft sine/warm triangle pads and gentle bell-like arpeggios that never overpower speech.
    """
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    
    # Chords (frequencies in Hz)
    # C minor: C3 (130.81), Eb3 (155.56), G3 (196.00), Bb3 (233.08)
    # Ab major: Ab2 (103.83), C3 (130.81), Eb3 (155.56), G3 (196.00)
    # Eb major: Eb2 (77.78), G2 (98.00), Bb2 (116.54), Eb3 (155.56)
    # Bb major: Bb2 (116.54), D3 (146.83), F3 (174.61), Bb3 (233.08)
    chords = [
        [130.81, 155.56, 196.00, 233.08],  # Cm7
        [103.83, 130.81, 155.56, 196.00],  # Abmaj7
        [77.78, 116.54, 155.56, 196.00],   # Ebmaj7
        [116.54, 146.83, 174.61, 233.08]   # Bb
    ]
    chord_len = 10.0  # 10 seconds per chord -> 40 seconds per cycle, repeats ~4 times
    
    for i in range(int(duration / chord_len) + 1):
        c_idx = i % len(chords)
        chord_freqs = chords[c_idx]
        start_idx = int(i * chord_len * SAMPLE_RATE)
        end_idx = min(len(t), int((i + 1) * chord_len * SAMPLE_RATE))
        if start_idx >= len(t):
            break
        
        seg_len = end_idx - start_idx
        seg_t = np.linspace(0, seg_len / SAMPLE_RATE, seg_len, endpoint=False)
        
        # Soft envelope (smooth rise and fall)
        env = np.sin(np.pi * (seg_t / (seg_len / SAMPLE_RATE))) ** 1.5
        
        chord_wave = np.zeros(seg_len)
        for freq in chord_freqs:
            # Fundamental + soft second harmonic for warmth
            w = 0.6 * np.sin(2 * np.pi * freq * seg_t) + 0.25 * np.sin(4 * np.pi * freq * seg_t + 0.4)
            chord_wave += w
        
        # Gentle high arpeggio note
        arp_freq = chord_freqs[(i % len(chord_freqs))] * 2.0
        arp_env = np.exp(-((seg_t % 2.5) / 1.2)) * 0.15
        arp_wave = np.sin(2 * np.pi * arp_freq * seg_t) * arp_env
        
        audio[start_idx:end_idx] += (chord_wave * 0.18 + arp_wave) * env
    
    # Master volume (keep soft to never compete with voice dialogue: ~ -20 dB)
    audio = audio * 0.14
    
    # Overall fade in / out
    fade_in_samples = int(SAMPLE_RATE * 3.0)
    fade_out_samples = int(SAMPLE_RATE * 5.0)
    audio[:fade_in_samples] *= np.linspace(0, 1, fade_in_samples)
    audio[-fade_out_samples:] *= np.linspace(1, 0, fade_out_samples)
    
    write_wav('cinematic_music.wav', audio)

def generate_scene_transition():
    """Gentle sci-fi scene transition swoosh with rising frequency and soft bell."""
    dur = 1.0
    t = np.linspace(0, dur, int(SAMPLE_RATE * dur), endpoint=False)
    # Frequency glide from 200 Hz to 900 Hz
    freq = 220.0 + 680.0 * (t / dur)**2
    phase = 2 * np.pi * np.cumsum(freq) / SAMPLE_RATE
    swoosh = np.sin(phase) * (np.sin(np.pi * t / dur) ** 2)
    # Shimmering high harmonic
    shimmer = 0.3 * np.sin(2 * np.pi * 1760 * t) * np.exp(-t * 4.0)
    audio = (swoosh * 0.25 + shimmer) * 0.35
    write_wav('scene_transition.wav', audio)

def generate_ui_click():
    """Clean high-tech UI tactile feedback chirp."""
    dur = 0.06
    t = np.linspace(0, dur, int(SAMPLE_RATE * dur), endpoint=False)
    freq = 1400.0 - 600.0 * (t / dur)
    phase = 2 * np.pi * np.cumsum(freq) / SAMPLE_RATE
    audio = np.sin(phase) * np.exp(-t / 0.015) * 0.25
    write_wav('ui_click.wav', audio)

def generate_calc_complete():
    """Dual-tone futuristic harmonic crystal chime indicating computation completion."""
    dur = 1.4
    t = np.linspace(0, dur, int(SAMPLE_RATE * dur), endpoint=False)
    # Frequencies: A5 (880 Hz) and E6 (1318.5 Hz) + soft high harmonic
    tone1 = np.sin(2 * np.pi * 880.0 * t) * np.exp(-t / 0.35)
    tone2 = 0.7 * np.sin(2 * np.pi * 1318.5 * (t - 0.08) * (t > 0.08)) * np.exp(-(t - 0.08) / 0.45) * (t > 0.08)
    tone3 = 0.35 * np.sin(2 * np.pi * 2637.0 * (t - 0.16) * (t > 0.16)) * np.exp(-(t - 0.16) / 0.25) * (t > 0.16)
    audio = (tone1 + tone2 + tone3) * 0.3
    write_wav('calc_complete.wav', audio)

def main():
    print("[AUDIO] Generating scientific soundscape assets...")
    generate_lab_ambience()
    generate_cinematic_music()
    generate_scene_transition()
    generate_ui_click()
    generate_calc_complete()
    print("[AUDIO] All sound assets successfully created!")

if __name__ == '__main__':
    main()
