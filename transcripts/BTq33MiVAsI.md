---
video_id: BTq33MiVAsI
title: EEVblog #1252 - LED Panel Lighting Flicker Investigated
url: https://www.youtube.com/watch?v=BTq33MiVAsI
source: youtube-asr
---

**Dave Jones:** Hi, if you're wondering why this video looks a bit different, it's because I don't have my studio lights turned on. Both these Aputure Amaran lights I usually have two of these either side of me to light up the mailbag or light up

**Dave Jones:** the bench that I'm actually working on. And these are very nice quality high color rendering index studio lights. Absolutely fantastic at a fixed color temperature. If you don't know, all of my lights in my lab here are a matched color

**Dave Jones:** temperature so that least reasonably accurate colors in my videos. So not only do I have two of these, I've got an array of overhead studio lights above the bench as well, which are those square panel lights. And I recently had

**Dave Jones:** all of the lights in this new lab changed under a New South Wales government scheme where they will replace your original troffer lights, which are the tubes. In fact, these ones are actually LEDs, but anyway, fluoro tube lights troffers up there with these

**Dave Jones:** newfangled LED panel lights. They just drop in and the government will do it for almost free. I had to pay a little bit of cost or whatever, but it's heavily government subsidized and they replace them. I Now I actually tested

**Dave Jones:** the panels that they were going to install before they I signed up to this thing to have them replaced and I checked the color temperature and they were the correct color temperature. Shouldn't care about CRI cuz I have a

**Dave Jones:** higher quality studio lights that give better quality light for that. So it's not a problem. So this is just for not shooting video, just for general lab use. Unfortunately, the problem is I didn't check out the drivers for the

**Dave Jones:** thing and it turns out you can probably see it here in this video, there is flicker. You should be able to see some sort of little horrible shimmery flickery thing here. It's really awful and it's even worse if you use a webcam.

**Dave Jones:** On the left-hand side here that you're watching, this is my regular webcam. This is actually it's not a webcam, it's my old Canon HFM-400. It's just a little old Canon camcorder. And it's quite good. I do that via HDMI video capture. And on the

**Dave Jones:** right-hand side is the Logitech C922 webcam, one of the best webcams on the market. Now, I took down the offending panel, and it might look okay at the moment, but let's have a look. Let's have a look. Whoa, look at the

**Dave Jones:** webcam. Look at the webcam. Look at that. That's terrible, Muriel. Wow, look at that. So, the So, the camcorder handles it okay, but it definitely shows up on the Logitech webcam. Camcorders and these webcams, you can actually enable the 50-60 Hz

**Dave Jones:** anti-flicker mode, and I've got that enabled. And I don't get this flickering problem with my other panel studio lights I've got, or of course with these professional studio lights as well. So, what's the problem? Well, let's investigate. Now, it's obviously not

**Dave Jones:** going to be the panels themselves, because the panels are just LEDs. There's no active driver circuitry inside here. So, it's clearly going to be the driver that's the problem here. And both of these are SunLED energy brand. It turns out that this is an

**Dave Jones:** Australian company, not too far from here. So, they've just rebadged some Wan Hung Low brand in China, put their own model number on it. Cuz if you search for this model number and the model number of the driver down here, all you

**Dave Jones:** get is some New South Wales government database thing. So, yeah, clearly they've just bulk bought these and rebadged them. So, I think this puppy here is going to be the cheapest possible thing, and that's why it's flippering flickering

**Dave Jones:** flippering? I think we'll run with flippering. So like I said, there's absolutely no data on this. These are only like 24 watt panels. So they're not particularly bright. The overhead studio panel lights that I've got in here that from my old

**Dave Jones:** lab, they're actually 60 watts a piece and you can see you can see the new ones flickering over there. I can't see these flickering in real life. But it might eventually be bad on the eyes. But this driver here is going to be dodgy as and

**Dave Jones:** I've taken off the end caps here and it looks like they're just soldered directly on. Even the mains input soldered directly on. That's a bit how you doing. They've got the holes in the case for the screw terminals down in

**Dave Jones:** there, but they don't use them. Jeez, not off to a good start. Well, there's your problem. Now whilst it might look, you know, fairly neat and tidy, the simplicity is the issue here. The primary side here, nothing essentially wrong here.

**Dave Jones:** We've got an input fuse that's just flapping around in the breeze a little bit, but it's okay. We've got ourselves a common mode choke and some filtering. So you know, that's okay. But and it's going directly into this primary side

**Dave Jones:** switcher chip here and well, therein lies the problem. There's nothing else. Look at the secondary side. There should be a little bit more on the bottom here. Of course, you know, single-sided. This isn't even FR4. This is like phenolic

**Dave Jones:** base. It's a bit how you doing. They're saving some cost there. But anyway, we've just got a few passives around here. Passives? Jeez, I'm not doing very well today, am I? Anyway, this is all primary side stuff and this is all secondary side

**Dave Jones:** stuff. They've got the high voltage isolation slot there. So that's all okay, right? But the problem is the secondary side there's our there's our diode, but secondary side is so simplistic. There is no traditional like a regulation on the

**Dave Jones:** secondary side. There is no optocoupler feedback to the primary side. So, how are they actually regulating this constant current? Cuz this is a constant current driver. It's 500 to 550 milliamps constant current. Anyway, there's no way that they're doing

**Dave Jones:** secondary regular current constant current regulation there. It's a primary side regulation function. So, this transformer going to have to be getting a tap back on the transformer. If we have a look on the bottom, there you go. There's your There's one winding. That's

**Dave Jones:** the switching winding. And this would be your feedback winding here. The reason that they're doing that is because it lowers the cost. You don't need any secondary side regulator IC. You don't need any optocoupler. That's why you're almost certainly going

**Dave Jones:** to get flicker on the output. It depends on the type and size of your output cap of you know how much you're actually going to get. And that's just a 100 low E, is it? Well, at least it's 105°

**Dave Jones:** rated. And there's nothing inherently wrong with having transformer feedback instead of like optocoupler feedback or whatever. That's actually fine. The problem with this is is that it has no secondary side current constant current regulation. And they've got a piss weak

**Dave Jones:** amount of output filtering as well. So, yeah, they've really cut costs on this. That's why you're going to get a metric crap ton of ripple and hence flicker on this thing. And unfortunately, these model numbers here are not telling me

**Dave Jones:** anything. I get diddly squat searching for that. But look, they tell you what type of material is they chem one. So, the best we can do is look at the data sheet for this puppy. It's almost certainly you know directly pulled

**Dave Jones:** from the data sheet or app note. First of all, I'm just curious to know what uh the compliance voltage of the LEDs happens to be there. 38 volts, of course, that will depend upon the number of LED LEDs you've got in the string,

**Dave Jones:** the type of LEDs, the drive current, and the voltage drop, the configuration all inside there. But, yeah. And if I use my AMTI 520i probe here with the toroid attachment and put it in wire mode, there's our current waveform. It's

**Dave Jones:** jumping around like a jack-in-the-box. Let's fix that triggering. That's pretty some noise rejection. There you go. Bob's your uncle. So, it's mostly 100 hertz ripple there because it's full wave rectified. That's why your 50-60 hertz anti-flicker filter on your webcam is is

**Dave Jones:** typically not working. And of course, if you get that flicker on your regular camera, then your depends on the frame rate you're shooting at and all that sort of stuff and the beat frequencies as to how it actually flickers. So, that magnitude

**Dave Jones:** there 2 volts, that means nothing because I haven't current scaled it to match what this thing is. So, what you've got to do is look up your manual. And in wire mode with toroidal attachment, 1 amp per output volt. So,

**Dave Jones:** I've got to set that back to 1:1 probe and 240 millivolts equals 240 milliamps. But, of course, if you want to do it nicely, you can actually change that to amps. So, it's now 240 milliamps. It's now scaling in milliamps. Nice.

**Dave Jones:** Most digital scopes will have the feature to change the units and the scaling. And in this case, you can see 1 volt per amp here. It's just nice to set it up like that just so you don't mentally goof it. And if you want to see

**Dave Jones:** the voltage waveform, I'm just probing that and yes, it is safe because the secondary side is transformer isolated. I've done a whole video on that how not to blow up your scope, and uh 10 volts per division, 10, 20, 30. There was the

**Dave Jones:** 38 volts that we saw before, and that's the current waveform. So, obviously, this thing is just a real pile of turd, and that's why you get the flicker. And for those playing along at home, you want to know what the uh high-frequency

**Dave Jones:** switching is, 62.7 kHz there. It's a little bit tricky to trigger on that. If we wind that out, there you go. So, let's have a look at another panel that I got some time back just as a trial. It's a non-flickering

**Dave Jones:** series, as I said, you can't have a non-flickering panel cuz it's just the LEDs inside. It's all about the driver. Anyway, this is a 48-W jobbie, crap CRI, but I didn't care about the CRI, but the color temperature I cared about.

**Dave Jones:** Supposed to be 5,500, but it wasn't. I think it was like 6,700 or something. Ah, completely blue balls. And it came with yet another uh Chinese driver, an AGT uh brand one, and but it's supposed to be ripple free. It's

**Dave Jones:** advertised as a flicker-free one, and well, the flicker comes from the ripple. There you go. So, let's take this apart and see the uh construction design uh difference. So, right from the get-go, you can see the difference. Well,

**Dave Jones:** they've got some uh large heatsinks on here cuz this is a 48-W jobbie. You can also see that they haven't tried to uh cut costs because they've got the uh screw terminals on either end, and they cost money. That's why they didn't have

**Dave Jones:** them on the other one. They were penny-pinching every cent. Look at the size of this uh transformer. As I said, it is a higher uh wattage jobbie, uh double the power. And look, they've got three output uh ripple caps. I think the others were 330

**Dave Jones:** Samsungs. Yeah, okay, whatever. Look at the large output uh diodes they've got. But on the bottom side is where you can see, like primary side, here's our driver over here, which is very similar to before. We've got a uh bridge

**Dave Jones:** rectifier, and we've got the input filtering and the fusing, and uh we've got a smaller SO8 controller primary side but of course we've got a primary side a switching large switching transistor because as I said it's higher power but the secondary side is the

**Dave Jones:** tail. Aha, that's actually conformal coat. Yeah, they got it on the primary side as well. Looks like they haven't done the whole board. They've just almost mastered off. Nice touch just to prevent moisture causing issues in there. So you know, you can get moisture

**Dave Jones:** in these things up in the roof that heats up cools down all that sort of jazz so but we've got a secondary side constant current controller here with then of course that will be driving our switching down there with the

**Dave Jones:** heat sink but it's basically just a bridge rectifier over to the main filter cap. Then it uses a proper secondary side constant current controller and you'll notice just like the other one there is actually no optocoupler feedback from the secondary back to the

**Dave Jones:** primary so they're also using a winding hence yep they've got the two pairs on the side there one pair will be for the switching one pair will be for the feedback but the difference of course is that the

**Dave Jones:** constant current regulation is done on the secondary side and they've got big ass filter caps. That's why this one is going to have well won't be entirely ripple free but will have bugger all that it essentially won't flicker. Big

**Dave Jones:** difference and there's probably what double triple the bomb cost there? That could be a chem too. What is their markings on there for what type of board material? Concentration only for you? What? That's hilarious. Anyway, uses a similar

**Dave Jones:** cheap chem type phenolic base material but it looks to be a bit better than the other one but yeah, I reckon it's probably like three times the bomb cost in that compared to the other one. I know it is higher wattage and you know,

**Dave Jones:** you've got to have the metal work and the big external power transistors and stuff, but yeah, that's like there's a big difference. All right, so let's just measure this puppy and see what we get. I haven't touched the scope. That was

**Dave Jones:** the same scale as before. Big difference. So, we're 50 milliamps per division there. So, like it's not much. Remember, this is a actually a 1.1 amp. So, over an amp output compared to less than half that for the uh uh

**Dave Jones:** previous panel. So, as a percentage of the total current, it's not much. Of course, this is AC coupled, and you can see that there is some 100 hertz there. Of course, if you have a look at your time base, 10 milliseconds, there you

**Dave Jones:** go. It's 100 hertz, and you go into the high frequency stuff. We can single shot capture that. There you go, switching frequency 47 kilohertz. But you can see there's just a huge difference. It's we're getting 100s of milliamps of ripple before. That's

**Dave Jones:** That's why it's flickering. That's why you can see it. You're not going to see it. You might be able to measure a teeny tiny bit of flicker somehow if you had sensitive enough stuff to measure that, but you're

**Dave Jones:** basically you're not going to see that on camera or on it's not going to be a problem on the eye as well. All right, let's take a brief look at the chip used on this sucker, shall we? It's not on on

**Dave Jones:** bright's website, but I was able to get this is it's got Yeah, on bright confidential. Yeah, right. Nothing Google can't find. Anyway, it tells you right here can achieve low system cost for isolated lighting by primary side control in the single stage converter,

**Dave Jones:** significantly simplifies the LED lighting system design by eliminating the secondary side feedback components and the optocoupler. Penny pinching all the way to the bank. It's got high power factor, they claim. Quasi-resonant operation, all sorts of stuff. Fast startup, blah blah blah. And it's got

**Dave Jones:** comprehensive protection as well, which it can do via the feedback coil on the transformer. So, LED short circuit protection, cycle by cycle current limiting, building leading edge blanking, under voltage lockout, all sorts of stuff. So, yeah, but it's a

**Dave Jones:** great chip for this low cost application. The side effect, of course, is horrible amounts of ripple. And here's the schematic, which is basically what we've got on the board here. Um we've got our bridge rectifier on the input.

**Dave Jones:** We had a few more, you know, a fuse and some filtering stuff and things like that. And we've just got a resistive divider here powering the chip itself. And we've got a external transistor. Was that on there? But this is interesting.

**Dave Jones:** We don't have a switching transistor on the board. So, I I got to assume it's the same part. The part number's the same. But, of course, this one says it's in a SOP 20 23 six package. That one's not. It's in an SO8

**Dave Jones:** package. So, I maybe it's a slight variation on the part that actually in a bigger SO package that has the built-in power transistor. So, anyway, this is the best and only data sheet confidential what I can find. So, it we

**Dave Jones:** assume it's got must have a built-in switching transistor. So, but it's basically the same as this. And you can see here's our feedback coil as well. They should actually show that going all the way down there like that to show

**Dave Jones:** that it's actually coupled. That anyway, the auxiliary winding feedback and that allows them to sense with all the compensation. And the output is just that. It's a single wave rectifier, a one lousy output filter cap, one Hung Low brand, and straight to the LED, and

**Dave Jones:** Bob's your uncle. Like there there's no secondary anything. It's it's doing the current regulation via the feedback coil here. So, yeah, it's pretty how you doing. But, it's cheap and it works if you don't mind the flicker. So, there

**Dave Jones:** you go. We might be able to improve the ripple a little bit by increasing the output filter capacitance here, but it's pretty how you doing. It's 100% ripple. That is just yeah, awful. No wonder it flickers like buggery. But, you can't

**Dave Jones:** just increase the capacitance willy-nilly. You got to make sure that the diodes are capable of it and the thermals are there and everything else. And it's just I know, don't hack them. Just get a one that's properly designed

**Dave Jones:** with secondary side current limit and a decent amount of filtering. And of course, it's dependent upon your the shutter speed of your camera. It's auto you know, it's always auto changing or you can fix it to avoid these things.

**Dave Jones:** But, even my high-end Sony camcorders, you can see even with my main studio lights on, even with these lights up there. I've got like eight of them on and they sort of the light filters through and mixes with my

**Dave Jones:** other non-flicker lights and you can still see a little bit of flickering and shimmering in there. So, it's really annoying. So, I'm either going to have to try and experiment and fix these or just toss them in the bin. They're

**Dave Jones:** horrible. I don't mind the panels. The panels are okay. So, there you go. Let that be a lesson. Beware of these cheap ass LED drivers and make sure you get ones that specifically say flicker-free or low ripple or whatever it is.

**Dave Jones:** Otherwise, you're most likely going to end up with the lowest common denominator like we've got here. Anyway, hope you found that useful. If you like the video, please give it a big thumbs up. As always, discuss down below in the

**Dave Jones:** comments or over on the EVblog forum. Catch you next time. Mhm.
