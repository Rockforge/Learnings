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


(if (> 4 5)
    (message "4 falsely greater than 5")
  (message "4 is not greater than 5"))

(defun type-of-animal (characteristic)
  "Print message in echo area depending on CHARACTERISTIC"
  (if (equal characteristic "fierce")
      (message "it is a tiger!")
    (message "it is not fierce")))

(type-of-animal "fierce")
(type-of-animal "striped")

(if (eq nil ())
    (message "They're the same")
  (message "They're not the same"))

(setq true "Hello")
(set 'hello "hello")


(point-max)

(message "we are %d characters into this buffer."
         (- (point)
            (save-excursion
              (goto-char (point-min)) (point))))
(point)

(defun my-double (number)
  "Double the number passed"
  (interactive "p")
  (message "The number is now %d" (* number 2)))

fill-column

(defun check-fill-column (number)
  "Check if the number passed is greater than the fill column"
  (if (> number fill-column)
      (message "The number is greater than fill-column")
    (message "The number is not greater than fill-column")))

(check-fill-column 90)

(defun hello ()
  (message "Hello world"))

(describe-function 'hello)

(defun simplified-beginning-of-buffer ()
  "Move point to the beginning of buffer;
leave mark at previous position"
  (interactive)
  (push-mark)
  (goto-char (point-min)))


(defun append-to-buffer (buffer start end) ;; Make a function definition with the name append-to-buffer, then have three arguments
  "Append to specified buffer the text of the region. ;; Documentation
It is inserted into that buffer before its point.

When calling from a program, give three arguments:
BUFFER (or buffer name), START and END.
START and END specify the portion of the current buffer to be copied."

  (interactive
   (
    list
    (
     read-buffer
     "Append to buffer: "
     (other-buffer (current-buffer) t)
     )
    (region-beginning)
    (region-end)
    )
   )

  (let
      (
       (oldbuf (current-buffer))
       ) ;; varlist

    (save-excursion ;; body
      (let* ((append-to (get-buffer-create buffer))
             (windows (get-buffer-window-list append-to t t))
             point)
        (set-buffer append-to)
        (setq point (point))
        (barf-if-buffer-read-only)
        (insert-buffer-substring oldbuf start end)
        (dolist (window windows)
          (when (= (window-point window) point)
            (set-window-point window (point))))))))
(defun simplified-end-of-buffer ()
  "Goto the end of buffer"
  (interactive)
  (push-mark)
  (goto-char (point-max)))


(defun is-this-buffer (buffer-name)
  "Check if the this is the buffer"
  (if (eq (current-buffer) (get-buffer buffer-name))
      (message "They're the same")
    (message "They're not the same")))

(is-this-buffer "learning.el")
