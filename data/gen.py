import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

months = [
    "October", "November", "December", "January", "February", "March",
    "April", "May", "June", "July", "August",
    "September", "October", "November", "December", "January", "February",
    "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December", "January", "February",
    "March", "April", "May", "June", "July", "August", "September"
]

years = [
    "Y1", "Y1", "Y1", "Y1", "Y1", "Y1", "Y1", "Y1", "Y1", "Y1", "Y1",
    "Y2", "Y2", "Y2", "Y2", "Y2", "Y2", "Y2", "Y2", "Y2", "Y2", "Y2", "Y2",
    "Y3", "Y3", "Y3", "Y3", "Y3", "Y3", "Y3", "Y3", "Y3", "Y3", "Y3", "Y3", "Y3"
]

obs = np.array([
    24.5, 36.0, 27.7, 11.0, 37.0, 19.5, 53.0, 35.5, 57.5, 48.5, 14.0,
    19.0, 35.0, 31.0, 20.0, 53.0, 52.0, 58.0, 41.0, 53.0, 48.0, 48.5, 14.0,
    24.5, 29.8, 33.5, 23.9, 32.0, 44.5, 38.8, 47.0, 44.3, 52.8, 48.5, 14.0, 21.8
])

exp = np.array([
    18, 32, 30, 12, 40, 52, 61, 35, 50, 37, 6,
    20, 26, 36, 15, 45, 45, 59, 32, 50, 41, 6, 1,
    18, 47, 44, 22, 51, 44, 52, 36, 45, 23, 6, 1, 18
])

# Pressure percentage:
# positive = observed workload was higher than expected
# negative = observed workload was lower than expected
pressure_pct = ((obs - exp) / exp) * 100

# One-row heatmap
heatmap_values = pressure_pct.reshape(1, -1)

fig, ax = plt.subplots(figsize=(18, 4))

# Cap colour scale so extreme months like Exp=1 do not ruin the whole heatmap.
# The labels still show the real values.
norm = TwoSlopeNorm(
    vmin=-100,
    vcenter=0,
    vmax=200
)

im = ax.imshow(
    heatmap_values,
    cmap="RdYlGn_r",
    norm=norm,
    aspect="auto"
)

# X labels
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=90)

# Y label
ax.set_yticks([0])
ax.set_yticklabels(["Pressure"])

# Year labels above the heatmap
for i, year in enumerate(years):
    ax.text(
        i,
        -0.85,
        year,
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

# Add values into cells
for i, value in enumerate(pressure_pct):
    ax.text(
        i,
        0,
        f"{value:.0f}",
        ha="center",
        va="center",
        fontsize=9,
        color="black"
    )

# Draw vertical separators between years
year_change_positions = [
    i - 0.5
    for i in range(1, len(years))
    if years[i] != years[i - 1]
]

for xpos in year_change_positions:
    ax.axvline(x=xpos, color="black", linewidth=1.5)

# Titles and colour bar
ax.set_title(
    "Observed vs Expected Workload Pressure by Month",
    fontsize=16,
    pad=35
)

cbar = plt.colorbar(im, ax=ax)
cbar.set_label("Observed above expected (%)")

# Tidy layout
ax.tick_params(axis="x", length=0)
ax.tick_params(axis="y", length=0)

plt.tight_layout()

# Save and show
plt.savefig("obs_vs_expected_pressure_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()
