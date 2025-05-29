import cv2

# Yüz algılayıcıyı yükle
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Kamerayı başlat (0 = dahili kamera)
cap = cv2.VideoCapture(0)

# Kamera açılamazsa çık
if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Görüntü alınamadı!")
        break

    # Gri görüntüye çevir (yüz tespiti için)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Her yüzü bulanıklaştır
    for (x, y, w, h) in faces:
        # Yüz bölgesini al
        face_region = frame[y:y+h, x:x+w]

        # GaussianBlur ile bulanıklaştır
        blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)

        # Bulanık yüzü orijinal görüntüye yapıştır
        frame[y:y+h, x:x+w] = blurred_face

    # Sonucu göster
    cv2.imshow("Canli Yuz Bulaniklastirma", frame)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()
