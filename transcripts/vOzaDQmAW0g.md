---
video_id: vOzaDQmAW0g
title: EEVblog #505 - IR Learning Remote Control Hack
url: https://www.youtube.com/watch?v=vOzaDQmAW0g
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 23, "3": 32, "4": 47, "5": 60, "6": 71, "7": 83, "8": 101, "9": 115, "10": 127, "11": 146, "12": 163, "13": 176, "14": 191, "15": 218, "16": 233, "17": 248, "18": 269, "19": 278, "20": 295, "21": 313, "22": 319, "23": 330, "24": 339, "25": 352, "26": 358, "27": 370, "28": 383, "29": 395, "30": 405, "31": 426, "32": 442, "33": 450, "34": 465, "35": 477, "36": 492, "37": 508, "38": 518, "39": 528, "40": 541, "41": 550, "42": 566, "43": 577, "44": 593, "45": 610, "46": 619, "47": 632, "48": 640, "49": 657, "50": 668, "51": 679, "52": 690, "53": 701, "54": 713, "55": 725, "56": 742, "57": 757, "58": 770, "59": 784, "60": 797, "61": 809, "62": 830, "63": 839, "64": 859, "65": 867, "66": 875, "67": 886, "68": 902, "69": 924, "70": 942, "71": 957, "72": 983, "73": 998, "74": 1007, "75": 1022, "76": 1034, "77": 1051, "78": 1068}
---

**Dave Jones:** Hi, just a quick video about hacking this uh universal remote control. I'm trying to build a uh countdown timer for my new segment and I want the timer to be able to switch my camera off and on automatically.

**Dave Jones:** I thought, oh yeah, I could probably either use uh a genuine Canon remote or one of the imitation ones with the proper key already programmed in there and just uh use the Arduino to short out the button.

**Dave Jones:** That's a pretty easy hack, but uh I got to wait weeks for to get one that get one of those delivered. And I don't want to use my uh genuine one, of course.

**Dave Jones:** And then I thought, oh, maybe I'd get this um uh USB infrared toy from um Dangerous Prototypes, which I've had uh for quite some time. And hooks up to the USB, and I can read the IR code from here.

**Dave Jones:** And I've done just that. And it can save it to a file, but unfortunately I thought you could actually program it to spit the code back out. It's even got the uh uh space on the back for a button, but uh that doesn't seem to be the case.

**Dave Jones:** It doesn't seem to be a firmware option to actually do that. And yeah, I could probably find a way to, you know, or program it manually or something like that to spit out the received IR command.

**Dave Jones:** And I know there's other ways to do it. More than one way to skin a cat here. As always, I can there's libraries for the Arduino that you can read commands and then IR commands and then spit them back out, but I didn't want to dick around.

**Dave Jones:** So, anyway, I got this uh learning remote control from the local uh supermarket. It's a Scandia uh brand, and I thought we'd uh crack it open and uh have a look inside, see if it's um it should be easy to hack to get it to uh simulate the remote control cuz I've already programmed it.

**Dave Jones:** It's got the learning function. Here we go. I'll stop it. press the green button there and and there we go. It should have switched back on there. And uh I've programmed this button here to switch uh to the other mode.

**Dave Jones:** And um sorry to switch to the playback mode. And then if you hold down the learn button there. There we go. Learning key. Okay. We can select key. And let's say we wanted to set this one as zoom for example.

**Dave Jones:** Waiting. Then if I zoom telephoto. Boom. Success. Select key. That one. Program that. There we go. So now these two Oh, and sorry, I've got to press ox again to save it.

**Dave Jones:** And I should find that these two keys now do my remote control. Uh do the zoom. Yes, they do. Look at that. Awesome. Oh, and you can actually see the LED blinking in there because uh video cameras can actually see infrared uh light.

**Dave Jones:** There you go. You can see it flickering away there. Awesome. So, there you go. I've got that programmed in. So, now uh we're going to crack it open and uh see how hackable it is.

**Dave Jones:** Let's do it. And we can just uh pry this just pry this sucker open. And uh oh, looks like we're our springs are stuck. Sometimes you got to push those little springs out.

**Dave Jones:** Tada. And we're in like Flynn. Oh, look at that. We've got two separate boards here. That's actually going to be very handy because I was going to say um like a you know um if you just wanted a small module sometimes you can just like hack off uh the bottom of the board for example just you know saw it off or something if you just want a little small uh compact board instead

**Dave Jones:** of using the big you know huge long full universal remote. And it looks like we can just desolder. Can probably cuz this all this board here does is it's got the conductive um carbon on there for the membrane overlay.

**Dave Jones:** It's got surface mount leads which light up the uh buttons and a few resistors, but that's it. It's got the battery contacts on here, but it looks like Yeah, the battery contacts just go straight down there to pins on that board.

**Dave Jones:** Hey, that's really quite nice. I like that. That's a win. I thought uh that we'd have to um you know, maybe saw off the board or something. Or I could have just used it as the whole board and then in my uh solution, I was just going to bend the uh LED at right angles like that cuz it needs to mount flat on the back of my thing and then poke out

**Dave Jones:** through a uh red pix. So, I was just going to um bend the LED at right angles. But uh there you go. That one I'm rather rather happy with that.

**Dave Jones:** So this brand or this particular model is very hackable. Uh I don't know what model it is actually. It's just Scandia. I don't know. Uh Scandia is an Australian uh company who just uh import these from China.

**Dave Jones:** So they probably, you know, are rebadged under 20 different brands, I'm sure. So, that one looks like a very nicely self-contained board that you can just rip off and and we can access the pins, the the matrix pins, because this is the thing about hacking these things is that these keys are in a matrix.

**Dave Jones:** You can see there's not many pins. I'm not sure how many keys are on this thing. You know, 30 or something, I don't know, 40 30 keys or something.

**Dave Jones:** I don't know. There's a lot. So, they don't have individual pins for each one. So they put them in a matrix uh configuration and uh which means they're actually harder to drive.

**Dave Jones:** You can do it with just a single uh you can drive it with an Arduino, but you can only usually only just do a single button because of the nature of the uh switching matrix.

**Dave Jones:** It'll get uh all confused. I won't go into the uh details on that. But um we should be able to do at least a single button. So what I'm going to do is buzz out.

**Dave Jones:** Where's my button? It's going to be that one. It's going to be that one. So, I've got to find which pins on there map through to that button there.

**Dave Jones:** And that's actually real easy to do because the uh carbon ink on these things is generally going to be a couple hundred ohms. Let's just go from one side to the other there.

**Dave Jones:** There we go. 270 ohms. So, if I'm searching for this button here, there's a contact carbon contact on either side. So, all I've got to do is probe from the carbon contact up to um and find out which pin is on there.

**Dave Jones:** And here we go. I found it. The top contact up here goes to this bottom. No, sorry. The top corner pin up here. There we go. You got 100 ohms.

**Dave Jones:** And you can tell because if you go to the other pins, they're all, you know, a couple hundred K or a meg or something like that. So, there you go.

**Dave Jones:** That's a dead giveaway. And the other contact down here is oh sorry not that one that one down there. So there you go. So all I've got to do to activate that particular button which is my start I've programmed a start stop button for my remote is put a switch between there and there and there.

**Dave Jones:** That's it. And very brief overview of a matrix uh keypad like this. They've you've no doubt seen this before. They've got rows like this and column drivers. And there's basically a switch between each row and column uh intersection like that.

**Dave Jones:** And you can have that for as many and make as many keys as you want. And the software sits there just scanning these rows and columns until you push an individual button.

**Dave Jones:** And by knowing the combination of the two points that uh get shorted out, it can determine which keys being pressed. Now um this is a real problem to drive this with external circuitry because these are not ground reference.

**Dave Jones:** So it's not like you can just use an open collector output here for example it you know it could be a MOSFET or whatever inside a typical microcontroller for example like an Arduino.

**Dave Jones:** Um, or you can use an external driver transistor, for example. That will be ground reference like that. And you can't just go whack that willy-nilly across one of these switches if this circuitry uses the same ground reference.

**Dave Jones:** Now, in this case, I could power this the remote from its um own individual battery and then that's fine. I can put one individual um transistor or an output of an Arduino acting as an open collector open drain output like that.

**Dave Jones:** So you switch it the output zero or then you switch it to an input which is similar to an open effectively uh works as an open collector output like that.

**Dave Jones:** And in that case yes I can drive one individual button for example this one with my external Arduino. But if I want to do more than that, then um I'm going to run into a big problem.

**Dave Jones:** I'm going to have probably have to use optoouplers an optooupler for each switch or a relay or, you know, a little rear relay or something for each uh switch to short them out or maybe a cos uh switch or something like that.

**Dave Jones:** But uh I won't go into the details, but because I only need to switch one switch, I'll just power this from its own battery. Um and that should last for ages.

**Dave Jones:** you know, a year or something. Good enough of a pair of doubleas's. I'm sure I can measure that current. But I should be able to just hook my uh one uh output pin on my Arduino up to the individual switch I want on those pins that I buzzed out.

**Dave Jones:** And it should just allow me to emulate that switch. Easy. Now you can see the uh carbon ink here. This is the Yeah, this is the key that I want to uh do here.

**Dave Jones:** So you can see that is then jumping down that that conductive carbon ink which as we saw from there to there is you know a couple hundred ohms or thereabouts and we saw and then that drops down to a via so it actually drops down to that trace down there and it's also shared with that one there but it goes all the way back and up here.

**Dave Jones:** We should eventually oh where is it? We should eventually be able to find our way all the way back to the pin over here. But anyway, um usually when you Yeah, sometimes you got to hack into these things.

**Dave Jones:** If it's just a one board solution like this, then you have to probably hack into these uh traces in here. And it's not easy cuz those VAS, look, this is a singlesided board.

**Dave Jones:** The VAS don't go through to the other side of the PCB. So, it's not like you can just solder a wire on the back side onto that via. So, if you've got one of those boards, you probably have to uh drill out.

**Dave Jones:** I was expecting to have to do this. is I was expecting to have to drill like a hole, you know, if I want to access that Yeah. that trace there.

**Dave Jones:** Then I'd have to drill into that uh spot down there. And then, you know, if I wanted the wire to come in from the backside and I wanted to maybe, you know, keep the remote in uh with the button still on it or something, then, you know, you have to drill through and then solder over to that track and scrape off the solder mask and stuff like that.

**Dave Jones:** But you can see how they've made this as a singlesided uh board. We've got our regular traces on here with the solder mask as a single-sided board. And then they've overlaid the carbon traces on top of there.

**Dave Jones:** And they've just had the exposed copper and then the carbon makes uh contact with the exposed pad underneath there. And that's how they manufacture these boards as a singlesider.

**Dave Jones:** But luckily, this is a two board solution and we can just hack directly onto these pins. A fantastic. This is almost this is ideal really. It's practically uh designed.

**Dave Jones:** Look, nice little compact board. It's got its own LCD powered from uh 3 volts. And uh we can do some wonderful stuff with this. I really like this particular model.

**Dave Jones:** And by the way, this is a Sunwave Technology SR800. And there you go. I've mapped out these four colored buttons here. I could go and do others, but really I I only need the uh one.

**Dave Jones:** I only need that green key. But there you go. You can see that all four of those share a common row or a common uh column there. And then we've got four separate uh pins over here for the four individual keys.

**Dave Jones:** All right, let's give this thing a go. See if it works. I've got a Freerronics 11 uh Arduino Uno compatible board here and uh I've programmed a sketch into this so that digital output uh zero here goes to a logic zero or i.e.

**Dave Jones:** uh shorts out those two pins cuz I've got ground hooked over to here shorts out that record pin that I've pre-programmed into there. And uh that's it. And after it it times out after a little bit and then it sets it back to an input.

**Dave Jones:** So it doesn't set it to logic high. It sets it back to a high impedance input. And that's important. So let's plug it in. Um I've uh made sure that the camera I'm actually filming this with um doesn't accept the infrared uh code.

**Dave Jones:** Only my secondary camera here will. So you can see that it's uh got an output there and we'll see it hopefully press record. I've got this powered from a separate uh battery here and that's important of course that we're not connecting the common grounds between these two systems.

**Dave Jones:** So let's plug it in and see if it outputs our infrared code uh to switch on. And you'll uh see it when it sends a code, it switches on the backlight of this LCD here, which is really handy.

**Dave Jones:** So here we go. Plug it in. Boom. Look at that. Bingo. switched it on and after a few uh seconds it should switch that back off. Come on. There we go.

**Dave Jones:** Bingo. Easy. Works a treat. But unfortunately, look what happens when I disconnect it here. Look, it's just continually transmitting. Continually transmitting. And it will eventually switch it off. And that actually switched the camera on unintentionally really because what it's doing is when it's switching it off.

**Dave Jones:** This remote control uh thinks that that button is being pressed all the time. And obviously this firmware in here is smart enough to know that oh okay it's got a stuck button.

**Dave Jones:** I'm just going to time out. I'm not going to transmit anymore so it doesn't waste the uh battery. So it's really handy. So that can either be a good or a bad uh function depending on uh whether or not well if it's taking any extra battery power by having that button effectively pressed all the time then that could be a problem but I can measure that to

**Dave Jones:** ensure that's not the case. Otherwise, we have to find a way to uh ensure that when the power to this board is removed because we've still got the power.

**Dave Jones:** I mean, we could disconnect the power to this as well, but it's better if you're using this remote control from its own battery source just to leave the power hooked up all the time.

**Dave Jones:** And you can see that with the power uh disconnected here, then we can't actually uh do anything. We can't operate any of the other buttons. You see how it's completely locked that out?

**Dave Jones:** But if we turn the power on here, then Oh, he just accidentally turned it on. Then, oh, sorry, something wrong with my uh then we can still operate our buttons like that.

**Dave Jones:** Um, there we go. Just switched it off. Brilliant. So, that's not an easy problem to um overcome. So I I think the easiest way to uh do that is in my project is just to uh use a double uh ganged power switch so that I'm turning off the power to this the same time as I'm turning off the power to the battery to the remote as well.

**Dave Jones:** Now, you might think because all of our pins are commoned up on this one. Well, all of the four uh colored pins in the row are commoned up there on the one pin and we're using different supplies that we can have the one common going over and then use our Arduino to drive four in this case four different buttons.

**Dave Jones:** Well, I've written a sketch to uh do just that. It operates the uh zoom as well. So, zoom up and down, zoom in and out. Um, plus it uh switches the record off and on and also a fourth channel uh switches it in to playback mode.

**Dave Jones:** And let's give it a go and we'll find that it is hasn't switch hasn't switched it on. So there's that's not working whereas it should. It should have first switched it on then it should zoom in and out and it's not doing that and then it should go into uh playback mode and well it's just no it's not doing you can see that it's uh attempting to send

**Dave Jones:** codes there. But if you flip it over here you'll find that what's happened is it's going into all these different modes. It's pressing the wrong buttons. And that's not because I've uh decoded them incorrectly on the uh pins here.

**Dave Jones:** That's because it's just it's going burko. It just does not work at all. And of course, for this to send the codes, it needs to be in the ox mode.

**Dave Jones:** I could of course program all the other codes into the same codes into all those eight buttons, but gez, you know, like anyway, I basically just wanted to show that even though they're all commoned up like that, you're still not going to be able to get it to easily work like that.

**Dave Jones:** But it does work on a separate supply with just the one pin, which is all we want. And let's see what happens if we join up the common grounds between this battery and the Arduino board here.

**Dave Jones:** You can see it's uh doing its regular cycling through the record off and on just on that individual button and it's working just fine. Well, if I touch the ground here and join them up, you'll notice that we can sit here and we can wait forever, but it's never going to switch back.

**Dave Jones:** It's just not working anymore. So, you can't join those two different grounds together. Doesn't work. And if I release it, there we go. We eventually switched back once I released it and it's now working again.

**Dave Jones:** So, what's the final application of this thing? Well, let me show you. Catch you next time.
