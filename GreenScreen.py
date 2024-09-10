import cv2
import numpy as np
import tkinter as tk
from tkinter import Label, Button

kayit = cv2.VideoCapture(0)
renk_alt_sinir = np.array([0, 0, 0])
renk_ust_sinir = np.array([5, 255, 255])
def goruntu():
    while True:
        kayit = cv2.VideoCapture(0)
        bc, cevir = kayit.read()
        hsv = cv2.cvtColor(cevir, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, renk_alt_sinir,renk_ust_sinir)
        red_cevir = cv2.bitwise_and(cevir, cevir, mask=mask)
        cv2.imshow("normal goruntu press 'q' for off", cevir)
        cv2.imshow("donusturulmus goruntu press 'q' for off", red_cevir)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
root = tk.Tk()
root.title("Görüntü İşleme")
root.configure(bg="green")

kayit = cv2.VideoCapture(0)
kayit.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
kayit.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

show_frames_button = Button(root, text="Görüntüleri göster", command=goruntu)
show_frames_button.pack()

root.mainloop()

kayit.release()
cv2.destroyAllWindows()