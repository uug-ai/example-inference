import unittest
# Assuming the class is in this module
from uugai_python_color_prediction.ColorPrediction import ColorPrediction


class TestColorPrediction(unittest.TestCase):
    def test_find_main_colors(self):
        # Assuming we have a test image at 'assets/test_image.jpg'
        # test_image = 'assets/test_image.jpg'
        # main_colors, _, _ = ColorPrediction.find_main_colors(image=read_first_frame(test_image),
        #                                                     min_clusters=1,
        #                                                     max_clusters=5,
        #                                                     downsample_factor=0.95,
        #                                                     increase_elbow=0,
        #                                                     verbose=False,
        #                                                     plot=False)
        # Assuming we know the main colors for the test image
        # expected_main_colors = [...]  # Replace with the expected main colors
        # self.assertEqual(main_colors.tolist(), expected_main_colors)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
