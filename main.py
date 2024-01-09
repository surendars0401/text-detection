import cv2
import pytesseract
from collections import Counter


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'#tesseract file location

cap = cv2.VideoCapture(0)


frame_display_delay = 1  
text_detection_interval = 20 
frame_counter = 0 
ocr_interval = 3  


detected_numbers_list = []
max_list_length = 20  

final_output_printed = False

ocr_count = 0

while True:
    ret, frame = cap.read()

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    blurred = cv2.bilateralFilter(gray, 9, 75, 75)

   
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    ocr_counter = 0  # Initialize OCR counter

    for contour in contours:
        
        [x, y, w, h] = cv2.boundingRect(contour)

       
        if w > 100 and h > 200:
            roi = gray[y:y + h, x:x + w]
            roi = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

            frame_counter += 1
            ocr_counter += 1 

            if frame_counter % text_detection_interval == 0 and ocr_counter % ocr_interval == 0:
               
                ocr_count += 1

                
                custom_oem_psm_config = r'--oem 3 --psm 11 -c tessedit_char_whitelist=0123456789'

                detected_numbers = pytesseract.image_to_string(roi, config=custom_oem_psm_config).strip()

                
                if detected_numbers:
                    detected_numbers_list.append(detected_numbers)

               
                if len(detected_numbers_list) > max_list_length:
                    detected_numbers_list.pop(0)

                
                if len(detected_numbers_list) == max_list_length and not final_output_printed:
                    most_common_numbers, _ = Counter(detected_numbers_list).most_common(1)[0]
                    print("Final Detected Numbers (after majority vote):")
                    print(most_common_numbers)
                    final_output_printed = True 


                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

   
    cv2.putText(frame, f"OCR Count: {ocr_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    
    cv2.imshow('Text Detection', frame)

 
    if cv2.waitKey(frame_display_delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
