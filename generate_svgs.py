"""
generate_svgs.py - High-Quality 2D Vector Graphic Generator
Generates clean, scalable SVG assets for characters, laboratory environment,
and specialized scientific conceptual diagrams.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, 'static', 'images')
os.makedirs(IMAGES_DIR, exist_ok=True)

def write_svg(filename, content):
    path = os.path.join(IMAGES_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"[SVG] Generated: {path}")

def generate_lab_background():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811" />
      <stop offset="40%" stop-color="#0a101f" />
      <stop offset="100%" stop-color="#04060c" />
    </linearGradient>
    <linearGradient id="wallPanel" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141c2e" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#0a0f1d" stop-opacity="0.9" />
    </linearGradient>
    <linearGradient id="floorGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080c18" />
      <stop offset="20%" stop-color="#0e172a" />
      <stop offset="100%" stop-color="#04060a" />
    </linearGradient>
    <linearGradient id="holoCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.1" />
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.1" />
    </linearGradient>
    <radialGradient id="chamberGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6" />
      <stop offset="40%" stop-color="#818cf8" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#050811" stop-opacity="0" />
    </radialGradient>
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8" stroke-opacity="0.4" />
    </pattern>
  </defs>

  <!-- Deep Lab Space Background -->
  <rect width="1920" height="1080" fill="url(#bgGrad)" />

  <!-- Laboratory Ceiling Architecture -->
  <polygon points="0,0 1920,0 1780,140 140,140" fill="#0d1424" />
  <line x1="200" y1="140" x2="1720" y2="140" stroke="#38bdf8" stroke-width="2" opacity="0.4" filter="url(#neonGlow)" />
  <line x1="400" y1="0" x2="350" y2="140" stroke="#1e293b" stroke-width="2" />
  <line x1="960" y1="0" x2="960" y2="140" stroke="#1e293b" stroke-width="2" />
  <line x1="1520" y1="0" x2="1570" y2="140" stroke="#1e293b" stroke-width="2" />

  <!-- Back Wall Structural Panels -->
  <rect x="80" y="140" width="1760" height="600" fill="url(#gridPattern)" />
  <rect x="120" y="170" width="420" height="540" rx="8" fill="url(#wallPanel)" stroke="#1e293b" stroke-width="1.5" />
  <rect x="1380" y="170" width="420" height="540" rx="8" fill="url(#wallPanel)" stroke="#1e293b" stroke-width="1.5" />

  <!-- Central Scientific Visualization Aperture -->
  <circle cx="960" cy="420" r="320" fill="#040711" stroke="#1e293b" stroke-width="2" />
  <circle cx="960" cy="420" r="300" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="8 6" opacity="0.6" />
  <circle cx="960" cy="420" r="260" fill="none" stroke="#818cf8" stroke-width="1" stroke-dasharray="14 10" opacity="0.5" />
  <circle cx="960" cy="420" r="200" fill="url(#chamberGlow)" />

  <!-- Quantum / Cosmic Holographic Rings in Background -->
  <ellipse cx="960" cy="420" rx="270" ry="80" fill="none" stroke="#38bdf8" stroke-width="1.2" opacity="0.5" transform="rotate(-25 960 420)" />
  <ellipse cx="960" cy="420" rx="270" ry="80" fill="none" stroke="#a855f7" stroke-width="1.2" opacity="0.4" transform="rotate(35 960 420)" />

  <!-- Background Data Readouts on Lateral Columns -->
  <g opacity="0.65" font-family="'Courier New', monospace" font-size="12" fill="#38bdf8">
    <text x="145" y="210">SYSTEM: QUANTUM METRIC ANALYZER</text>
    <text x="145" y="235">l_P = sqrt(hbar*G/c^3) = 1.616e-35 m</text>
    <text x="145" y="255">t_P = sqrt(hbar*G/c^5) = 5.391e-44 s</text>
    <text x="145" y="275">E_P = 1.956e+09 J [1.22e+19 GeV]</text>
    <text x="145" y="305">METRIC TENSOR EVALUATION: ONLINE</text>
    <path d="M 145 320 L 510 320" stroke="#38bdf8" stroke-width="1" opacity="0.5" />
    <path d="M 145 340 L 220 340 L 240 370 L 320 370 L 340 340 L 510 340" fill="none" stroke="#38bdf8" stroke-width="1" />
  </g>

  <g opacity="0.65" font-family="'Courier New', monospace" font-size="12" fill="#34d399">
    <text x="1405" y="210">COMPUTATION NODE: MATLAB R2026</text>
    <text x="1405" y="235">SCRIPT: QuantumGravity.m</text>
    <text x="1405" y="255">G_uv = (8*pi*G / c^4) * T_uv</text>
    <text x="1405" y="275">SPIN FOAM AREA SPECTRA: DISCRETE</text>
    <text x="1405" y="305">SIMULATION RESOLUTION: 300 DPI</text>
    <path d="M 1405 320 L 1770 320" stroke="#34d399" stroke-width="1" opacity="0.5" />
    <circle cx="1430" cy="360" r="15" fill="none" stroke="#34d399" stroke-width="1.5" />
    <circle cx="1480" cy="360" r="25" fill="none" stroke="#34d399" stroke-width="1.5" />
    <circle cx="1550" cy="360" r="10" fill="none" stroke="#34d399" stroke-width="1.5" />
  </g>

  <!-- Laboratory Floor with Reflective Horizon -->
  <polygon points="0,740 1920,740 1920,1080 0,1080" fill="url(#floorGrad)" />
  <line x1="0" y1="740" x2="1920" y2="740" stroke="#38bdf8" stroke-width="2.5" opacity="0.7" filter="url(#neonGlow)" />

  <!-- Floor Perspective Grid Lines -->
  <g stroke="#1e293b" stroke-width="1" opacity="0.45">
    <line x1="960" y1="740" x2="960" y2="1080" />
    <line x1="960" y1="740" x2="600" y2="1080" />
    <line x1="960" y1="740" x2="200" y2="1080" />
    <line x1="960" y1="740" x2="-200" y2="1080" />
    <line x1="960" y1="740" x2="1320" y2="1080" />
    <line x1="960" y1="740" x2="1720" y2="1080" />
    <line x1="960" y1="740" x2="2120" y2="1080" />
    <line x1="0" y1="800" x2="1920" y2="800" />
    <line x1="0" y1="880" x2="1920" y2="880" />
    <line x1="0" y1="980" x2="1920" y2="980" />
  </g>

  <!-- Floor Reflection Glow from Central Window -->
  <ellipse cx="960" cy="780" rx="400" ry="30" fill="url(#holoCyan)" />
</svg>'''
    write_svg('lab_background.svg', svg)

def generate_character_nathaniel():
    """Dr. Nathaniel Brooks: Senior Theoretical Physicist (~35 yrs, dark navy suit, neat dark hair)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 900" width="100%" height="100%" id="char-nathaniel-svg">
  <defs>
    <linearGradient id="suitGradNathaniel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="50%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#090d16" />
    </linearGradient>
    <linearGradient id="skinGradNathaniel" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fbd3b6" />
      <stop offset="100%" stop-color="#e2af89" />
    </linearGradient>
    <linearGradient id="hairGradNathaniel" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2d2a29" />
      <stop offset="100%" stop-color="#171514" />
    </linearGradient>
  </defs>

  <!-- ROOT CHARACTER GROUP -->
  <g id="nathaniel-root">

    <!-- SHADOW ON FLOOR -->
    <ellipse cx="250" cy="870" rx="140" ry="24" fill="#000000" opacity="0.45" />

    <!-- LEGS & LOWER BODY -->
    <g id="nathaniel-lower-body">
      <path d="M 180 580 L 190 850 L 225 850 L 235 580 Z" fill="#0f172a" />
      <path d="M 265 580 L 275 850 L 310 850 L 320 580 Z" fill="#0d1424" />
      <!-- Shoes -->
      <path d="M 180 845 L 230 845 L 235 865 L 175 865 Z" fill="#05070a" />
      <path d="M 270 845 L 320 845 L 325 865 L 265 865 Z" fill="#05070a" />
    </g>

    <!-- TORSO & SUIT -->
    <g id="nathaniel-torso">
      <!-- White crisp collared shirt -->
      <polygon points="220,290 280,290 265,390 235,390" fill="#f8fafc" />
      <!-- Silk Dark Cyan / Navy Tie -->
      <polygon points="245,300 255,300 258,410 250,430 242,410" fill="#0284c7" />
      <polygon points="245,295 255,295 258,310 242,310" fill="#0369a1" />

      <!-- Suit Jacket -->
      <path d="M 160 300 Q 140 450 150 600 L 350 600 Q 360 450 340 300 Q 250 280 160 300 Z" fill="url(#suitGradNathaniel)" stroke="#334155" stroke-width="1.2" />
      <!-- Suit Lapels -->
      <polygon points="175,300 230,410 210,410 160,300" fill="#243048" />
      <polygon points="325,300 270,410 290,410 340,300" fill="#243048" />

      <!-- ID Badge -->
      <rect x="175" y="380" width="32" height="48" rx="3" fill="#ffffff" opacity="0.9" stroke="#94a3b8" stroke-width="1" />
      <rect x="180" y="385" width="22" height="15" fill="#38bdf8" />
      <line x1="180" y1="406" x2="202" y2="406" stroke="#0f172a" stroke-width="2" />
      <line x1="180" y1="412" x2="198" y2="412" stroke="#64748b" stroke-width="1.5" />
      <line x1="180" y1="418" x2="194" y2="418" stroke="#64748b" stroke-width="1.5" />
    </g>

    <!-- ARMS & GESTURES -->
    <g id="nathaniel-arms">
      <!-- Left arm (relaxed professional / slight gesture) -->
      <path id="nathaniel-left-arm" d="M 160 310 Q 130 430 145 540 Q 155 570 170 575" fill="none" stroke="#0f172a" stroke-width="44" stroke-linecap="round" />
      <circle cx="172" cy="576" r="16" fill="url(#skinGradNathaniel)" />

      <!-- Right arm (expressive speaker gesture / pointing) -->
      <g id="nathaniel-right-arm-group" class="arm-gesture">
        <path id="nathaniel-right-arm" d="M 340 310 Q 375 420 360 520 Q 350 550 335 560" fill="none" stroke="#0f172a" stroke-width="44" stroke-linecap="round" />
        <!-- Hand / Palm -->
        <g id="nathaniel-right-hand" transform="translate(330, 560)">
          <path d="M 0 0 C 10 -15, 25 -10, 20 10 C 15 25, -5 20, 0 0 Z" fill="url(#skinGradNathaniel)" />
          <path d="M 12 -5 C 22 -15, 30 -5, 20 12" fill="none" stroke="url(#skinGradNathaniel)" stroke-width="6" stroke-linecap="round" />
        </g>
      </g>
    </g>

    <!-- NECK & HEAD GROUP (can tilt/nod) -->
    <g id="nathaniel-head-group" class="head-container">
      <!-- Neck -->
      <rect x="232" y="240" width="36" height="50" rx="6" fill="url(#skinGradNathaniel)" />

      <!-- Head Base -->
      <path d="M 200 160 C 200 80, 300 80, 300 160 C 300 240, 280 265, 250 265 C 220 265, 200 240, 200 160 Z" fill="url(#skinGradNathaniel)" />

      <!-- Ears -->
      <ellipse cx="196" cy="170" rx="8" ry="16" fill="url(#skinGradNathaniel)" />
      <ellipse cx="304" cy="170" rx="8" ry="16" fill="url(#skinGradNathaniel)" />

      <!-- Neatly styled dark hair (35yo professional) -->
      <path d="M 194 150 C 190 90, 230 65, 250 65 C 275 65, 310 85, 306 150 C 298 120, 280 110, 250 110 C 220 110, 202 125, 194 150 Z" fill="url(#hairGradNathaniel)" />
      <path d="M 194 135 C 190 165, 205 165, 205 145 Z" fill="url(#hairGradNathaniel)" />
      <path d="M 306 135 C 310 165, 295 165, 295 145 Z" fill="url(#hairGradNathaniel)" />

      <!-- Eyebrows (Calm, analytical) -->
      <g id="nathaniel-eyebrows" class="eyebrows">
        <path d="M 215 145 Q 230 140 242 144" fill="none" stroke="#1f1e1d" stroke-width="4.5" stroke-linecap="round" />
        <path d="M 258 144 Q 270 140 285 145" fill="none" stroke="#1f1e1d" stroke-width="4.5" stroke-linecap="round" />
      </g>

      <!-- Eyes (Natural blinking system) -->
      <g id="nathaniel-eyes" class="eyes-container">
        <!-- Left eye -->
        <g id="nathaniel-eye-left">
          <ellipse cx="230" cy="160" rx="9" ry="6" fill="#ffffff" />
          <circle cx="231" cy="160" r="4.2" fill="#3b2b1a" />
          <circle cx="232" cy="158" r="1.3" fill="#ffffff" />
          <path class="eye-lid" d="M 221 160 Q 230 152 239 160" fill="none" stroke="#2d2a29" stroke-width="2" />
        </g>
        <!-- Right eye -->
        <g id="nathaniel-eye-right">
          <ellipse cx="270" cy="160" rx="9" ry="6" fill="#ffffff" />
          <circle cx="269" cy="160" r="4.2" fill="#3b2b1a" />
          <circle cx="270" cy="158" r="1.3" fill="#ffffff" />
          <path class="eye-lid" d="M 261 160 Q 270 152 279 160" fill="none" stroke="#2d2a29" stroke-width="2" />
        </g>
      </g>

      <!-- Nose -->
      <path d="M 250 158 L 246 185 L 254 186" fill="none" stroke="#c48a60" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />

      <!-- 5 MOUTH VISEMES (REST, OPEN, ROUND, WIDE, MID) -->
      <g id="nathaniel-mouth" class="mouth-container">
        <!-- 1. REST (Default closed lips) -->
        <g id="nathaniel-viseme-rest" class="viseme" style="display: inline;">
          <path d="M 238 214 Q 250 216 262 214" fill="none" stroke="#994d3a" stroke-width="3.5" stroke-linecap="round" />
          <path d="M 242 216 Q 250 220 258 216" fill="none" stroke="#b0624e" stroke-width="2" />
        </g>
        <!-- 2. OPEN ('ah', 'aa') -->
        <g id="nathaniel-viseme-open" class="viseme" style="display: none;">
          <ellipse cx="250" cy="216" rx="13" ry="10" fill="#4a1515" stroke="#994d3a" stroke-width="2" />
          <path d="M 240 212 Q 250 214 260 212" fill="#ffffff" />
          <path d="M 243 222 Q 250 218 257 222" fill="#e06666" />
        </g>
        <!-- 3. ROUND ('oh', 'oo', 'w') -->
        <g id="nathaniel-viseme-round" class="viseme" style="display: none;">
          <ellipse cx="250" cy="216" rx="9" ry="11" fill="#4a1515" stroke="#994d3a" stroke-width="2.5" />
          <ellipse cx="250" cy="217" rx="6" ry="7" fill="#2d0b0b" />
        </g>
        <!-- 4. WIDE ('ee', 'ih', 'ae') -->
        <g id="nathaniel-viseme-wide" class="viseme" style="display: none;">
          <path d="M 235 214 Q 250 211 265 214 Q 250 222 235 214 Z" fill="#4a1515" stroke="#994d3a" stroke-width="2" />
          <rect x="240" y="213" width="20" height="4" rx="1" fill="#ffffff" />
        </g>
        <!-- 5. MID ('m', 'b', 'p', 'th', 's') -->
        <g id="nathaniel-viseme-mid" class="viseme" style="display: none;">
          <path d="M 236 215 Q 250 218 264 215" fill="none" stroke="#883c2a" stroke-width="4.5" stroke-linecap="round" />
        </g>
      </g>

    </g> <!-- end head group -->

  </g>
</svg>'''
    write_svg('nathaniel_character.svg', svg); write_svg('adrian_character.svg', svg)

def generate_character_julian():
    """Dr. Julian Hayes: Quantum Physics & Computational Researcher (~28 yrs, blue smart-casual shirt, energetic)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 900" width="100%" height="100%" id="char-julian-svg">
  <defs>
    <linearGradient id="shirtGradJulian" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="60%" stop-color="#0369a1" />
      <stop offset="100%" stop-color="#075985" />
    </linearGradient>
    <linearGradient id="skinGradJulian" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fed7aa" />
      <stop offset="100%" stop-color="#fbb686" />
    </linearGradient>
    <linearGradient id="hairGradJulian" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#382d26" />
      <stop offset="100%" stop-color="#1e1814" />
    </linearGradient>
  </defs>

  <!-- ROOT CHARACTER GROUP -->
  <g id="julian-root">

    <!-- SHADOW ON FLOOR -->
    <ellipse cx="250" cy="870" rx="140" ry="24" fill="#000000" opacity="0.45" />

    <!-- LEGS & LOWER BODY (Dark charcoal smart-casual trousers) -->
    <g id="julian-lower-body">
      <path d="M 180 570 L 192 850 L 228 850 L 238 570 Z" fill="#1e293b" />
      <path d="M 262 570 L 272 850 L 308 850 L 320 570 Z" fill="#182234" />
      <!-- Smart Leather Shoes -->
      <path d="M 182 845 L 232 845 L 238 865 L 176 865 Z" fill="#2d2218" />
      <path d="M 268 845 L 318 845 L 324 865 L 262 865 Z" fill="#2d2218" />
    </g>

    <!-- TORSO & SMART-CASUAL SHIRT -->
    <g id="julian-torso">
      <!-- Dark belt -->
      <rect x="180" y="555" width="140" height="18" rx="2" fill="#111827" />
      <rect x="238" y="553" width="24" height="22" rx="2" fill="#94a3b8" />

      <!-- Blue Smart-Casual Shirt -->
      <path d="M 165 300 Q 145 440 160 560 L 340 560 Q 355 440 335 300 Q 250 285 165 300 Z" fill="url(#shirtGradJulian)" stroke="#0284c7" stroke-width="1.2" />
      <!-- Open Collar -->
      <polygon points="215,295 240,360 250,330 230,295" fill="#38bdf8" />
      <polygon points="285,295 260,360 250,330 270,295" fill="#38bdf8" />
      <polygon points="240,330 260,330 250,365" fill="#fbb686" />

      <!-- Center Button Placket -->
      <line x1="250" y1="360" x2="250" y2="555" stroke="#075985" stroke-width="2.5" />
      <circle cx="250" cy="385" r="3" fill="#e0f2fe" />
      <circle cx="250" cy="430" r="3" fill="#e0f2fe" />
      <circle cx="250" cy="475" r="3" fill="#e0f2fe" />
      <circle cx="250" cy="520" r="3" fill="#e0f2fe" />

      <!-- Lab Researcher Badge -->
      <rect x="285" y="380" width="30" height="45" rx="3" fill="#ffffff" opacity="0.9" stroke="#94a3b8" stroke-width="1" />
      <rect x="290" y="385" width="20" height="14" fill="#0284c7" />
      <line x1="290" y1="405" x2="310" y2="405" stroke="#0f172a" stroke-width="1.8" />
      <line x1="290" y1="411" x2="305" y2="411" stroke="#64748b" stroke-width="1.4" />
    </g>

    <!-- ARMS & GESTURES (Enthusiastic, computational researcher) -->
    <g id="julian-arms">
      <!-- Left arm (Interactive gesture, holding tablet / pointing) -->
      <g id="julian-left-arm-group" class="arm-gesture">
        <path id="julian-left-arm" d="M 165 310 Q 125 410 145 490 Q 155 520 180 515" fill="none" stroke="#0284c7" stroke-width="40" stroke-linecap="round" />
        <!-- Hand with futuristic computing slate -->
        <g id="julian-left-hand" transform="translate(170, 500)">
          <rect x="-10" y="-15" width="45" height="30" rx="3" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" transform="rotate(-15)" />
          <circle cx="5" cy="0" r="14" fill="url(#skinGradJulian)" />
        </g>
      </g>

      <!-- Right arm (Expressive explanatory gestures) -->
      <g id="julian-right-arm-group" class="arm-gesture">
        <path id="julian-right-arm" d="M 335 310 Q 365 410 345 500 Q 330 535 310 545" fill="none" stroke="#0284c7" stroke-width="40" stroke-linecap="round" />
        <g id="julian-right-hand" transform="translate(305, 545)">
          <circle cx="0" cy="0" r="14" fill="url(#skinGradJulian)" />
          <path d="M 5 -8 C 15 -18, 22 -6, 12 5" fill="none" stroke="url(#skinGradJulian)" stroke-width="5" stroke-linecap="round" />
        </g>
      </g>
    </g>

    <!-- NECK & HEAD GROUP (Curious, youthful 28yo researcher) -->
    <g id="julian-head-group" class="head-container">
      <!-- Neck -->
      <rect x="233" y="240" width="34" height="50" rx="5" fill="url(#skinGradJulian)" />

      <!-- Head Base -->
      <path d="M 205 165 C 205 90, 295 90, 295 165 C 295 240, 275 260, 250 260 C 225 260, 205 240, 205 165 Z" fill="url(#skinGradJulian)" />

      <!-- Ears -->
      <ellipse cx="201" cy="172" rx="8" ry="15" fill="url(#skinGradJulian)" />
      <ellipse cx="299" cy="172" rx="8" ry="15" fill="url(#skinGradJulian)" />

      <!-- Textured modern short dark hair (textured cut) -->
      <path d="M 198 150 C 195 85, 235 60, 255 60 C 280 60, 305 80, 302 150 C 292 115, 270 105, 250 105 C 225 105, 208 120, 198 150 Z" fill="url(#hairGradJulian)" />
      <!-- Textured hair strands -->
      <path d="M 220 70 Q 235 55 245 68" fill="none" stroke="#4a3b32" stroke-width="4" stroke-linecap="round" />
      <path d="M 245 62 Q 260 50 270 65" fill="none" stroke="#4a3b32" stroke-width="4" stroke-linecap="round" />
      <path d="M 198 135 C 194 160, 208 160, 208 140 Z" fill="url(#hairGradJulian)" />
      <path d="M 302 135 C 306 160, 292 160, 292 140 Z" fill="url(#hairGradJulian)" />

      <!-- Eyebrows (Curious, lively, slightly raised) -->
      <g id="julian-eyebrows" class="eyebrows">
        <path d="M 218 142 Q 232 136 244 141" fill="none" stroke="#261e18" stroke-width="4.5" stroke-linecap="round" />
        <path d="M 256 141 Q 268 136 282 142" fill="none" stroke="#261e18" stroke-width="4.5" stroke-linecap="round" />
      </g>

      <!-- Eyes (Blinking system, bright, expressive) -->
      <g id="julian-eyes" class="eyes-container">
        <!-- Left eye -->
        <g id="julian-eye-left">
          <ellipse cx="232" cy="158" rx="9" ry="6.5" fill="#ffffff" />
          <circle cx="233" cy="158" r="4.3" fill="#2d3748" />
          <circle cx="234" cy="156" r="1.5" fill="#ffffff" />
          <path class="eye-lid" d="M 223 158 Q 232 150 241 158" fill="none" stroke="#261e18" stroke-width="2" />
        </g>
        <!-- Right eye -->
        <g id="julian-eye-right">
          <ellipse cx="268" cy="158" rx="9" ry="6.5" fill="#ffffff" />
          <circle cx="267" cy="158" r="4.3" fill="#2d3748" />
          <circle cx="268" cy="156" r="1.5" fill="#ffffff" />
          <path class="eye-lid" d="M 259 158 Q 268 150 277 158" fill="none" stroke="#261e18" stroke-width="2" />
        </g>
      </g>

      <!-- Nose -->
      <path d="M 250 156 L 247 182 L 253 183" fill="none" stroke="#c48a60" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />

      <!-- 5 MOUTH VISEMES (REST, OPEN, ROUND, WIDE, MID) -->
      <g id="julian-mouth" class="mouth-container">
        <!-- 1. REST (Default closed lips) -->
        <g id="julian-viseme-rest" class="viseme" style="display: inline;">
          <path d="M 239 212 Q 250 215 261 212" fill="none" stroke="#a35440" stroke-width="3.5" stroke-linecap="round" />
          <path d="M 242 214 Q 250 218 258 214" fill="none" stroke="#ba6853" stroke-width="2" />
        </g>
        <!-- 2. OPEN ('ah', 'aa') -->
        <g id="julian-viseme-open" class="viseme" style="display: none;">
          <ellipse cx="250" cy="214" rx="13" ry="10.5" fill="#4a1515" stroke="#a35440" stroke-width="2" />
          <path d="M 240 210 Q 250 212 260 210" fill="#ffffff" />
          <path d="M 243 220 Q 250 217 257 220" fill="#e06666" />
        </g>
        <!-- 3. ROUND ('oh', 'oo', 'w') -->
        <g id="julian-viseme-round" class="viseme" style="display: none;">
          <ellipse cx="250" cy="214" rx="9.5" ry="11" fill="#4a1515" stroke="#a35440" stroke-width="2.5" />
          <ellipse cx="250" cy="215" rx="6.5" ry="7" fill="#2d0b0b" />
        </g>
        <!-- 4. WIDE ('ee', 'ih', 'ae') -->
        <g id="julian-viseme-wide" class="viseme" style="display: none;">
          <path d="M 236 212 Q 250 209 264 212 Q 250 220 236 212 Z" fill="#4a1515" stroke="#a35440" stroke-width="2" />
          <rect x="241" y="211" width="18" height="4" rx="1" fill="#ffffff" />
        </g>
        <!-- 5. MID ('m', 'b', 'p', 'th', 's') -->
        <g id="julian-viseme-mid" class="viseme" style="display: none;">
          <path d="M 237 213 Q 250 216 263 213" fill="none" stroke="#944330" stroke-width="4.5" stroke-linecap="round" />
        </g>
      </g>

    </g> <!-- end head group -->

  </g>
</svg>'''
    write_svg('julian_character.svg', svg); write_svg('ethan_character.svg', svg)

def generate_scientific_diagrams():
    """Vector diagrams for scenes 2, 3, 4, 6."""
    # 1. String Theory
    string_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="strGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#a855f7" />
      <stop offset="100%" stop-color="#f43f5e" />
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="12" fill="#0d1424" stroke="#1e293b" stroke-width="2" />
  <text x="300" y="38" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">SUPERSTRING THEORY: FUNDAMENTAL MODES</text>
  <text x="300" y="62" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="12">1D Vibrating Energy Filaments Replacing 0D Point Particles</text>
  <!-- Open String -->
  <path d="M 80 180 Q 140 100 200 180 T 320 180" fill="none" stroke="url(#strGrad)" stroke-width="4" stroke-linecap="round" />
  <circle cx="80" cy="180" r="6" fill="#38bdf8" />
  <circle cx="320" cy="180" r="6" fill="#f43f5e" />
  <text x="200" y="220" text-anchor="middle" fill="#38bdf8" font-size="12" font-family="monospace">Open String (Gauge Bosons)</text>
  <!-- Closed String (Graviton mode) -->
  <ellipse cx="450" cy="180" rx="70" ry="40" fill="none" stroke="url(#strGrad)" stroke-width="4" transform="rotate(-15 450 180)" />
  <path d="M 400 180 Q 450 140 500 180 Q 450 220 400 180" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 3" />
  <text x="450" y="250" text-anchor="middle" fill="#a855f7" font-size="12" font-family="monospace">Closed String (Spin-2 Graviton)</text>
  <!-- Formula -->
  <rect x="60" y="300" width="480" height="60" rx="6" fill="#111827" stroke="#334155" />
  <text x="300" y="335" text-anchor="middle" fill="#34d399" font-family="monospace" font-size="14">m^2 = (1 / alpha') * (N - 1)  [Vibrational Mass Spectrum]</text>
</svg>'''
    write_svg('string_theory.svg', string_svg)

    # 2. Loop Quantum Gravity Spin Network
    lqg_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <rect width="600" height="400" rx="12" fill="#0d1424" stroke="#1e293b" stroke-width="2" />
  <text x="300" y="38" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">LOOP QUANTUM GRAVITY: SPIN NETWORKS</text>
  <text x="300" y="62" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="12">Quantized Geometry — Spacetime as Discrete Area &amp; Volume Eigenvalues</text>
  <!-- Spin Network Nodes and Links -->
  <g stroke="#38bdf8" stroke-width="2.5">
    <line x1="160" y1="180" x2="260" y2="130" />
    <line x1="260" y1="130" x2="380" y2="150" />
    <line x1="380" y1="150" x2="440" y2="230" />
    <line x1="440" y1="230" x2="330" y2="260" />
    <line x1="330" y1="260" x2="160" y2="180" />
    <line x1="260" y1="130" x2="330" y2="260" stroke="#a855f7" stroke-width="2" stroke-dasharray="5 4" />
    <line x1="160" y1="180" x2="380" y2="150" stroke="#a855f7" stroke-width="2" stroke-dasharray="5 4" />
  </g>
  <!-- Nodes (Quanta of Volume) -->
  <circle cx="160" cy="180" r="14" fill="#38bdf8" />
  <circle cx="260" cy="130" r="16" fill="#818cf8" />
  <circle cx="380" cy="150" r="15" fill="#c084fc" />
  <circle cx="440" cy="230" r="13" fill="#34d399" />
  <circle cx="330" cy="260" r="17" fill="#fb923c" />
  <!-- Labels on links: j = 1/2, 1, 3/2 -->
  <text x="200" y="145" fill="#fde047" font-family="monospace" font-size="11">j = 1/2</text>
  <text x="325" y="135" fill="#fde047" font-family="monospace" font-size="11">j = 1</text>
  <text x="425" y="185" fill="#fde047" font-family="monospace" font-size="11">j = 1/2</text>
  <text x="390" y="260" fill="#fde047" font-family="monospace" font-size="11">j = 2</text>
  <text x="230" y="235" fill="#fde047" font-family="monospace" font-size="11">j = 3/2</text>
  <!-- Formula -->
  <rect x="60" y="300" width="480" height="60" rx="6" fill="#111827" stroke="#334155" />
  <text x="300" y="335" text-anchor="middle" fill="#38bdf8" font-family="monospace" font-size="13">A_j = 8*pi*gamma*l_P^2 * sqrt(j*(j+1))  [Discrete Area Spectrum]</text>
</svg>'''
    write_svg('spin_network.svg', lqg_svg)

    # 3. Black Hole Information & Holographic Principle
    holo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bhHolo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#000000" />
      <stop offset="70%" stop-color="#02040a" />
      <stop offset="90%" stop-color="#38bdf8" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#fbbf24" stop-opacity="0" />
    </radialGradient>
  </defs>
  <rect width="600" height="400" rx="12" fill="#0d1424" stroke="#1e293b" stroke-width="2" />
  <text x="300" y="38" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">THE HOLOGRAPHIC PRINCIPLE &amp; BLACK HOLES</text>
  <text x="300" y="62" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="12">Maximum Entropy Proportional to Boundary Horizon Area, Not Bulk Volume</text>
  <!-- Accretion Disk / Photon Ring -->
  <ellipse cx="300" cy="180" rx="190" ry="45" fill="none" stroke="#fbbf24" stroke-width="12" opacity="0.65" transform="rotate(-10 300 180)" />
  <ellipse cx="300" cy="180" rx="150" ry="32" fill="none" stroke="#f97316" stroke-width="8" opacity="0.85" transform="rotate(-10 300 180)" />
  <!-- Horizon Sphere -->
  <circle cx="300" cy="180" r="75" fill="url(#bhHolo)" />
  <circle cx="300" cy="180" r="75" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3" />
  <text x="300" y="185" text-anchor="middle" fill="#38bdf8" font-size="11" font-family="monospace">Event Horizon Area A</text>
  <!-- Formula -->
  <rect x="60" y="300" width="480" height="60" rx="6" fill="#111827" stroke="#334155" />
  <text x="300" y="335" text-anchor="middle" fill="#fbbf24" font-family="monospace" font-size="14">S_BH = (k_B * c^3 * A) / (4 * G * hbar) = (k_B * A) / (4 * l_P^2)</text>
</svg>'''
    write_svg('black_hole_horizon.svg', holo_svg)

    # 4. Quantum Sensor & Atom Interferometer (Scene 6)
    sensor_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <rect width="600" height="400" rx="12" fill="#0d1424" stroke="#1e293b" stroke-width="2" />
  <text x="300" y="38" text-anchor="middle" fill="#f8fafc" font-family="'Segoe UI', sans-serif" font-size="16" font-weight="bold">NEXT-GEN QUANTUM SENSORS: ATOM INTERFEROMETRY</text>
  <text x="300" y="62" text-anchor="middle" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="12">Ultra-Precise Gravimetry &amp; Tests of Gravitational Dephasing</text>
  <!-- Laser pulses -->
  <line x1="80" y1="120" x2="520" y2="120" stroke="#ef4444" stroke-width="3" opacity="0.8" />
  <line x1="80" y1="200" x2="520" y2="200" stroke="#ef4444" stroke-width="3" opacity="0.8" />
  <line x1="80" y1="280" x2="520" y2="280" stroke="#ef4444" stroke-width="3" opacity="0.8" />
  <text x="60" y="125" text-anchor="end" fill="#ef4444" font-size="11" font-family="monospace">pi/2 Laser</text>
  <text x="60" y="205" text-anchor="end" fill="#ef4444" font-size="11" font-family="monospace">pi Laser</text>
  <text x="60" y="285" text-anchor="end" fill="#ef4444" font-size="11" font-family="monospace">pi/2 Laser</text>
  <!-- Atomic wavepacket paths (Diamond interferometer) -->
  <path d="M 150 120 L 300 200 L 450 280" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6 4" />
  <path d="M 150 120 L 300 120 L 450 280" fill="none" stroke="#34d399" stroke-width="3" />
  <circle cx="150" cy="120" r="7" fill="#38bdf8" />
  <circle cx="300" cy="200" r="7" fill="#38bdf8" />
  <circle cx="300" cy="120" r="7" fill="#34d399" />
  <circle cx="450" cy="280" r="9" fill="#fbbf24" />
  <text x="470" y="285" fill="#fbbf24" font-family="monospace" font-size="12">Interference Fringe: Delta Phi = k_eff * g * T^2</text>
</svg>'''
    write_svg('quantum_sensor.svg', sensor_svg)

def main():
    print("[SVG] Generating presentation vector assets...")
    generate_lab_background()
    generate_character_nathaniel()
    generate_character_julian()
    generate_scientific_diagrams()
    print("[SVG] All vector assets successfully generated!")

if __name__ == '__main__':
    main()
