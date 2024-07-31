import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class BalloonDetect(Node):

    def __init__(self):
        super().__init__('balloon_detect')
        self.subscription = self.create_subscription(
            Image,
            '/camera',
            self.image_callback,
            10)
        self.publisher = self.create_publisher(Image, 'image_processed', 10)
        self.br = CvBridge()

    def image_callback(self, msg):
        # Convert ROS Image message to OpenCV image
        current_frame = self.br.imgmsg_to_cv2(msg)
        
        # Convert to HSV color space
        hsv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        # Define range for blue color
        lower_blue = np.array([100, 150, 0])
        upper_blue = np.array([140, 255, 255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Find circles in the mask
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100, param1=50, param2=30, minRadius=0, maxRadius=0)

        # If circles are detected
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                # Draw the circle in the output image
                cv2.circle(current_frame, (x, y), r, (0, 255, 0), 4)

        # Convert OpenCV image back to ROS Image message
        processed_image_msg = self.br.cv2_to_imgmsg(current_frame)

        # Publish the processed image
        self.publisher.publish(processed_image_msg)

def main(args=None):
    rclpy.init(args=args)
    balloon_detect = BalloonDetect()
    rclpy.spin(balloon_detect)
    balloon_detect.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
