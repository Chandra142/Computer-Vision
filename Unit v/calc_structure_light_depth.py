import numpy as np

def calculate_structure_light_depth(baseline, alpha_deg, beta_deg):
    alpha_rad = np.radians(alpha_deg)
    beta_deg = np.radians(beta_deg)

    try:
        denom = (1/np.tan(alpha_rad)) + (1/ np.tan(beta_rad))
        z = baseline / denom
        return round(z,4)
    except ZeroDivisionError
        return float('inf')
    
    baseline_dist = 150.0
    fixed_projector_angle = 60.0
    detect_camera_angles = [45.0, 48.0,50.0,52.0,52.0]
    