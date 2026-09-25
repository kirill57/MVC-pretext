// Figure 3.3.16: four continuous paths from the identity to familiar linear maps.
(() => {
  "use strict";

  function initialize() {
    const root = document.getElementById("c3s3-four-linear-moves-slate");
    if (!root) return;
    document.documentElement.style.overflow = "hidden";
    document.body.style.overflow = "hidden";
    root.style.height = "auto";

    const canvas = document.createElement("canvas");
    canvas.width = 900;
    canvas.height = 520;
    canvas.style.cssText = "display:block;width:100%;height:auto";
    canvas.setAttribute("role", "img");
    canvas.setAttribute("aria-label", "Four panels animate a unit square under rotation, reflection, projection, and shear. Dashed gray outlines and basis arrows show the original square.");

    const controls = document.createElement("div");
    controls.style.cssText = "display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:5px 8px;font:14px system-ui,sans-serif;color:#263238";
    const play = document.createElement("button");
    play.type = "button";
    play.textContent = "Play";
    play.style.cssText = "padding:5px 14px;border:1px solid #23559b;border-radius:5px;background:#23559b;color:white;font:inherit;cursor:pointer";
    const slider = document.createElement("input");
    slider.type = "range";
    slider.min = "0";
    slider.max = "1000";
    slider.value = "0";
    slider.setAttribute("aria-label", "Transformation progress");
    slider.style.cssText = "flex:1 1 160px;min-width:120px;accent-color:#23559b";
    const progress = document.createElement("output");
    progress.textContent = "t = 0.00";
    progress.style.minWidth = "66px";
    const legend = document.createElement("span");
    legend.textContent = "Gray: original   Blue/orange arrows: moving basis";
    legend.style.cssText = "flex-basis:100%;font-size:12px;color:#56616f";
    controls.append(play, slider, progress, legend);
    root.append(canvas, controls);

    const ctx = canvas.getContext("2d");
    const panels = [
      { title: "rotation", x: 12, y: 8, color: "#315fb0", fill: "rgba(71,118,212,.25)",
        map: (x, y, t) => {
          const a = Math.PI * t / 2;
          return [x * Math.cos(a) - y * Math.sin(a), x * Math.sin(a) + y * Math.cos(a)];
        }, det: () => 1 },
      { title: "reflection", x: 456, y: 8, color: "#ad581d", fill: "rgba(232,147,66,.27)",
        map: (x, y, t) => [x, (1 - 2 * t) * y], det: t => 1 - 2 * t },
      { title: "projection", x: 12, y: 266, color: "#b3313b", fill: "rgba(223,88,101,.25)",
        map: (x, y, t) => [x, (1 - t) * y], det: t => 1 - t },
      { title: "horizontal shear", x: 456, y: 266, color: "#187b72", fill: "rgba(49,169,154,.25)",
        map: (x, y, t) => [x + 0.7 * t * y, y], det: () => 1 },
    ];
    let t = 0;
    let playing = false;
    let frame = 0;
    let startTime = 0;
    const duration = 4800;

    function point(panel, x, y) {
      return [panel.x + 185 + 70 * x, panel.y + 130 - 70 * y];
    }

    function segment(a, b, color, width = 1.5, dash = []) {
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(a[0], a[1]);
      ctx.lineTo(b[0], b[1]);
      ctx.strokeStyle = color;
      ctx.lineWidth = width;
      ctx.lineCap = "round";
      ctx.setLineDash(dash);
      ctx.stroke();
      ctx.restore();
    }

    function arrow(a, b, color, width = 2.3, dash = []) {
      const dx = b[0] - a[0];
      const dy = b[1] - a[1];
      const length = Math.hypot(dx, dy);
      if (length < 3) {
        ctx.beginPath();
        ctx.arc(a[0], a[1], 3.5, 0, 2 * Math.PI);
        ctx.fillStyle = color;
        ctx.fill();
        return;
      }
      segment(a, b, color, width, dash);
      const angle = Math.atan2(dy, dx);
      const head = 8;
      ctx.beginPath();
      ctx.moveTo(b[0], b[1]);
      ctx.lineTo(b[0] - head * Math.cos(angle - .45), b[1] - head * Math.sin(angle - .45));
      ctx.lineTo(b[0] - head * Math.cos(angle + .45), b[1] - head * Math.sin(angle + .45));
      ctx.closePath();
      ctx.fillStyle = color;
      ctx.fill();
    }

    function polygon(points, fill, stroke, dash = []) {
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(points[0][0], points[0][1]);
      for (const p of points.slice(1)) ctx.lineTo(p[0], p[1]);
      ctx.closePath();
      ctx.fillStyle = fill;
      ctx.fill();
      ctx.strokeStyle = stroke;
      ctx.lineWidth = 2;
      ctx.setLineDash(dash);
      ctx.stroke();
      ctx.restore();
    }

    function determinant(value) {
      if (Math.abs(value) < .005) return "0";
      if (Math.abs(value - 1) < .005) return "+1";
      if (Math.abs(value + 1) < .005) return "−1";
      return (value > 0 ? "+" : "−") + Math.abs(value).toFixed(2);
    }

    function drawPanel(panel) {
      ctx.fillStyle = "#fbfcfe";
      ctx.fillRect(panel.x, panel.y, 432, 246);
      ctx.strokeStyle = "#d7dee7";
      ctx.lineWidth = 1;
      ctx.strokeRect(panel.x + .5, panel.y + .5, 431, 245);
      ctx.fillStyle = "#202b37";
      ctx.font = "bold 18px system-ui,sans-serif";
      ctx.fillText(panel.title, panel.x + 16, panel.y + 27);

      const o = point(panel, 0, 0);
      const e1 = point(panel, 1, 0);
      const e2 = point(panel, 0, 1);
      const corner = point(panel, 1, 1);
      const p1 = point(panel, ...panel.map(1, 0, t));
      const p2 = point(panel, ...panel.map(0, 1, t));
      const p12 = point(panel, ...panel.map(1, 1, t));

      segment(point(panel, -1.5, 0), point(panel, 2.2, 0), "#d1d9e2", 1);
      segment(point(panel, 0, -1.2), point(panel, 0, 1.35), "#d1d9e2", 1);
      polygon([o, e1, corner, e2], "rgba(107,114,128,.17)", "#7e8793", [6, 4]);
      polygon([o, p1, p12, p2], panel.fill, panel.color);
      // Redraw the fixed dashed outline so it remains visible at t = 0.
      polygon([o, e1, corner, e2], "rgba(0,0,0,0)", "#7e8793", [6, 4]);
      arrow(o, e1, "#747e8b", 1.6, [4, 3]);
      arrow(o, e2, "#747e8b", 1.6, [4, 3]);
      ctx.fillStyle = "#5e6875";
      ctx.font = "italic 15px Georgia,serif";
      ctx.fillText("e₁", e1[0] + 6, e1[1] + 18);
      ctx.fillText("e₂", e2[0] - 22, e2[1] - 5);
      arrow(o, p1, "#2156b0", 2.8);
      arrow(o, p2, "#c46915", 2.8);
      if (Math.abs(panel.det(t)) < .01) segment(o, p1, panel.color, 3.2);
      ctx.fillStyle = panel.color;
      ctx.font = "16px system-ui,sans-serif";
      ctx.fillText("det = " + determinant(panel.det(t)), panel.x + 16, panel.y + 230);
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (const panel of panels) drawPanel(panel);
      slider.value = String(Math.round(t * 1000));
      progress.textContent = "t = " + t.toFixed(2);
    }

    function stop() {
      playing = false;
      cancelAnimationFrame(frame);
      play.textContent = t >= 1 ? "Replay" : "Play";
    }

    function tick(now) {
      if (!playing) return;
      t = Math.min(1, (now - startTime) / duration);
      draw();
      if (t >= 1) stop();
      else frame = requestAnimationFrame(tick);
    }

    play.addEventListener("click", () => {
      if (playing) {
        stop();
      } else {
        if (t >= 1) t = 0;
        playing = true;
        play.textContent = "Pause";
        startTime = performance.now() - t * duration;
        frame = requestAnimationFrame(tick);
      }
    });
    slider.addEventListener("input", () => {
      if (playing) stop();
      t = Number(slider.value) / 1000;
      draw();
      play.textContent = t >= 1 ? "Replay" : "Play";
    });
    document.addEventListener("visibilitychange", () => {
      if (document.hidden && playing) stop();
    });
    draw();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize, { once: true });
  } else {
    initialize();
  }
})();
