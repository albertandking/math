"""Generate chapter figures for the textbook site.

The script creates a small set of PNG figures used by the early chapters.
These figures focus on intuition and avoid visual clutter.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
import math
from pathlib import Path

import matplotlib.pyplot as plt


ROOT: Path = Path(__file__).resolve().parent.parent
FIGURE_DIR: Path = ROOT / "assets" / "figures"


def multiply_matrix_vector(matrix: tuple[tuple[float, float], tuple[float, float]], vector: tuple[float, float]) -> tuple[float, float]:
    """Multiply a 2x2 matrix by a 2D vector.

    :param matrix: Two-by-two transformation matrix.
    :param vector: Two-dimensional vector.
    :return: Transformed vector.
    """
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def ensure_output_dir(path: Path) -> None:
    """Create the target directory if it does not already exist.

    :param path: Output directory for generated figures.
    """
    # Create the shared output folder once before generating any figures.
    path.mkdir(parents=True, exist_ok=True)


def apply_axes_style(ax: plt.Axes, xlabel: str, ylabel: str) -> None:
    """Apply a consistent style to a plot axis.

    :param ax: Matplotlib axis object.
    :param xlabel: Label for the x-axis.
    :param ylabel: Label for the y-axis.
    """
    # Keep the early-chapter plots visually consistent for students.
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
    # Use a modestly high DPI so text labels stay readable on the website.
    plt.tight_layout()
    plt.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close()


def chapter_01_linear_rule() -> None:
    """Generate the first chapter figure for a simple linear rule."""
    xs: list[int] = [0, 1, 2, 3]
    ys: list[int] = [2 * x + 1 for x in xs]

    plt.figure(figsize=(6, 4))
    # Plot both the sampled points and the line that connects them.
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
    # Put the two functions on the same axes so students can compare shapes directly.
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
    # Show the curve together with the secant line through the two sample points.
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
    # Display the same vector once as a point and once as an arrow from the origin.
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
    # Connect the two sample points so the notion of geometric distance is visible.
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


def chapter_04_matrix_grid() -> None:
    """Generate a figure that presents a matrix as a row-column table."""
    matrix_values: list[list[int]] = [
        [2, 1, 0],
        [3, -1, 4],
    ]

    plt.figure(figsize=(6.2, 3.2))
    ax: plt.Axes = plt.gca()
    ax.imshow(matrix_values, cmap="Blues", aspect="equal")

    # Annotate each cell so students can relate row-column position to actual values.
    for row_index, row_values in enumerate(matrix_values):
        for column_index, value in enumerate(row_values):
            ax.text(column_index, row_index, str(value), ha="center", va="center", color="#102a43", fontsize=12, fontweight="bold")

    # Use ASCII tick labels to avoid missing-glyph warnings in default matplotlib fonts.
    ax.set_xticks([0, 1, 2], labels=["Col 1", "Col 2", "Col 3"])
    ax.set_yticks([0, 1], labels=["Row 1", "Row 2"])
    ax.set_title("Matrix as a Row-Column Table")
    ax.set_frame_on(False)
    save_figure("ch04_matrix_grid.png")


def chapter_04_linear_transform() -> None:
    """Generate a figure showing a linear transformation of the unit square."""
    matrix: tuple[tuple[float, float], tuple[float, float]] = (
        (1.5, 0.8),
        (0.2, 1.3),
    )
    unit_square: list[tuple[float, float]] = [
        (0.0, 0.0),
        (1.0, 0.0),
        (1.0, 1.0),
        (0.0, 1.0),
        (0.0, 0.0),
    ]
    transformed_square: list[tuple[float, float]] = [multiply_matrix_vector(matrix, point) for point in unit_square]

    plt.figure(figsize=(6.3, 5.0))
    ax: plt.Axes = plt.gca()

    # Show the original square in a lighter style so the transformed shape stands out.
    ax.plot(
        [point[0] for point in unit_square],
        [point[1] for point in unit_square],
        color="#9fb3c8",
        linewidth=2.0,
        label="original square",
    )
    ax.fill(
        [point[0] for point in unit_square],
        [point[1] for point in unit_square],
        color="#d9e2ec",
        alpha=0.45,
    )

    # Plot the transformed square produced by the matrix.
    ax.plot(
        [point[0] for point in transformed_square],
        [point[1] for point in transformed_square],
        color="#3366cc",
        linewidth=2.4,
        label="transformed square",
    )
    ax.fill(
        [point[0] for point in transformed_square],
        [point[1] for point in transformed_square],
        color="#bcccdc",
        alpha=0.45,
    )

    # Draw the transformed basis vectors to make the action of the matrix more explicit.
    basis_x: tuple[float, float] = multiply_matrix_vector(matrix, (1.0, 0.0))
    basis_y: tuple[float, float] = multiply_matrix_vector(matrix, (0.0, 1.0))
    ax.arrow(0, 0, basis_x[0], basis_x[1], head_width=0.1, head_length=0.12, linewidth=2.0, color="#cc6633", length_includes_head=True)
    ax.arrow(0, 0, basis_y[0], basis_y[1], head_width=0.1, head_length=0.12, linewidth=2.0, color="#2f855a", length_includes_head=True)
    ax.annotate("A e1", basis_x, xytext=(6, -12), textcoords="offset points")
    ax.annotate("A e2", basis_y, xytext=(6, 6), textcoords="offset points")

    ax.set_xlim(-0.4, 2.7)
    ax.set_ylim(-0.4, 2.2)
    ax.set_aspect("equal", adjustable="box")
    apply_axes_style(ax, "x", "y")
    ax.set_title("Linear Transformation of a Square")
    ax.legend(loc="upper left")
    save_figure("ch04_linear_transform.png")


def chapter_05_pca_point_cloud() -> None:
    """Generate a point-cloud figure for the PCA intuition section.

    The plot shows an oblique cloud of two-dimensional samples together with
    the principal and secondary directions through the sample center.
    """
    angle_radians: float = math.radians(32.0)
    major_direction: tuple[float, float] = (math.cos(angle_radians), math.sin(angle_radians))
    minor_direction: tuple[float, float] = (-major_direction[1], major_direction[0])

    # Predefined coordinates keep the figure deterministic across runs.
    major_coordinates: list[float] = [-3.2, -2.6, -2.1, -1.5, -0.9, -0.2, 0.5, 1.2, 1.9, 2.5, 3.0]
    minor_offsets: list[float] = [0.20, -0.18, 0.10, -0.12, 0.08, -0.05, 0.04, -0.09, 0.11, -0.15, 0.17]

    points: list[tuple[float, float]] = []
    for major_coordinate, minor_offset in zip(major_coordinates, minor_offsets):
        x_value: float = major_coordinate * major_direction[0] + minor_offset * minor_direction[0]
        y_value: float = major_coordinate * major_direction[1] + minor_offset * minor_direction[1]
        points.append((x_value, y_value))

    center_x: float = sum(point[0] for point in points) / len(points)
    center_y: float = sum(point[1] for point in points) / len(points)

    plt.figure(figsize=(6.3, 5.2))
    ax: plt.Axes = plt.gca()

    # Show the sample cloud first so the principal direction feels data-driven.
    ax.scatter(
        [point[0] for point in points],
        [point[1] for point in points],
        color="#3366cc",
        s=42,
        alpha=0.9,
        label="samples",
    )

    axis_half_length: float = 3.7
    principal_start: tuple[float, float] = (
        center_x - axis_half_length * major_direction[0],
        center_y - axis_half_length * major_direction[1],
    )
    principal_end: tuple[float, float] = (
        center_x + axis_half_length * major_direction[0],
        center_y + axis_half_length * major_direction[1],
    )
    secondary_half_length: float = 1.6
    secondary_start: tuple[float, float] = (
        center_x - secondary_half_length * minor_direction[0],
        center_y - secondary_half_length * minor_direction[1],
    )
    secondary_end: tuple[float, float] = (
        center_x + secondary_half_length * minor_direction[0],
        center_y + secondary_half_length * minor_direction[1],
    )

    # Draw the two orthogonal directions through the cloud center.
    ax.plot(
        [principal_start[0], principal_end[0]],
        [principal_start[1], principal_end[1]],
        color="#cc6633",
        linewidth=2.4,
        label="principal direction",
    )
    ax.plot(
        [secondary_start[0], secondary_end[0]],
        [secondary_start[1], secondary_end[1]],
        color="#2f855a",
        linewidth=2.2,
        linestyle="--",
        label="secondary direction",
    )

    ax.scatter([center_x], [center_y], color="#222222", s=30, zorder=5)
    ax.annotate("center", (center_x, center_y), xytext=(6, 6), textcoords="offset points")
    ax.annotate("PC1", principal_end, xytext=(6, -12), textcoords="offset points", color="#cc6633")
    ax.annotate("PC2", secondary_end, xytext=(6, 6), textcoords="offset points", color="#2f855a")

    x_values: list[float] = [point[0] for point in points]
    y_values: list[float] = [point[1] for point in points]
    ax.set_xlim(min(x_values) - 0.9, max(x_values) + 0.9)
    ax.set_ylim(min(y_values) - 0.9, max(y_values) + 0.9)
    ax.set_aspect("equal", adjustable="box")
    apply_axes_style(ax, "x", "y")
    ax.set_title("Point Cloud and Principal Directions")
    ax.legend(loc="upper left")
    save_figure("ch05_pca_point_cloud.png")


def generate_all() -> None:
    """Generate all currently defined chapter figures."""
    generators: Iterable[Callable[[], None]] = (
        chapter_01_linear_rule,
        chapter_02_linear_vs_quadratic,
        chapter_02_average_rate,
        chapter_03_point_and_arrow,
        chapter_03_distance,
        chapter_04_matrix_grid,
        chapter_04_linear_transform,
        chapter_05_pca_point_cloud,
    )
    for generator in generators:
        # Keep the workflow simple: each generator is independent and writes one file.
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
