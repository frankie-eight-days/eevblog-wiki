---
video_id: ln8Mlz4NsW8
title: EEVblog #393 - LiPo Battery Discharge Testing
url: https://www.youtube.com/watch?v=ln8Mlz4NsW8
source: youtube-asr
timestamps: {"0": 4, "1": 39, "2": 74, "3": 103, "4": 127, "5": 158, "6": 188, "7": 227, "8": 262, "9": 297, "10": 324, "11": 352, "12": 375, "13": 406, "14": 427, "15": 456, "16": 482, "17": 506, "18": 534, "19": 548, "20": 578, "21": 599, "22": 627, "23": 645, "24": 679, "25": 712, "26": 735, "27": 768, "28": 809, "29": 826, "30": 858, "31": 890, "32": 926, "33": 946, "34": 983, "35": 1017, "36": 1043, "37": 1054, "38": 1082, "39": 1104, "40": 1138, "41": 1155, "42": 1186, "43": 1201, "44": 1222, "45": 1255, "46": 1281, "47": 1309, "48": 1335, "49": 1361, "50": 1389, "51": 1415, "52": 1427, "53": 1453, "54": 1470, "55": 1501, "56": 1521, "57": 1553, "58": 1584, "59": 1603, "60": 1625, "61": 1645, "62": 1668, "63": 1698, "64": 1730, "65": 1746}
---

**Dave Jones:** Hi, just a quick video because so many people have asked for an update on the USB power supply or the power supply projects in general. You know, I've started two of them and well, as you might know, I haven't been doing any work on them for quite some time, but I am now back into it. So, this is just an update on the USB the battery powered USB supply that I was working on and you've seen this prototype in a couple of videos and I've got some firmware up

**Dave Jones:** and running on it now. So, micro supply version 1.0 and you know, it's displaying I can set and display the constant voltage and the constant current modes. So, just a little bit of the menu interface here. I haven't got the full menu done yet, but basically voltage at the top this is currently displaying output volts here and output current. I haven't zeroed the thing or anything like that yet. So, and this little selection device allows you to select if you press this, it allows you to toggle between

**Dave Jones:** volts and amps there and you'll notice if you actually uh you'll notice that there's a little S there. Well, when I let's say we want to set our volts. This is our up down button here. I can just go up like that. So, now it's actually displaying when you press those buttons, it briefly displays the set. That's what the S is for. Briefly displays the set voltage and the set current. So, I can set that 3.25 and 3.34.

**Dave Jones:** Haven't tweaked the thing as yet and you can do and if you want to set the current limit, just go down here and you can set your current limit like that. I haven't got the key velocity stuff all set in there, but it does work just a treat. So, that is a little bit on the user interface with this two-line by eight character LCD. It's adequate.

**Dave Jones:** Yeah, it's it's not the it's not the best for displaying a whole bag of information, but it is certainly usable. Now, with this So, you know, I've done some tests on it, and I'm reasonably happy with it, but you know me, I'm going to change it because I originally wanted to put it into this polycase here. It was going to sit here. I was going to have punched holes, and it was going to run from you know, just single cell mobile phone battery, but I decided, well, if you're

**Dave Jones:** going to make the thing battery powered, it may as well have a lot of capacity in it. So, I decided that the mobile phone battery just wasn't, you know, really the greatest capacity. These are only like, you know, 12 1400 milliamp hours at tops is really all I could fit into this case here at at 3.7 volts, of course, single cell. It was going to sit under the board, and I was going to have a clear Perspex window on the top so you could see the

**Dave Jones:** LCD and stuff like that, but you know, I decided really it if you're going to do it, do it properly and get a decent battery. So, I discovered this thing on HobbyKing. And this is a 5000 milliamp hour 20C single cell lithium polymer battery, and it's a bit of a beast. It's designed for 20C discharge. So, you know, it's very high discharge capacity battery designed for remote control, you know, cars and other toys and things like that. You can even get like a 40C discharge version. I

**Dave Jones:** mean, we don't need the discharge capacity of, you know, 20C cuz um, even this, uh, cheap 20C version at, uh, a rated 5, um, amp hours, that's 100 amps discharge, um, this thing is capable of. They're absolutely incredible lithium polymer cells, let alone the 40C version, double that, absolutely incredible. So, anyway, I thought, uh, at the end of this video, um, after I've done a little bit of a rant here I, on the update, um, of the power supply, I will, uh, test the capacity of this battery at, uh, lower C

**Dave Jones:** version. So, stick around for that at the end. But, yeah, these are absolutely cheap. They're, this, uh, this one is the highest capacity you can get. It's 10 mm, uh, thick by, um, uh, 120 or something like that by 40. And, uh, it just so happens that 40 is the exact width of the LCD like that. So, I thought, you know, I can What I'll probably do is re-package this thing so that the, um, uh, board, it, you know, base the design around this battery so that the board is

**Dave Jones:** long and thin like that. It's the same width, so the LCD sits on there like that. There'll be USB, uh, charge sockets or other, maybe a higher capacity, uh, charge socket as well on the input. And then, uh, we'd have the screen in there, then we'd have the circuitry, and we'd have a couple of, um, output binding posts on the other side there. And it'd be, you know, it doesn't have to be all that thick, you know, it's it's only going to be, if you take the board plus

**Dave Jones:** that, we can even make it thinner than that, you know, it's not that thick at all, it's not that wide. Uh, this is reasonably, uh, heavy, but, uh, well, what the heck, you you know, that's the price you pay for the huge capacity of this thing. But, I figure, if you're going to have a battery-powered power supply, you might as well have, um, a decent, uh, capacity in the thing. So, I thought I'd base it around this. And yeah, have a long cylindrical package and that'll mean a custom case for this

**Dave Jones:** thing as well. I can get that laser cut out of clear acrylic or something like that, like just the exact width so you can see the LCD through it and I'll have a similar sort of interface with the buttons on the side down here like that, all all along the side here and that should be really quite nice. I'm going to stick with the same LCD. I rather like this. It's quite neat.

**Dave Jones:** It's working quite well. I've got my interface working with it. So, pretty done, happy with that. So, I think that is the avenue I'll go with this thing cuz I was going to make a few changes to the board anyway, re re-spin it. So, I might as well re-spin it for a higher capacity battery and a different form factor. And um really a few of the components on here quite wimpy. This one because I was basing it on the lower capacity battery, I really didn't want to go that high in

**Dave Jones:** current or output power. So, I think with this new one I might step it up a notch and have a higher output voltage regulator and a higher output switch mode or a higher power capable switch mode converter perhaps just for some extra output capacity. So, there you go.

**Dave Jones:** That's the update. I am working on it and it does actually do the business and work here. So, for example, like a current, I can let's set the current. Let's go down here. Let's set it. Yeah, and I need more room on the board to put proper silk screen labels and stuff. This board was pretty packed by the time I got everything on there. I mean, there really wasn't much room left for about silk screens. I put the little name on there at an angle, squeezed it in. I squeezed in my

**Dave Jones:** platypus underneath there and it was, you know, um it was really quite a squeeze, so hopefully, uh this will give me some more uh um uh room to uh lay out the components, have a bit more uh silk screen designation. Anyway, I've got my um current limit set to say 288, that'll do. 288 milliamps, 3.3 volts output.

**Dave Jones:** I've got a 10 ohm high power 10 ohm resistor here. I'll whack it across, and uh we should get our current limit at around There you go, 288 milliamps. So, it's uh it's working quite nicely. And uh I've measured a bit of its performance, and I'm quite happy with it. But, yeah, it's a bit it's a bit wimpy. So, thought I'd step it up a bit.

**Dave Jones:** And the good thing about these Turnigy batteries, I took the opportunity just to get a couple of different uh samples of the thing. Just be careful of these tabs, by the way. You don't want to short them out. That's why they come with uh these uh the these protective uh tape over the ends of them. But, anyway, even this whopping 5,000 milliamp hour one, this was only like eight bucks or something. I mean, you know, unbelievably cheap. And they have the same size, but in a 3,300 milliamp hour,

**Dave Jones:** that's uh cheaper again, but it is uh thinner and lighter weight compared to the 5,000 milliamp hour one. But, I'll um I'll design the thing around the 5,000 milliamp hour one, I think. Um you know, just because well, you can.

**Dave Jones:** It's the same size and shape. Depends on what uh price and weight you want, but there's not a huge price difference. Um and they've got smaller ones like this 2,200 milliamp hour. Once again, it's uh 20C, and I think you can get higher capacity versions as well. And it's smaller, and then they step down to this nice little uh 1,000 milliamp hour 20C one. So, that might come in handy for some other projects. So, these are really quite neat. And by me, you know, less than 10 bucks, unbelievable. You know,

**Dave Jones:** for the capacity you can get in this thing and 20C discharge. Man. Anyway, I thought I'd do some measurements on that. So, I'm going to hook up my BK Precision electronic load here and we'll see and up to my PC and we'll see if we can get a battery discharge curve on this thing.

**Dave Jones:** One as I said, I don't want to do 20C, but let's do you know, a benchmark at 1C or something and see what we get. And by the way, I think I mentioned that I did actually capture the layout of this board, the full layout. So, I might even though I'm going to change it, I might still go through and add some commentary on top of that layout and upload that upload that just like I did with my previous power supply one cuz they're I think they're really

**Dave Jones:** interesting videos just adding commentary to real time or sped up real time PCB layout cuz you know, it took me like you know, and you know, a 5 hours or a day or something to lay out this board properly. So, I'll speed that up and might add some commentary.

**Dave Jones:** Now, I've got my BK Precision 8500 electronic load hooked up to the PC here via the USB adapter which I got with it. You can get an RS232 or a USB. I've got both using the USB and I've hooked it up to the PC software here and as it so happens the PC software that comes with this BK Precision one, it does actually have a battery discharge application. So, it allows us to specifically set up the battery and discharge it and get the discharge curve and save it and it calculates the

**Dave Jones:** milliamp hour capacity of the battery and so forth. So, I haven't tried it yet. Um let's see if it works. I hope it works. Now, as I've mentioned before, one of the really annoying things about this BK Precision 8500 load is that it doesn't have standard these binding posts great. Look at them big fat chunky. Love the things great looking knob on them, but they don't have support for standard banana jacks like that even if you take them off there hopeless.

**Dave Jones:** So you know, I've got like a nice you know, a high amperage banana plug to alligator clip cable. I can use just for this thing but man now I've got to like budget in there with it you know squeezing in the binding post hopeless. Now of course you can use your constant voltage constant current bench power supply to charge up a lithium polymer cell but you got to watch it.

**Dave Jones:** It's not you know, you got to know what you're doing got to set it precisely to 4.2 volts. You got to watch the time limit on the thing and you know, got to be very careful if you're doing that but what I got from Hobby King as well for like 20 two or 25 bucks or something is a six cell Turnigy again. It's the same brand lithium polymer it does everything does lithium polymer nickel metal of various lithium types nickel metal hydride NiCad lead acid up to six cells. Of course this is only

**Dave Jones:** a single cell. It's really nice. I mean for like under 30 bucks. It's absolutely incredible. So that's what I charged up this battery with it's got the big positive and negative banana terminals out there. I actually use this to charge up my batteries for my quadcopter. They're also Turnigy lithium polymer high discharge batteries as well. They're 35 35 to 45 C discharge for my quadcopter / Canyon Copter. So yeah, really quite neat. So I have fully charged this battery according to this thing. So, let's give

**Dave Jones:** it a go. And of course, fully charged you would expect it to read 4.20 volts and that's exactly what we get. As I've mentioned before, this BK Precision Electronic Load is really incredibly accurate as good or better than your typical Fluke high-end Fluke multimeter.

**Dave Jones:** So, you know, really precision bit of kit. And as you can see, it's got the link remote function on there. So, it is hooked up to the software and ready to go. And here's the PV8500 PC software that comes with it and it looks rather neat. It is actually hooked up. So, it's actually monitoring this thing at the moment. You can see that it's 4.2 volts here. I don't like these dicky readouts. They're actually quite hard to read. They've made them look like seven segment. It looks worse in

**Dave Jones:** real life than on the camera here. But those background ones just really bleed into the the digits don't stand out much at all. It's really quite annoying. So, they tried to go all wanky there and they've just failed. Anyway, you can set it up to various like constant voltage mode, constant current mode, constant resistance mode, and constant power mode. And for those who want to whinge that I'm not actually screen capturing this thing, I'm just shooting the LCD with my camcorder, don't bother. Give me a break. Now, this Turnigy battery at a

**Dave Jones:** nominal 5,000 milliamp hours at 3.7 volts, you might multiply those two figures and it's got a nominal watt hour capacity which is sometimes more important than the milliamp hour capacity. In fact, in most cases it probably is. It's 18.5 watt hours nominal capacity. That means this thing should be able to, you know, roughly deliver 1 watt continuous power for 18 and a half hours. And ideally, I'd probably like to that's how I've tested batteries uh battery capacity in the past tested and specified battery capacity is in uh watt

**Dave Jones:** hours. So, I can probably do that here with the constant wattage mode. I could probably get the graph and everything, but I really want to um it doesn't look like you can you might be able to save the data and I don't know. I'm going to use the battery uh capacity wizard and check it out. It's got a specific battery discharge wizard.

**Dave Jones:** Zoom in on this sucker and uh it But, unfortunately, um like it looks quite neat, but unfortunately, it looks like it only has constant uh current capability. It doesn't allow you even though the supply uh this uh load can do it, it it doesn't allow you to do constant resistance or constant uh wattage, constant power, which is really quite annoying. But, anyway, it looks like we'll have to get our uh discharge um capacity uh graph in um continuous current because the reason you want to use continuous is because the DC to DC

**Dave Jones:** converter is essentially a continuous power and most um you know, products that are, you know, they're going to operate on on an average continuous power and the DC to DC converter is going to have an efficiency loss there, but it's essentially constant power. So, that's why it's more useful to uh analyze and specify your batteries in terms of watt hours for a project like this. But, anyway, we don't have that um luxury here. So, um uh you know, milliamp hours will do. So, this is has a nominal 5,000 milliamp

**Dave Jones:** hour at uh I don't know what that's rated at. I can't get the data sheet if it's actually rated for the full 20C or it's rated for 1C discharge or whatever it is. I don't know. So, we will just have to uh um just discharge it at 1C, see if it gets around about that figure. And of course, once it's finished doing it, it will actually calculate the capacity or should calculate the capacity in milliamp hours. Haven't actually tried it yet. Now, when you're testing these

**Dave Jones:** batteries, you want them not to just discharge them all the way. You can damage the thing. So, you don't want to leave the thing running overnight and come back and found, "Oh, it didn't cut out." And you know, you've ruined your battery.

**Dave Jones:** So, you want this setting they've got a safety volt setting here and you can set that to a minimum voltage and I presume when it gets down to that minimum voltage it will just stop the discharge. And or you can do it based on time or you can do it based on capacity as well. So, if you know this thing has a certain capacity, then you know, you do it. I the safe the best way to do it is with the safety voltage. Now, I don't have the data sheet for this

**Dave Jones:** thing, but the next best thing, we do have a Panasonic data sheet for a you know, a similar lithium polymer cell not as high capacity. It's only rated for you know, 2900 milliamp hours, but it's going to be very similar and the I've gone I've done videos on these you know, lithium polymer charging tutorials and stuff like that.

**Dave Jones:** Various battery testing battery capacity testing tutorials before. So, check those out if you want to, but it's going to have a similar this this Turnigy one should have a very similar discharge characteristic to this cuz it's also a lithium polymer standard 4.2 charging voltage and safety cut out voltage I reckon should be about 3 volts cuz really that's where it you know, it just drops off like that. Just drops off like a brick wall and you've used up you know, 95 to 99% of your usable capacity

**Dave Jones:** of your battery. So, you really don't want the thing to run under 3 volts. If you want to squeeze an extra percent out, maybe you could go under that, but you know, not 3 volts. So, we'll set our safety voltage down here to 3 volts.

**Dave Jones:** And uh yeah, I assume that would do that. Our sampling time, uh I don't know, it goes for an hour. We'll set up Let's disable that. So, it's going to sample once per second. And uh now all we need to do is set up the discharge current. And it looks like it's got a discharge current list over here. And um this is rather interesting. Looks like it's set up like multiple stages. Um but we really don't need that. So, can I just delete I wonder if I can just delete one of

**Dave Jones:** those. Import, export, no. Cell. So, we want to discharge this thing at 1 C just to get a uh baseline of how this thing works. So, um you know, it's it's got a very low ESR, this thing. It's capable of 20 C discharge.

**Dave Jones:** So, it'll easily handle uh 5 amp discharge, no problem at all. And really 5 amps is uh well above uh well, quite significantly above any uh discharge current that's going to be used in say my little portable USB power supply. But it'll give us good baseline. So, it should do that, I believe.

**Dave Jones:** It should uh as soon as I press go, start down here, it should start discharging at 5 amps immediately for 2 hours. But we know it's going to be all over in 1. And it should our safety voltage cut out at 3 volts. I'm assuming. The help doesn't tell me that, but um you know, based on my experience, that's what this kind of software should do. And um I've mentioned before in that previous um in my electronic load uh tutorial I I project video, I think, that you can do

**Dave Jones:** this yourself. You don't need a fancy 300 watt programmable DC electronic uh load. You can design You can design and build your own load. A lot of people, very popular project, actually. A lot of people on the EEVblog forum are designing and building really quite nice do-it-yourself electronic loads. And a lot of them are even microcontroller programmable or and/or PC programmable supplies. So, you can do this yourself.

**Dave Jones:** Um you can do it with a DAC card and a you know, and a FET and you know, not much else and an op-amp, not much else really. So, um you don't necessarily need a high-end electronic load like this one to get these sort of discharge characteristic uh curves. You can certainly do it yourself. And I've uh done it myself before using, you know, National Instruments DAC card or something like that and a little black box which, you know, discharges batteries. Or if, you know, I've done it in the manual method.

**Dave Jones:** I've designed my own little battery discharge logger over the years and there's many different ways to do it. But anyway, I'm going to give this a go. So, here we go. I'm going to press uh start and hopefully this thing will jump up to 5 amps and it will start recording and get our discharge curves. So, here we go.

**Dave Jones:** Uh time, yes. Safety voltage, 3 volts. Here we go. Start. And I've started, but whoop. 4 volts? No. What's going on? Oh, I think I know what I've done wrong. It's delay. This is a delay. It's actually a delay before it starts doing that. So, you want to start that with delay zero.

**Dave Jones:** Like that. Okay. So, it was it was waiting 2 hours. So, let's actually set that to, you know, seconds. So, delay 0 seconds. It doesn't allow us It allows us 10 milliseconds minimum. So, right. I I now it should um after 1 second delay jump to 5 amps. I think that's what it's saying there.

**Dave Jones:** Okay, there we go. And yep, we are 5 amps and spot on 5 amps and we're dropping 4.07 4.2 you remember it was at? It's instantly dropped down to 4.07 due to the internal ESR and uh you'll find that will continue to drop of course until we get down to 3 volts which should be our safety cut off voltage here.

**Dave Jones:** And uh so I could hopefully safely go away, but it's only an hour. I'll still be here. Um so we'll come back when that is done and we should see you can start see it's slowly starting to step down there.

**Dave Jones:** Little tiny step. So we should see our discharge curve look very close to that. We'll get a sharper uh drop at the start and then you know, a reasonably linear slope and then it'll start to curve off, curve off and then boom, should drop off the end there. Um yeah, probably this one might be a little bit flatter than that at the end point. I don't know. We'll find out.

**Dave Jones:** That's the idea of this test. But anyway, there's our capacity going up, our capacity in amp hours. I'm assuming it is because it's voltage and current. So it'd be um amp hour capacity. So it is working very nicely.

**Dave Jones:** See you in an hour. And I lied, it's not an hour yet. Uh we're at about 1.87. I couldn't help myself. Had to press record again. Uh 1 1. 87 uh amp hours at the moment. Uh and uh we're you know, we're still at 3.75 volts here and it looks like a linear drop, but it's uh not going to be by the time we get to the end of it. And uh just in case you're wondering, uh no, this thing does not get warm at all

**Dave Jones:** because the internal ESR is so low. Internal ESR of a battery is what actually causes them to heat up, of course. And, this one's designed for 20 times this discharge current. So, you won't even see this thing right, you know, rise in temperature by a degree.

**Dave Jones:** And, what do you know? It's almost an hour there to completion time. It seems to have stopped. And, it's, yeah, we were practically spot on the 5 amp hours there. So, it is essentially exactly as rated right there. And, it's jumped back up, of course. It's jumped back up to 3.16 volts cuz there's no longer any load. But, that was practically spot on an hour. Go figure.

**Dave Jones:** Geez, they don't lie on their label, do they? Now, whether or not that capacity is the same at 20 C, I don't know. You'd expect it to be a bit less, but there you go. And, we have that characteristic discharge curve with that fall off, rapid fall off. And, yeah, if we went down to like 2.6, it just would have fall It'll just fall off like a brick wall right there. So, at 3 volt cutoff, we're using uh, you know, 95% plus capacity of the battery, 98,

**Dave Jones:** maybe even 99% capacity of the battery. So, the low voltage battery detection in this micro supply should be set to around 3 volts. And, it can like automatically switch off the output once it reaches that and stuff like that.

**Dave Jones:** There's no buzzer in it to sort of alert you, but the LCD can certainly pop up low bat, low bat. And, we can view report down here. But, before I do that, I think I'll uh hit that save curve to file, and bingo, it allows you to uh save that to a bitmap or nice JPEG or PNG. Let's choose PNG.

**Dave Jones:** Don't mind PNG, so we can save that. We've got our graph, and uh presumably we can save our data as well because uh load plot from file, save plot to file, we can .plt files. Well, yeah, whatever. Okay.

**Dave Jones:** And uh presumably we can export Well, maybe if we uh go into view report, we can export. Excel or TXT. Excellent. Well, we should be able to name TXT. I don't see any data in there, though, so maybe it's uh Where are you, date? No. Not sure what's going on there.

**Dave Jones:** Hmm. So, that's not a bad little app. It certainly did cut out at the safety voltage of 3 volts, which occurred very rapidly there. And if we left it running after that, if you were doing this test manual, for example, and even if you're sitting there watching it, but you weren't paying attention because you're too busy soldering something for a couple of minutes, well, you know, your battery drops down, and you can uh over discharge your battery, and uh it won't be a happy little camper,

**Dave Jones:** that's for sure. So, having a safety cutoff like this works really well. Now, the other thing they've got is um the X axis here is actually in capacity. Um usually I prefer that in time, but we should be able to export the uh data and do that in uh time. I mean, sometimes you want it in capacity, but others you want time, but our depletion time was 59 minutes and 11 seconds and 4.2 volts start voltage, and it's uh almost smack on 5 amp hours capacity with a

**Dave Jones:** constant current load that will change like with a voltage like in terms of watt hours with a constant wattage load, but there you go. That gives you a good indication that this cell is certainly not Well, they're certainly not ripping you off.

**Dave Jones:** Anyway, it does meet its claimed spec. So, there you go. That's just a little update on the USB power supply and I will endeavor to spend some more time on it. So, hopefully more videos coming soon. Catch you next time.
