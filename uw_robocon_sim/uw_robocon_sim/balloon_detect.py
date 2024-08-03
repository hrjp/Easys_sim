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
        self.current_frame = self.br.imgmsg_to_cv2(msg)
        
        # Convert to HSV color space
        hsv = cv2.cvtColor(self.current_frame, cv2.COLOR_RGB2HSV)

        # Define range for red color
        lower_red = np.array([0, 10, 10])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([170, 10, 10])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        mask_red = cv2.bitwise_or(mask1, mask2)

        # Define range for blue color
        lower_blue = np.array([100, 10, 10])
        upper_blue = np.array([130, 255, 255])
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

        # Define range for yellow color
        lower_yellow = np.array([20, 10, 10])
        upper_yellow = np.array([60, 255, 255])
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Combine the masks
        mask = cv2.bitwise_or(mask1, mask2)
        mask = cv2.bitwise_or(mask, mask_blue)
        mask = cv2.bitwise_or(mask, mask_yellow)

        self.mask2boudingbox(mask_red, "Red")
        self.mask2boudingbox(mask_blue, "Blue")
        self.mask2boudingbox(mask_yellow, "Yellow")

        # # Find contours in the mask
        # contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # # If contours are found
        # if len(contours) > 0:
        #     for contour in contours:
        #         # Find the bounding rectangle of the contour
        #         x, y, w, h = cv2.boundingRect(contour)

        #         # Get the color of the contour
        #         color = ""
        #         if cv2.contourArea(contour) > 500:
        #             if cv2.pointPolygonTest(contour, (x + w // 2, y + h // 2), False) >= 0:
        #                 if cv2.countNonZero(cv2.bitwise_and(mask1, mask1, mask=mask)) > 0:
        #                     color = "Red"
        #                 elif cv2.countNonZero(cv2.bitwise_and(mask2, mask2, mask=mask)) > 0:
        #                     color = "Red"
        #                 elif cv2.countNonZero(cv2.bitwise_and(mask_blue, mask_blue, mask=mask)) > 0:
        #                     color = "Blue"
        #                 elif cv2.countNonZero(cv2.bitwise_and(mask_yellow, mask_yellow, mask=mask)) > 0:
        #                     color = "Yellow"

        #             # Draw the bounding rectangle in the output image
        #             cv2.rectangle(self.current_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #             # Put the color label on the bounding box
        #             cv2.putText(self.current_frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Convert OpenCV image back to ROS Image message
        processed_image_msg = self.br.cv2_to_imgmsg(self.current_frame, encoding="rgb8")

        # Publish the processed image
        self.publisher.publish(processed_image_msg)
    
    def mask2boudingbox(self, mask, color):
        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # If contours are found
        if len(contours) > 0:
            for contour in contours:
                # Find the bounding rectangle of the contour
                x, y, w, h = cv2.boundingRect(contour)

                # Get the color of the contour
                if cv2.contourArea(contour) > 50:

                    # Draw the bounding rectangle in the output image
                    cv2.rectangle(self.current_frame, (x, y), (x + w, y + h), (0, 255, 0), 1)

                    # Put the color label on the bounding box
                    cv2.putText(self.current_frame, color, (x, y - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

def main(args=None):
    rclpy.init(args=args)
    balloon_detect = BalloonDetect()
    rclpy.spin(balloon_detect)
    balloon_detect.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
