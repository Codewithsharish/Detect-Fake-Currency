# Detect-Fake-Currency using Image Processing
With this Project, I build a fake currency detection system for detecting fake currency and real currency. In today’s time, the production and circulation of inauthentic currency notes have been increasingly sophisticated. That’s why there needs to be a system to check whether a currency is fake or real.

This model I build, use a grayscale image, segmentation, and feature extraction.

# METHODOLOGY:
Image Acquisition: The image is provided to the model. There should be two images – a note which you want to detect and a corresponding real note.

RGB to GRAYSCALE: The RGB image is converted into a GRAYSCALE image.

Segmentation: The image is segmented to crop Gandhi Ji image and thin strip image.

Feature Measurement: Feature measurement is done to measure the number of lines on a thin strip. This is a really lengthy process.

Finding Correlation: We find a correlation between Gandhi Ji’s image on the original note and a fake note. If the result is greater than 0.5 then we will consider it legitimate otherwise the currency is fake.

Classification: Finally, we will classify the image as real or fake.

