---
video_id: dFAuPuHiECE
title: Guest Video: - Kaizer Power Electronics - Sony BVP-7AP Vintage Video Camera Teardown
url: https://www.youtube.com/watch?v=dFAuPuHiECE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 28, "2": 58, "3": 84, "4": 115, "5": 132, "6": 170, "7": 194, "8": 229, "9": 255, "10": 283, "11": 308, "12": 340, "13": 364, "14": 395, "15": 427, "16": 453, "17": 476, "18": 497, "19": 520, "20": 545, "21": 570, "22": 603, "23": 632, "24": 661, "25": 682, "26": 710, "27": 733, "28": 752, "29": 771, "30": 790, "31": 812, "32": 838, "33": 867, "34": 897, "35": 924, "36": 961, "37": 990, "38": 1011, "39": 1035, "40": 1053, "41": 1080, "42": 1104, "43": 1127, "44": 1155, "45": 1175, "46": 1192, "47": 1212, "48": 1232, "49": 1251, "50": 1266, "51": 1283, "52": 1305, "53": 1323}
---

**Dave Jones:** Hi, my name is Mads Baumkamp. I'm from Denmark and I have been doing electronics as a hobby for about 10 years. I run the kaiserpowerelectronics.dk blog and also with this YouTube channel associated to it. I primarily do with high voltage, high current and Tesla coil building, and I have done quite a few from small to large.

**Dave Jones:** And I also do a lot of teardowns in expensive, exotic, decommissioned equipment. So, I hope you will enjoy this video and a huge thanks to Dave for giving me this opportunity to reach out to a much larger audience, for which I think my channel will be interesting.

**Dave Jones:** Hello, I'm Mads Baumkamp and this is Kaiser Power Electronics. This is a Sony color video camera model BVP7AP. And if you have watched any broadcast TV transmission live or recorded in the 90s, there is a good chance that this little baby was used in the production or the live transmission.

**Dave Jones:** It features a huge Fujifilm 8.5-119mm lens. And it's a real heavy camera. It's very big. And as you can see, the sheer size of it. And this isn't even the whole story. This is just a camera and a communication unit. There is no part for recording or storing any kind of data in this.

**Dave Jones:** That would all sit in the central control unit, that I unfortunately can only show you a picture of. And I have made this camera run alone by just finding out what voltage and where to put it in. Let's take a closer look at the camera itself.

**Dave Jones:** Here we can see the marking plate with the model number and the DC voltage. The back part here says that it's only to be used with the central control unit 355. At the front we have the Fujinon 14x zoom lens. The Fujinon 14x zoom lens, which comes with a nice handle for zooming with a motor assist.

**Dave Jones:** On the other side we can see the nice 3 CCD shield. Now, all around the camera there are so many knobs and buttons and so on. But here at the front of the viewfinder, here are all the controls for setting brightness and contrast and peaking and so on for the viewfinder.

**Dave Jones:** But it also has some audio controls for the built-in microphone. At the underside here we have some different white balance settings. Camera, shutter, gain, output. Also another white balance switch. And up under here there is a selector for color, filter, temperature. And hiding again up here is a shutter on-off button.

**Dave Jones:** Along all these, which are mainly associated to the video part, then here at the back is the intercom controls. And this goes on both sides where it also has a plug for the external microphone that the interviewer would use. Then at the back here we have all the connectors that goes out to the CCU.

**Dave Jones:** Now this had a power cable and then another two cables here for the CCU and one for VTR. I have not been able to find a price tag on this camera, but I am guessing that it was not low at all. It is a modularly built camera, so the whole unit here at the back that communicates with the central control unit only sits here with three screws.

**Dave Jones:** Then you can actually take the whole unit off and I think you could replace it with a recording module. So you could do full mobile recordings. Now I have really looked forward to show you this part that is inside, because it was absolutely nothing like anything I expected.

**Dave Jones:** I did not expect to find a small rack-mount computer inside a camera, but here it is. Small, beautiful cards, all custom tasks that we have the little CPU board sitting at the bottom. There is some audio for the intercom amplifiers. Another that says red, green, blue.

**Dave Jones:** So perhaps a little test pattern generator. And over here we have everything that has to do with the sensor for the image generation, which is hiding behind this little black cover. Here we can see the two PAL cards, as this is a European camera.

**Dave Jones:** But I am completely amazed about how beautifully built this system are. So you can take out these small cards here. This is the first PAL card. I really can't tell much about this right now. As you can see it has a little bus connector.

**Dave Jones:** And it goes down here at the small bus connector at the motherboard at the bottom. And I assume that the PS card that we have over here at the right side is the power supply. But what the other here does, has a lot with the black setting, test level, gain, gamma, white clubbing, FLR, PED.

**Dave Jones:** These are some shortings that I do not know. But I am really looking forward to taking this further apart and show you what it is. And I think that from... I can just show you an example of the image quality that this camera can do right now, just up here in the right corner of the picture.

**Dave Jones:** That it is not impressive. The sensors are not doing that well. It was only made for 700 lines of TV resolution. And by today's standards this is nothing to really use for anything. But I did find a cheap PAL to USB converter on eBay.

**Dave Jones:** And I will see if I can find a PAL output on one of these cards. And see if we can get this to actually stream something live to a modern PC. The racks are now empty and this camera is absolutely madness. It is incredible how much stuff they have gotten into so little space.

**Dave Jones:** And with so many wires going all over the place. I mean, assembling this has not been an easy job. There is simply just wires going everywhere. So, over here we have a high voltage supply. Which I am not sure if these CCD sensors require a higher voltage.

**Dave Jones:** Because the camera is supplied by 12 volt DC. But I am sure we will find out. So, I have taken out all the boards and let's take a look at them. Here we have the processor board. I am not sure if this is just for the CCU or also the other analog image boards.

**Dave Jones:** But it features a small microcontroller and an EEPROM. Which says, sign video broadcast television equipment to rent higher. So, perhaps this camera was only rented at first and then later bought out. Then here we have the two boards that was marked MD and C level.

**Dave Jones:** I am not completely sure what they do. They have a few tremors. But it also has a 36 MHz crystal here. And you see the IC, it is a 74F175PC. So, I can look that up. Up here we have the two microphone amplifier boards.

**Dave Jones:** This one is for the intercom and this one is probably for the external microphone. Then we get over to the analog image boards. First over here we have the power supply. It is an old switch mode power supply. And a little funny thing, see the two transistors sitting up here.

**Dave Jones:** Not really enough space for them to have good enough cooling sitting next to each other. So, they just bend good around with a little insulation on the legs. Then here we have, this board was marked EN and PAL. And this contains a lot of PR and also has a lot of balance parts.

**Dave Jones:** But not near the amount that we see on this board. It is absolutely insane having to adjust these boards when they have first been built. And are going in for calibration. Must have been some job to do that. And over here we have the first PAL board.

**Dave Jones:** And it actually has a, I think it is a crystal for the PAL frequency. So, hopefully on this board I can find some test points. Or something else where I can find a clean PAL signal to inject into my little USB converter. Now over here I also removed the cover or the print that was sitting over the sensors.

**Dave Jones:** Here we can see the sensor board marked G for green. And you have R for red and B for blue. Now all these white wires then connect down to the different sensors that we cannot see right now. But I will remove the lens assembly and then we can take a look inside the sensors.

**Dave Jones:** Now the lens is taking off. And here you can see one of the reasons why I am doing a teardown on this. Then here on the UV filter it has a, I don't know what you call it, glass pest. This camera has been sitting outside in bad weather.

**Dave Jones:** It has taken a lot of rain. So unfortunately there is now something between the layers in the UV filter. And it is completely useless to get a proper picture through it. And there is no way to really clean it or get a new one.

**Dave Jones:** I could probably find something and cut it to fit. But I am not sure I would get a good picture afterwards. And even then the resolution of the camera is simply not good enough to keep it. But it seems that I will have to remove these screws.

**Dave Jones:** And I will see if I can take the whole front off and get into the sensor boards. This is just an incredible amount of wires going everywhere. I know I said it before when we looked at the main board at the bottom. But this is just ridiculous.

**Dave Jones:** There is an absolutely ridiculous amount of wires. So entwined that it is almost impossible to get this taken apart. As you can see the whole head of the camera is right now in a, let's just call it an exploded view. But what we have revealed is up here we have a 29.5 MHz crystal.

**Dave Jones:** Sitting along with something that is shielded beneath this little golden metal plate. Over here seems like a power distribution board up to the three sensors. And the brown funnel thing here is the optical color filters. Where we have the red board and the green board.

**Dave Jones:** And the blue board here for the three different color sensors. That is all glued together in this assembly. I don't think I can get this further apart without risking to break anything. And I really wouldn't do that. I assumed that the two backplates would only reveal the backside of the backplanes.

**Dave Jones:** And I did wonder where the controller for the whole backplane actually was. And here it is. It's a Hitachi HD6305 which is a CMOS microcontroller. It's a 8-bit CMOS MCU with 2 KB of RAM and 128 bytes of RAM. Now this has 31 I.O.

**Dave Jones:** pins. And this is what along with the massive amount of custom parts, custom boards here. Which is stamped Sony. Makes up the backplane. And it just keeps getting better and better and better. This camera is absolutely stuffed with parts. I can't describe this anymore because it just keeps popping out from every corner and so on.

**Dave Jones:** So this is the backplane board of the intercom and CCU unit. And this basically encodes the signal into a special high frequency combined signal of audio and video and so on to the CCU unit. Where decoding is being done and then over to the PAL format again.

**Dave Jones:** So maybe I could also here at the inputs find something I can use at the PAL to USB converter. Or else I did also notice this because this I actually missed early on. That it has a little plug here that says test out.

**Dave Jones:** And it has a BNC plug. Who knows, maybe this is just a PAL output. But taking a view again. Massive amount of wires going everywhere. And unfortunately I do not have been able to find a manual for this. Every site that has one would want me to pay for it to download it.

**Dave Jones:** So I did not want to waste money on that. But this has really been a pleasure to take apart and look at because this is a stunning piece of engineering. So I will get it all together again and hopefully no parts are missing.

**Dave Jones:** No small screws. And yeah, it will run again. This is kind of the test setup. It is setup just with an adapter. Then I am using a cheap DVR to USB converter that I found on eBay. It came with a lovely software here called TVR.

**Dave Jones:** Which also came with a serial number in a text file. So that is probably seriously legit. And then I have my green screen. So let us see how this camera really looks. I will use my good friend here as a color test on the camera.

**Dave Jones:** So here you can see me film from the front camera of a modern smartphone. But now let us see how it looks like on the old analog video recorder. The resolution on the recording here is 720 x 576 pixels. It is encoded in MPEG-2.

**Dave Jones:** And this is given in a whopping 3.6 GB data per hour. So yes, this software actually gives the data rate per hour. So how do you like the color difference between the smartphone camera and the old analog here? It is suddenly much more soft.

**Dave Jones:** Let us put the volume down and let us see. There is really an issue about setting up white balance probably. Because it is all manually controlled. You have to set up your scene right. And I really cannot see how anybody would have worked with this.

**Dave Jones:** It quite takes a cameraman when you can compare it to a phone camera like this where you just push record. You get an instant good result. It takes care of everything for you because this is just a massive load of work to make anything good.

**Dave Jones:** But there is also that little difference that the screens that we are looking at today are so much better than what this is originally designed for. So we cannot really compare it. But at least we can see what it can produce on today's hardware and if it is really useful for anything.

**Dave Jones:** If you made it this far in the video, I will now present you for the opportunity to own this camera. All you have to do is that you go to www.eevblog.com forum and you find the appropriate thread. I will put a link down in the description of the video.

**Dave Jones:** And here you can have a chance to win this camera. If you have a cool project that you would like to use it for or take it apart and build something completely new which I would really like to see. Because as a whole piece I don't think this camera has much to offer in today's digital world.

**Dave Jones:** But please do comment on what kind of project you would like to use it for and it can be yours. There is however that little catch that this is a heavy camera. So you would have to pay me for shipping it to you.

**Dave Jones:** And that is in around maybe 50-60 euros anywhere in Europe. So be aware of that. Please ask me about the shipping details if that is a problem. But I hope that somebody will bring new use to this camera. I hope you enjoyed the teardown.

**Dave Jones:** I hope you enjoyed seeing the camera itself. I hope you enjoyed seeing what it can do. And I especially hope that you really enjoyed that the encoder is just not working that well. So the image is a little stuttering and the sound keeps lagging behind and so on.

**Dave Jones:** So that software that follows with the DVR to USB is completely utter useless. But I am not going to try to use any other software because for me this project is over. But this camera is looking for a new owner and a new future.

**Dave Jones:** So until next time. See ya.
