---
video_id: f-K5WFaStwg
title: EEVblog #227 - Light Scythe
url: https://www.youtube.com/watch?v=f-K5WFaStwg
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 29, "2": 48, "3": 70, "4": 80, "5": 94, "6": 117, "7": 137, "8": 153, "9": 167, "10": 190, "11": 205, "12": 215, "13": 241, "14": 254, "15": 283, "16": 299, "17": 320, "18": 337, "19": 359, "20": 371, "21": 399, "22": 417, "23": 446, "24": 462, "25": 477, "26": 491, "27": 503, "28": 518, "29": 537, "30": 550, "31": 571, "32": 591, "33": 613, "34": 633, "35": 659, "36": 675, "37": 689, "38": 702, "39": 716, "40": 732, "41": 748, "42": 769, "43": 787, "44": 803, "45": 819, "46": 836, "47": 852, "48": 865, "49": 883, "50": 899, "51": 913, "52": 929, "53": 945, "54": 966, "55": 987, "56": 1002, "57": 1017, "58": 1040, "59": 1056, "60": 1065, "61": 1082, "62": 1098, "63": 1116, "64": 1130, "65": 1145, "66": 1162, "67": 1192, "68": 1206, "69": 1222, "70": 1235, "71": 1278, "72": 1296, "73": 1309, "74": 1329, "75": 1348, "76": 1361, "77": 1378, "78": 1399, "79": 1412, "80": 1426, "81": 1444, "82": 1461, "83": 1480, "84": 1495}
---

**Dave Jones:** Ten had some perfect examples of light painting, which is using a camera with a long exposure and then a light source, and moving around in creative ways to get very, very unusual effects. So here's a lot of stuff. There's a huge community of open source, yeah, open

**Dave Jones:** source, sorry, light paint is out there already. You can get some really eerie effects, you can highlight buildings and landscapes and things that you wouldn't otherwise kind of see. I really love that concept and I wanted to, a way to make the images a bit more controlled,

**Dave Jones:** as in putting a particular effect that I want on them. So, what I did was, take, here's another example. This is Roberts and Valenswassers in the hack space. I am a cat, a few people recognise this. This guy's an internet celebrity. And we culminated the steps of the upper house

**Dave Jones:** for an evening out. I really love this sort of image because it shows that it's actually really there, it's not photoshopped in. You can see the reflections, anywhere that you've got a slightly wet surface, we were really lucky because it happened to be raining.

**Dave Jones:** Here's another one, you can see the actual, the way that it's interacting with the environment. If you have puddles and things, they look spectacular as well. So what's involved with actually making a light side? This is a complete set of hardware right here.

**Dave Jones:** I've actually got two of them, there's two of them in that photo. What it is, is the image is created on the machine, on the PC first of all. So you can choose a picture, you can choose text, whatever you like. There's a set of software which I made which will automatically take

**Dave Jones:** text or images and convert it into a series of pixels that are compatible with this strip. This little thing here is a radio link, I'm sure you guys have seen the XBees. They're small, I think this one's a 900 megahertz radio. And it's basically, if you're doing

**Dave Jones:** an electronics project, it's a fantastic way to get data from one location to another and sort of forget about the actual implementation of it. That might be a bit of heresy to a radio club actually. I can just treat this like a serial pipe and I just pipe the data

**Dave Jones:** in at one end and it comes out the other. All I've had to do is set a network number. If I want to do one-to-one communication, I can do that, but at the moment it's one-to-many. So I can have multiple light sides all imaging the same information at the same time.

**Dave Jones:** So you can have a couple of people running around in the photo doing weird things. Inside the box itself, I'll show you on my, let's not plug in. This is extremely complicated compared to what it actually needs to be. The next generation is going to be much, much smaller and is actually going to live entirely inside the

**Dave Jones:** staff itself. So what we've got is a microcontroller on the bottom there, the red one. It's the Arduino, if anyone's familiar with them. They're cheap, they're friendly, they're open source. Anyone can get in and use them. We've got the RF module on the top, that's

**Dave Jones:** the XP. On top of that, we've just got a little custom circuit board that I made, which has got some voltage level converters in it, because this board is really, really nice and it handles batteries really nicely, but unfortunately it's all 3.3 volt stuff.

**Dave Jones:** So this script actually requires 5 volts in order to operate. Just a simple interface, I've got one push button and one dial. The dial does nothing. So that's future proof. The main magic is in economies of scale and the fact that you can buy this LED strip for

**Dave Jones:** about $35 a meter from China. Inside it, it's really hard to see, but there's actually two LEDs and then a chip for each pair of LEDs. And that actually takes care of everything that's needed to drive the LEDs and all the colour and all the actual interfacing.

**Dave Jones:** So all I do is send serial data down one end and it's clocked out the other end and it just continues all along the end of the chain. So, I'm going to just power that up. Test pattern. And you can cut this to length, so if you want to make a Christmas light since your

**Dave Jones:** program will cost a few dollars' worth of components and then the strip. So the software itself. All this is open source, it's all on my website if anyone wants to make their own. So you create the image. There is, if you want to make your own text, and I'll do

**Dave Jones:** that right now actually. Okay, so I just go create text. And what's your call sign again? DK2MB. DK2MB. It's creating the text with DK2MB. Gives a nice curly font that I chose previously. Got the green as the inside colour, blue as the outside colour.

**Dave Jones:** All this is selectable and programmable and you can change it to your satisfaction later on. It's saying press enter to transmit it to the size. My radio link's plugged in so I just hit enter. It's opened the file. It's calculated that there are 290 columns wide in this image.

**Dave Jones:** It says I'll give each column 20 milliseconds, so the total time to do the entire thing is 5.8 seconds. So what I'll do is, and it's opened the serial port and it's ready to go. This is actually like the third generation of LightSide.

**Dave Jones:** It took me a couple generations to figure out that it was a much better idea for me to have a push button here so that I can push it when I'm in the field rather than running back to the laptop, hitting go, running back

**Dave Jones:** to the camera, hitting the shutter button and then trying to get in the shot. If I push this now, it'll just start displaying. Ready when you are. Oh, how long? About 6 seconds, maybe 10 is fair. We're going to do live science. That's true.

**Dave Jones:** You might see it as a bit of an after. It might be very faint but it should be there. Is it better with the lights off maybe? Yeah, if you can turn the lights off easily that's good. At any rate, if it doesn't work, we'll just turn the lights off.

**Dave Jones:** 3, 2, 1. It's a bit hard to capture it in here because it's... The screen there is burning out. Yeah, yeah. And I've got the blu-ray. I think everyone sees the rough principle of the idea. Here's the XBee unit itself. It's tiny as it is.

**Dave Jones:** There's practically no power. This one's actually sitting on a little USB shield so you can just plug it into the PC and it shows up as a serial device. It works out of the box with pretty much no configuration but you can set it up to be

**Dave Jones:** more sophisticated so it will only talk one-to-one or you can multicast or you can do pretty much anything you can do with a medium packet radio setup but just over a really short range. I think this one is... This one is all of 60 milliwatts which is actually quite hefty.

**Dave Jones:** This is a 60 milliwatt one. This is, I think, the largest one you can get maybe. I bought this originally to be the telemetry for my quadcopter. I ended up using it for this instead because I want a high reliability serial link because

**Dave Jones:** there's nothing more frustrating than getting a shot, spending 10 minutes lining up to get a shot at the steps of the opera house and then you've lost some data because there was a bit of radio noise and so you've got an image which is almost perfect but there's

**Dave Jones:** some pixels that are stuffed up midway through the image so that's why I've gone for the 60 milliwatt one. I'll pass that around if anyone wants to have a look at it. They're cheapest chips. The cheapest module is about $20 and maybe $20 for the carrier board and the holder itself

**Dave Jones:** I've just laser cut really, really quickly and glued together. That text we saw where it created the nice cursive text is actually a thing called ImageMagick which is all free. You can drive it from the command line or you can drive it from a GUI.

**Dave Jones:** So what it does is you just give it a text and it makes the image and you can do things like resize an image or you can put text in it or you can make rectangles or you can desaturate or you can do pretty much anything you would do in Photoshop from the command line which

**Dave Jones:** is really, really handy when you're trying to do automated stuff like this where you just want to work with one command. So that makes the image. There's a couple of Python programs which will convert any GIF image into a light startable image and then there's LightSizeTransmit which actually transmits it over the serial link

**Dave Jones:** so those programs are all gathered together at the moment but you can run them separately if you need to. The limitations of colour. So here's the actual rainbow. Here's what this strip does at the moment. We're only limited to 7 colours. The next generation of strip which I actually have got but haven't been bothered to make

**Dave Jones:** the software for yet will have, instead of 7 colours, it will have 16 million colours. A little bit bigger. Yeah, exactly right. It's a proper 24-bit colour. Come to think of it, it may actually be dropped down to 7 bits worth of colour per channel.

**Dave Jones:** But at any rate, it's... And actually that is precisely the same price as the existing one. So there's clever buggers in trying to just keep making it cheaper and better. Is the light output for the LEDs matched? For each colour? Because I can see you might oversaturate on some colours and not others?

**Dave Jones:** Absolutely, absolutely. No. So this is a really good point. This strip, you just give it a 7 or an 8-bit value for red, green and blue per pixel. And you can choose, from that you can choose 16 million colours. My previous iteration, which never quite got into the working stage because of some timing issues,

**Dave Jones:** had a different module called Shift Bright in each one, instead of this really, really cheap strip. So the entire thing cost about $500 because Shift Brights are not cheap. And what the Shift Bright had was, in addition to you giving it the RGB,

**Dave Jones:** it also had a little E2 prom in there. So it has a little memory that allows you to compensate for the fact that not all LEDs are created equal. So if you wanted to be incredibly attentive about it, you could go through and calibrate each individual LED

**Dave Jones:** and you'd go, oh, number 7 is a bit bright, so let's have it turn things down automatically so I don't have to pre-process it. That never got off the ground, and then this stuff came out and $35 a metre is pretty darn good.

**Dave Jones:** I can't get past that. So each LED is reversible? Absolutely, absolutely. And it's a serial shift register. So you put data on this side and it gets squirted out on the other side. And the code is completely modular, so I just say this particular chain,

**Dave Jones:** I've got 64 vertical pixels here, and I can extend it as long as I like. So I have planned around making a 5 metre one that I can dangle off a bridge and then walk. Is it shift and latch? Is shift then latch, or is it...

**Dave Jones:** This particular strip, there's a clock, data and a latch. The next generation of the strip, which is the $16 million colour one, is just clock and data. But I think there's actually a latch command or something like that that gets propagated, so it doesn't have...

**Dave Jones:** yeah, you're exactly right. If there's no latch, then what you have is the image slowly marching down the strip, whereas if, as the way it is now, the image gets pushed there and then rolled across off the LEDs with one command. So there's no weird persistence of vision or strange visual artefacts that you get.

**Dave Jones:** Although, wouldn't a long exposure take care of that, possibly? It's... If you move it long enough? Yeah, LEDs are really unforgiving in long exposures. So what I was really, really concerned about with this initially was... This is fine because all of these... this is bang, bang.

**Dave Jones:** All of these are red, green and blue, fully on or fully off. The next generation of stuff has... everyone knows PWM. So it does PWM of the registers... sorry, of the LEDs inside. So if it's got... if you set your red to be half brightness,

**Dave Jones:** it's actually flipping it on and off at a particular frequency, and I was worried that that would show up in the long exposure photo. I've done a couple of preliminary tests, and no, it doesn't. So I'm pretty thankful for that, because otherwise you'd get some fairly funky artefacts in your photos.

**Dave Jones:** So what do the Chinese make this kit for? It's not just for... Yeah, yeah, yeah. They sell it... that's a really good question. Who knows what a lot of the stuff that's on, like, Deal Extreme and that is actually intended for. But... It must go to, like, web developers.

**Dave Jones:** Yeah, shop displays and discos and things like that. Yeah, typically it comes in... Yeah, yeah, it comes in a five-minute roll, and it has a little control board, and the control board has a couple of cheesy pre-programmed things in there. So it'll slice across colours, and it will fade between one and the other.

**Dave Jones:** You know, you can choose any particular colour, or you can have it fade between two different ones. You know, some reasonably limited pre-programmed stuff. But in order to get that kind of... something that you put in the window of your chemist shop or whatever,

**Dave Jones:** they've actually made a really, really sophisticated piece of technology that you can pipe through an entire image with. So I'm happy to... happy to purchase it now that the price has dropped down and hack away at it. Tips for taking photos. You need good friends.

**Dave Jones:** It'll hopefully stay good friends, because, yeah, a lot of patience is required, and it doesn't happen quickly. Cameras can do a long exposure. Pretty much any camera can do it nowadays, even simple point-and-shoots. The image you saw there was, what was that, six characters,

**Dave Jones:** and that was about six seconds, so that's a good example of how long your camera needs to be open for. If it's a much longer message, then I've done shots with 20-second exposures and 30-second exposures. This is the areas we're going to try in the future.

**Dave Jones:** Different fonts, different locations and effects. We were really lucky to have the Steps of the Opera House, because it had just been wet, and we're getting all these nice little specular reflections off it. Wet surface is fantastic. Glass walls are also fantastic. If you walk at an angle to the shot,

**Dave Jones:** you get this lovely swooshing effect where the image is coming out of nowhere. And there's a lot of ways to play around with it, and really just scratching the surface. That's pretty much it as far as the light side goes. Does anyone have any questions on that?

**Dave Jones:** Yeah. Yeah, that's... Not yet, but it's been on the to-do list, actually. You can certainly go... As you've seen, this is actually pumping out a new column of data every 20 million seconds. I can go faster than that. That's just a nice compromise value I've got for long exposures

**Dave Jones:** and being able to walk across a scene consistently. So you could... Sorry? Yes. So you could easily attach it to a car and... Yeah, I actually got contacted by a journalist asking me if you could use it on a racetrack and have it sort of sweeping out behind a race car.

**Dave Jones:** My answer was yes, but I haven't tried it yet. I've got a race car. I could try it. Yeah. Might have to line that up. Maybe I should try it on my little Subaru first. It could display the speed. Yeah, that's right, actually.

**Dave Jones:** 120 miles an hour. I'm actually really, really lazy. This thing's been sitting in my car for the last couple of months, actually, because it's a big pole and I forget to take it out when I get back home. Does the camera zoom on exposure?

**Dave Jones:** There's only one way to find out. I just imagine you screaming through a speed zone and they look at the photo and it just says, Sorry. I'm either going to be picking on or... It's just loser. Has anyone else thought of these? Yeah, I thought I was the first.

**Dave Jones:** There's actually a guy in Texas that has done a similar thing before, but in a much... I'm going to say uncategorised, so it's a much less user-friendly way. So he pre-programs it onto a microcontroller. Oh, yeah. And the way he actually edits his data is he has a big Excel sheet

**Dave Jones:** and then colours in the cells one by one. And that makes some Arduino code in a text thing and then you copy and paste that, put it in your IDE, download it. But it has the advantage that he can just work in the field with it.

**Dave Jones:** Yeah, yeah. Which is really cool. But it takes 10 times as long to set up for another shot. So that's when you did it at the opera house? Yes. How long would the exposure be on that? About 15 seconds for the... And you just walked across it with the same sort of principle you just used?

**Dave Jones:** Yes, absolutely. I'll just... I'll zoom back to the photo so you can see it again. That one there? Yeah, that was about 15 seconds. Actually, this is using two light sides. So I was standing in the front just holding mine. That's actually displaying the same image,

**Dave Jones:** but I'm keeping it stationary so we don't actually see the text. Right. And then a friend of mine was walking through in the background like that and getting a nice little sort of angle to the camera kind of perspective effect there. Yeah. And these people here, these were...

**Dave Jones:** These were performing a fantastic function. They're actually blocking the light because there's a lamppost just behind there. So we tried a couple of shots and there was this big kind of halo there. So it's like, ah, shit, Jim, are you going to stand there?

**Dave Jones:** Thanks. It's quite a challenge not to sort of do this as you walk along. It is, yeah. That's what I'm getting at. Yeah. I sort of obviously don't know enough about cameras, but why aren't we seeing a blur of the people, the person walking behind?

**Dave Jones:** They're staying extremely still. Yeah. I'm staying dead still and the person that's walking through, you actually are seeing a blur, but it's just so faint. OK. They're not really lit up by anything and they're holding the side out like that away from them.

**Dave Jones:** So you're just seeing this very, very faint and because there's so much bright lighting everywhere else, you can't really see it. Yeah. There's a couple of other ones where we sort of screwed up and the shot doesn't come out as well as you'd hope.

**Dave Jones:** You walk along for a bit and then you trip over the stick a bit or you bump it and then you end up in this really weird artifact where the text goes, ba-dunk, in the middle. And also, walking at a steady pace is really, really hard.

**Dave Jones:** So it takes a couple of tries before you get one that looks good. And also, getting everything synchronised is really tricky as well. It's a bit easier now that I've finally realised that the button on the front is a really good idea. That took like three generations worth of code before you go,

**Dave Jones:** button. Yeah, awesome. But couldn't you build a sort of wall at the end of it? So it would look at how fast you're going. Absolutely, yeah. There's a huge amount of tweaking and expansion. So you could actually set it up so that if you wanted to make

**Dave Jones:** an entire image like this, so you go, swish, swish, and it would do an image in mid-air, you could totally do that. There's a large amount of room for expansion and stuff like that. It's actually such a narrow line. So it looks like they come in half-metre lengths.

**Dave Jones:** Half-metre lengths in any way. You can see the join down there. Yeah, so joined together, this has got like three or four strips all in series. You can cut them every two pixels, as closely as you like. Is there any limit to how long you can join these things?

**Dave Jones:** By default, it's five metres long. It just behaves as a shift register, so you send data in one side and it comes out the other. I think you can join them up as long as you like. The only thing is that the copper tape that runs along

**Dave Jones:** will have a bit of voltage drop, so you'd want to have another power bus running to it every so often. Got it. I've had five-metre strips displaying images, no problem. Nice. And this is your controller here. Maybe two amps for the whole two minutes.

**Dave Jones:** So I'll just push the button and transmit the data to it. Whoa! Have you thought about putting this on some sort of dolly-based track system and pushing it along? Yeah, it'd be interesting to do. You can get a lot of smooth motion. Smooth motion.

**Dave Jones:** Especially if you had something like a skateboard and you could tilt the wheels a bit so it would do a nice little arc. Yes. That would be really cool. And maybe as the camera panned around like that, you could pan the camera and you could have the...

**Dave Jones:** Yeah, yeah. Oh, the camera. No, no, you couldn't, because it's going to be a stationary photo, doesn't it? Yeah, you could move it in synchronisation though. Because you're walking through 3DC and you're leaving a ribbon of image behind you, so as long as the camera isn't moving too much

**Dave Jones:** or too far in and out with respect to that side, you can do whatever you like. Actually, after I published it, I got a couple of people contacting me, including an advertising agency in Brazil that wanted to use this for a car shoot.

**Dave Jones:** And they wanted to fly me across to Brazil and set up this big thing. Wow. Did you take them up on that? I haven't really heard back from them in a couple of months, so I guess that's fallen through. But that's pretty exciting for a while.

**Dave Jones:** I might get to go to Brazil. Fantastic. I mean, it's all open source. Anyone can make their own. But they want the person who's done it first. If they want to fly me to Brazil, that's fine. Yeah, you can handle that. That's the Zigbee receiver.

**Dave Jones:** It's an XB900MHz. Yep. Is it legal to turn it on? It's 60 megawatts. Sorry, 60 milliwatts. 60 milliwatts. Not a megawatt one. I can't afford that. These are actually some samples that Ted brought in to show us and they're similar light painting things.

**Dave Jones:** So there's a whole bunch of different techniques here. I'll give away some secrets. My best guess at what it is, having done a bit of this stuff before, is that that's kind of an LED torch or a glow stick on a leash, and then you just spin it around really far and sort of process as you go,

**Dave Jones:** and eventually you end up with a nice sphere. You've got some Datomir green laser pointers, highlighting a person sitting in a chair. Yep. And these rather nice kind of explosion-type things is you set fire to steel wool and then curl it around on a rope

**Dave Jones:** or I think he used an egg beater for one of those. Brilliant. These are tricks of the trade. Right. And this really, really nice tree-like structure, I haven't actually seen this technique before. Apparently it's EL wire and you're sort of jangling it around as you go.

**Dave Jones:** Right. So that's a technique I'm going to have to give a try at some stage.
