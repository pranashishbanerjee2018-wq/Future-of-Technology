/**
 * animation_controller.js - 2D Vector Character & Stage Animation Controller
 * Coordinates mouth visemes, natural eye blinking, head nods, gestures,
 * and dynamic camera/hologram transitions across all 7 scenes.
 * Characters: Dr. Nathaniel Brooks & Dr. Julian Hayes
 */

class AnimationController {
  constructor() {
    this.activeSpeaker = null;
    this.blinkTimers = { nathaniel: null, julian: null, adrian: null, ethan: null };
    this.nodTimers = { nathaniel: null, julian: null, adrian: null, ethan: null };
    this.visemes = ["rest", "open", "round", "wide", "mid"];

    this.initElements();
    this.startBlinkingLoops();
  }

  initElements() {
    this.wrapNathaniel = document.getElementById("char-nathaniel-wrapper") || document.getElementById("char-adrian-wrapper");
    this.wrapJulian = document.getElementById("char-julian-wrapper") || document.getElementById("char-ethan-wrapper");
    // Aliases
    this.wrapAdrian = this.wrapNathaniel;
    this.wrapEthan = this.wrapJulian;

    this.hologramFrame = document.getElementById("hologram-frame");
    this.holoMedia = document.getElementById("holo-media");
    this.holoTitle = document.getElementById("holo-title");
    this.holoCaption = document.getElementById("holo-caption");
    this.stageContainer = document.getElementById("main-stage");
  }

  /**
   * Set mouth viseme for a character: 'REST', 'OPEN', 'ROUND', 'WIDE', 'MID'
   */
  setViseme(speaker, visemeName) {
    const target = visemeName.toLowerCase();
    const isSenior = (speaker === "nathaniel" || speaker === "adrian");
    const prefixes = isSenior ? ["nathaniel-viseme-", "adrian-viseme-"] : ["julian-viseme-", "ethan-viseme-"];

    this.visemes.forEach((v) => {
      prefixes.forEach(prefix => {
        const el = document.getElementById(prefix + v);
        if (el) {
          el.style.display = (v === target) ? "inline" : "none";
        }
      });
    });
  }

  /**
   * Update speaking/listening state between the two researchers
   */
  setSpeakerState(speaker) {
    this.activeSpeaker = speaker;

    if (speaker === "nathaniel" || speaker === "adrian") {
      if (this.wrapNathaniel) {
        this.wrapNathaniel.classList.add("speaking");
        this.wrapNathaniel.classList.remove("listening");
      }
      if (this.wrapJulian) {
        this.wrapJulian.classList.remove("speaking");
        this.wrapJulian.classList.add("listening");
        this.triggerNod("julian");
      }
      this.setViseme("julian", "REST");
      this.triggerGesture("nathaniel", "explain");
    } else if (speaker === "julian" || speaker === "ethan") {
      if (this.wrapJulian) {
        this.wrapJulian.classList.add("speaking");
        this.wrapJulian.classList.remove("listening");
      }
      if (this.wrapNathaniel) {
        this.wrapNathaniel.classList.remove("speaking");
        this.wrapNathaniel.classList.add("listening");
        this.triggerNod("nathaniel");
      }
      this.setViseme("nathaniel", "REST");
      this.triggerGesture("julian", "explain");
    } else {
      // Neither speaking (pause or scene transition)
      if (this.wrapNathaniel) {
        this.wrapNathaniel.classList.remove("speaking");
        this.wrapNathaniel.classList.remove("listening");
      }
      if (this.wrapJulian) {
        this.wrapJulian.classList.remove("speaking");
        this.wrapJulian.classList.remove("listening");
      }
      this.setViseme("nathaniel", "REST");
      this.setViseme("julian", "REST");
    }
  }

  /**
   * Trigger natural blinking for characters with randomized intervals
   */
  startBlinkingLoops() {
    const blinkNathaniel = () => {
      const eyelids = document.querySelectorAll("#nathaniel-eyes .eye-lid, #adrian-eyes .eye-lid");
      eyelids.forEach(el => el.setAttribute("d", "M 221 160 Q 230 166 239 160"));
      setTimeout(() => {
        eyelids.forEach(el => el.setAttribute("d", "M 221 160 Q 230 152 239 160"));
      }, 160);
      const nextTime = 2500 + Math.random() * 3000;
      this.blinkTimers.nathaniel = setTimeout(blinkNathaniel, nextTime);
    };

    const blinkJulian = () => {
      const eyelids = document.querySelectorAll("#julian-eyes .eye-lid, #ethan-eyes .eye-lid");
      eyelids.forEach(el => el.setAttribute("d", "M 223 158 Q 232 165 241 158"));
      setTimeout(() => {
        eyelids.forEach(el => el.setAttribute("d", "M 223 158 Q 232 150 241 158"));
      }, 160);
      const nextTime = 2200 + Math.random() * 3200;
      this.blinkTimers.julian = setTimeout(blinkJulian, nextTime);
    };

    blinkNathaniel();
    blinkJulian();
  }

  triggerNod(speaker) {
    const isSenior = (speaker === "nathaniel" || speaker === "adrian");
    const headGroup = document.getElementById(isSenior ? "nathaniel-head-group" : "julian-head-group") ||
                      document.getElementById(isSenior ? "adrian-head-group" : "ethan-head-group");
    if (headGroup) {
      headGroup.classList.remove("head-nod");
      void headGroup.offsetWidth; // Force reflow
      headGroup.classList.add("head-nod");
    }
  }

  triggerGesture(speaker, gestureType) {
    const isSenior = (speaker === "nathaniel" || speaker === "adrian");
    const armGroup = document.getElementById(isSenior ? "nathaniel-right-arm-group" : "julian-right-arm-group") ||
                     document.getElementById(isSenior ? "adrian-right-arm-group" : "ethan-right-arm-group");
    if (armGroup) {
      armGroup.classList.remove("gesture-point", "gesture-explain");
      void armGroup.offsetWidth;
      if (gestureType === "point") {
        armGroup.classList.add("gesture-point");
      } else if (gestureType === "explain") {
        armGroup.classList.add("gesture-explain");
      }
    }
  }

  /**
   * Apply visual configuration for the active scene
   */
  applySceneVisuals(scene) {
    if (!scene) return;

    const holoStation = document.querySelector(".central-hologram-station");
    const conclusionOverlay = document.getElementById("conclusion-title-overlay");

    // Hide conclusion overlay by default unless Scene 7
    if (conclusionOverlay) {
      if (scene.id === 7) {
        conclusionOverlay.classList.add("active");
      } else {
        conclusionOverlay.classList.remove("active");
      }
    }

    // Configure Center Holographic Screen per Scene
    switch (scene.id) {
      case 1:
        // Scene 1: Intro lab with general relativity vs quantum
        this.updateHologram(
          "static/images/spacetime_fluctuations_comparison.png",
          "THEORETICAL IMPASSE: GENERAL RELATIVITY VS. QUANTUM MECHANICS",
          "Continuous Spacetime (G_uv) vs. Quantum Operators (Psi)"
        );
        if (holoStation) holoStation.style.width = "58%";
        break;

      case 2:
        // Scene 2: Two Pictures of Reality
        this.updateHologram(
          "static/images/spacetime_fluctuations_comparison.png",
          "CLASSICAL CURVATURE VS. QUANTUM PROBABILITIES",
          "Einstein Field Equations: G_uv = (8*pi*G/c^4) T_uv"
        );
        if (holoStation) holoStation.style.width = "62%";
        break;

      case 3:
        // Scene 3: What is Quantum Gravity & Planck scale
        this.updateHologram(
          "static/images/length_scale_hierarchy.png",
          "MICROSCOPIC HIERARCHY: ZOOMING INTO THE PLANCK REGIME",
          "Planck Length l_P = 1.616e-35 m (61 Orders of Magnitude)"
        );
        if (holoStation) holoStation.style.width = "64%";
        break;

      case 4:
        // Scene 4: Candidate theories (Cycle through String Theory / Spin Networks)
        this.updateHologram(
          "static/images/string_theory.svg",
          "THEORETICAL CANDIDATE: SUPERSTRING THEORY & QUANTIZED LOOPS",
          "Vibrating 1D Strings (Spin-2 Graviton) | LQG Spin Networks"
        );
        if (holoStation) holoStation.style.width = "62%";
        break;

      case 5:
        // Scene 5: MATLAB Scientific Station (Expanded display for calculations)
        this.updateHologram(
          "static/images/planck_constants_dashboard.png",
          "MATLAB ENGINE: NUMERICAL QUANTUM GRAVITY PIPELINE [QuantumGravity.m]",
          "Planck Scale Calculations & Physical Constants Dashboard (300 DPI)"
        );
        if (holoStation) holoStation.style.width = "72%";
        // Sub-cycle to Schwarzschild radius plot
        setTimeout(() => {
          if (this.activeSpeaker && scene.id === 5) {
            this.updateHologram(
              "static/images/schwarzschild_radius_vs_mass.png",
              "MATLAB COMPUTATION: SCHWARZSCHILD EVENT HORIZON SCALING",
              "r_s(M) = 2GM / c^2 (Evaluated Across 50 Mass Decades)"
            );
          }
        }, 12000);
        break;

      case 6:
        // Scene 6: Future Technologies
        this.updateHologram(
          "static/images/quantum_sensor.svg",
          "HORIZONS OF TECHNOLOGY: QUANTUM SENSORS & GRAVIMETRY",
          "Atom Interferometry, Gravitational-Wave Probes & Tensor Networks"
        );
        if (holoStation) holoStation.style.width = "60%";
        break;

      case 7:
        // Scene 7: Grand Finale
        this.updateHologram(
          "static/images/black_hole_horizon.svg",
          "THE UNIVERSE STILL HAS SECRETS: UNDERSTANDING REALITY",
          "Theoretical Physics, Mathematics, and Computation"
        );
        if (holoStation) holoStation.style.width = "64%";
        break;
    }
  }

  updateHologram(mediaSrc, titleText, captionText) {
    if (this.holoMedia) {
      this.holoMedia.style.opacity = "0.2";
      setTimeout(() => {
        this.holoMedia.src = mediaSrc;
        this.holoMedia.style.opacity = "1";
      }, 200);
    }
    if (this.holoTitle) {
      this.holoTitle.textContent = titleText;
    }
    if (this.holoCaption) {
      this.holoCaption.textContent = captionText;
    }
  }

  reset() {
    this.setSpeakerState(null);
    this.setViseme("nathaniel", "REST");
    this.setViseme("julian", "REST");
  }
}

window.AnimationController = AnimationController;
