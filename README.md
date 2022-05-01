# Canny Edge Detector

The Canny Edge Detector is an algorithm used to perform edge detection in image processing. This repository contains an implementation in Python.

## Usage

Run `python src/main.py <image-name> <low-threshold?> <high-threshold?>` to execute the algorithm, where:

- `<image-name>` is the input image (that must be contained in `input/` directory);
- `<low-threshold?>` and `<high-threshold?>` are the low and high thresholds to be used in hysteresis threshold step. These parameters are optional and their default values in the implementation are `20` and `40`, respectively. Note: if only the low threshold is provided, the high threshold will be the double of it.

The output images will be stored in `output/` directory, which are:

- `_output-step-1.png`: grayscale smoothed/blurred image, obtained using Gaussian kernel;
- `_output-step-2.png`: horizontal gradient of the image, obtained using Sobel kernel;
- `_output-step-3.png`: vertical gradient of the image, obtained using Sobel kernel;
- `_output-step-4.png`: gradient magnitude of the image, obtained using Pythagorean Theorem;
- `_output-step-5.png`: non-maximum suppressed image;
- `output-detected-edges.png`: **the actual result image**, which is obtained from the application of the hysteresis thresholding on the non-maximum suppressed image.

## Examples

### Flower Image

1. Input: <br> ![Input](./docs/example-1.png)
2. Smoothed: <br> ![Smoothed](./docs/example-2.png)
3. Horizontal gradient: <br> ![Horizontal gradient](./docs/example-3.png)
4. Vertical gradient: <br> ![Vertical gradient](./docs/example-4.png)
5. Gradient magnitude: <br> ![Gradient magnitude](./docs/example-5.png)
6. Non-maximum suppressed: <br> ![non-maximum suppressed](./docs/example-6.png)
7. **[Result]** Hysteresis thresholding: <br> ![Hysteresis thresholding](./docs/example-7.png)

### Bird Image

1. Before: <br> ![Bird before](./docs/example-8.png)
2. After: <br> ![Bird before](./docs/example-9.png)

### Butterfly Image

1. Before: <br> ![Butterfly before](./docs/example-10.png)
2. After: <br> ![Butterfly before](./docs/example-11.png)

### Egypt Image

1. Before: <br> ![Egypt before](./docs/example-12.png)
2. After: <br> ![Egypt before](./docs/example-13.png)

## License

This project is licensed under the [MIT License](./LICENSE).
