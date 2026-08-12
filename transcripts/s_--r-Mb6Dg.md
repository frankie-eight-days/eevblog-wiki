---
video_id: s_--r-Mb6Dg
title: EEVblog #297 - Canon LANC Bus Reverse Engineering
url: https://www.youtube.com/watch?v=s_--r-Mb6Dg
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 23, "3": 43, "4": 55, "5": 78, "6": 85, "7": 94, "8": 106, "9": 130, "10": 145, "11": 164, "12": 175, "13": 187, "14": 199, "15": 220, "16": 233, "17": 244, "18": 257, "19": 270, "20": 280, "21": 294, "22": 305, "23": 321, "24": 332, "25": 341, "26": 355, "27": 370, "28": 382, "29": 393, "30": 405, "31": 422, "32": 439, "33": 448, "34": 470, "35": 481, "36": 488, "37": 497, "38": 510, "39": 521, "40": 541, "41": 555, "42": 571, "43": 587, "44": 603, "45": 615, "46": 633, "47": 644, "48": 661, "49": 676, "50": 692, "51": 714, "52": 730, "53": 743, "54": 752, "55": 770, "56": 781, "57": 793, "58": 808, "59": 832, "60": 848, "61": 868, "62": 879, "63": 895, "64": 906, "65": 925, "66": 940, "67": 959, "68": 975, "69": 987, "70": 1001, "71": 1014, "72": 1029, "73": 1039, "74": 1049, "75": 1065, "76": 1076, "77": 1094, "78": 1110, "79": 1120, "80": 1130, "81": 1146, "82": 1162, "83": 1184, "84": 1204, "85": 1224, "86": 1237, "87": 1250}
---

**Dave Jones:** Hi, check out this cool on air uh display light I scored on eBay. It's really quite neat. It's one of these um etched uh polycarbonate um surfaces like this.

**Dave Jones:** So, it's actually etched in the back there. It's actually routed in there and it just lights it up on the edge and it's really quite neat. I thought, you know, it'd be nice thing to stick on the wall and have it when I'm actually recording.

**Dave Jones:** Makes it feel like a professional recording studio, you know. Fantastic. Because uh one of the more annoying aspects of my Canon HFG10 video camera I'm using to record this blog is that there's no light on top to tell me when it's actually recording, especially not like right in line with the lens.

**Dave Jones:** So, I'm looking at the lens instead of looking at the screen like this because what it uh all it has, you've seen these video cameras, very common, they've only got a little record light, one of those little red circles.

**Dave Jones:** It's only it's tiny. It's on the LCD. When I hit record, that pops up. Sure enough, it's telling me it's recording. But sometimes I sit here yapping away in front of the camera for 5 minutes and I realize I haven't hit record or I well, I pressed it and it didn't register or I or I pressed it and accidentally stopped instead of started recording and occasionally I lose uh

**Dave Jones:** info. It's really annoying. So, I thought it'd be nice to maybe hack in this thing into the camera. I'm obviously not going to stick this on top of the camera.

**Dave Jones:** It would just be a fun thing to have up on the wall, but it'd be nice if it was synchronized to my video camera, to the actual record function in the video camera.

**Dave Jones:** So, I thought maybe is there some way I can hack it into the uh camera itself. And um I I don't know if it's possible. So, that's what this video is going to be about.

**Dave Jones:** A start of an investigation into the LAN C wireless standard. This is one of these wired remote controls I've got for my camera. It's not a genuine uh Canon one, but uh it allows you to zoom in and zoom out and change the rate of how fast you zoom in and zoom out and stuff like that and allows you to start and stop recording as well.

**Dave Jones:** This is and uh set the focus. It's got a few other features which don't work on this Canon camera cuz um the protocol is called LAN C L C and I believe it's originally it's mostly on Sony cameras but the Canon ones do have it too.

**Dave Jones:** And uh it it is a bit of a standard but not all cameras implement all functions. And I've heard that apparently uh not only can you send signals to the camera to start, stop, and do stuff like that, but I think it actually sends out data on this one wire bus as well.

**Dave Jones:** It's a one wire, it's a five, I believe it's a 5V one wire bus. I haven't actually uh checked it yet. I've just done a little bit of Googling and apparently it might actually send out some data.

**Dave Jones:** So, if it does send out a data saying I'm recording, maybe I can tap into that and turn on an LED or something like that, your light up or switcher relay which you know lights up this sign or something.

**Dave Jones:** So, I thought I'd just have a look, take this thing apart and uh try and capture the data on this LAN C bus and see what I get. Let's give it a go.

**Dave Jones:** Hang on. Oh, I'll show you a really annoying look. Rant time. Okay. You design one of these. Okay. You're in a quiet recording studio. Okay. And look, you can hear the tactile button.

**Dave Jones:** It's ridiculous. Why use tact buttons? Why not use the soft rubber ones so you can't hear them? It's bloody ridiculous. I'm going to press stop now. Now, this is actually a bank brand one.

**Dave Jones:** It's just one of these cheap, you know, eBay uh imitation ones. And uh there are a couple of screws on the back and annoyingly a couple of screws under the uh under the overlay on the top there.

**Dave Jones:** And I had to peel that back and get the screws out. But anyway, we are in in like Flynn. Here we go. There we go. Tada. And we got one chip on the back.

**Dave Jones:** And that's it. Let's take a look at it. And there's not much on here at all. We've got a Wholettech brand uh micro controller here. There reasonably common in like very extremely lowcost uh consumer gear.

**Dave Jones:** We've got a resonator here and we've got looks like a some sort of regulator there and a couple of electrolytic caps and a few um SO 23s and diodes and other stuff.

**Dave Jones:** It's got a bit more than what I uh thought would be in there, but anyway. Yeah, there's not uh not much at all. We've got the um we've got the soft button uh switches down here, which of course the overlay goes on top.

**Dave Jones:** They've got the you know the carbonized um uh bit on the bottom of the rubber. The conductive uh bit there which just shorts out the two tracks on the board.

**Dave Jones:** We've got these annoying tacked switches. Why generate too much noise? Ridiculous. And um we've got a rotary uh encoder switch here to choose the different um values for the uh speed control.

**Dave Jones:** And that's about it. Anyway, um we've only got the it looks like we've got um three wires coming in. So one is presumably power, ground, and the other's data.

**Dave Jones:** Obviously based on the colors, I'd say white's your data and red's your power and blacks your ground. So should be able to hook the scope onto this thing and capture the data.

**Dave Jones:** uh well coming out of this thing into the camera, but more importantly to see if anything's coming out of the camera into this board so that we can possibly uh design our own little widget and uh capture that data.

**Dave Jones:** All right, let's do some measurements here. First off, we've got our our ground is on the side of the cap there. So, same as the input pins, but it's easier to probe the solder pads there.

**Dave Jones:** And we're getting Hey, 5.68. That's rather unusual. That's what we got coming in on the red and the black wires. Why that's not 5 volts. It's clearly not, you know, your regular 5 vols plus minus 5%.

**Dave Jones:** It's not your normal 5 volt supply rail. So that's rather odd. And let's measure the um presumably this uh electrolytic here is on the output of this voltage regulator.

**Dave Jones:** So I don't even need to know the pin out of the regulator. And hey, no surprises at all. 3.3 volt rail. So, um, it looks like the microcontroller is powered from the 3.3 volt, uh, rail.

**Dave Jones:** And, uh, presumably that little I'm going to guess that that transistor there is the open collector switching transistor for the bus, which pulls that bus line low. That would be my guess.

**Dave Jones:** And I've just soldered a quick and dirty lead onto there so that I can attach my scope probe onto here. and uh you know because you don't want to be trying to hold it, you know, probe it on there and operate the scope when you're trying to reverse engineer these things and hack them.

**Dave Jones:** It's just it's just not good. So, let's hook that up to the scope and see if we can capture anything. And sure enough, we are getting something on there.

**Dave Jones:** We're getting multiple data packets. Look at that. No problems at all. Now, one of the uh problems with my uh Agyant 3000 series scope here is that it doesn't it's got really good uh signal um uh like many different uh triggering modes like a serial decode modes, but it doesn't have um one wire bus.

**Dave Jones:** So, um it's, you know, it's just really annoying. So, I'll just decode this manually. But what I like I can just, you know, single shot capture that and have a look.

**Dave Jones:** But you'll notice that uh the triggering is not that stable. It jumps around. So what I'm going to do is just try and uh just for the fun of it.

**Dave Jones:** Not that I really need to, but I'm going to try and get a stable trigger based on the dead period in there where it's high. So to do that, what we do is we capture it here.

**Dave Jones:** And we can see we're getting about 10 milliseconds per division here. So it's roughly 10 milliseconds that that well it's actually slightly less than 10 milliseconds by the looks of it where it's high.

**Dave Jones:** So what we want to do is we want to go into our trigger menu here and instead of our regular edge trigger we want to set a pulse width trigger and we want the sources channel one of course but and we want it to be high.

**Dave Jones:** So we choose the high one there for greater than. So not less than but greater than 20 nconds. We want it greater than let's say 6 milliseconds. Five or six milliseconds or to do it because there's nothing else in there.

**Dave Jones:** Getting fussy now. 6.0 milliseconds. Let's try that. And so when it detects a 6 millisecond high period like that, it will trigger. So now we should get a very stable trigger hopefully.

**Dave Jones:** Fingers crossed. Let's try it. There we go. Perfect. Bingo. And that's a way to get nice steady triggering on your scope in order to see those packets. Beautiful. So now we can actually singleshot capture this.

**Dave Jones:** And at first I thought, oh okay, this is, you know, these are individual packets like this. But uh zooming in because I I knew that it was uh supposed to be like a um 8 bit uh field.

**Dave Jones:** There's supposed to be a start bit and then a stop bit at the end of it. It just didn't seem right. And what's actually happening is this entire packet here is not one packet of data.

**Dave Jones:** It's actually one two three four five six seven or eight I think eight packets of data. Now this seems to be matching the information on the I found on a website uh precisely.

**Dave Jones:** We've got one bunch of information here which they call a telegram apparently. So one telegram of information contains those eight individual packets of one start bit, eight data bits and one stop bit.

**Dave Jones:** And the distance between two telegrams uh varies but depending on the type of camera. Now I'm in Australia so I've got a PAL camera. I didn't import this one.

**Dave Jones:** It's an Australian version. So it uses the PAL standard and it apparently has 20 milliseconds between It's not quite. I I haven't got the cursor right in there. I could go in there and set it up, but it's supposed to have 20 milliseconds between the uh telegrams there.

**Dave Jones:** And the NTSC version has 16.6 milliseconds. So, I'm certainly getting very close to my 20 there. And each individual packet, one, two, three, four, five, six, seven, eight of them here.

**Dave Jones:** Um the distance between those is supposed to be supposed to be uh 100 uh 1.2 milliseconds to 1.4 I believe. So there you go. I'm getting 1 we can get in there.

**Dave Jones:** I'm getting 1.26 or thereabouts. 1.25 milliseconds between the individual packets. And one of the good things about and with each bit by the way being 104 microsconds. So if we go in there and have a look at that we can now is it 104?

**Dave Jones:** It is bingo 100 and four or pretty close to it. And the good thing about this is that apparently the timing is exactly the same as RS232 at 9600 boards.

**Dave Jones:** So maybe I can actually uh use my serial decode feature after all. So if we go into our serial trigger mode here, we can set it up for RS UART RS232.

**Dave Jones:** And we can set the signals up. Channel one is our receive. We're not worrying about our transmit. We don't have it. And our bus uh configuration. We can set it up eight data bits.

**Dave Jones:** Uh no par. The board rate 9600 bits per second. So we're right there. and the uh bit order at least significant bit first. So bit zero first when you zoom in there it'll be bit zero first 1 2 3 4 5 6 7 8.

**Dave Jones:** So let's give that a go. And we should be able to decode that. And there it is. And it doesn't like that at all. It's decoding the odd bit.

**Dave Jones:** But I think we've got our polarity idle low incorrect here. We're idling high. So, we need to switch that to idle high. And let's single shot trigger that again.

**Dave Jones:** Bingo. There you go. We now have our decoded data. Beautiful. And we can see that changing in real time. Fantastic. Because this scope actually does hardware decoding of this uh serial interface in real time.

**Dave Jones:** So, we can even trigger off um certain data bits if we or certain bytes if we want to. Now, because this is continually changing like this and I'm not pressing any buttons on the remote control, then I'm going to presume that uh the uh the controller, the wired remote control doesn't actually send any information until you press a button.

**Dave Jones:** I it just wouldn't make sense to do that. I could be wrong, but uh Gutfield says it's not going to do that. So, clearly data is changing here. So this indicates that this is changing data being output from the camera.

**Dave Jones:** So I think the camera is well and truly outputting some sort of data either a time code or something like that which I've read it actually might do. Um so cuz that almost looks like it's doing some sort of counting you know very fast some sort of uh counting thing as it goes up or something like that.

**Dave Jones:** It's certainly outputting some sort of information. And then we're getting this blip blip blip blip blip blip thing happening here. I'm not sure what's going on there. All right.

**Dave Jones:** Now, let's see what happens here if I press the zoom button. Bang. Look at that. The first two bites there are first two packets are changing. The other ones seem to be continuing on their merry way.

**Dave Jones:** And if I hold it down, let's zoom into those first two packets, shall we? There we go. So, we're in there. Let's turn off the cursors for a minute.

**Dave Jones:** And let's press the down zoom out, I think it is. Bingo. Look at that. Those two bits certainly changing. And so, what it looks like happening here is that some like the first two bytes are input bytes.

**Dave Jones:** So they're input bytes to the camcorder, whereas these ones over here seem to be output bytes that are outputting information. So the first one, so if I press the zoom out, I believe there's that consistent pattern there.

**Dave Jones:** There it is. And if I do the other one, zoom in, bingo, it's exactly the same. The first bite's exactly the same if I alternate between the two. But you'll notice that this second one here that zoom out and zoom in doesn't have that bingo.

**Dave Jones:** That works really well. So it goes from FF to So we're looking at D7 uh there in hex of course. Uh D7 and FD is the zoom in I believe and then zoom out.

**Dave Jones:** Aha. Look the data bit's changing because I've changed my rotary encoder. So it is now zooming in and zooming out as I press those buttons. But if I put my rotary encoder to a certain spot, I can get it.

**Dave Jones:** So it actually ah look. Yeah, it's changing. Okay. So there's not doesn't look like there's a fixed code based on just the zoom in zoom out. It's a code based on what level of zoom in and zoom out you have.

**Dave Jones:** So, if I hold, let's say, if I hold down zoom out, and I change the rotor encoder, it's not a rotor encoder, it's a switch. There we go. So, I'm turning the switch and it's cycling through.

**Dave Jones:** Bingo. There you go. It's got a different command. So, there it is. As I press these switches and so I hold in the zoom and I can touch the switch.

**Dave Jones:** faster, faster, faster, slower to a point where I can actually get it to Yeah, it's tiny. So, you hardly even notice. I'm holding that and it's slowly zooming out.

**Dave Jones:** There we go. So, that's uh that's rather neat. We're certainly capturing this data and it looks like it is outputting data here, then that's really what we're interested in.

**Dave Jones:** And what I'm doing quickly now is just pressing the record off and on. Now obviously I can't capture the screen the same time as I'm not recording but I can't see any differences in these packets here these bites here these three which are after the first two.

**Dave Jones:** So that's bite uh uh two three and four. I can't see anything in there when I start and stop the record button. I can't see anything change. So there's nothing happening there.

**Dave Jones:** And of course, I don't have to uh dick around trying to reverse engineer this because somebody else has already done it for me. And the info is on that uh website and but it doesn't mean it's going to be specific to this particular camera though because not all cameras, especially Canons, don't implement everything.

**Dave Jones:** But it basically says that the uh fourth packet here, the fourth bite is the one that contains the status information coming from the camera. So, we've got uh bite zero 1 2 3 4.

**Dave Jones:** So, that one in there with the double bit, that's the one, the double low there. That's the one we're interested in. That's the one we want to see. And we'll see if it changes.

**Dave Jones:** So, I'm going to press uh stop here and see if it there's any difference. No, unfortunately not. I pressed uh stop and that packet did not change at all.

**Dave Jones:** That individual bite didn't change. Not a sausage. Didn't see a damn thing. That's disappointing. That's supposed to be the status coming from the camera. So maybe this whole idea is shot down right there.

**Dave Jones:** Maybe this Canon camera just does not output its uh record, stop, you know, play, pause status. Bummer. And these last three packets here, I'm not seeing any change there at all.

**Dave Jones:** We're getting data out of it, but I'm I'm not I don't care too much about that. I'm pressing stop and start record here and I'm not seeing it's just, you know, it's just outputting a whole bunch of data which might be some sort of time code, but I can't see any like fixed individual bit change in there when I press start and stop.

**Dave Jones:** So, this is not looking at all promising. What a bummer. Well, I think I've had enough for today. I can't find it. I expected to see at least one of those bits in there sort of toggle um when I pressed the record button, but unfortunately I'm not seeing that at all.

**Dave Jones:** I'm going to have to review the footage again, play around with it some more, but I think I'll call it quits for now. But anyway, that was a an interesting first investigation anyway into the LAN Cabus and uh what it outputs from this Canon HF G10 camera.

**Dave Jones:** So, I it's worthy of a bit more investigation. So, if you noticed uh something on the video or you know something more about it specifically for this uh Canon or Canon cameras in general, um please let me know.

**Dave Jones:** jump on over to the uh forum or put it in the comments or something like that. So, I hope you enjoyed that. Just a quick little uh sort of hack debugging video there.

**Dave Jones:** And as always, if you like the video, please give it a thumbs up and I'll catch you next time.
