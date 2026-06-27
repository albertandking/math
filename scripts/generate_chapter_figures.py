"""Generate chapter figures for the textbook site.

The script creates a small set of PNG figures used by the early chapters.
These figures focus on intuition and avoid visual clutter.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from pathlib import Path

import matplotlib.pyplot as plt


ROOT: Path = Path(__file__).resolve().parent.parent
FIGURE_DIR: Path = ROOT / "assets" / "figures"


def ensure_output_dir(path: Path) -> None:
    """Create the target directory if it does not already exist.

    :param path: Output directory for generated figures.
    """
    path.mkdir(parents=True, exist_ok=True)


def apply_axes_style(ax: plt.Axes, xlabel: str, ylabel: str) -> None:
    """Apply a consistent style to a plot axis.

    :param ax: Matplotlib axis object.
    :param xlabel: Label for the x-axis.
    :param ylabel: Label for the y-axis.
    """
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.axvline(0.0, color="black", linewidth=0.8)


def save_figure(filename: str) -> None:
    """Save the current figure to the shared figure directory.

    :param filename: Target PNG filename.
    """
    output_path: Path = FIGURE_DIR / filename
    plt.tight_layout()
    plt.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close()


def chapter_01_linear_rule() -> None:
    """Generate the first chapter figure for a simple linear rule."""
    xs: list[int] = [0, 1, 2, 3]
    ys: list[int] = [2 * x + 1 for x in xs]

    plt.figure(figsize=(6, 4))
    plt.plot(xs, ys, marker="o", color="#3366cc", label="y = 2x + 1")
    for x_value, y_value in zip(xs, ys):
        plt.annotate(f"({x_value}, {y_value})", (x_value, y_value), xytext=(5, 5), textcoords="offset points")

    ax: plt.Axes = plt.gca()
    apply_axes_style(ax, "x", "y")
    ax.set_title("Linear Rule")
    ax.legend()
    save_figure("ch01_linear_rule.png")


def chapter_02_linear_vs_quadratic() -> None:
    """Generate a comparison figure for linear and quadratic functions."""
    xs: list[float] = [value / 10 for value in range(-20, 41)]
    linear_values: list[float] = [2 * x + 1 for x in xs]
    quadratic_values: list[float] = [x * x for x in xs]

    plt.figure(figsize=(6.5, 4.2))
    plt.plot(xs, linear_values, color="#3366cc", label="y = 2x + 1")
    plt.plot(xs, quadratic_values, color="#cc6633", label="y = x^2")

    ax: plt.Axes = plt.gca()
    apply_axes_style(ax, "x", "y")
    ax.set_title("Linear vs Quadratic")
    ax.legend()
    save_figure("ch02_linear_vs_quadratic.png")


def chapter_02_average_rate() -> None:
    """Generate a secant-line figure for average rate of change."""
    xs: list[float] = [value / 10 for value in range(0, 41)]
    ys: list[float] = [x * x for x in xs]

    x1: float = 1.0
    x2: float = 3.0
    y1: float = x1 * x1
    y2: float = x2 * x2
    slope: float = (y2 - y1) / (x2 - x1)
    secant_values: list[float] = [y1 + slope * (x - x1) for x in xs]

    plt.figure(figsize=(6.5, 4.2))
    plt.plot(xs, ys, color="#cc6633", label="y = x^2")
    plt.plot(xs, secant_values, color="#3366cc", linestyle="--", label="secant line")
    plt.scatter([x1, x2], [y1, y2], color="#222222", zorder=5)
    plt.annotate("A", (x1, y1), xytext=(6, -12), textcoords="offset points")
    plt.annotate("B", (x2, y2), xytext=(6, -12), textcoords="offset points")

    ax: plt.Axes = plt.gca()
    apply_axes_style(ax, "x", "y")
    ax.set_title("Average Rate of Change")
    ax.legend()
    save_figure("ch02_average_rate.png")


def chapter_03_point_and_arrow() -> None:
    """Generate a figure showing a vector as both point and arrow."""
    plt.figure(figsize=(5.5, 5.0))
    ax: plt.Axes = plt.gca()
    ax.scatter([3], [2], color="#cc6633", s=50)
    ax.annotate("Point (3, 2)", (3, 2), xytext=(8, 6), textcoords="offset points")
    ax.arrow(0, 0, 3, 2, head_width=0.18, head_length=0.22, linewidth=2.0, color="#3366cc", length_includes_head=True)
    ax.set_xlim(-0.5, 4.0)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect("equal", adjustable="box")
    apply_axes_style(ax, "x", "y")
    ax.set_title("Vector as Point and Arrow")
    save_figure("ch03_point_and_arrow.png")


def chapter_03_distance() -> None:
    """Generate a figure for the distance between two vectors."""
    point_a: tuple[float, float] = (1.0, 2.0)
    point_b: tuple[float, float] = (4.0, 6.0)

    plt.figure(figsize=(5.8, 5.0))
    ax: plt.Axes = plt.gca()
    ax.scatter([point_a[0], point_b[0]], [point_a[1], point_b[1]], color="#cc6633", s=50)
    ax.plot([point_a[0], point_b[0]], [point_a[1], point_b[1]], color="#3366cc", linewidth=2.0)
    ax.annotate("A(1, 2)", point_a, xytext=(6, -14), textcoords="offset points")
    ax.annotate("B(4, 6)", point_b, xytext=(6, -14), textcoords="offset points")
    ax.set_xlim(0.0, 5.0)
    ax.set_ylim(0.0, 7.0)
    ax.set_aspect("equal", adjustable="box")
    apply_axes_style(ax, "x", "y")
    ax.set_title("Distance Between Two Points")
    save_figure("ch03_distance.png")


def generate_all() -> None:
    """Generate all currently defined chapter figures."""
    generators: Iterable[Callable[[], None]] = (
        chapter_01_linear_rule,
        chapter_02_linear_vs_quadratic,
        chapter_02_average_rate,
        chapter_03_point_and_arrow,
        chapter_03_distance,
    )
    for generator in generators:
        generator()


def main() -> int:
    """Run the figure generation workflow.

    :return: Process exit code.
    """
    ensure_output_dir(FIGURE_DIR)
    generate_all()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
