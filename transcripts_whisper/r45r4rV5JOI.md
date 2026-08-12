---
video_id: r45r4rV5JOI
title: EEVblog #1141 - Padauk 3 CENT Micro - Programmer
url: https://www.youtube.com/watch?v=r45r4rV5JOI
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 21, "2": 37, "3": 56, "4": 72, "5": 91, "6": 109, "7": 123, "8": 143, "9": 157, "10": 168, "11": 185, "12": 199, "13": 220, "14": 235, "15": 250, "16": 264, "17": 282, "18": 294, "19": 315, "20": 330, "21": 345, "22": 361, "23": 380, "24": 398, "25": 418, "26": 431, "27": 444, "28": 462, "29": 480, "30": 494, "31": 510, "32": 527, "33": 543, "34": 563, "35": 578, "36": 601, "37": 614, "38": 637, "39": 653, "40": 675, "41": 694, "42": 712, "43": 738, "44": 757, "45": 776, "46": 793, "47": 810, "48": 822, "49": 841, "50": 856, "51": 872, "52": 888, "53": 901, "54": 921, "55": 936, "56": 951, "57": 969, "58": 989, "59": 1006, "60": 1022, "61": 1038, "62": 1051, "63": 1071, "64": 1091, "65": 1106, "66": 1122, "67": 1137, "68": 1152, "69": 1166}
---

**Dave Jones:** Hi, in a previous video we took a look at this Padauk in-circuit emulator for these 3-cent microcontrollers. So I thought we'd now have a look at, and we got a program running on our 3-cent microcontroller, but it was actually on the in-circuit emulator, which is close enough, but it wasn't actually the real deal.

**Dave Jones:** So I thought we'd now try the programmer and see if we can actually program a chip. What we're going to do is we're going to program the PMS154C. This is actually not a 3-cent micro, it's actually about 5 cents or maybe a bit under in volume

**Dave Jones:** because it's the bigger cousin to the PMS150. It's the same series, but it's got twice the memory in it. It's also got three 11-bit PWM modules, which is fantastic, plus two 8-bit timers as well. So this little SO8 chip, for 5 cents or less,

**Dave Jones:** has, I believe, five PWM modules in it. Fantastic. It's got a couple of other things, I think a comparator and a LCD bias generator, so you can generate a bias if you're driving a tiny little custom LCD display or something like that. It's not a full-on LCD module, but it's got a little DC bias generator.

**Dave Jones:** Cool! Anyway, so we're going to program one of these on a real chip using the Padauk programmer, which they kindly sent to us. So, updates from the previous video. So, updates from the previous video are that, yes, you can actually get these chips pre-programmed.

**Dave Jones:** You can't do it directly from Padauk, but their official suppliers, which are linked in on their website, they're all Chinese suppliers, so it may not be the easiest place to deal with, but they will actually program these for, like, I believe it's at, like, 0.2 cents each or something like that.

**Dave Jones:** So they will program, and LCSC have kindly offered, for a limited time, I believe, to program them for free for people. I'm not sure of the minimum volume. You're going to have to contact them and all that sort of stuff, but I believe that they will program.

**Dave Jones:** They've extended the offer. They've offered pre-program them in bulk for me, and they've also extended that offer to my audience as well. So I'm not sure how long that's going to last. Anyway, you can get these things programmed. So, obviously, you know, the whole value proposition of a 3-cent microcontroller,

**Dave Jones:** sub-3-cent microcontroller, is that you don't... you don't program with one of these. You need to get them programmed from the factory, in the tubes, or on the reels, or whatever, and then you populate them, pick and place, straight onto your projects, because these are one-time programmable,

**Dave Jones:** so you wouldn't build in, like, a connector to program them onto your board, or even pads or anything to program onto your board. You get them programmed in the tube. As I said in a previous video, it's really easy to validate and qualify,

**Dave Jones:** like, a small microcontroller for a specific niche application like this. You know, you can test it over voltage, and temperature, and you can test and inspect the code line by line, and you can ensure that there's no bugs and stuff like that. So you can be pretty confident in getting, like, a whole reel of these, you know,

**Dave Jones:** many thousands of these actually programmed, and it doesn't cost much at all. Even if you do goof it, well, what's it going to cost you? You know, 50 or 100 bucks or something for a whole reel of these things. Now, the other thing is, a lot of people are questioned, of course,

**Dave Jones:** the 3-cent micro with the 60 U.S. dollar or 100 U.S. dollar, depending where you buy it from, programmer, and the match-in 60 or 100 dollar in-circuit emulator. Now, of course, if you're going to develop with these chips, get the in-circuit emulator. It's an incredible value, and it's, you know, it's super valuable to do that.

**Dave Jones:** But, of course, you wouldn't, you know, for, like, small one-off stuff, yeah, get the programmer. I think it's good value, but a lot of people question, "Okay, it's a bit expensive for these 3-cent micros," and fair enough. So a lot of people ask, "Well, can we actually reverse engineer?"

**Dave Jones:** And, like, open-source the whole thing and maybe program it with an Arduino. You know, everyone's got one of those, so they can just hook the chips up and stuff like that. And I asked Paduk, and they said, "Look, there's a lot of complex algorithms in there,

**Dave Jones:** a lot of not-just-digital thing. There's lots of analog voltage-level stuff. There's lots of compensation that they do and other timing-type stuff." And they said, "Sorry, we're not going to release the programming information for the chips." So that's a bit of a bummer, but, hey,

**Dave Jones:** I can understand that they recommend that you use the proper programmer or the programming services of their official suppliers, because they've got the big automated machines that take all the chips and untube them and unreal them and then, like, program them in a bulk thing, and then they'll re-real them or re-tube them for you,

**Dave Jones:** ready to put, populate onto your boards. So I'll leave that as a separate video today. We're just going to program a real chip, and we'll put it onto a breadboard, and we'll flash a real lead on a real chip. Not on this in-circuit emulator.

**Dave Jones:** Rubbish. So, thankfully, I've gone through all this before, so this will be a summary. Right, what I've done is I've changed the project from the last video. It is now using the 154C chip, and the software's actually quite smart. If you want to change the chip that you're actually using, just go to your .pre file here,

**Dave Jones:** and you actually just, like, literally change it from 150 to 154. That's what I--we used the 150 last time, we're using the 154 now. And it automatically changes. It automatically detects that you've actually changed that, and it actually chooses the new include file,

**Dave Jones:** when you--next, when you go to build the thing, it actually changes the include file for you. It's actually very smart, and a lot of people were very impressed by this Padook software, and I continue to be very impressed, and the programmer software is actually pretty good as well.

**Dave Jones:** It's a bit quirky, but the documentation is usable, and it's quite nicely integrated for the single 3 meg executable for this, it handles--it's a separate executable for the programmer, as we'll see, but it's really nicely integrated. Anyway, that's all we had to do.

**Dave Jones:** There was a difference--I'll show you right now, actually. If we have the 3 volt low voltage dropout like we did last time, and then we actually compile that, you'll see that it gives us an error, LVR error. LVR must be greater than 3.5 volts for sysclock onto IHRC onto clock source that we're using.

**Dave Jones:** So that's interesting that there's a difference in that between... the 150 and the 154, which is exactly the same family chip, except that it's got like double the memory and a few extra features. So yeah, that's interesting. So we just change that to 3.5 there, and we just build it again,

**Dave Jones:** and Bob's your uncle. Look at that. Fantastic. So there's all our--it's compiled, everything's happy, this chip has twice the memory than what we got in the previous one, hex 7E8, 97 hex of that, 751 hex free, convert that to decimal for all you decimal fanboys,

**Dave Jones:** and we've got double the amount of RAM in here. We've only used 4 bytes out of our 128 byte RAM. So we've got double the RAM of the 64 in the 150 series. And a lot of people talked about this in the comments to the--

**Dave Jones:** and on the forum to the previous video. A lot of people mentioned, well, like a GCC might be a solution. You're right, a GCC version of, you know, to support the Padauk architecture. And, well, that should be okay, but a lot of people pointed out,

**Dave Jones:** that the GCC compiler isn't really optimized for the-- the really small memory architectures on these real low-end microcontrollers, and they've given examples of other 805, 108, other PIC stuff people have tried to target with the GCC compiler before, and it's done a pretty terrible job of it.

**Dave Jones:** There are other compilers and stuff like that for it, but basically, yeah, like you could probably do it, but because it's a small amount of memory, limited stack size and stuff like that, so if you get-- if you get a compiler, C compiler that's not optimized for these really low memory

**Dave Jones:** amount of SRAM architectures like this, not about code size, it could be about SRAM, so, you know, if you've got a lot of stack and stuff like that, a lot of routines that need to push stuff onto the stack, you could chew up your memory quite fast if your compiler's not optimized for it,

**Dave Jones:** so it's probably better to use the Padauk Mini-C, as they call it, or the Padauk Assembler, but the Mini-C seems to work just fine. You're actually going to get much, if anything, like code optimization for going for the Assembler over the Mini-C here,

**Dave Jones:** but, hey, we haven't actually evaluated that yet. So we've got exactly the same code as last time, and we're just going to flash a LED. So we've compiled our thing for our 154C target. So there you go, we've got the 154C SO8 chips.

**Dave Jones:** We've targeted those in here, and it's all compiled. Now, what we can do now is call up the programmer, so we'll turn on our program here, initializers, everything's like a bit of a shift. We'll go into all this shift stuff in a minute.

**Dave Jones:** We'll plug it into our USB port, and testproject.pdk. I think it's already stored in there. It could be non-volatile, stored in there from our previous attempt at this. Anyway, we can go in here, we go to the OPT writer, so we've built our project,

**Dave Jones:** it saves it as a .pdk file, so it's not Intel HEX or anything like that. So if we have a look at the .pdk file it produces here, it is like a binary file, it contains all the stuff, it contains the information on the chip,

**Dave Jones:** and everything used, so it doesn't look like an Intel HEX equivalent format. Anyway, this is what the writer uses, so if we go into our OPT writer here, let's load it up, ta-da, and let's have a look. Now, we can, let's actually load our file in here, testproject.pdk,

**Dave Jones:** so open it up, and we're in, it's verified, it's talking to the unit, everything's hunky-dory, and it actually shows you on there that it's the PMS154C, so it already knows, you don't have to select it in the software, it's all embedded in the file,

**Dave Jones:** gives you the checksum and all that sort of stuff, and I see shift, for a 14-pin, it's 1. I see shift thing. Now, what it is, is that it says check jumper here, so this S16, that's an SO or DIP16, basically what it means is put it in JP2.

**Dave Jones:** Now, if we have a look at the back of this thing, this is JP2 in here, it's telling us to use JP2, this is actually a jumper actually provided, like it shorts out all the pins, it was originally on this one over here, so it tells you for this particular chip, move it over to JP2 here,

**Dave Jones:** you've just got to reconfigure it, it basically just reconfigures the pins for the zero insertion force, the ZIF, or text tool socket. Now, because we've got different types of chips that we could potentially program here, so a 16-pin one, a 14-pin SO, a 10-pin MSOP package, or an 8-pin SO, which we've got here,

**Dave Jones:** or even a SOT236, which I've also got, but I don't have the right adapter yet, I can bodge one up, I've got the SO8, so we have to shift, here's our little adapter, focus you bastard, alright, here's our little adapter, if you haven't seen these before,

**Dave Jones:** they're a zero insertion force socket, and they've just got the pins in there, you can see those move in and out like that, and that allows you to get your little, just dropped an SO chip, it's gone into the carpet, luckily, I've got a few, so, let's just get another one,

**Dave Jones:** I just wasted another four and a half cents, or whatever. Anyway, the little SO8 chip will then go inside our nice zero insertion force socket there, lovely. So there's our chip inside our socket there, and this is what it means by shifting, because they're different pinouts on the chip, we have to actually, it says shift four,

**Dave Jones:** so we need to go to the fifth pin down for this SO one. So there we go, we're now in the fifth pin down like that, so that's what it means by shift on that instruction there. Okay, so now we've put our file in there, now we've got other stuff, here's the date, here's the sysclock,

**Dave Jones:** so all this stuff was imported in that PDK file, so the integration between the programmer software and the IDE interface is really quite nice, like, Padauk have done an awesome effort, a lot of people were impressed by the IDE, and rightly so, the integration with the programmer software, whilst a little bit quirky, is really quite good,

**Dave Jones:** and they do have English documentation for the programmer, which is, you know, it is really just fine. So our sysclock, 16 megahertz on two, we don't have our write protector or anything like that, and our LVR is 3.5 volts like we changed before, so let's just do blank check now, shall we?

**Dave Jones:** Will it work? Pass! I see blank, there you go, no problems whatsoever. Oh, the NG on there, the one NG I accidentally pressed wrong, press the button, NG is no good. Now we've got a rolling code system here, which allows you to put a serial number into, embed into the chip,

**Dave Jones:** I'll show you this in the documentation in a second, but it's not supported because we haven't enabled it in the IDE. So if we have a look at our programmer manual here, which has still got some Chinese stuff in it, but it's still, it's pretty good.

**Dave Jones:** This seems to be a discreet, like, old version of software in here, the engineering type and simple type and stuff like that, but, it's pretty comprehensive, I like it, so it's pretty impressive. Rolling code, here it is, so we can start the relevant settings about rolling code,

**Dave Jones:** so there are three locations in memory there, 3FC through to 3FA, and presumably your program can read those back if you need to, but it can put a, basically a three byte rolling serial number code in there as you program, so each chip can get a unique ID.

**Dave Jones:** So that's a real nice little feature, and here we go, they explain the jumping, and stuff like that, how you have to shift them, and then shift it down by one if you've got the 14 pin, so if you've got the 16 pin package, you don't shift anything, if you've got the 14 pin package,

**Dave Jones:** you shift down by one, if you've got the 10 pin one, you shift down by two, and if you've got the 8 pin one, like us, you shift down by four, or something like that. So it is, it is pretty comprehensive, I like it, and I like the fact that they've got a 10 pin MSOP package as well,

**Dave Jones:** because that, you know, if you need an extra two pins, but you don't want to go to the, you know, the full 14, or 16 pin version, that could be, that could be very handy indeed. But look, like, it's nice, it's got nice drawings of how everything goes up, so it's all about like the PA,

**Dave Jones:** there's like four programming pins on the Padook chips, so they've got kind of a common pin configuration, but you do need to shift them in the programmer, which is fine, so, and check this out, you can get what's called a customer package, you can add your own package to this thing, so that's why if you go

**Dave Jones:** convert PDK here, to package, you can actually generate a, well, yeah, I haven't actually done it yet, but it is in the software here, which shows that you can actually define your own package, so if you wanted to have your own, like, custom header on a board, or something like that,

**Dave Jones:** if you really wanted to, it defeats the purpose of the 3 cent micro, but anyway, because the connector costs more than the micro does, anyway, you could define your own package, or do whatever, and it looks very powerful. So, you know, that's, that's really quite impressive.

**Dave Jones:** So, there you go, they've gone to the effort to, you know, do customized packages and things like that, they've really, you know, they've really thought about this stuff, so there you go, there's the in-circuit programming thing, it hooks up to PA3, PA6, and PA5 there, that's our, so the manual is pretty good, like, hats off to that.

**Dave Jones:** Anyway, here we go, so we can now program, auto-program our chip. Here we go, ta-da, verifying, boom, OTP, done, like that, because it's only like that. It's only 2K worth of program memory, and, what does it say, IC OK, and 1 has passed.

**Dave Jones:** So, yep, 1 OK, and of course we can, can we just push the program button? I don't want to do it again, don't want to try and ride over it. Anyway, you can just push the program button, or we can verify as well, but you probably can't verify after you set the security bit.

**Dave Jones:** So, the, but our security, the protect bit, is turned off. It's turned off in this particular case, but there you go, winner, winner, chicken dinner. Let's try and now flash our LED on our breadboard. OK, so what I've got here is just a little, little SO8 adapter board like this.

**Dave Jones:** I just got power and ground, hooked it up to the LED, and yes, the power and ground pin 8 is the ground. So, it's back to front, just watch that. Trap for young players, yes, an update by the way, this bloody LCD is still going with that DC bias.

**Dave Jones:** After what, nine months? How long has it been? I should have been asking for an update on that, bastard won't fail. So, but that doesn't mean the theory's not wrong, it's just that means that this big large segmented LCD is, it's working a treat.

**Dave Jones:** Anyway, oh, where's my chip? Bloody easy to lose. So, I couldn't be bothered soldering on there, so I'll have to line it up, and I'm going to press on it. Here we go, blinky, there you go. That's our, our, like in this case, 5 cent micro, but we'll say the 3 cent micro.

**Dave Jones:** Programmed, without a problem, and flashing a LED. So, that is neat. So, Padook have done an amazing job with this, with the whole thing. And, like, it's not new, they've been around for quite some time. And, whilst there is, you know, some chinglish type stuff, like, the help is very comprehensive in English,

**Dave Jones:** the manual's in English for the programmer, and it's all pretty much, it didn't take me long to figure out this at all. E.T. phone home. A bit silly holding this chip up like this, but anyway, um, there you go. This is quite impressive.

**Dave Jones:** I like it, we've programmed our 3 cent micro, no problems whatsoever. And, you can actually get these, um, not programmed to the factory, but programmed for practically free. Really, you know, but like, don't ask them to go and program one, or ten, or even a hundred, maybe.

**Dave Jones:** You know, you've got to order like thousands, and then they'll be happy to, uh, program them for you, I'm sure. So, there you go, hope you found that interesting. And, in a future video, I will hook up a scope and logic analyzer to all the pins on this programmer,

**Dave Jones:** and we'll see if we can, uh, start getting some data for this, and potentially reverse-engineer this, so that we can, like, get it into, like, an Arduino, uh, like, programmer, or, you know, any, like, low-cost open source, like, open the whole thing up, so that, uh, we can do that.

**Dave Jones:** Won't be as simple as just hooking these up to some pins on an Arduino, 'cause they said it's different voltage levels, and stuff like that, but hey, we could have, maybe have a little board that plugs on top, make it all open source, and then, you know, our 3-cent micro, a lot more people can use these things.

**Dave Jones:** They're amazing. Anyway, if you liked the video, please give it a big finger up, and, as always, discuss down below. Catch you next time.
