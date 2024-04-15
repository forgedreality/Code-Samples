from tkinter import *
class ScrollTxtArea:
    def __init__(self, root, height):
        self.height=height
        frame=Frame(root)
        frame.pack(side=LEFT, fill=BOTH, expand=YES)
        self.textPad(frame)
        return

    def textPad(self, frame):
        #add a frame and put a text area into it
        textPad=Frame(frame)
        self.text=Text(textPad, width=1, height=self.height, font="Helvetica 12 bold", fg="#0478a5", padx=5, pady=5)


        # add a vertical scroll bar to the text area
        scroll=Scrollbar(textPad)
        scroll.config(command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set, state="disabled")

        #pack everything
        self.text.pack(side=LEFT, fill=BOTH, expand=YES)
        scroll.pack(side=RIGHT, fill=Y)
        textPad.pack(side=LEFT, fill=BOTH, expand=YES)
        return

    # formatting {  }
    def update(self, new_copy):
        formatting_char = "ß"
        ftext = new_copy.split(formatting_char)

        self.text.configure(state="normal")
        self.text.insert(END, "\n")

        if len(ftext) >= 2:
            bclr = "#fff"
            tclr = "#0478a5"
            for s in ftext:
                if len(s) < 1:
                    pass

                fclose = s.find("]")

                if s[0] == "[" and fclose > 0:
                    # remove formatting string
                    fstring = s[0:fclose+1]
                    s = s.replace(fstring, "", 1)

                    # get the RGB numbers
                    d = fstring[1:-1].split(",")

                    # convert them to int for use later
                    d = [int(n) for n in d if n.strip()]

                    # choose text color based on bg color
                    # tclr = "#eee" if sum(d)/len(d) < 127 else "#111"
                    brightness = ((d[0]*299)+(d[1]*587)+(d[2]*114))/1000
                    brightnessPercent = round(brightness/255*100)
                    tclr = "#fff" if brightnessPercent < 50 else "#000"

                    # create hex color string
                    t = ["{:02x}".format(n) for n in d]
                    bclr = "#" + "".join(t)
                    self.text.tag_config(bclr, background=bclr, foreground=tclr)

                self.text.insert(END, s, bclr)
                bclr = "#fff"
                tclr = "#0478a5"
        else:
            self.text.insert(END, f"{new_copy}")

        self.text.configure(state="disabled")
        # auto-scroll
        self.text.see("end")
