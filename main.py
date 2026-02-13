import cv2

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect and decode
    data, points, _ = detector.detectAndDecode(frame)
    if points is not None:
        points = points[0].astype(int)
        # Draw bounding box
        for i in range(len(points)):
            cv2.line(frame, tuple(points[i]), tuple(points[(i+1)%len(points)]), (0,255,0), 3)
        if data:
            cv2.putText(frame, data, (points[0][0], points[0][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow("QR Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
