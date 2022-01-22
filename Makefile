%.html: %.md
	pandoc --standalone -c style/common.css -o $@ $<

all: slides.html

clean:
	rm -f slides.html
