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

/**
 * Re-typeset formulas after the page is swapped by Material's instant navigation.
 */
function renderMathInPage() {
  if (!window.MathJax || typeof window.MathJax.typesetPromise !== "function") {
    return;
  }

  if (typeof window.MathJax.typesetClear === "function") {
    window.MathJax.typesetClear();
  }

  window.MathJax.typesetPromise().catch((error) => {
    console.error("MathJax typeset failed:", error);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
    window.MathJax.startup.promise.then(() => {
      renderMathInPage();
    });
  }
});

if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
      window.MathJax.startup.promise.then(() => {
        renderMathInPage();
      });
    }
  });
}
