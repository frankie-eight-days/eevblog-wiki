---
video_id: AWlRGLxm7nc
title: EEVblog #267 - Voltage Detection Stick Teardown
url: https://www.youtube.com/watch?v=AWlRGLxm7nc
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 46, "3": 66, "4": 81, "5": 101, "6": 116, "7": 131, "8": 146, "9": 171, "10": 186, "11": 206, "12": 221, "13": 236, "14": 261, "15": 276, "16": 296, "17": 321, "18": 346, "19": 366, "20": 386, "21": 406, "22": 426, "23": 446, "24": 471, "25": 486, "26": 506, "27": 536, "28": 556, "29": 581, "30": 606, "31": 626, "32": 641, "33": 661, "34": 681, "35": 701, "36": 726, "37": 746, "38": 766, "39": 791, "40": 811, "41": 826, "42": 851, "43": 871, "44": 896, "45": 916, "46": 941, "47": 956, "48": 981, "49": 1006, "50": 1026, "51": 1046, "52": 1066, "53": 1081}
---

**Dave Jones:** Hi, welcome to another Teardown Tuesday, where I tear stuff down so you don't have to. But, I know you still want to, because it's cool, it's fun. Ha ha! So, what have we got? We've got one of these voltage detection sticks. Let's check them out, see how they work, see what's inside.

**Dave Jones:** And you know what we say here on the EEVblog, don't turn it on, take it apart. But... Hmm. I don't see any screws. Could require a little bit of persuasion. Hmm. Let's go. And of course these things come in many different brands, but they're all

**Dave Jones:** generally this stick type thing. They've all got a pocket clip up here for your average nerd who wants to stick it in their pocket. And this is the Fluke Volt Alert here, but we're not going to look at that one today. What we're going to tear down is this ideal brand, Volt Aware.

**Dave Jones:** And this Volt Aware one is a basic twist-on, twist-off type. It's Cat4 rated. It claims to have a detection range of 40 to 1,000 volts AC. Turns the beeper on and off, and it comes with all sorts of standard-y goodness as well, ULC rated, and stuff like that.

**Dave Jones:** Let's see if we can take this thing apart. Now this is the twist-on, twist-off type, but you just, it's not really obvious how to take the thing apart, but you just pull it like that, and it's got these guide channels down in there, and a mating little bump down in there which sort of

**Dave Jones:** slides the two halves. And of course it's powered from two AAA batteries. Don't need those, and there won't be anything in there. So all of our electronics is down in there, and there won't be much. I can sort of see through the transparent

**Dave Jones:** end there, you can see that there's a little tiny board, it'll probably have one chip on it, couple of passive components, and there's the sensor probe out the front there, it's just a flat bit of metal there, and well, we'll have to apply some force to get this sucker open I think.

**Dave Jones:** And you can see that the battery contact there, when it slides in to there, it actually makes, when you twist it, it makes contacts with one of those internal pads down in there. So that's a rather neat little solution, I don't mind that at all.

**Dave Jones:** First thing we're going to try is I see these little holes around here like this, maybe we can get a screwdriver in there and pry it off perhaps. That would be one of my first guesses. I'm not having much luck prying this thing open, I'm not sure how they've assembled it, whether they've

**Dave Jones:** this is sort of, this plastic end is sort of really snapped on first, then they insert the PCB and it locks in place. I've tried to pull the board out but, with a pair of long nose pliers, but that's rather tricky, so I'd probably ordinarily get the Dremel

**Dave Jones:** out and drill right around there, just grind it around and cut it off, but that's, the Dremel's not in the lab at the moment, so just get some side cutters and try and compensate. Ah, this is ugly. Excuse me. Wow, well that was really thick

**Dave Jones:** plastic around that thing, and it was quite messy, but there you go, there's two chips, so I'm going to wiggle that board out, which is the official technical term for it, double-sided load, look at that, it's rather interesting. Hmm, I like this one.

**Dave Jones:** Let's see if we can get the board out. Well that was wedged in there really well. Let me tell you, I had to cut away the plastic, but it looks like it's going to pop out like that. Hey, that's a rather neat solution.

**Dave Jones:** I really like the design of that. So I suspect these ones are a little bit more advanced than just a basic electrostatic digital detector that just detects the electrostatic field. It's still detecting the electrostatic field around a wire with the probe tip and a high impedance input,

**Dave Jones:** but there's probably some smart filtering or something going on in there, and maybe even a custom device to actually do it. Why else would you rub the numbers off? I don't know, maybe it is incredibly simple, but they just want you to think it's complex.

**Dave Jones:** Hmm, who knows? And here's the board under the microscope. I'll attempt to do this, sorry, I'm actually hand-holding my little compact camera at the moment against the stereo microscope, so this is really hard, it could fade in and out, but look at that!

**Dave Jones:** They've gouged out that chip that obviously connects to the antenna there. It's got the date code 1009C, I'm presuming that's the date code, the 9th week 10, but they've gouged out that IC! The bastards! So we can't tell what that is. And maybe we can get a closer view of the LED there.

**Dave Jones:** There we go. That's one of those 4-pin square packages, it's a red-green combined dual colour LED, and of course they've got one top and bottom, which of course allows the light to show out both sides of the module itself. So that's really rather nice, there's a tactile switch there, there's

**Dave Jones:** another IC there, and that one is unbranded. It's got regardless of the angle, I cannot see any branding on that chip at all. And check out that bodge resistor with the 302 on it there, that's a nice little bodge. That one, they've got a transistor or something

**Dave Jones:** there in that SOT 23 package, and there's the buzzer there, which is rather nice, it's round and it's sunken into the board like that. They've put a cutout, and they've got two pads on the end here where it connects in. That's a nice bit of

**Dave Jones:** mechanical design engineering. They've got a couple of more passives up near the antenna up there. Don't know the topology of this thing, but it's obviously detecting the electrostatic field, and there's a couple of diodes, I'm presuming that they're diodes there, those black ones, and that's it.

**Dave Jones:** There's some passive devices, and very disappointing, I was hoping to trace out this board, I really was, I was hoping that we'd, it'd be like a, you know, a really easy double-sided we'd be able to trace it out, it'd have the part numbers on it, it'd use some identifiable

**Dave Jones:** ICs, and those passives around the front end there, no surprise at all, you'd expect because this is an electrostatic detector, you'd expect some very high value resistances there, and that's exactly what we see. See the T226 up there, that's a 22 meg resistor, 395, you know, 3.9 meg, and

**Dave Jones:** there's another 4.7 meg and a 470k, so no surprises there at all. The 226 up there, the 22 meg, that'll most likely be in series with the probe tip. They're going into the detection IC on the bottom of it, this gouged out thing here, and yep,

**Dave Jones:** what that one is, I don't know. Your guess is as good as mine. And my guess for this input chip with the numbers rubbed off was going to be a Schmitt trigger, just a Schmitt trigger, logic gate device, like a 7414 or something

**Dave Jones:** like that, or a 4000 CMOS equivalent device, because this is a very common technique for using electrostatic sensitive touch switches and things like that. You can do it with just a Schmitt trigger. So I did a bit of a patent search here, and I came up with this

**Dave Jones:** United States patent number 5,103,165 from the April 7th, 1992, and it's from a James M. Surratt from Raleigh, North Carolina and I presume he worked for Static Control Components Inc. And they, it was filed in 1990 and was granted in 1992. And let's take a look

**Dave Jones:** at it. It is, well, the name of it is Insulated Handheld Non-Contacting Voltage Detection Probe. And bingo, that's pretty much exactly what we've got here. And it's the pen-style probe, it's even got the pocket clip on it. But most importantly, if we go down,

**Dave Jones:** bingo! We've got a schematic. Let's take a look at it. And what we've got down here, if you decode all the patentees, you eventually find the part number for the IC, and it's an MMN14584 which is a standard CMOS Schmitt trigger. So you could use like a 74HC14 or another

**Dave Jones:** 4000 series equivalent or something like that. It's probably not that fussy, although you might have to tweak the values for the individual device. Actually use the particular brand and model number, but it's basically just that. It's a Schmitt trigger. And here's the waveforms here, and it's got another schematic

**Dave Jones:** there, but here's the main schematic. So basically, and it's a 14-pin chip. And if you remember the look at the photo for our board, it's also a 14-pin chip. I don't think it's a coincidence. They're probably most likely using this same circuit here, and they've probably got a resistor on the input.

**Dave Jones:** It shows the antenna connects directly to pin 1, which is the input on one of the HEX Schmitt inverter gates. But I'd say they've probably got a resistor in series, they've got another resistor going to ground, and the output goes through the cap.

**Dave Jones:** So we might need to redraw this thing a little bit, just to make it a little bit clearer. But I think we might have the basic operation of the front end here. And here's this same circuit, but redrawn in, ta-da! DaveCAD. And what we've got here is up in the top left, we've got our antenna input.

**Dave Jones:** It's exactly the same circuit as before, except I've redrawn it with the Schmitt inverters in there instead of just the block chip, which doesn't make it very descriptive at all. You've got to sort of fill in the blanks there. It's not as easy.

**Dave Jones:** This one's a bit easier. Anyway, we've got our antenna input here, we've got our voltage detection, well, antenna, probe, whatever you want to call it. We've got just a simple voltage divider here. The value of that voltage divider will be set dependent upon the input voltage range you require, and the

**Dave Jones:** threshold voltage of your Schmitt inverter here. And then it's AC coupled and pulled high, and then that's for basically when there's no input voltage there. So it's pulled high, and then the input to this Schmitt inverter goes into this diode and resistor and cap arrangement here, which sort of

**Dave Jones:** smooths out the AC voltage and then puts it through another couple of Schmitt inverters and turns on the transistor. So basically the output transistor and this LED turns on when the input voltage from the antenna is above a certain threshold there. And that's all there is to it.

**Dave Jones:** It's pretty darn basic. If we take a look at the waveforms here from the patent, we can translate those to the Davecad schematic, and I've labelled them exactly the same as the points on the waveform. So point A is our AC input, and that's a reduced

**Dave Jones:** voltage input dependent upon the voltage divider there. And B is of course the squared up input, because that's what a Schmitt trigger does. A very slow-changing, varying input signal as it transitions through the Schmitt trigger threshold levels squares up the input. So you sine wave in and you get a square wave out, assuming it meets

**Dave Jones:** the threshold voltages. So what's point C here doing? Why have this resistor and cap at all? It doesn't seem to make much sense, because if you look at signal D here, this output D is just an inverted signal of point B here. And if you are talking about the 50 Hz signal

**Dave Jones:** and these values are set at a specific design value, then that's exactly what you're going to get. B and C, you can actually do without those components, assuming that the input is exactly on frequency and exactly doing the right thing that you want to actually detect.

**Dave Jones:** And it probably doesn't make much sense at the moment, but it might when we start looking at further on with what's happening with point E here. Because if, let's say we've got a very low frequency input, a low frequency input lower than our detection frequency, then C, if you look at this

**Dave Jones:** discharge curve here, it won't instantly go back there, it'll go through both thresholds, and that'll change the output waveform D to be different from just an inverted version of input signal B here. And that will start to affect the smoothing value that we'll look at

**Dave Jones:** in part E here. So we get our output signal D, which is a square wave, once again based on our input 50-60 Hz waveform, and it just smooths it out between the threshold voltages of this Schmitt inverter down here, based on the value of these two resistors need to be set, just to put it smack in the middle

**Dave Jones:** of the threshold voltage. So once the input goes above a certain level, and that's to get rid of any issues with like a duty cycle, if noise does get through and it's not the correct duty cycle, then it probably may not actually reach the threshold voltages or something like that.

**Dave Jones:** So that's just another mechanism to sort of filter things out a little bit. And then it double inverts that, or buffers it, to drive the output transistor which drives the LED. And that's pretty much all there is to it. And that is the basic operation of one of these voltage detection sticks.

**Dave Jones:** Check out this, you're going to love it. Next to 10 here is what it says. Figure 8 may use circuit parameters as follows. The diode is a 1N 4148. Fair enough. Transistor is a BC847. Fair enough. LED is a whatever. But look at the resistor values.

**Dave Jones:** R1, 18.5 milliohms 65 milliohms, 200, 65, 10 milliohms for R6. Gotta be shitting me. This thing's going to have a hell of a hard time working with resistor values in the order of milliohms. So clearly what's happened here is the Payton attorney who wrote this

**Dave Jones:** translated the good circuit description into Paytonese garbage like this, has thought that megohms means milliohms. The megohm symbol must equal milliohms. So I'm going to write milliohms in there. And well, it's not going to work at all. And clearly the guy who actually designed this thing hasn't checked it because

**Dave Jones:** that's a glaring mistake. It's ridiculous. So what's with the second chip on the board? Well, that one is probably just to drive like a pulse stretcher latch kind of thing to drive the buzzer and the LEDs in the intended way for this particular product.

**Dave Jones:** But I think it's probably using this basic front end, or maybe a slight variation of it because it matches up. I haven't actually traced out the PCB yet and I probably don't bother because I think it's probably going to use this circuit or a variation

**Dave Jones:** of it. And there you go. That's the ideal volt alert voltage stick. Probably most voltage sticks are going to work in a very similar way with a similar front end like this. So if you have any better information on exactly how these things work, or maybe even some alternative chipsets, some

**Dave Jones:** specialized chipsets on the market that might be able to do it, or some other patents, jump on the forum and share them with everyone and we can all discuss it on there. So there you have it. If you like Tear Down Tuesday, give the video a thumbs up, that helps a lot.

**Dave Jones:** Don't know what we've got in store for next week, but waiting's half the fun. Catch you next time.
