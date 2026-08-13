---
video_id: S-UqkM8iDKM
title: #1179 - PowerFilm Flexible Indoor Solar Cell
url: https://www.youtube.com/watch?v=S-UqkM8iDKM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 49, "3": 69, "4": 82, "5": 102, "6": 114, "7": 130, "8": 146, "9": 162, "10": 179, "11": 199, "12": 223, "13": 244, "14": 268, "15": 293, "16": 313, "17": 337, "18": 357, "19": 374, "20": 390, "21": 410, "22": 422, "23": 443, "24": 459, "25": 479, "26": 495, "27": 516, "28": 540, "29": 556, "30": 576, "31": 596, "32": 617, "33": 637, "34": 653, "35": 669, "36": 681, "37": 694, "38": 710, "39": 722, "40": 738, "41": 754, "42": 771, "43": 787, "44": 804, "45": 828, "46": 848, "47": 864, "48": 888, "49": 908, "50": 932, "51": 956, "52": 982, "53": 1012, "54": 1036, "55": 1056, "56": 1072}
---

**Dave Jones:** Don't they look sweet? Nice little thin, flexible solar cells. Ha! Cool bananas. Let's check them out. So what we've got is little low-light solar power, like solar energy harvesting development kits with these flexible film solar cells. And these are made in the United States of America!

**Dave Jones:** Fantastic. And these are made in the United States of America! Fantastic. And they come in two different shapes here, but they appear to be sort of like identical technology though, just different configurations. And we've got a little battery charging board and we've also got a Bluetooth

**Dave Jones:** development board as well, with these little lithium polymer batteries. And these use TI chipsets and processor as well. So we'll hook that up and get that working in a minute. They've got an Android thing. And these actually are kind of like open-sourcey. They come with the board files and stuff like that.

**Dave Jones:** So if you want to play around with your own. And there's the Bluetooth sensor development kit. They claim it works in less than 200 lux. And it's got the EagleCAD files and whatnot. And if we have a look on the back, ta-da! Here's our response curves.

**Dave Jones:** Terrific. So this is the two-cell panel here. This is the characteristic curve for it at the various current outputs. And there's the voltage curve. So you can work out the maximum power point if you like. Go for it. A little exercise for those playing along at home.

**Dave Jones:** But as, of course, with all these, you know, low-light solar cell technology, the power we're talking about is not much. You know, it's enough to run a calculator or something like that. You know, we're talking in the order of like 100 milliwatt or less.

**Dave Jones:** And let's actually operate it right under its, you know, its sort of like recommended spec limit there. And, you know, around about 70 lux, something like that. I've got my overhead studio lights turned off, so just getting residual light from the other side of the room.

**Dave Jones:** And we're getting about 2.3 volts, although we're going to get NAF all current. There we go. About, you know, 60, 70 microamps, something like that. But that's what you expect. But, you know, it's good enough for like a real ultra-low power energy harvesting.

**Dave Jones:** So this actually works quite down to really quite some low lux. I mean, we're talking 40 down there. I know this is not going to be precisely equivalent, sort of putting my hand over it, but still, you know, getting 38 microvolts. This is the short-circuit current, of course.

**Dave Jones:** But yeah, it still works. It works down to quite low lux levels. That's, yeah, it's pretty good. So let's install the LES100 monitor, and thankfully it doesn't want my first-born child, so just access files and Bluetooth. No worries. Let's go. So do you think they're teamed up with TI?

**Dave Jones:** Maybe. And we found the board, cool bananas. Got the solar panel hooked up here, and our little LiPo battery, and we can connect. Hopefully. Discovering. 9 services, total of 31 characteristics. Cool! Look at that! Like I bought one! Battery level, there you go.

**Dave Jones:** So we instantly get our battery level. It's in millivolts, of course, 3.9 volts. So, it's charging. Is it? No. If I put my hand over the solar panel. Nah, zippity-doo-dah. Oh, we've got our light sensor. Let me put my hand over that. Yep.

**Dave Jones:** Works a treat. There you go. That's it. Ah, we'll see how that compares to my light meter. There you go, that's close enough. Yep, no problem. That's pretty cool, we can control our latency time, our connection interval, all that sort of jazz. Connection interval.

**Dave Jones:** Let's go right down, and hopefully it'll take more power. If I put my hand over the solar cell again. It's going to chew the juice or what? Nope. It's just sitting there. But it's bluetooth, it takes bugger all. So, really, you know, it's all being

**Dave Jones:** powered from this. If we disconnect the battery, it won't work at all. Let's actually disconnect the battery, and see if she still talks. Battery level. Um... Connect. Um, but is that like, is that coming from the solar cell? So let's try it. Here we go, we'll cover it.

**Dave Jones:** Hmm... it's not connecting at all anymore. Take my hand off, is it going to reconnect? Nah, it's not going to do diddly squat. I think we might have had some capacitance on the board keeping it going. Because it's not going to reconnect. It's not going to work

**Dave Jones:** with just the solar panel. Yeah, there's no devices at all. And even if we shine a 20,000 lux torch on there, it's not going to do it. Okay, let's shine that torch on. See if our battery level can... if it's going to do anything at all.

**Dave Jones:** Not really. It's just sort of sitting idle. Our luxometer is going to go through the roof. Where is our sensor? It's down there somewhere. I think we maxed it out. Woo, there we go, that's better. So okay, we've got ourselves a Bluetooth connectivity kit with a

**Dave Jones:** TI Bluetooth micro that we can program, of course. Very cool. It came with a USB stick with the development tools and stuff like that. I won't go into them, it's just a regular, you know, TI development system. It just happens to be used for this little Bluetooth processor.

**Dave Jones:** We can change sort of stuff, but like we can't get anything on the actual solar panel. Like, nothing. What's the, you know, what's the voltage coming out of it? What's the charge rate? Stuff like that. All we've got is the battery voltage, and I'm sitting here and I don't

**Dave Jones:** see this thing really charging at all. It's just sort of wiggle, wiggle, wiggle, yeah. And like, so unfortunately we just can't really get much. The whole point of this is supposed to be evaluating the solar cells in an energy harvesting application, and, eh,

**Dave Jones:** doesn't seem to do much at all. But it looks as though we actually have an option to get rid of the battery and store the charge in a super cap. You can see they've got the charge curves here of time versus the amount of storage capacitance.

**Dave Jones:** Of course the greater the storage capacitance, the greater storage capacity you have in your capacitive battery, so to speak. But the longer it's going to take to charge up before your circuit starts up whatever application you've got, to do anything useful. But then

**Dave Jones:** you know, if like shade comes over or something and, you know, your solar cells interrupted, and it's not producing anything, then it comes, then the charge comes back out of your capacitor. And of course if your circuit takes too much, it's never going to charge up at all.

**Dave Jones:** So, you know, it's all a big trade-off. So I hooked on a 2.5 farad, huge, 2.5 farad, none of these microfarads or millifarads, rubbish, on there. And naturally it's going to take forever to charge up. It's just going to, I should put that on millivolts actually, like

**Dave Jones:** there we go, it's charging up slowly. And if I put my torch on it, it should go even faster. But yeah, we'll be waiting until the cows come home, that's too much capacitance. Hey, now we're talking! We're even overflowing! Check it out, I've got a

**Dave Jones:** 2200 microfarad cap, it says 1800 mic minimum. And that's charging fairly rapidly. Turn my torch on, it's going to charge even quicker. And apparently the bluetooth turns on at 3.2 volts I believe it is. So, oh, I should have my app on. It should be, it should be on now.

**Dave Jones:** Let me take that torch away. Yeah, it's draining down. See? No, it's holding the charge. There you go. Let's see if the app works. Yep, it's updating. There you go. Sweet! So it's working just from that on the ambient light. Granted, we're at about, what are

**Dave Jones:** we at? 2000 lux or something? We're at, we're only about you know, 1000 lux here on the bench, something like that. Depends, it's being like, you know, shielded by my camera and all sorts of stuff. Not exactly doing that, but you see? That it's actually

**Dave Jones:** working from just that. And if I kill that, you'll notice that the battery drains, and that should drain faster if we pull it quicker. Because the capacitor will take more power and it should actually die when we get to... can I put something

**Dave Jones:** on top of that? Put a multimeter on top of that. And it should die when we get to luxometer. Can we look at that? There you go, it's varying. So when it supposed to die when it gets to about 3.2. We'll see. These are not the droids you are looking for.

**Dave Jones:** Still going, still going. Not sure what it operates down to, but I think I said it won't start up or something at 3. Yeah, yep, yep, died. At about 3 volts there. There you go. And you see that has stopped discharging, because the process is not running anymore.

**Dave Jones:** In fact it's the capacitor's recovering. So there you go. That's dielectric absorption for you. I think I've done a video on that somewhere. Anyway, cool. That's great. That works a treat. Oh, yep, it just automatically recovered itself there. And once we got to, it's now back up.

**Dave Jones:** It'll be negative now, all the electrons will fall out. There you go, 4.2 from this little piddly solar cell. Now if I turn off my studio lights and we're at like 40 lux or no, 70 lux, was it before or something like that?

**Dave Jones:** Sorry about the, if you can't, you should be able to just see that screen. It's going down, yeah. Doesn't have enough to maintain that, so it's slowly discharging. And the other kit of course just comes with an, looks like an identical VTI charging

**Dave Jones:** energy harvesting chipset there, just doesn't have the Bluetooth-y part of it. So I guess if you're going to get the kit, you might as well get the Bluetooth interface, because then you can have a play around with that. You know, it comes with the code

**Dave Jones:** as a studio code and all that sort of jazz. So that seems to work fine, there is no iOS app, so if you've got one of those silly Apple things, you're screwed. Well, you're screwed anyway for buying Apple in the first place. But anyway, hey!

**Dave Jones:** Look at all the flame comments down below already. Oh! So thank you very much Powerfilm Solar for sending in these, and they are really quite jazzy. I'm not sure of the exact, you know, performance compared to other competing flexible thin film ones on the market, but these are

**Dave Jones:** made in Yankee land, and they appear pretty good. They're, like, use them for military applications and all sorts of commercial applications, and they'll even develop ones for your custom application and stuff like that. And Powerfilm do actually have a whole bunch of off-the-shelf products.

**Dave Jones:** They've got, you know, those portable USB battery packs, you know, solar charging battery packs and all that sort of stuff, the ones that you roll out, and things like that. So, but yeah, this doesn't seem to be on their website. Couldn't find it

**Dave Jones:** at first go. Maybe it's a new development tool. Anyway, I'll try and link it in down below. Thank you very much Powerfilm. That's very cool. I like that. There's not much that goes into manufacturing those. These new printable well, I'm not sure how these compare with the other

**Dave Jones:** printable ones, which I've got. Hang on. Yeah, if you remember these ones that came in a roll, and these ones were actually printed on a, like an ink jetty type printer, they can manufacture them as long as you like. I'm not sure about these

**Dave Jones:** Powerfilm ones, but obviously by looking at the edges there, they cut these off a longer strip, so they probably have a similar sort of printing process. If there's any, like, manufacturing videos or something, I'll embed it in here. And they obviously manufacture them in longer strips

**Dave Jones:** and they can cut them to whatever sort of, you know, power and size requirement you're looking for. So that's very cool. Thanks Powerfilm. Powerfilm are an Iowa-based manufacturer of flexible, thin-film solar panels that provide custom solar products for industrial, consumer, and military remote power applications.

**Dave Jones:** First, the solar material must be produced. The basic roll processing where we make the core solar module begins with a roll of plastic. A very thin roll tends to be somewhere around 30 microns thick and maybe 1,000 feet long. That roll goes through a sequence of deposition machines

**Dave Jones:** to put down, first, a back metal contact, followed by the semiconductor amorphous silicon. Actually, six layers of amorphous silicon, which makes the solar cell itself. That's the part that absorbs the light and turns it into electricity. And then a top conductive layer that is also transparent,

**Dave Jones:** lets the light in, but also is conductive enough to bring the electricity out the front face. So you have the metal on the back, the transparent conductor on the front. That's where you get the power out. From here, the film is then loaded onto a laser scribing machine.

**Dave Jones:** Here, the roll is unwound on a machine that uses laser heads to scribe the material into sections that begin to make up the individual solar cells on the roll. From here, the rolls are moved onto the printing stage. Electrical insulators are printed between the individual solar cells in order to isolate the positive and

**Dave Jones:** negative sections, as well as also being run through a silver print machine. The silver print machine prints conductive silver ink particles that increase electrical conductivity. Once it's been tested, it goes through a process where a copper bus bar is put on, which is something we will solder

**Dave Jones:** to to get the electrical connections later. Then a laminate is put on the front surface and the back surface, and that's usually a Teflon type product that is highly resistant to chemicals and water moisture. It will protect the module from the environment. The roll is then loaded into a die cutting machine.

**Dave Jones:** This machine unwinds the roll and die cuts it into individual modules which can be used in a variety of products. The die cut modules are then loaded into a machine that tests each module electrically, one at a time. The machine places each module

**Dave Jones:** onto a lighted surface and probes check electrical characteristics. The modules are then sorted into pass and fail bins. Passing modules are then loaded into a large machine called a pick and place. Here a robotic arm picks up individual modules, checks them for orientation and then places them onto a fabric surface.

**Dave Jones:** The robot keeps placing modules on a fabric in a pattern that has been determined by the computer. Once completed, a laser cuts the fabric piece forming the outline of the foldable solar panel. Panels are taken from the pick and place station and operators then string the modules together on the fabric body using a flexible

**Dave Jones:** multi-stranded wire known as a Litz wire. The steps here include using a soldering iron to burn away small sections of lamination over the conductive tape. Multiple connections are made to ensure that the solar panels are still operational even if a wire breaks. Once that is all done, we will then run it through a

**Dave Jones:** lamination process, through a high heat lamination process which helps bond everything together, helps reseal so that the moisture resistance is improved. The panels are then moved to the sewing cell. The edges of the panels are sewn. With the edges of the panels sewn, a top

**Dave Jones:** fabric wrap is added. Product labels are stitched on and strips are sewn over the wire attachment points. In the finishing cell, the operator adds a circuit board and connector. Grommets are added to the corners which allows the user to strap down the panel

**Dave Jones:** in windy conditions. Completed units are then taken outdoors for a final test prior to packaging. Passing units are then packaged and moved to the shipping department in cases ready to provide unlimited solar energy across the globe.
