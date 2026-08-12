---
video_id: N60WSQc-G_8
title: EEVblog #313 - Bus Pirate LCD Debugging
url: https://www.youtube.com/watch?v=N60WSQc-G_8
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 36, "3": 56, "4": 68, "5": 84, "6": 97, "7": 113, "8": 133, "9": 145, "10": 162, "11": 180, "12": 194, "13": 210, "14": 225, "15": 240, "16": 256, "17": 270, "18": 286, "19": 301, "20": 316, "21": 331, "22": 346, "23": 361, "24": 377, "25": 405, "26": 425, "27": 438, "28": 460, "29": 483, "30": 499, "31": 514, "32": 530, "33": 551, "34": 565, "35": 581, "36": 598, "37": 616, "38": 632, "39": 651, "40": 671, "41": 685, "42": 705, "43": 724, "44": 742, "45": 754, "46": 769, "47": 787, "48": 804, "49": 817, "50": 832, "51": 859, "52": 875, "53": 893, "54": 907, "55": 923, "56": 938, "57": 957, "58": 974, "59": 991, "60": 1003, "61": 1019, "62": 1035}
---

**Dave Jones:** Hi, I thought I'd do a little video on LCD. I've got here it's an 8 by 2 standard footprint LCD. It's from Newhaven display and I thought I'd just show powering the thing up and see what it looks like. It's a nice compact little 8

**Dave Jones:** by 2 LCD. It's actually upside down I believe. And I believe the text is showing this way. It's got a mounting bracket here. It's an industry standard footprint about 40 mm by 35 mm I think it is. Standard Hitachi uh

**Dave Jones:** sort of LCD pinout interface there. And this is the non-backlit version which is very thin. It's much thinner than the backlit one's about say that thick or something. It really is quite substantially thicker. So this is even got a transflective or more likely

**Dave Jones:** a reflective back in on it. And I've sold it normally it doesn't come with the pin header on there. I've soldered a pin header onto it. It's got standard mounting holes and these are available from every one hung

**Dave Jones:** low manufacturer on the planet. Eight characters by two lines. Really neat little compact display and this is actually a Newhaven one. There it is. It's an NHD 0208AZRNYBW.

**Dave Jones:** Um so I thought we'd power it up. Give it a go. Let's try it. And just to get this thing up and running really quickly with minimum amount of fuss I thought I'd use my Bus Pirate. Haven't used it before. I've got a Bus Pirate

**Dave Jones:** version 3.5. I think it's a slightly older model. It's available from Dangerous Prototypes. It's open source hardware. It's really good for you know decoding serial interfaces, you know, SPI, I squared C and all that sort of stuff. But it's got like built-in modes

**Dave Jones:** to drive LCDs and drive various you know dozens and dozens of types of chips. Really handy little device. It runs on a PIC 24. Um what is it? A 24 FJ64GA002 there. It's got a FT um 232 interface serial interface there.

**Dave Jones:** So, it's got, you know, the generic uh uh FT driver. And it's got a just a header on the output. And of course, this doesn't have enough pins to drive a standard LCD. So, uh you can get this uh

**Dave Jones:** companion board here, which is a which is the Bus Pirate LCD adapter. Once again, um I think maybe a new version is available. It's open source hardware CC-BY- SA. And um it just uh is has the standard interface

**Dave Jones:** for the HD44 um 780 LCD interface. But unfortunately, it doesn't um have a the dual in-line header pin header, which is what we need here for this LCD. So, I'm going to use a converter cable for that. I believe

**Dave Jones:** somebody's actually gone and made a new version of this cuz it is open source hardware. Would have been nice if it had like the dual in-line one and maybe like a couple of other flat flex ones as well, different pitches. But

**Dave Jones:** anyway, we can make do with this. It's got a 74 HC 59 5 on there. Serial to parallel converter. Really basic chip. It's got the contrast adjust. It's got everything we need. A couple of things for the backlight. We're not going to use the

**Dave Jones:** backlight, but this should be able to get our LCD up and running with minimum fuss. Let's give it a go. Haven't used this before. Should be interesting. So, I've just made up a converter cable here. Single in-line. I've soldered two

**Dave Jones:** headers back-to-back like that. And that just allows me to plug that directly into there. and this has got individual leads of course and I plug them in there cuz it's a standard pin out this pin out here from 1 through to

**Dave Jones:** 16 follows the pin out on here precisely. So that's you know it's really hard to goof up the pin out on that. So let's do it. Let's plug it into the serial port it uses a terminal program so we use Tera Term and try and talk to

**Dave Jones:** this and get a hello world running. Okay, I've got Tera Term here plugged in and it's set to 115,200 board on on the serial port which happens to be com 2 here and it's working just fine. You do question mark

**Dave Jones:** I'm talking to the device and there's all of the commands and various options. So now we can actually start talking to the thing we can go M for mode and it's got the various modes available as you can see one wire UART I

**Dave Jones:** squared C SPI you know two wire three wire and LCD. So we want number eight of course and we're we've got the LCD prompt here now. Excellent. So now we can use the capital these commands you've got to read the

**Dave Jones:** manual of course they're not obvious we use the W command for power on and if we have a look over here at the same time we should see so let's hit that and so let's have a look let's go here we go and power should

**Dave Jones:** switch on it does. There's the power so we're turning on power to the LCD and uh uh well we probably have to adjust the contrast pot and stuff like that. So let's try the contrast. It's not I'm turning it

**Dave Jones:** all the way one end and all the way to the other end this is on the LCD board and I'm getting nothing. So that is I think we have an issue there straight up something's going on cuz normally um would see all black

**Dave Jones:** characters come up when you apply power even then though you haven't um initialized the LCD and done stuff like that. So, would have expected to see all black characters on there. Um something's wrong. Bloody Murphy's Law. Nothing ever

**Dave Jones:** works first go. So, let's um I get let's see uh golden rule of troubleshooting, thou shall check voltages. So, I'm going to check pins one and two here, which are these two here, to see if we're getting voltage on

**Dave Jones:** our LCD here. Uh no. We're getting 0.5 vol- We're getting 0.5 volts. Um what? Fail. That should be uh 5 volts on pins one and two. So, let's That's ground and 5 volts there on our um Probably can't uh zoom in and get that

**Dave Jones:** at the same time. I won't bother, but let's have a look here. Ah, there we go. Not labeled on the back. Lovely. Love it. And uh that's ground and 5 volts. So, what? We are getting 5 volts. Um because,

**Dave Jones:** yeah, the power's switched on. We've got our V reg light We've got a power light uh LED there on, which indicates that power cuz this micro can switch power through to the output connector, and it is. But, we're not getting

**Dave Jones:** on here. What is going on? OH. OH, HANG ON. I think we have a trap for young players here. I'm suspecting this ribbon cable because it's supposed to be connected directly through. There's nothing but tracks on here. So,

**Dave Jones:** I think I've had this a dozen times before. I think our cable might be back to front. Might be swapped. I thought this was the cable that came with it. Um but it's um I don't think it is. Um let me

**Dave Jones:** let me check that. And yeah, I checked it and it does actually um it's it's been swapped. So, I've got another cable here. If we have a look at these two All right, hang on. Let's let's have a

**Dave Jones:** look at the difference on these two cables here. This is the one that didn't work. As you can see, it's uh pin one's here, pin one's there. Okay, and they've both got the notch over there like that. So,

**Dave Jones:** but if you look at this end the notches are different. This one has the notch on the outer side. That one's got the notch on the inner side. What? Fail. So, let's plug that in and see hopefully we haven't blown anything up.

**Dave Jones:** Probably not. Um So, now let's uh measure it. Well, might have something on the LCD. No, nothing yet. But let's measure pins one and two. And bingo, we now have 5 volts. Okay, so I unless this LCD is faulty

**Dave Jones:** we should, if we adjust this trim pot here see if I can get both on screen at once, we should get all black characters. Hey, there we go. There it is. Bingo. So, we've only got the one line, of

**Dave Jones:** course. So, we set our contrast just below where it sort of fades out like that. Oh, my notebook just shut down and switched off the power. But anyway, that should work a treat now. All right, one more time for the

**Dave Jones:** dummies. Let's give that a go again. Let's get back in here where all hunky-dory there. We need to get into the mode again. And uh let's get into LCD mode. We're in LCD mode. W, we'll hit that and we should see our LED here

**Dave Jones:** come on. Ta-da! Right, our power and we can just see the characters on the LCD there. Let me just trim that down just a tad.

**Dave Jones:** There we There we go. That'll do. Anyway, let's give that a go. Right, now um what we want to do now is go into the macro menu. So, we want to do a bracket zero like this. And that puts us into

**Dave Jones:** uh the macro uh various macro options. And uh that's the thing. This is pre-programmed into the uh Bus Pirate for um you know, testing LCDs and for other uh items, you know, for the SPI and I squared C and all that sort of stuff,

**Dave Jones:** but we're in the LCD menu and we can just go LCD reset. So, I believe we have to do one bracket. And yep, we've reset. And uh let's do init LCD. So, we need to do Sorry, two. Okay, bracket, which I like means

**Dave Jones:** command. Now, display lines, one line or multiple? Well, we got two lines, so we want to do two. Multiple init. There it is. Um it should be ready. There we go. Bingo! We've got our cursor. There you go. It's working.

**Dave Jones:** Um so, I I am pretty darn confident now that if we just um send this um characters and strings, they will be displayed on the LCD. So, we can do that directly according to the example EEVblog as a string like that. Otherwise, we can

**Dave Jones:** send a direct ASCII character just by typing in its value. So, EEVblog and it should pop up. Ta-da! Look at that. Too easy. How easy was that? Once we sorted out the stupid issue with the cable there, it works a

**Dave Jones:** treat. And it should in theory work for every you know Hitachi compatible LCD on the market. There are various slight subtle differences between them sometimes and I have encountered where you know I'll have 10 brands work with code and you

**Dave Jones:** think it's rock solid and then there's another one which is supposed to be compatible, but it just doesn't work due to some you know minor little difference, but pretty much you know 90 or 99% of them on the market are going

**Dave Jones:** to be compatible with this code. So, that's brilliant. And if you want to write something to the next line, presumably we're able to do that. Now, we can't just you know do hello world for example and have it

**Dave Jones:** wrap around because these the chipset for these LCDs is designed for 40 character display regardless of even if it's a tiny little eight character one like this. The chipset, the memory map in the chipset is the same across all the different

**Dave Jones:** LCDs and it has a maximum of 40 lines. So, what we need to do is we need to I think we can call up the macro menu again and here it is cursor position. So, this is what we want. We

**Dave Jones:** want four and then we want the cursor position. So, we can't just do cursor position nine and expect it to wrap around to the next character. It's not going to do it. It's going to display 40 and it will zero to 39 and the 40th one

**Dave Jones:** will be this first one. So, if we go 40 like this, we should see the cursor jump to bingo. We do. It's all working as expected. Brilliant. Is bus pirate a I'm liking this. It's a real easy way to

**Dave Jones:** experiment with LCDs. And then we can of course go uh EEVblog and let's do Sagan Whoop. Position in degrees. No. Whoa, what's that? {Exclamation mark} was probably bad. Whoop. That's horrible. Okay. Whoop. No, something's gone horribly wrong here. Let me check.

**Dave Jones:** No, servo active. Oh, god, I've done something horrible here. No, I shouldn't have uh Shouldn't have uh because I forgot to put the quote marks in. I'm a I'm a dumbo. PWM disabled. I've gotten into some PWM mode. There we go. Go figure.

**Dave Jones:** We're back to the LCD command. All right. Sagan {exclamation mark} quote bang. There it is. Winner. I like it. All right. And we can just type in characters directly. So, let's type in one and that will send one as the ASCII character one

**Dave Jones:** and let's see what we get. Hey, there we go. We just got a custom character by the looks of it. So, let's clear that. What's the command for clear again? Was it three? Three, there we go. Bang, and it's reset

**Dave Jones:** and homed our cursor. So, we can just type in one like that and it and it writes as you can see it writes the one there and it puts in the custom character down there because this is not part of the regular

**Dave Jones:** Uh No, well, it's yeah, it's just putting in, you know, dummy stuff. But, if we go, you know, 50, that's, you know, ASCII for 50. There it is. Bang. So, we can write directly, um, you know, ASCII characters in like that, or we can

**Dave Jones:** just do the string, of course. So, hello. And then we'll go four 40. We've got to do a hello world. Otherwise, it's not a proper test. Uh 40, yes. And then quote marks, hello world. Do we want the

**Dave Jones:** exclamation mark or not? Let's put in the exclamation mark. Hello world. There it is. Beautiful. I like it. And, uh, this LCD seems to be quite good. I like it. Uh, it's not the best, uh, light here, but that's, you know, it's a

**Dave Jones:** bit glarey, bit reflective, bit dark when I turn it down like that. But, the contrast on this Newhaven display is, uh, is pretty good. I rather like it. This is the non- backlit version. And, uh anyway, I think it's going to work out

**Dave Jones:** Well, this, uh, four-man is going to work a treat. I won't use the Newhaven one, cuz they're, uh, fairly expensive compared to what you can, uh, get them, um, in, uh, other brands. But, uh, I had this one, so I thought I'd, uh, try it

**Dave Jones:** out. And they're a nice little compact format LCD. I really like them. Uh, 40 mm by 35 or so. And, uh I would recommend I think they're 8 mm, um, thick in like from the back of that, uh, bracket there to the front. So,

**Dave Jones:** quite low profile. And, uh, you can get them for only a couple of bucks each in significant quantities, anyway. So, really neat little display. Anyway, I hope you like that. That's, um, some little LCD testing with the Bus Pirate.

**Dave Jones:** And if you want to discuss it, jump on over to the EEVblog forum and uh please give it a thumbs up if you like it cuz that helps a lot. Catch you next time.
