import cv2
import matplotlib.pyplot as plt
depth_map = cv2.imread('Unit v/tof2.jpg', cv2.IMREAD_UNCHANGED)

centre_depth = depth_map[200,200]
print(f"Distance to centre: {centre_depth} mm")

def tof_distance(time_ns):
	c = 3e8
	time_s = time_ns * 1e-9 
	distance = (c*time_s)/2
	return distance

time_ns = 12
distance = tof_distance(time_ns)
print(f"obj is {distance:.2f} meter away.")

"""(.venv) C:\Users\ramch\OneDrive\Desktop\C_vision>python -u "c:\Users\ramch\OneDrive\Desktop\C_vision\Unit v\Time_of_fly.py"
Distance to centre: [ 38  29  22 255] mm
obj is 1.80 meter away.
Object is 1.80 meters away from the camera."""


#example2

def tof_distance(time_ns: float) -> float:
	"""Return one-way distance (meters) from round-trip ToF in nanoseconds."""
	speed_of_light = 3e8  # meters/second
	time_seconds = time_ns * 1e-9
	return (speed_of_light * time_seconds) / 2


if __name__ == "__main__":
	tof_ns = 12.0
	distance_m = tof_distance(tof_ns)
	print(f"Object is {distance_m:.2f} meters away from the camera.")




