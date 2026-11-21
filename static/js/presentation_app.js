/**
 * presentation_app.js - Master Scientific Presentation Coordinator
 * Orchestrates 165-second timeline, exactly 7 scenes, two-character dialogue queue,
 * speech synthesis lip-sync, MATLAB dashboard, audio layers, and user controls.
 */

class PresentationApp {
  constructor() {
    this.TOTAL_DURATION = 165; // Exactly 165 seconds (2 min 45 sec)
    this.currentTime = 0;
    this.isPlaying = false;
    this.currentSceneIndex = 0;
    this.currentDialogueIndex = 0;
    this.subtitlesEnabled = true;
    this.soundEnabled = true;

    this.scenesData = null;
    this.matlabData = null;

    this.timelineInterval = null;
    this.dialogueQueueTimeout = null;

    // Audio Elements
    this.audioMusic = null;
    this.audioAmbience = null;
    this.sfxClick = null;
    this.sfxTransition = null;
    this.sfxCalc = null;

    this.init();
  }

  async init() {
    this.initAudioElements();
    this.initControllers();
    await this.loadData();
    this.bindUIEvents();
    this.initParticles();
    this.updateTimelineUI();
    this.updateDiagnostics();
    this.logDiagnostic("Presentation system initialized and ready.", "good");
  }

  initAudioElements() {
    this.audioMusic = new Audio("static/audio/cinematic_music.wav");
    this.audioMusic.loop = true;
    this.audioMusic.volume = 0.12; // Soft background music

    this.audioAmbience = new Audio("static/audio/lab_ambience.wav");
    this.audioAmbience.loop = true;
    this.audioAmbience.volume = 0.08; // Subtle futuristic laboratory hum

    this.sfxClick = new Audio("static/audio/ui_click.wav");
    this.sfxClick.volume = 0.25;

    this.sfxTransition = new Audio("static/audio/scene_transition.wav");
    this.sfxTransition.volume = 0.3;

    this.sfxCalc = new Audio("static/audio/calc_complete.wav");
    this.sfxCalc.volume = 0.35;
  }

  initControllers() {
    this.animCtrl = new AnimationController();

    this.speechEngine = new SpeechEngine(
      // onVisemeChange
      (speaker, viseme) => {
        this.animCtrl.setViseme(speaker, viseme);
      },
      // onSpeechStart
      (speaker, dialogueId) => {
        this.animCtrl.setSpeakerState(speaker);
        this.updateActiveSpeakerUI(speaker);
        this.logDiagnostic(`Speaking: [${speaker.toUpperCase()}] Dialogue ID: ${dialogueId}`);
      },
      // onSpeechEnd
      (speaker, dialogueId) => {
        this.animCtrl.setSpeakerState(null);
        this.updateActiveSpeakerUI(null);
      },
      // onLogEvent
      (msg, level) => {
        this.logDiagnostic(msg, level);
      }
    );
  }

  async loadData() {
    try {
      const sRes = await fetch("data/scenes.json");
      this.scenesData = await sRes.json();
    } catch (e) {
      console.warn("Could not load scenes.json; using built-in dataset fallback", e);
    }

    try {
      const mRes = await fetch("data/quantum_gravity_data.json");
      this.matlabData = await mRes.json();
      this.populateMatlabDashboard();
    } catch (e) {
      console.warn("Could not load quantum_gravity_data.json", e);
    }

    this.renderSceneMarkers();
    this.renderSceneNavMenu();
  }

  bindUIEvents() {
    // Start button on splash screen
    const startBtn = document.getElementById("btn-start-presentation");
    if (startBtn) {
      startBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        const splash = document.getElementById("splash-overlay");
        if (splash) splash.classList.add("hidden");
        this.startPresentation();
      });
    }

    // Play / Pause Toggle
    const playPauseBtn = document.getElementById("btn-play-pause");
    if (playPauseBtn) {
      playPauseBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        if (this.isPlaying) {
          this.pausePresentation();
        } else {
          this.resumePresentation();
        }
      });
    }

    // Restart Button
    const restartBtn = document.getElementById("btn-restart");
    if (restartBtn) {
      restartBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.restartPresentation();
      });
    }

    // Previous / Next Scene
    const prevBtn = document.getElementById("btn-prev-scene");
    if (prevBtn) {
      prevBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.jumpToScene(this.currentSceneIndex - 1);
      });
    }
    const nextBtn = document.getElementById("btn-next-scene");
    if (nextBtn) {
      nextBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.jumpToScene(this.currentSceneIndex + 1);
      });
    }

    // Subtitles Toggle
    const subBtn = document.getElementById("toggle-subtitles");
    if (subBtn) {
      subBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.subtitlesEnabled = !this.subtitlesEnabled;
        subBtn.classList.toggle("active", this.subtitlesEnabled);
        const overlay = document.getElementById("subtitles-overlay");
        if (overlay) overlay.style.display = this.subtitlesEnabled ? "flex" : "none";
      });
    }

    // Sound Toggle
    const soundBtn = document.getElementById("toggle-sound");
    if (soundBtn) {
      soundBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        this.soundEnabled = !this.soundEnabled;
        soundBtn.classList.toggle("active", this.soundEnabled);
        this.speechEngine.setMuted(!this.soundEnabled);
        if (!this.soundEnabled) {
          this.audioMusic.pause();
          this.audioAmbience.pause();
        } else if (this.isPlaying) {
          this.audioMusic.play().catch(() => {});
          this.audioAmbience.play().catch(() => {});
        }
      });
    }

    // Fullscreen Toggle
    const fsBtn = document.getElementById("toggle-fullscreen");
    if (fsBtn) {
      fsBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        if (!document.fullscreenElement) {
          document.documentElement.requestFullscreen().catch(() => {});
        } else {
          document.exitFullscreen().catch(() => {});
        }
      });
    }

    // Scene Menu Dropdown Toggle
    const sceneMenuBtn = document.getElementById("btn-scene-menu");
    const sceneNavMenu = document.getElementById("scene-nav-menu");
    if (sceneMenuBtn && sceneNavMenu) {
      sceneMenuBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        this.playSfx(this.sfxClick);
        sceneNavMenu.classList.toggle("open");
      });
      document.addEventListener("click", (e) => {
        if (!sceneNavMenu.contains(e.target)) {
          sceneNavMenu.classList.remove("open");
        }
      });
    }

    // MATLAB Modal Open / Close
    const matlabBtn = document.getElementById("btn-matlab-results");
    const matlabModal = document.getElementById("matlab-modal");
    const closeModalBtn = document.getElementById("btn-close-modal");
    if (matlabBtn && matlabModal) {
      matlabBtn.addEventListener("click", () => {
        this.playSfx(this.sfxCalc);
        matlabModal.classList.add("open");
      });
    }
    if (closeModalBtn && matlabModal) {
      closeModalBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        matlabModal.classList.remove("open");
      });
      matlabModal.addEventListener("click", (e) => {
        if (e.target === matlabModal) {
          matlabModal.classList.remove("open");
        }
      });
    }

    // Diagnostics Panel Toggle
    const diagBtn = document.getElementById("btn-diagnostics");
    const diagPanel = document.getElementById("diagnostics-panel");
    const closeDiagBtn = document.getElementById("btn-close-diag");
    if (diagBtn && diagPanel) {
      diagBtn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        diagPanel.classList.toggle("open");
        this.updateDiagnostics();
      });
    }
    if (closeDiagBtn && diagPanel) {
      closeDiagBtn.addEventListener("click", () => {
        diagPanel.classList.remove("open");
      });
    }

    // Modal Tabs
    const tabBtns = document.querySelectorAll(".tab-btn");
    tabBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        tabBtns.forEach(b => b.classList.remove("active"));
        document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));
        btn.classList.add("active");
        const targetId = btn.getAttribute("data-tab");
        const targetPane = document.getElementById(targetId);
        if (targetPane) targetPane.classList.add("active");
      });
    });

    // Plot Gallery Pills in Modal
    const plotPills = document.querySelectorAll(".plot-pill");
    const modalPlotImg = document.getElementById("modal-plot-viewer");
    plotPills.forEach(pill => {
      pill.addEventListener("click", () => {
        this.playSfx(this.sfxClick);
        plotPills.forEach(p => p.classList.remove("active"));
        pill.classList.add("active");
        const plotSrc = pill.getAttribute("data-plot");
        if (modalPlotImg) modalPlotImg.src = "static/images/" + plotSrc;
      });
    });

    // Timeline Scrubbing Click
    const timelineTrack = document.getElementById("timeline-track");
    if (timelineTrack) {
      timelineTrack.addEventListener("click", (e) => {
        const rect = timelineTrack.getBoundingClientRect();
        const frac = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
        const targetSec = frac * this.TOTAL_DURATION;
        this.seekToTime(targetSec);
      });
    }

    // Keyboard Shortcuts
    document.addEventListener("keydown", (e) => {
      if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
      if (e.code === "Space") {
        e.preventDefault();
        if (this.isPlaying) this.pausePresentation();
        else this.resumePresentation();
      } else if (e.code === "ArrowRight") {
        e.preventDefault();
        this.jumpToScene(this.currentSceneIndex + 1);
      } else if (e.code === "ArrowLeft") {
        e.preventDefault();
        this.jumpToScene(this.currentSceneIndex - 1);
      } else if (e.key === "m" || e.key === "M") {
        document.getElementById("toggle-sound")?.click();
      } else if (e.key === "s" || e.key === "S") {
        document.getElementById("toggle-subtitles")?.click();
      } else if (e.key === "f" || e.key === "F") {
        document.getElementById("toggle-fullscreen")?.click();
      }
    });
  }

  playSfx(audio) {
    if (!this.soundEnabled || !audio) return;
    try {
      audio.currentTime = 0;
      audio.play().catch(() => {});
    } catch (e) {}
  }

  startPresentation() {
    this.currentTime = 0;
    this.currentSceneIndex = 0;
    this.currentDialogueIndex = 0;
    this.isPlaying = true;

    if (this.soundEnabled) {
      this.audioMusic.currentTime = 0;
      this.audioAmbience.currentTime = 0;
      this.audioMusic.play().catch(() => {});
      this.audioAmbience.play().catch(() => {});
    }

    this.updatePlayPauseIcon();
    this.startTimelineClock();
    this.enterScene(0);
  }

  resumePresentation() {
    this.isPlaying = true;
    this.updatePlayPauseIcon();
    if (this.soundEnabled) {
      this.audioMusic.play().catch(() => {});
      this.audioAmbience.play().catch(() => {});
    }
    this.startTimelineClock();
    this.executeCurrentDialogue();
  }

  pausePresentation() {
    this.isPlaying = false;
    this.updatePlayPauseIcon();
    if (this.timelineInterval) {
      clearInterval(this.timelineInterval);
      this.timelineInterval = null;
    }
    if (this.dialogueQueueTimeout) {
      clearTimeout(this.dialogueQueueTimeout);
      this.dialogueQueueTimeout = null;
    }
    this.speechEngine.cancelSpeech();
    this.audioMusic.pause();
    this.audioAmbience.pause();
    this.logDiagnostic("Presentation paused.");
  }

  restartPresentation() {
    this.pausePresentation();
    this.currentTime = 0;
    this.currentSceneIndex = 0;
    this.currentDialogueIndex = 0;
    this.animCtrl.reset();
    this.startPresentation();
    this.logDiagnostic("Presentation restarted from 00:00.");
  }

  startTimelineClock() {
    if (this.timelineInterval) clearInterval(this.timelineInterval);

    this.timelineInterval = setInterval(() => {
      if (!this.isPlaying) return;

      this.currentTime += 0.25;
      if (this.currentTime >= this.TOTAL_DURATION) {
        this.currentTime = this.TOTAL_DURATION;
        this.onPresentationFinished();
        return;
      }

      this.updateTimelineUI();

      // Check for scene boundary transition
      if (this.scenesData && this.scenesData.scenes) {
        const expectedScene = this.scenesData.scenes.findIndex(
          s => this.currentTime >= s.start_sec && this.currentTime < s.end_sec
        );
        if (expectedScene !== -1 && expectedScene !== this.currentSceneIndex) {
          this.enterScene(expectedScene);
        }
      }
    }, 250);
  }

  enterScene(sceneIndex) {
    if (!this.scenesData || !this.scenesData.scenes[sceneIndex]) return;

    this.currentSceneIndex = sceneIndex;
    const scene = this.scenesData.scenes[sceneIndex];
    this.currentDialogueIndex = 0;

    this.playSfx(this.sfxTransition);
    this.animCtrl.applySceneVisuals(scene);
    this.updateSceneHeaderUI(scene);
    this.logDiagnostic(`Entered Scene ${scene.id}: ${scene.title}`);

    // If Scene 5 (MATLAB), play subtle calculation chime
    if (scene.id === 5) {
      setTimeout(() => this.playSfx(this.sfxCalc), 800);
    }

    this.executeCurrentDialogue();
  }

  executeCurrentDialogue() {
    if (!this.isPlaying || !this.scenesData) return;
    const scene = this.scenesData.scenes[this.currentSceneIndex];
    if (!scene || !scene.dialogues) return;

    const dialogue = scene.dialogues[this.currentDialogueIndex];
    if (!dialogue) {
      // Completed all dialogues in current scene, wait for next scene time
      return;
    }

    this.displaySubtitle(dialogue);

    this.speechEngine.speakDialogue(dialogue, () => {
      if (!this.isPlaying) return;

      this.currentDialogueIndex++;
      // Short natural conversational pause (400ms) before the other researcher responds
      this.dialogueQueueTimeout = setTimeout(() => {
        if (this.isPlaying) {
          this.executeCurrentDialogue();
        }
      }, 450);
    });
  }

  displaySubtitle(dialogue) {
    const overlay = document.getElementById("subtitles-overlay");
    const speakerLabel = document.getElementById("sub-speaker");
    const subText = document.getElementById("sub-text");

    if (!overlay || !speakerLabel || !subText) return;

    if (dialogue.speaker === "nathaniel" || dialogue.speaker === "adrian") {
      speakerLabel.textContent = "Dr. Nathaniel Brooks (Senior Theoretical Physicist)";
      speakerLabel.className = "subtitle-speaker-label speaker-nathaniel-label";
    } else {
      speakerLabel.textContent = "Dr. Julian Hayes (Quantum & Computational Researcher)";
      speakerLabel.className = "subtitle-speaker-label speaker-julian-label";
    }

    subText.textContent = dialogue.text;
  }

  jumpToScene(targetIndex) {
    if (!this.scenesData || !this.scenesData.scenes) return;
    const maxIdx = this.scenesData.scenes.length - 1;
    const clamped = Math.max(0, Math.min(maxIdx, targetIndex));
    const targetScene = this.scenesData.scenes[clamped];

    this.speechEngine.cancelSpeech();
    if (this.dialogueQueueTimeout) clearTimeout(this.dialogueQueueTimeout);

    this.currentTime = targetScene.start_sec;
    this.enterScene(clamped);
    this.updateTimelineUI();
  }

  seekToTime(seconds) {
    this.currentTime = Math.max(0, Math.min(this.TOTAL_DURATION, seconds));
    if (!this.scenesData) return;

    const foundIdx = this.scenesData.scenes.findIndex(
      s => this.currentTime >= s.start_sec && this.currentTime < s.end_sec
    );
    const sceneIdx = foundIdx !== -1 ? foundIdx : (this.currentTime >= this.TOTAL_DURATION ? 6 : 0);

    this.speechEngine.cancelSpeech();
    if (this.dialogueQueueTimeout) clearTimeout(this.dialogueQueueTimeout);

    if (sceneIdx !== this.currentSceneIndex) {
      this.enterScene(sceneIdx);
    } else {
      // Seek dialogue within scene
      const scene = this.scenesData.scenes[sceneIdx];
      const dIdx = scene.dialogues.findIndex(
        d => this.currentTime >= d.start_sec && this.currentTime <= d.end_sec
      );
      this.currentDialogueIndex = dIdx !== -1 ? dIdx : 0;
      this.executeCurrentDialogue();
    }

    this.updateTimelineUI();
  }

  onPresentationFinished() {
    this.pausePresentation();
    this.currentTime = this.TOTAL_DURATION;
    this.updateTimelineUI();
    this.animCtrl.setSpeakerState(null);
    this.logDiagnostic("Presentation reached conclusion (165s).", "good");
  }

  updateTimelineUI() {
    const fill = document.getElementById("timeline-progress-fill");
    const timeDisplay = document.getElementById("time-display");

    const pct = (this.currentTime / this.TOTAL_DURATION) * 100;
    if (fill) fill.style.width = `${pct}%`;

    if (timeDisplay) {
      const curM = Math.floor(this.currentTime / 60);
      const curS = Math.floor(this.currentTime % 60);
      const totM = Math.floor(this.TOTAL_DURATION / 60);
      const totS = Math.floor(this.TOTAL_DURATION % 60);
      const pad = (n) => (n < 10 ? "0" + n : n);
      timeDisplay.textContent = `${pad(curM)}:${pad(curS)} / ${pad(totM)}:${pad(totS)}`;
    }
  }

  updateSceneHeaderUI(scene) {
    const badge = document.getElementById("scene-badge");
    const title = document.getElementById("scene-title");

    if (badge) badge.textContent = `SCENE ${scene.id} / 7`;
    if (title) title.textContent = scene.title;

    // Update scene nav active state
    document.querySelectorAll(".scene-nav-item").forEach((el, idx) => {
      el.classList.toggle("current", idx === (scene.id - 1));
    });
  }

  updateActiveSpeakerUI(speaker) {
    const nathanielPlate = document.querySelector("#char-nathaniel-wrapper .character-nameplate") || document.querySelector("#char-adrian-wrapper .character-nameplate");
    const julianPlate = document.querySelector("#char-julian-wrapper .character-nameplate") || document.querySelector("#char-ethan-wrapper .character-nameplate");

    if (nathanielPlate) {
      let pulse = nathanielPlate.querySelector(".speaking-pulse-indicator");
      if (speaker === "nathaniel" || speaker === "adrian") {
        if (!pulse) {
          pulse = document.createElement("span");
          pulse.className = "speaking-pulse-indicator";
          nathanielPlate.appendChild(pulse);
        }
      } else if (pulse) {
        pulse.remove();
      }
    }

    if (julianPlate) {
      let pulse = julianPlate.querySelector(".speaking-pulse-indicator");
      if (speaker === "julian" || speaker === "ethan") {
        if (!pulse) {
          pulse = document.createElement("span");
          pulse.className = "speaking-pulse-indicator";
          julianPlate.appendChild(pulse);
        }
      } else if (pulse) {
        pulse.remove();
      }
    }
  }

  updatePlayPauseIcon() {
    const btn = document.getElementById("btn-play-pause");
    if (!btn) return;
    btn.innerHTML = this.isPlaying
      ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>`
      : `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>`;
  }

  renderSceneMarkers() {
    if (!this.scenesData || !this.scenesData.scenes) return;
    const track = document.getElementById("timeline-track");
    if (!track) return;

    this.scenesData.scenes.forEach(scene => {
      const marker = document.createElement("div");
      marker.className = "scene-marker";
      const pct = (scene.start_sec / this.TOTAL_DURATION) * 100;
      marker.style.left = `${pct}%`;
      track.appendChild(marker);
    });
  }

  renderSceneNavMenu() {
    if (!this.scenesData || !this.scenesData.scenes) return;
    const menu = document.getElementById("scene-nav-menu");
    if (!menu) return;

    menu.innerHTML = "";
    this.scenesData.scenes.forEach((scene, idx) => {
      const item = document.createElement("div");
      item.className = `scene-nav-item ${idx === 0 ? "current" : ""}`;
      item.innerHTML = `
        <span class="scene-nav-title">${scene.id}. ${scene.title}</span>
        <span class="scene-nav-time">${scene.time_range}</span>
      `;
      item.addEventListener("click", () => {
        this.jumpToScene(idx);
        menu.classList.remove("open");
      });
      menu.appendChild(item);
    });
  }

  populateMatlabDashboard() {
    if (!this.matlabData) return;

    const engineBadge = document.getElementById("modal-engine-badge");
    if (engineBadge) {
      engineBadge.textContent = this.matlabData.execution_engine;
    }

    const jsonBox = document.getElementById("modal-json-content");
    if (jsonBox) {
      jsonBox.textContent = JSON.stringify(this.matlabData, null, 2);
    }

    // Populate Planck constant values
    const ps = this.matlabData.planck_scale;
    if (ps) {
      document.getElementById("dash-lP") && (document.getElementById("dash-lP").textContent = `${ps.planck_length_m.toExponential(4)} m`);
      document.getElementById("dash-tP") && (document.getElementById("dash-tP").textContent = `${ps.planck_time_s.toExponential(4)} s`);
      document.getElementById("dash-EP") && (document.getElementById("dash-EP").textContent = `${ps.planck_energy_GeV.toExponential(3)} GeV`);
      document.getElementById("dash-mP") && (document.getElementById("dash-mP").textContent = `${ps.planck_mass_kg.toExponential(4)} kg`);
    }

    // Populate Schwarzschild benchmark table
    const bmTable = document.getElementById("benchmark-table-body");
    if (bmTable && this.matlabData.schwarzschild_benchmarks) {
      bmTable.innerHTML = "";
      this.matlabData.schwarzschild_benchmarks.forEach(bm => {
        const row = document.createElement("tr");
        row.style.borderBottom = "1px solid rgba(148, 163, 184, 0.15)";
        row.style.padding = "8px 0";
        row.innerHTML = `
          <td style="padding: 6px 12px; color: #f8fafc; font-weight: 600;">${bm.name}</td>
          <td style="padding: 6px 12px; font-family: monospace; color: #38bdf8;">${bm.mass_kg.toExponential(3)} kg</td>
          <td style="padding: 6px 12px; font-family: monospace; color: #fbbf24;">${bm.schwarzschild_radius_m.toExponential(3)} m</td>
          <td style="padding: 6px 12px; font-family: monospace; color: #34d399;">${bm.hawking_temperature_K.toExponential(3)} K</td>
        `;
        bmTable.appendChild(row);
      });
    }
  }

  updateDiagnostics() {
    const diag = this.speechEngine.getVoiceDiagnostics();
    document.getElementById("diag-voices-loaded") && (document.getElementById("diag-voices-loaded").textContent = diag.voicesLoaded ? "Yes" : "Waiting");
    document.getElementById("diag-total-voices") && (document.getElementById("diag-total-voices").textContent = diag.totalVoices);
    const nathanielVoiceEl = document.getElementById("diag-nathaniel-voice") || document.getElementById("diag-adrian-voice");
    const julianVoiceEl = document.getElementById("diag-julian-voice") || document.getElementById("diag-ethan-voice");
    if (nathanielVoiceEl) nathanielVoiceEl.textContent = diag.nathanielVoice || diag.adrianVoice;
    if (julianVoiceEl) julianVoiceEl.textContent = diag.julianVoice || diag.ethanVoice;
    document.getElementById("diag-distinct") && (document.getElementById("diag-distinct").textContent = diag.isDistinct ? "Verified Distinct" : "Warning: Shared Voice");

    const engineStatus = this.matlabData ? this.matlabData.execution_engine : "Awaiting Data";
    document.getElementById("diag-matlab-engine") && (document.getElementById("diag-matlab-engine").textContent = engineStatus);
  }

  logDiagnostic(msg, level = "info") {
    const logBox = document.getElementById("diag-event-log");
    if (!logBox) return;

    const time = new Date().toTimeString().split(" ")[0];
    const line = document.createElement("div");
    line.style.color = level === "good" ? "#34d399" : (level === "warn" ? "#fbbf24" : "#94a3b8");
    line.textContent = `[${time}] ${msg}`;
    logBox.appendChild(line);
    logBox.scrollTop = logBox.scrollHeight;
  }

  initParticles() {
    const canvas = document.getElementById("particles-canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    resize();
    window.addEventListener("resize", resize);

    const particles = [];
    for (let i = 0; i < 45; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        size: Math.random() * 2 + 1,
        alpha: Math.random() * 0.5 + 0.2
      });
    }

    const animate = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = "rgba(56, 189, 248, 0.4)";

      for (let p of particles) {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
      }
      requestAnimationFrame(animate);
    };
    animate();
  }
}

// Instantiate presentation app on DOM ready
document.addEventListener("DOMContentLoaded", () => {
  window.presentationApp = new PresentationApp();
});
