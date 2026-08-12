---
video_id: zDcl0-t7ceY
title: EEVblog #406 - Keithley 480 Picoammeter Teardown & Calibration
url: https://www.youtube.com/watch?v=zDcl0-t7ceY
source: youtube-asr
---

**Dave Jones:** Hi, today is going to be vintage teardown, repair, troubleshooting, and calibration time. Check out what I've got. It's a vintage Keithley 480 pico ammeter. Fantastic instrument. It dates from about 1979, although the manual, the Keithley manual for this thing which you can download,

**Dave Jones:** which has all the full schematics and calibration and servicing information in it, was last printed in 1990. So, I think this thing had a pretty darn long life. And you know I'm into small currents and stuff like that. I've

**Dave Jones:** got a whole range of Keithley gear over here in including pico ammeter sources and stuff like that. So, I thought this is a nice little match for that. Sure, I've got my micro current to measure low currents, but this little Keithley unit

**Dave Jones:** nice score I thought. I got it for 65 bucks on eBay. And these are pretty rare to find in Australia. They are not so rare in the US, of course, and that's probably about the going price for these

**Dave Jones:** things. So, I thought I'd snap it up. Now, it was actually advertised as um you know, it it would fire up. It would you know, power up but untested. Fair enough. It's pretty hard to test this thing unless you've got the proper

**Dave Jones:** instruments to do it. So, yeah, it the it showed a picture of something on the display and I thought okay, at least powers up. Beauty. But I got it plug the thing in and what? Nothing. Nothing on the display. So, that's a bit

**Dave Jones:** of a bummer. But that means we can do a repair and troubleshooting video. So, let's give it a go. Once again, this one will be a real time repair. So, I've no idea if this thing is actually repairable. Should be. They're pretty

**Dave Jones:** simple inside. There's not much in them. So, I'd be surprised if I couldn't fix this thing. It could be a very simple thing. Could be a blown fuse. I don't know. We'll find out. Let's go. And here it is. It's very old school.

**Dave Jones:** It's got the old-fashioned gang push-button range switches here. And it's very simple. It's got a single BNC input. It's got a zero adjust pot down here on the front panel, which is really nice. And it has ranges from 1 milliamp

**Dave Jones:** full scale all the way down to 1 nanoamp full scale there. So with a 3 and 1/2 digit display there as you can see behind the red Perspex there. It can has a resolution of about 1 picoamp, which is

**Dave Jones:** really quite nice. Very handy unit for measuring low currents. And it is a feedback operational type. So the burden voltage on this thing is incredibly low. This one is spec'd to about 250 microvolts burden voltage. Now, it's got

**Dave Jones:** a tilting bail here. And if we have a look on the back, it's got selectable 240 and 110. It's already set to 240 volts. So, you know, presumably that's not the reason why it is blowing. It's got an Australian plug on it. And

**Dave Jones:** well, yeah. We'll find out. It's got a couple of banana jacks on the output here. And the good thing about this is that it's the output directly from that feedback operational amplifier without going through any additional circuitry. So, you can get

**Dave Jones:** the direct output from the feedback amp, which is really quite nice. There's no indication of date on this thing, but we do have a operating instructions on the back. I rather like that. That's quite neat. Why can't all units

**Dave Jones:** do this? And it tells you down here input burden voltage. There it is. Input burden burden voltage is 200 microvolts or less for an on-range reading when zero is properly adjusted. So, the burden voltage is incredibly low. Um its specs

**Dave Jones:** aren't too bad at all. Um half a percent to 8% plus a few three or four digits there. Not too bad at all. So, I rather like it. Um of course, on the 1 milliamp range, you're only going to get um

**Dave Jones:** maximum input voltage is uh 20 volts. And you'll note up the top here that it is designed to have a battery uh pack in it as well. I've no idea if this one um has got one. Based on the weight of it,

**Dave Jones:** it's very light. So, I'm assuming this one doesn't have the battery um option in it. So, uh yeah, trust me. I've powered this thing up and we get absolutely nothing on the display. So, it's troubleshooting time. First thing we're going to do is uh

**Dave Jones:** check the mains plug to see if like there's a mains fuse blown. I assume like there's a mains fuse inside. There's not one on the back panel. So, we'll just measure the resistance and bingo. Yes, um this is quite common um

**Dave Jones:** to when you're measuring primaries of transformers, you can see the multimeter skipping like that. That's the auto ranging being confused by the massive inductance in the transformer, but there you go. So, yep, we're measuring the primary of the transformer there and it looks like

**Dave Jones:** Oh, look. Look, the the display just popped up. Did you see that? I'm sure it did. Yeah, look. The display's popping on. How the hell is it doing that? There must be some stored charge in there. Couldn't couldn't be

**Dave Jones:** getting it from the multimeter. That's that's bizarre. I I didn't notice that before. No, it looks like it's it's not going to do that anymore. I hope you got that on camera there. But anyway, um the uh primary is um in

**Dave Jones:** intact and the primary is in there regardless of the uh power switch. So, this is effectively a soft uh power switch on this secondary of the transformer. You're not going to believe it. Man, I cannot cop a break. Look at this.

**Dave Jones:** It's working. I swear it wasn't working before. The thing has decided to work all of a sudden. Oh, man. Massively disappointed. I was hoping this would be a troubleshooting video. But maybe there is something Maybe there's an intermittent

**Dave Jones:** issue there. So, yeah. We may have to Well, we're definitely going to crack it open and have a look, but that's a That's a real bummer. And back in the glory days of Keithley, of course, before the evil Danaher group took them

**Dave Jones:** over, it was made in the good old United States of America. Sure it brings a tear to the eye of some Yanks out there, but yeah, you won't catch me singing the Star-Spangled Banner. So, we'll whip those out. Looks like

**Dave Jones:** they go into posts into the other side. Very old school for these instrument cases. Very typical and still used today for this style of instrument case. And one thing to note, you don't see this very often, is this right-angle

**Dave Jones:** cable clamp here. Mains input cable clamp on the bottom of the case instead of the back panel. I have no idea why they've done that. That's weird, but anyway, let's put it up this way. Screws are out. And

**Dave Jones:** let's crack it open. Tada! There it is. Piece of cake. Lovely. And that is wonderfully, wonderfully old school. I love it. Check out all the square traces on the PCB there. Beautiful. Look at this crystal. Look at the size of

**Dave Jones:** that sucker. That's We'll go in and have a look at that. That looks It's a 100 kHz. 100 kHz crystal. Look at the size of it. Um I'll see if we can get a date code off one of these uh chips and see

**Dave Jones:** uh see what the uh build date of this thing is. There's no data on there. There's a cal inspection sticker. All of the um all of the stuff is under the shielded can, of course. Um this is all just the display

**Dave Jones:** and power supply stuff outside here, but all the um the feedback amplifier and everything's inside here. One interesting thing to note is that the BNC input here Check check this out. They've got a shield there. Right? They've got a shield over the

**Dave Jones:** BNC, and then they've got a little what looks like an unshielded Um it's not quite a coax. It looks like just a single core wire uh with some uh tubing on it coming out there and going down into the can down

**Dave Jones:** under there. So, that's I you know, I don't know why they've bothered to uh do that, why they've taken that outside of the can, and all that sort of stuff. Weird. Well, certainly no shortage of uh test points here. Here's our power

**Dave Jones:** supply. We've got plus minus 15 there, plus 5 V test points. We can uh check those out. And um yeah, we've just got some axial uh filter capacitors. Our transformer is up here. We've got an internal fuse, which isn't blown, of

**Dave Jones:** course, because it's working. And we've got a battery and line switch here, which allows us to select the battery module, which presumably plugs into this this connector here. So, we don't have the battery module on there. And looks

**Dave Jones:** like we've got a bridge rectifier there, two more uh rectifier diodes there. So, they might be getting another tap on the transformer. You can see multiple uh taps on the secondary side of the transformer there. Trim pot, there's

**Dave Jones:** another couple of uh trim pots down inside the uh can down here. So, I'm not exactly uh sure what they're designed to do. I have to read the calibration information for that. And we have some date codes here, folks. We've got a uh

**Dave Jones:** 4000 series of 4011, classic 91 uh 42nd week, 1991. So, and this one's uh directly soldered in. So, that um you know, it was at least manufactured uh 91-92. So, it's a relatively uh recent unit, probably as recent as you can get these

**Dave Jones:** things, I would guess. And uh this um ICL chip over here is a 93 one, but it's in a socket. I'm not sure um why we've got a socket there. We've got another 93 one down here. So, I certainly haven't

**Dave Jones:** been replaced, and those IC sockets were uh factory fitted. And we've got uh curiously a uh blank socket down here. So, I don't know what that one's for, but uh there you go. So, definitely um early '90s unit.

**Dave Jones:** Beautiful. And it's a rev revision F PCB. And check out the shielding spring that they've got here. Um the curious thing about that um is well, it's designed to mate to something, but inside the lid, there's no um you know, shielding on the

**Dave Jones:** upper part of the case for it to mate to. So, I don't know. Maybe uh something to do with the charger board, but I can't see it. So, don't know what's going on there. Now, let's take a look at the data sheet

**Dave Jones:** for these two puppies here. We've got an ICL 71C03 and an ICL8052. And as it turns out, they're actually a pair of They're a matched pair of devices. And what they are is a precision 4 and 1/2 digit AD converter and display

**Dave Jones:** driver. It doesn't tell you that, but that's what it is, as we'll see. And apparently, it was pretty darn state-of-the-art. It's designed 4 and 1/2 digit accuracy um uh 2 200 mV to 2 V uh full scale capability, auto zero,

**Dave Jones:** auto polarity, as you'd expect of a dual slope uh conversion uh unit like this. Typically, less than two microvolts peak-to-peak noise. Um, you know, accuracy guaranteed plus minus one count over the entire full scale range, guaranteed zero reading. So, a pretty

**Dave Jones:** darn nice chip for its day. I like it. Um, use of these chips pairs eliminates clock feed-through problems and avoids critical board layout. Woohoo! Beautiful stuff. And it's also, uh, does a three and a half digit mode, which is what, um, it's used here. And

**Dave Jones:** you can get up 30 readings per second to do that. And I love here how they're tooting their horn, almost ideal differential linearity and time proven dual slope conversion. Ah, love it. It's got a medium quality reference in it,

**Dave Jones:** not a high quality reference. It's a medium quality reference, 40 ppm. Yeah, not that, uh, terrific, but, um, more than good enough for this. Five pico amp, uh, input current down there. And it's a dual chip solution. And they've

**Dave Jones:** got them in the one data sheet, which is, um, quite unusual. Using Usually they'll have, um, separate data sheets for each one. But, and here's the block diagram for the two chip solution. And you can see the, um, 71C03

**Dave Jones:** with the, uh, red outline here, like this. And the, um, 8052 is that one there. So, the 8052 just contains a few, uh, buffers and the inner integration amp. And you need the, um, external integration capacitor and, uh, various

**Dave Jones:** external components there, internal, uh, voltage reference, and the main, um, ICL71C03, uh, contains the, uh, switching and the zero crossing detector and all the multiplexer multiplexing and latching and counting solution for that. And you'll notice that it's not a seven

**Dave Jones:** segment display, um, output here. It's a four digit, uh, BCD, um, output. So, you need a BCD to seven segment, uh, decoder. So, we should find that chip elsewhere in the design, probably on the front panel there. And, uh, as you can

**Dave Jones:** see, it can drive a 4 and 1/2 digit display, but in this case, we're only driving 3 and 1/2 digits. And there's a pin to uh strap it to 4 and 1/2 or 3 and 1/2 digit mode there. And, as you can

**Dave Jones:** see, there's not much to it, but it's a it was a very precision device for its day. And if we check out the bottom of the board here, here's this uh shielding tab again. It's all the one piece of

**Dave Jones:** bent metal. So, we don't know what it's going to on the top there. Doesn't appear to go into anything, but the bottom here, of course, down to a big shielding plate on the bottom of the case there. And uh yeah, not much doing

**Dave Jones:** there. Um check out the big star ground point up here. Look at that. Nice. Kind of looks like almost a flying spaghetti monster. I see a vision. Look at that. Beautiful. Um I love all the square traces and

**Dave Jones:** everything like that. It looks like it hasn't been reworked, really. It looks like it is um all factory soldered. Down here, there's a quite a bit of flux residue on the hand soldering for the transformer, but that that's not uncommon even these days.

**Dave Jones:** We've got some uh guard traces around there, little guard rings around these um and they're those uh test points that we saw before through the main cover. So, we'll whip that uh metal cover off later and we'll take a

**Dave Jones:** look. And on the front panel there, there's our BCD to seven-segment decoder, a um CD4511, absolute classic. Uh over here, we have a National Semiconductor DS75492.

**Dave Jones:** And that is a um uh hex uh MOS display driver. So, that's just uh driving um the heavy current on the digits. And there's that crystal, 100.000 kHz. I love it. I haven't seen one that big in a long time. So, as I said, it's

**Dave Jones:** a a real bummer that this thing's working. I was hoping to do a troubleshooting thing on this, but anyway, let's give it a go. Let's measure these rails. I don't know where a ground is, but presumably, I don't know, the can in the

**Dave Jones:** can here or the can of the crystal. Let's give it a go. So, our 5-V rail, there it is. 5 5.02, not a problem. -15, yep. +15, not a problem. There are our three power rails. So, this thing's just

**Dave Jones:** hunky-dory. I have no idea why it wasn't working before. Um it's really weird. Very strange. And there's that rather unusual input can. I just took the shield off there and it just, you know, they've gone to a lot of trouble to

**Dave Jones:** actually design that so it wedges in there and like just over the BNC. And there it is. There's a single solid core cable going out there over into the shielded can. Weird. Why they just didn't run that on the PCB with a ground

**Dave Jones:** trace over it, I've got uh no idea. But, but, you know, look, they've done the zeros here. Like the There's a zero adjust pot and they've just got those running right over there. Don't know why they didn't do that with

**Dave Jones:** the uh with that. Why they went to all that trouble. Hm. Weird. Like, you know, like you would have ordinarily just designed this input can, designed the circuitry, laid out the board so the input can like extended over this input

**Dave Jones:** BNC and the zero pot here. That's how I would have designed it. Now, as you may have seen before, it looks like we're not getting a zero reading on some of these ranges. I mean, that's the 1-nA range there. So, we're getting like 5 pA

**Dave Jones:** there with no input. And others is showing is showing zero, not a problem, but we're getting five on that as well. So, it looks like we're getting five on those alternate ranges there, and we'll probably get five on this one

**Dave Jones:** based on that. No. There we go. So, that one, that one, and that range, we're getting five. So, um and if we do the zero adjust button here, let's put that in. Zero adjust. Let's tweak that down, shall we? Let's go down

**Dave Jones:** to the lowest range. I haven't read the manual, but it's okay. I've got my tongue at the right angle. And give that a little tweak. And we're down to zero there. And let's try that again. There we go.

**Dave Jones:** Nice. Okay. Everything's fine. I say we just get my um Keithley current source out and uh whack some current into this thing and see if it's spot-on. Hopefully, it won't be cuz then we'll have to go through the

**Dave Jones:** calibration procedure. All right. What I've got is my uh Keithley 261 pico amp current source. So, it's a perfect match for this thing. I've also got the uh 225 current source. So, uh if we need to go to higher currents for the milliamp

**Dave Jones:** ranges, this can't uh do that. This starts from uh 10 to the minus five. So, it starts from 10 microamps um full scale down to uh you know, femtoamps. It can go Look, this this knob is dicky. It's completely

**Dave Jones:** dodgy. Uh there we go. No, ruined. Uh got to really tighten, maybe flatten the shaft out on this thing, and do that. But, uh anyway, trust me, this thing does actually go down to a minimum of 10 to the power of

**Dave Jones:** minus 12, i.e., 10 picoamps full scale. And you can adjust that because this shows the uh where the decimal point is, then we're talking about um you know, 10 femtoamps resolution on this thing. It's really quite good and more than good enough for

**Dave Jones:** um the testing the range of this thing, which is one uh nano um amp full scale. Anyway, what I've got this thing on is the 10 microamp range, so it's 10.00 microamps here, and I've got it on the

**Dave Jones:** uh uh 10 microamp range here, and there it is, 9.99. You saw it before it was 10.00, so you know, something's drifted somewhere a little bit, but it's basically spot on, and we should be able to tweak that. There we go, and look at

**Dave Jones:** that. Just dial it in. We're only one least significant digit out between these two units. Absolutely incredible. We can dial that up to exactly 10. There we go, we can tweak it. It's hard to read that uh uh LED display, I think, at

**Dave Jones:** least on the screen here. So, I might have to up the current on that thing. I might just change the resistor network there or something like that, just to make it a bit brighter, maybe. It's a bit washed out, but yeah, look at that.

**Dave Jones:** I can just dial in that digit there. Fantastic. I love it. So, that's bloody spot on, unfortunately. And you can see it blinking over range there. And I just noticed something that I shouldn't be doing. There's the mains cord there,

**Dave Jones:** right next to my um lead. That's probably not the best idea. So, let's get that completely away from there. And so what we're going to do now is we'll just try out the negative uh polarity. I can just swap the leads, of course, or I

**Dave Jones:** can just use my negative switch here, and bang, that's, you know, we're only talking it's changed by two least significant digits. So, it's basically spot on plus minus one. I love it. Um and of course we go down, we get a flashing over range

**Dave Jones:** there. And uh so that is working a treat. So, let's change this uh range down, and if we go up a range, there we go, 9.9, not a problem. We should get nine. Yep. Or 10 I was expecting there, so

**Dave Jones:** Ah, man, this thing's spot on. Not going to do any troubleshooting, not going to do any repair. Looks like we're not going to do any calibration, either. Bummer. And if we go up to the 100 microamp range, yeah, that's as

**Dave Jones:** basically as high as we can go on this um uh 261 current source. But look at that. I mean, that's we're talking. Look at that. That's just ridiculous. Down to the 1 microamp range, we're absolutely bang on. So, let's keep

**Dave Jones:** going. Excuse the crude adjustment here. What are we on now? We're on the 100 nanoamp range. Bang on. Absolutely bang on. Look uh that's just that's just filthy. That really is. Unbelievable. Ah. It's obscene. There we go. And we're now down on the 10 nanoamp

**Dave Jones:** range. If you remember, there's all the ranges there. There they are. 1 1 nanoamp through to 1 milliamp. Haven't tested the 1 milliamp one yet. I'll have to get my other current source out to do that. But there you go, we're bang on.

**Dave Jones:** That's 10 nanoamp range. Not a problem. And there we go. We're down to our 1 nanoamp and we're picking up some noise here. You can see it's jumping around. I mean, what I've got here is I've just got a shielded BNC. You can see it. You

**Dave Jones:** can see it changing as I play around with that. I mean, we're right down in the noise here. Um if you want to do good low current measurements, Keithley have the I think it's called the low current measurement

**Dave Jones:** handbook or low, you know, something like that. I'll link it in here and it is one of the industry standard reads on low current measurement like this. I mean, you know, I've done a little bit of twist in the wire there just to keep it

**Dave Jones:** low, but really, you know, I mean, this probably isn't going to cut it, as you can see. And if we go back up a range to 10 nanoamps there, you can see that it's basically spot-on. And then if

**Dave Jones:** I start to handle that, you can see it starting to kick in there. So, really, you're getting triboelectric effects in the cable and all sorts of stuff there. So, really, you don't want to touch it. Hands off, keep it as short. There's a

**Dave Jones:** whole art to doing this. Keep it, you know, double-shielded boxes and all sorts of weird and wonderful techniques, which will no doubt be in the Keithley measurement handbook. So, check that out, but if we go right down to the lowest range

**Dave Jones:** there, then we adjust that, it is it is bang on if I don't touch that cable at all. If I get anywhere near that cable, bang, it's just going all around the place. But this thing seems to be

**Dave Jones:** in perfect calibration. It's absolutely bang on. I'd be a fool to even attempt to touch this thing. Let's go to switch it to negative mode, so we're getting minus one nanoamp. Ah, near enough. I'm not going to complain about that.

**Dave Jones:** I'd really have to probe it all properly and spend hours around to try and get that right, but there you go, positive and negative. And if we switch up a range there, it's bang on one negative and positive. Brilliant.

**Dave Jones:** Bang on one nanoamp. Do you believe it? Look at that. I can just dial that in, and I can probably dial this one in if I don't get my hands near it. Look at that. Great stuff. And I have to test out the milliamp

**Dave Jones:** range. So, I've got my other Keithley current source here, which is the 225, which covers a larger range and doesn't go as low. So, it goes all the way from 99.9 milliamps here, so 100 milliamps basically, all the way down to 99.9

**Dave Jones:** nanoamps. So, this one has a resolution of 100 picoamps, so not nearly as low as the current source we had before. So, with these two instruments, I can cover practically and with my other power supplies, I can cover practically

**Dave Jones:** everything from 10 femtoamps all the way up to, you know, amps. Crazy. Many, many orders of magnitude. And with this one, you can adjust the maximum output voltage anywhere from 10 volts right up to 100 volts. And also,

**Dave Jones:** it's got the it's got the positive and negative switch as well. And it's also got an output filter. So, let's hook this thing up. All right, so I've got this set to 1 milliamp here, 1.00 milliamp. We've obviously got an extra

**Dave Jones:** digit over here. And look at this. We are bang on, folks. Absolutely bang on. I love it. So, we can dial in. Look at that. That's pornographic, really. We can just dial in those digits and it matches precisely.

**Dave Jones:** Fantastic. So, if we switch that down to microamp range, once again, we're bang on. So, these two units match. I mean, I obviously keep them in cal to calibrate my microcurrents. There we go, a couple of less significant digits out there.

**Dave Jones:** Whoop-de-doo, folks. And of course, um this thing and we're not even near full scale on this thing where the accuracy is the is is the best on this thing. We're right down at 1.00. So, let's go down. There we go. Ah. Ah. Couple of less

**Dave Jones:** significant digits out there. Ah, what a bummer, huh? So, 99.9, let's wind the wick up. There we go, 99.9. Uh that's obscene. And let's just try the negative there. Switch it around. Huh. And we almost forgot to have a look

**Dave Jones:** under the metal can there. But look at this beautiful uh point-to-point hand soldering with the uh turrets there completely surrounded by the ground plane on top there. Beautiful. So, they've just gone completely point-to-point. We've got uh metal cans

**Dave Jones:** here. Beautiful. But by far the most interesting thing in this is look how they're doing the range switching here. I mean, I I don't know if these um switches are actually connected up to anything. Looks like there are some traces going down

**Dave Jones:** there. But look at that. These things push on these gold uh leaf contacts here, which then push on that gold pin like that. It's just beautiful. I They've gone to a lot of effort there to switch to ensure that

**Dave Jones:** they um switch very low noise. They're just switching part of the circuit. There it's interesting though that they don't do it to the lowest two ranges down here. There's none of that switching at all on those lowest two ranges where you think it would be

**Dave Jones:** um absolutely critical to uh do that thing. So, I have to look at the uh schematic for that. But that is that that is just lovely. They've deemed that they have to go to that effort to get the uh to get the signal integrity, the

**Dave Jones:** low noise on this thing instead of using the you know, the crummy switches inside these gang switches. I mean, no matter how good you manufacture these switches, they're probably going to be pretty crusty. So, they've gone for a beautiful

**Dave Jones:** you know, um very probably a very heavily plated uh gold leaf um contact there onto another heavily plated gold pin. Beautiful. And let's just go for the money shot there. Ah, look at that. Ah, could play with that all day.

**Dave Jones:** And if we go and have a look at our schematic here, I'll link it in down below. And by the way, if you want to check out the manual for this thing which has the full schematic and theory

**Dave Jones:** of operation and all sorts of stuff, it'll make a great bedtime reading, I'm sure. But here we go. We've got some switching down here and that's the decimal point switching. So that's all the digital stuff. So that's what those

**Dave Jones:** crummy gang switches will be used for is just the digital part of the decimal point switching, of course. But all of that beautiful low noise gold leaf contact there is all part of the feedback amplifier. And here's the feedback amplifier here.

**Dave Jones:** There's the zero adjust pot there. It's By the way, you would do this with a, you know, a real top spiker fit input op-amp these days, but they actually used a JFET input front end with matched JFETs. And incidentally, these two resistors,

**Dave Jones:** they've got an asterisk next to them. They're if you look at the notes, they're actually selected at the factory to match the transistors there. Here you go. You can see the switch contacts in the feedback path there for the

**Dave Jones:** feedback resistors. There they are. There and there your gold leaf contacts and they have to be incredibly reliable, incredibly low noise contacts when you're talking about an instrument of this caliber. And if you notice before we had four of those gold spring

**Dave Jones:** contacts and there's the four contacts and they've also got some of the other range switches here which is switching some more non-critical stuff. And you can see that the 10 nanoamp range and the 100 nano amp range there isn't

**Dave Jones:** actually um switched at all as we noticed um inside the unit. So, we bring the unit back over here again, you'll notice that the There you go. We've got our four spring leaf contacts and the These uh and the two lowest ranges

**Dave Jones:** aren't switched in there at all with those gold leaf contacts because um they are fixed across the feedback path and then the others are put in parallel. So, as you can see, there's not much to these things. It literally is just a

**Dave Jones:** feedback amplifier. And uh if you used a modern um op-amp in there, I mean, this thing was designed in, you know, uh the late '70s. Uh they just weren't around then, so they had to, you know, hand match these JFET inputs, but you can

**Dave Jones:** just get a um FET input um op-amp, a really uh low bias current, you know, precision op-amp these days just to do that. Put a feedback resistor in there, some um low-pass uh filtering caps on there, and Bob's your uncle. And there's

**Dave Jones:** the output um terminals and the output banana jacks on the back panel. So, you can access directly the output of the feedback amplifier. And that um you know, I won't go into theory of feedback uh amps here. I may have even done it uh

**Dave Jones:** before, but um basically, it converts uh current into voltage on the output with effectively only the uh difference between the offset voltage between the inputs to the op-amp um which is your burden voltage on the input. So, this is how you can get

**Dave Jones:** incredibly low burden voltage, unlike my microcurrent one which just uses a traditional shunt resistor. This one is a feedback amplifier which works differently, so you can get even lower burden voltage than my microcurrent. And by the way, just as an aside, if you're

**Dave Jones:** playing around with uh very uh you know uh low current precision circuits like this just be careful how you handle this or try to avoid handling them if at all possible because your hands if you you know your hands aren't clean or even if

**Dave Jones:** you've just washed them they can still have oils and stuff which can leave residues on critical parts of the circuit cuz we're talking about you know 100 megaohm resistors here that one's 99 meg and you know if you start getting in

**Dave Jones:** there and you get all sorts of dirt and residue and you know all sorts of other gunk in there it can you know upset the calibration of this thing so just be careful. So of course it turns out I was

**Dave Jones:** wrong about these being access points it seemed a bit weird that they were very deep down in there they're just little plastic holders to keep those posts in place so that that those contact switches don't bend and just for kicks let's make

**Dave Jones:** sure the burden voltage is less than the 200 microvolts claim. So what I've got is I'm feeding in 1 milliamp here and I've got a banana to BNC jack here so that we can get in here with our meter and probe it. Now

**Dave Jones:** I'm going to use my Agilent U1272A cuz it's got the 50 millivolt range so it can the resolution can go all the way down to 1 microvolt. Fantastic and as you can see it's pretty darn close to zero there and let's get in

**Dave Jones:** there and probe this sucker. Let me try and apply some pressure you got to be careful here but yeah we're definitely under the 200 microvolts there we're only about 110 microvolts. Love it. And just to double check on a lower range

**Dave Jones:** there I've got the 100 nanoamp range there and we're only about 80 odd microvolts. And because I'm sure there will be people who will ask how does it compare to my micro current here? Well here it is I've got 100 microamps in

**Dave Jones:** there, and we're getting 99.96 microamps out of this sucker. This one obviously has and allows us to get an extra digit of resolution there. And there it is, um, measuring in the order of 100 nanoamps there. And it might be,

**Dave Jones:** uh, two least significant digits out on here, but I'm not actually feeding in 100. I'm feeding in, uh, 99.9 microamps. So, um, you know, in theory, if everything's absolutely bang on perfect, this should be 99.9 nanoamps there, or 99.9 millivolts, cuz

**Dave Jones:** it's 1 millivolt per nanoamp range on my microcurrent. So, there you go. Everything's well within spec. And if you don't have a calibrated current source like I do, you can, uh, easily test this, um, in fact, this is probably

**Dave Jones:** the recommended, uh, method to, um, actually, uh, calibrate these because, uh, you can easily get, um, high precision voltage and resistance standards. So, I've got my, um, MV106, uh, DC voltage standard you've seen here before. Way overkill, I mean, the

**Dave Jones:** Keithley 480, uh, picoammeter, you know, is only rated to like 0.5% and this sucker is, uh, a couple orders of magnitude better than that. So, um, I've also got my resistance standard here, which you've, um, seen before, which is basically just a, uh, 50 ppm

**Dave Jones:** resistor in a box. I've got a 10K one and a 1K one. Um, usually you would, uh, use a much higher, uh, value than this for, um, testing the lower current ranges, but this is the best, um, this

**Dave Jones:** is the best resistor I've got. I've got larger resistance, uh, values, but they're, you know, uh, a few percent or something like that. They're certainly not precision. So, we're talking about, you know, point double 05% um, accurate resistor in a box here. You can buy

**Dave Jones:** those for about 20 bucks or, uh, something like that from Digi-Key. Yes, you can pay 20 bucks for one resistor, but it's a pretty darn schmick one. So, um, I've got it hooked up here. We're on the 10 V range, but I'm outputting 1 V here,

**Dave Jones:** 1 V on 10 K, we're going to get 100 Oh, there it is, 100 microamps. We are absolutely bang on to the least significant digit. Of course, if I take that up to 10 V on the uh voltage standard here. Oh, one least

**Dave Jones:** significant digit out at 10 milliamps. There you go. And of course, if you you know, you've got to be careful what you're doing here. You've got to take into account the burden voltage. We've already measured that, 250 microvolts.

**Dave Jones:** So, it's insignificant here. It's actually 100 microvolts. The spec is 200 microvolts. So, you know, it's down in the noise here. Now, you might think that we're simply able to reduce the voltage here and um measure the lower

**Dave Jones:** current ranges, but that's not really the case. You can see it's um slightly out here. So, I've got 10 millivolts there over my 10 K, which is going to be 1 microamp there. And you can see we're out. But, I know it's not out. It's

**Dave Jones:** because the offset voltage now becomes a very significant proportion of the burden offset voltage in this thing becomes a very significant proportion of our of our you know, of our calibration setup here. So, that's why the manual for this thing will recommend minimum

**Dave Jones:** input impedances for this thing for for these various ranges. But, what that essentially translates to is not necessarily a minimum input source impedance, but a minimum input voltage essentially so that the burden voltage of this thing doesn't matter. Now, look, if we go even lower,

**Dave Jones:** like well, we'll go up one there. So, we'll go at one A. See, it gets closer there as we go up. So, we're 10 microamps there, but we'll get more further out as we go down. So, let's drop that down even

**Dave Jones:** further, zero and one there. Now, we're even we're way out, okay? We're just you know, we're we're just completely and utterly gone. If I put that to one one millivolt, there we go. We're completely out. And if we take a look at

**Dave Jones:** this Dave CAD drawing here, we can see exactly what's going on here. We've got our MV106 voltage standard generating our test voltage here. We've got our 10K series resistor going into our feedback amplifier here. Now, at the moment,

**Dave Jones:** let's just ignore the feedback resistance here and we've got that measured VOS or offset or burden voltage there of around 100 microvolts. Let's just you know, round it to 100 microvolts. It's going to change per range and all that

**Dave Jones:** sort of stuff, but let's just take that as a value. So, let's have the one volt that we had before. One volt minus 100 microvolts divided by 10K because that's what's flowing into this this feedback amplifier here gives us

**Dave Jones:** 99.99 microamps and we were measuring bang on. So, you know, the error is in the VOS error here is insignificant in this case where we had the one volt and we were generating 100 microamps. It's pretty darn close. But,

**Dave Jones:** then if we drop our test voltage here from the MV106 to 10 millivolts, then we can see our 100 microvolt offset voltage becomes very significant. You do the math here and it's 990 microamps. So, we'll actually measure that and we

**Dave Jones:** should get roughly that figure. And then if we drop it even further, we're going to ridiculously low voltage here. One millivolt minus 100 microvolts, of course it's going to have a very a um error or a 10% error there of 90

**Dave Jones:** microamps. So, let's actually measure that. So, let's go up here and we've got it set to 1 V here and we're getting our 100 microamps as we saw before, spot-on. Because um in theory, we should actually expect 99.99

**Dave Jones:** microamps, but because um that value is one uh digit um better than the resolution we've got here, eh it's you know, it's insignificant, especially when you consider the accuracy of this thing. So, or the intended accuracy of this thing. So,

**Dave Jones:** it's insignificant, but if we wind that down to 10 mV here, I'm on the 100 mV range, we're generating 10 mV. You'll notice that we were expecting What were we expecting before? We were expecting 990 microamps and there you go. We're

**Dave Jones:** getting reasonably close to that and but our error is going to get um significantly larger, as you'll see in a second. Now, and if we switch down to our 10 mV range, we'll generate 1 mV. There you go. We're getting that 90

**Dave Jones:** microamps, which we expect, but uh-huh, well, you know, reasonably close to it, within a ballpark, but let's switch down this range and see what happens. 100 nA. Look at this. We're measuring 20 like that. So, our error is

**Dave Jones:** very hugely significant. The you know, it's it's almost now pointless. It it just reads gibberish now. Why is it doing that? And here's the answer. I've added an additional Dave CAD drawing here with a formula, which now becomes

**Dave Jones:** very, very significant based on our source resistance RS. So, I basically relabeled the 10k resistor RS. That's our source resistance. Um our feedback resistor here is RFB for feedback and I've redrawn the VOS as a voltage source here, which is a better which is a more

**Dave Jones:** common representation of it, but it's the same thing. It's that 100 microvolts, but that 100 microvolts we measured way before is not a fixed value. It's actually multiplied by this term here which is RFB plus RS divided by RS. So, let's take

**Dave Jones:** uh the example of the 100 microamp range. That's got a 10k feedback resistor. What happens if you plug 10k and 10k into this formula here? This term here becomes a value of two. So, the VOS at 100 microvolts gets

**Dave Jones:** multiplied by two. And then, if you change the range again, let's say you jump to the 100 nanoamp range, then RFB, the feedback resistor, is actually a 1 meg resistor. And you can look up these values on the schematic for yourself,

**Dave Jones:** and I recommend you go do that. Um have the schematic here as you follow along, in fact. So, then the term becomes huge, and that VOS just goes completely out the window. So, that's why we're reading absolute gibberish as we go as we switch

**Dave Jones:** down those ranges cuz as we switch down the ranges to, you know, 100 nanoamps, 10 nanoamps, 1 nanoamp, this RFB gets much, much larger, and this term becomes much, much larger, and VOS just goes out the window, and we're only got a 1

**Dave Jones:** millivolt source here, and VOS is way bigger than that at well, in theory, and you just read absolute gibberish. It just doesn't work. That's why if you read the manual for this thing, it will specify a minimum RS or source

**Dave Jones:** resistance value here based on whatever range it is you're measuring. Now, the manual actually says for a 10k source resistance here, which is what we're using ignoring the source resistance of the MV106 for a minute, then the lowest range we can use is the

**Dave Jones:** 10 microamp range. If we go any lower than that, it just, you know, the error term becomes too significant. And if you really want to go into it, and you can read the manual for this, there's an additional

**Dave Jones:** voltage source in here, which is the VN, which is the noise source, which is going to depend on your series capacitance as well, as well as your feedback capacitance in here like this, and all sorts of stuff like that. And it starts

**Dave Jones:** to become very, very complicated with lots of traps for young players if you're measuring very low values of current like this. There's a real art to measuring this sort of stuff and knowing where all your error terms and things like that are.

**Dave Jones:** So, I won't go into details on that. It's in the Some of it's in the Some of it's in the manual for this thing if you want to read it. It's very interesting. And of course, our simple little dumb ass,

**Dave Jones:** you know, like I've got just wires just hanging loose over here. It's, you know, it's pretty pathetic, actually. So, you know, this isn't the way to do it. As I said before, you've really got to um uh you know,

**Dave Jones:** do like have dual shielded boxes and shielded leads and, you know, all sorts of, you know, great quality contacts and stuff like that if you're really going down to very low levels of current like in the order of under 100 nA. Once you get

**Dave Jones:** under, you know, that sort of microamp figures sort of those sort of things start becoming quite significant, and you've really got to know what you're doing. So, maybe I'll do another video on that, you know, all that sort of

**Dave Jones:** stuff of really accurately measuring low value resistances. But, yeah, you've got to have precision high value resistors in, you know, double shielded boxes, and they've got to be isolated with minimum amounts of capacitance and all sorts of stuff. Really get tricky. Quite a

**Dave Jones:** fascinating topic, though. And here's what I'm talking about in terms of the double shielded test fixture here. Now, you can see that the outer case here is actually connected to the earth. That's you can see the earth symbol there. It's

**Dave Jones:** connected to the earth of the DC voltage calibrator over here. And of course we've got our low and high and our sense lines. And internal you you might also shield this circuitry internally from the shield which is non-mains reference

**Dave Jones:** to the Keithley 480 over here. So you'd have the internal precision resistors. They recommend 10K, 10 meg, and 100 meg. And based on those three and the individual test voltage over here, you can generate all the required currents.

**Dave Jones:** But that's what you would do. You would put this inside an earth shielded box over here. And you'll notice that it's only connected to mains earth over here because the Keithley is not mains earth referenced on the input. And then the

**Dave Jones:** internal ground, you might shield that internally as well if you're going really low. Probably not need double shielding. Probably not needed in this particular case. But if you had another instrument that was going even lower than this one, then that would be

**Dave Jones:** important. So there you have it. I hope you enjoyed that little teardown and little look at calibration checking this very nice Keithley 480 picoammeter. And if you can pick up one of these puppies, I highly recommend it. You know, I

**Dave Jones:** wouldn't pay more than you know, 100 bucks for one for sure. But they're a really nice bit of kit for measuring low currents. And it'll be a nice addition to the lab here I think. And it was bang

**Dave Jones:** on. I can't believe it. So yeah, sorry about that. I still don't know what was initially wrong with this thing cuz it definitely was not working when I first plugged it in. It wasn't working at home when I first got it. And then I brought

**Dave Jones:** it to the lab here, and it didn't work either. But all of a sudden, bang. So, I don't know, maybe there was a dicky contact in the switch or something like that. And after a couple of goes, it

**Dave Jones:** just self-cleaned or something like that. That is the only thing I can think of. So, yeah, sorry about that. I was hoping to get a troubleshooting and repair video, and ah, Murphy gets you every time. You hope for a fire, and you don't bloody well

**Dave Jones:** get one. Either in the fire of the circuit itself, the unit itself, or the calibration. I was hoping maybe we could, you know, tweak a few more pots and actually go through the calibration procedure, but it's bang on. So,

**Dave Jones:** certainly not going to touch it. So, anyway, if you want to discuss it, jump on over to the EVblog forum. And if you like it, please give it a big thumbs up. Catch you next time.
