# DLP Membrane Defect Detector
This framework detects membrane holes and unwanted debris, which are factors that lead to error in digital light processing (DLP) 3D printing, using traditional computer vision algorithms.

View `main.ipynb` for project details.

## Challenges
 - Shadow and light source reflection disallow simple thresholding.
 - Contours of the same defect patch sometimes appear disconnected. Since each contour is analyzed individually according to its shape, the defect may be misinterpreted. For instance, a single wrinkle patch can be viewed as multiple holes.
 - So far images of membranes are taken without resin poured in. When there is resin, the bubbles are deemed as holes or wrinkles. There should be a separate class for the bubbles.
 - So far all holes are assumed to be round and near circular.

## Future Improvements
 - Streamline the workflow from image acquisition through automated analysis.
 - Add user interface.
 - Add a bubble detection feature.
 - Improve lighting settings or remove shadowing with photo editting techniques.
 - Group nearby contours to better reveal the shape of a defect.
 - *Gain more data and implement machine learning instead of relying on geometric analyses.*

## Acknowledgments
 - Matthew Chew from R&D, LuxCreo for mentorship
 - Ethan Pan from R&D, LuxCreo for hardware setup
