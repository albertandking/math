// Configure MathJax so MkDocs-rendered formulas are processed correctly.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
  startup: {
    // Let Material's instant navigation trigger typesetting explicitly.
    typeset: false,
  },
};

// #region debug-point A:runtime-reporting
const DEBUG_SERVER_URL = "http://127.0.0.1:7777/event";
const DEBUG_SESSION_ID = "mathjax-first-load";
const DEBUG_RUN_ID = "pre-fix";
const DEBUG_PREFIX = "[DEBUG]";
function reportMathDebug(hypothesisId, location, msg, data) {
  fetch(DEBUG_SERVER_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      sessionId: DEBUG_SESSION_ID,
      runId: DEBUG_RUN_ID,
      hypothesisId,
      location,
      msg: `${DEBUG_PREFIX} ${msg}`,
      data,
      ts: Date.now(),
    }),
  }).catch(() => {});
}
function getMathDebugSnapshot() {
  return {
    readyState: document.readyState,
    arithmatexCount: document.querySelectorAll(".arithmatex").length,
    mjxContainerCount: document.querySelectorAll("mjx-container").length,
    scriptCount: document.querySelectorAll('script[id^="MathJax"]').length,
  };
}
// #endregion

/**
 * Re-typeset formulas after the page is swapped by Material's instant navigation.
 */
function renderMathInPage() {
  // #region debug-point A:render-entry
  reportMathDebug("A", "assets/javascripts/mathjax.js:renderMathInPage:entry", "renderMathInPage invoked", getMathDebugSnapshot());
  // #endregion
  if (!window.MathJax || typeof window.MathJax.typesetPromise !== "function") {
    // #region debug-point A:mathjax-not-ready
    reportMathDebug("A", "assets/javascripts/mathjax.js:renderMathInPage:not-ready", "MathJax typesetPromise unavailable", {
      hasMathJax: Boolean(window.MathJax),
      typesetPromiseType: typeof window.MathJax?.typesetPromise,
      ...getMathDebugSnapshot(),
    });
    // #endregion
    return;
  }

  if (typeof window.MathJax.typesetClear === "function") {
    // #region debug-point C:before-typeset-clear
    reportMathDebug("C", "assets/javascripts/mathjax.js:renderMathInPage:before-clear", "Calling typesetClear before typesetPromise", getMathDebugSnapshot());
    // #endregion
    window.MathJax.typesetClear();
  }

  window.MathJax.typesetPromise()
    .then(() => {
      // #region debug-point D:typeset-success
      reportMathDebug("D", "assets/javascripts/mathjax.js:renderMathInPage:success", "typesetPromise resolved", getMathDebugSnapshot());
      // #endregion
    })
    .catch((error) => {
      // #region debug-point E:typeset-error
      reportMathDebug("E", "assets/javascripts/mathjax.js:renderMathInPage:error", "typesetPromise rejected", {
        message: error?.message ?? String(error),
        ...getMathDebugSnapshot(),
      });
      // #endregion
      console.error("MathJax typeset failed:", error);
    });
}

document.addEventListener("DOMContentLoaded", () => {
  // #region debug-point B:dom-content-loaded
  reportMathDebug("B", "assets/javascripts/mathjax.js:DOMContentLoaded", "DOMContentLoaded fired", {
    hasStartupPromise: Boolean(window.MathJax?.startup?.promise),
    ...getMathDebugSnapshot(),
  });
  // #endregion
  if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
    window.MathJax.startup.promise.then(() => {
      // #region debug-point B:startup-promise-dom
      reportMathDebug("B", "assets/javascripts/mathjax.js:DOMContentLoaded:startup-promise", "MathJax startup promise resolved after DOMContentLoaded", getMathDebugSnapshot());
      // #endregion
      renderMathInPage();
    });
  }
});

if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    // #region debug-point B:document-subscribe
    reportMathDebug("B", "assets/javascripts/mathjax.js:document$.subscribe", "Material document$ subscription fired", {
      hasStartupPromise: Boolean(window.MathJax?.startup?.promise),
      ...getMathDebugSnapshot(),
    });
    // #endregion
    if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
      window.MathJax.startup.promise.then(() => {
        // #region debug-point B:startup-promise-subscribe
        reportMathDebug("B", "assets/javascripts/mathjax.js:document$.subscribe:startup-promise", "MathJax startup promise resolved after document$ subscription", getMathDebugSnapshot());
        // #endregion
        renderMathInPage();
      });
    }
  });
}
