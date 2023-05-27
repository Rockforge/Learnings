(let ((zebra "stripes")
      (tiger "fierce"))
  (message "One kind of animal has %s and another is %s." zebra tiger))

(let ((birch 3)
      pine
      fir
      (oak 'some))
  (message
   "Here are %d variables with %s, %s, and %s value."
   birch pine fir oak))

(message "The name of this buffer is %s" (buffer-name))

(defun add-2 (a)
  "Add numbers a and b"
  (interactive "p")
  (message "the result is %d" (+ a 2)))

; The %d and %s are control sequences or format specifiers
(add 10 10)
