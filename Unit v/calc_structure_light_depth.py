import numpy as np

def calculate_structure_light_depth(baseline, alpha_deg, beta_deg):
    """Compute object depth using triangulation from projector/camera angles.

    Args:
        baseline: Distance between projector and camera.
        alpha_deg: Projector angle in degrees.
        beta_deg: Camera angle in degrees.

    Returns:
        Depth value rounded to 4 decimals, or inf when geometry is singular.
    """
    alpha_rad = np.radians(alpha_deg)
    beta_rad = np.radians(beta_deg)

    try:
        denom = (1 / np.tan(alpha_rad)) + (1 / np.tan(beta_rad))
        if np.isclose(denom, 0.0):
            return float("inf")
        z = baseline / denom
        return round(float(z), 4)
    except ZeroDivisionError:
        return float("inf")


if __name__ == "__main__":
    baseline_dist = 150.0
    fixed_projector_angle = 60.0
    detected_camera_angles = [45.0, 48.0, 50.0, 52.0, 54.0]

    print("Structure Light Depth Results")
    for beta in detected_camera_angles:
        depth = calculate_structure_light_depth(
            baseline_dist, fixed_projector_angle, beta
        )
        print(f"camera_angle={beta} deg -> depth={depth}")
    