import cv2

# Step 1: Read image
image = cv2.imread("images/imagessample2.jpg")

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian Blur (reduces noise)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Apply Canny Edge Detection
edges = cv2.Canny(blurred, 100, 200)

# Step 5: Show all outputs
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray)
cv2.imshow("Blurred Image", blurred)
cv2.imshow("Edge Detection", edges)

# Step 6: Save edge-detected output
cv2.imwrite("output_edges.jpg", edges)

print("Edge-detected image saved as output_edges.jpg")

# Wait until key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()