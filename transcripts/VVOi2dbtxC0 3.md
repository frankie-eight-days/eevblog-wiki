---
video_id: VVOi2dbtxC0
title: EEVacademy #6 - PID Controllers Explained
url: https://www.youtube.com/watch?v=VVOi2dbtxC0
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 31, "3": 46, "4": 58, "5": 74, "6": 88, "7": 102, "8": 113, "9": 125, "10": 138, "11": 153, "12": 165, "13": 179, "14": 199, "15": 214, "16": 233, "17": 253, "18": 265, "19": 280, "20": 293, "21": 311, "22": 326, "23": 345, "24": 362, "25": 377, "26": 396, "27": 414, "28": 430, "29": 444, "30": 463, "31": 473, "32": 488, "33": 500, "34": 511, "35": 529, "36": 545, "37": 558, "38": 576, "39": 594, "40": 606, "41": 619, "42": 633, "43": 648, "44": 667, "45": 686, "46": 699, "47": 713, "48": 725, "49": 740, "50": 755, "51": 771, "52": 787, "53": 804, "54": 822, "55": 836, "56": 848, "57": 863, "58": 879, "59": 894, "60": 907, "61": 923, "62": 936, "63": 952, "64": 970, "65": 991, "66": 1009, "67": 1025, "68": 1042, "69": 1055, "70": 1071, "71": 1084, "72": 1098, "73": 1115, "74": 1127, "75": 1141, "76": 1155, "77": 1175, "78": 1189, "79": 1202, "80": 1214, "81": 1228, "82": 1241, "83": 1255, "84": 1269, "85": 1279, "86": 1294, "87": 1308, "88": 1323, "89": 1341, "90": 1358, "91": 1373, "92": 1392, "93": 1408, "94": 1428, "95": 1442, "96": 1466, "97": 1483, "98": 1495, "99": 1514, "100": 1528, "101": 1544, "102": 1559, "103": 1576, "104": 1595, "105": 1630}
---

**Dave Jones:** Hello everyone. Let's talk about the coolest topic ever, maybe. Basic control theory. And what we're going to do is we're going to talk about PID controllers and introduce the most fundamental concepts of control theory. This is the start of a

**Dave Jones:** a few control theory videos. So, any feedback would be really appreciated. So, let's start. So, control theory is something fundamental to most things, but it isn't always on the surface evident. Rockets are controlling for their their pitch and yaw and other

**Dave Jones:** variables for stability. Uh ovens control for their temperature and cars control for all kinds of things, but one of the one of the obvious examples is cruise control, which controls for speed. Even you in your day-to-day activities are a basic

**Dave Jones:** controller or at least a whole ton of them. When you walk to the shop, let's say this guy here, Bob, walking to the shop with his GPS, he gets his coordinate from his geocaching GPS. Um it just gives you a coordinate and he

**Dave Jones:** knows the coordinate of the shop and he can um subtract the two, get the distance, and that distance to the shop is the error, which is basically the fundamental concept of control theory. Control theory is controlling and minimizing error.

**Dave Jones:** So, there's a few things about error. Error is the set point, which is where you want to be, minus the feedback, which is where you are. And this is an example with the position, but it doesn't have to be the case. It could be

**Dave Jones:** with speed or it could be with acceleration or magnetic field strength or energy, power, all kinds of variables can be controlled using the minimization of error or control theory. An error of zero would often be the position called

**Dave Jones:** the steady-state position, and it is usually the goal. In cases where it's not the goal, I'm sure they'd be very happy with zero error anyway. After getting back from the shop, Bob realized that he'd eaten far too much

**Dave Jones:** chocolate, felt guilty, and bought a treadmill. So, on the treadmill, he realized this is another element of control theory. He's controlling the speed of his feet." But, what is he actually controlling? What is he looking to do? Well, he's not actually

**Dave Jones:** controlling his speed, he's controlling his um position. He wants to be in the center of the treadmill, and if he starts drifting back, he knows he's not going fast enough, and if he starts drifting forward, he knows he's he knows

**Dave Jones:** he's going too fast. So, that is if his actual position is greater than his desired position, then he is he's got an error less than zero. If his actual position is less than his desired position, then his error is greater than

**Dave Jones:** zero, and he should speed up. So, what do we do with this error? Well, we use this error to control effort, and effort is basically how much effort Bob's putting on on the treadmill. If he's not putting on in enough effort, he'll fly

**Dave Jones:** off the back and hit his head. If he puts too much effort in, he runs into this stand thing here at the front, which So, control theory is evident in basically all elements of things you do, from running to walking to your body

**Dave Jones:** heat regulation, and while it may not be the uh a PID controller or any like formally represented mathematical controller, it is explainable through basic control theory concepts. Most control theory textbooks and lectures have diagrams like this throughout the entire book. This is a

**Dave Jones:** basic diagram which represents the two previous examples, where the set point is the position Bob should be, and the feedback is the position Bob is. Um he gets that feedback from his eyes, and he uses his legs to move him to different

**Dave Jones:** positions, and his brain controls his legs, and he looks at the error to make decisions with his brain. So, if we go through that like this, you see why it's called a control loop, because it's a loop. It just goes round

**Dave Jones:** and round and round and for control loops in digital systems, it's usually a periodic loop. It goes round once every second, 10 milliseconds, something like that. Which then makes very fast and sensible, hopefully, adjustments to the system so that the system is controlled.

**Dave Jones:** When Bob was walking to the shop, his his position was going up the whole time, but his error was going down and that is what we want to do. We want to minimize error. So, up the top here, his

**Dave Jones:** position is equal to the initial error, if you look over here. And his error is actually the distance to the shop initially. So, in this case, the error units are in the same units as the position, which is

**Dave Jones:** which is much simpler than it could be. Because sometimes you have to convert the units so that they equal each other and they're comparable. So, one of the most common industry controllers is the PID controller. That's the proportional,

**Dave Jones:** integral, derivative controller. And these things are found everywhere from motherboard fan controllers to heaters to balancing Segway things. They're in all kinds of things and they're quite a primitive controller, but they're really easy to tune and pretty fast to get up

**Dave Jones:** and running. So, we're going to talk about that. Okay, so a PID controller can actually be separated into three different controllers, a proportional controller, an integral controller, and a derivative controller. We're going to talk about a proportional controller's behavior.

**Dave Jones:** A proportional controller is actually analogous to a mechanical spring where the default position is when the spring isn't stretched or compressed and that default position would be the controller's set point. If the controller the the spring was stretched, then the distance between the

**Dave Jones:** set point and the default point is the error. This is the error. When the error is negative, the force is negative. The controller outputs a force in this case. When the error is positive, then the force is positive, trying to

**Dave Jones:** move it back to its set point. Now, you'll notice that there's an equation up this top corner here, and this equation should be quite familiar to many of you. It's the exact same form as Hooke's law, where Hooke's law is F =

**Dave Jones:** K delta X. And delta X in this um is really the difference of positions, but error is a more general way of expressing differences of position. It's just the difference of an arbitrary unit, which isn't necessarily distance. So,

**Dave Jones:** a proportional controller is basically an ideal spring. An integral controller can be used in lots of things, and it's especially useful when you need to have error eventually go to zero. And these things like there are examples like precision ovens and

**Dave Jones:** um anything that balances anything, all kinds of things require zero error because if there is any error, it ends up not performing to spec or ending up halfway uh across a continent if it was a plane, or just it just ends missing its target.

**Dave Jones:** Um So, integral controllers are one of the more useful controllers for in scenarios where you need zero error. Now, we're going to talk about an oven controller. Ovens aren't usually controlled with integral controllers. They They probably should be controlled

**Dave Jones:** with a thing called a bang-bang controller cuz um that is the scenario where bang-bang controllers are basically optimal. But but um for this scenario, because it's simple, we're going to use an integral only controller. Bit weird, but whatever. Anyway, so in this

**Dave Jones:** example, we're trying to heat up this oven, and we're going to do it manually because it's not a very smart oven. We just have this knob which you can turn, but we've put a thermometer in the oven, and we want to make sure that we're

**Dave Jones:** cooking our chicken at Uh no, apparently I'm cooking it at 10° cuz that's what my plot says. We're cooking our chicken at 10°. All right. Anyway, so initially the oven's temperature is zero because someone put it in the fridge, and that

**Dave Jones:** would mean that the error is 10 the set point minus zero the actual point. So, that's here.

**Dave Jones:** Now, if you create get the area of this error here, then that is equivalent to the integral up to time one.

**Dave Jones:** So, our effort would be K times the that integral we just had before. And in this case, the integral's result is just 10, and for simplicity, we're just going to have the constant out the front as one, but this can be anything.

**Dave Jones:** So, initially our control effort U is zero because we haven't actually started the controller, but after time one, we're able to calculate our new control effort, which will be 10. We then move forward the system by one more second, and the oven is heated up a

**Dave Jones:** little bit because we've put a little bit of energy into the heating elements. Okay, so after the first sample, we're up to this sample two. We're taking a reading at the second second. We now we've realized that the

**Dave Jones:** oven has gone up 2°, and that would lower our error by two. So, it was initially 10°, and 10 minus two is eight. Now, integrals add up areas. That's how they work. And so, the the The of the integral in this case

**Dave Jones:** would be 10 plus the area here which is eight. So, our next control effort for the next period between two and three will be 18. And if you follow this through for a little while, the oven heats up more cuz

**Dave Jones:** we're putting more effort in. We got five and we add the five to the thing and that results in a control effort of 23. 23 is the the area here plus the area here plus the area here. And the oven

**Dave Jones:** has heated up even more at this point and the integral component is actually getting quite large. And notice there's nothing driving the integral component smaller. That's very important. And it's one of the biggest pitfalls of integral controllers, as we'll see in a moment.

**Dave Jones:** So, the oven's temperature is now 9°. We have one more degree to go, so the error is one and we just add that to the the result. So, that's 24, the effort. And now, we have all that accumulated

**Dave Jones:** area here. And we're still probably heating up the oven because even if you dial it up to 11, then it takes ages to heat up. There is thermal mass of the oven that takes a lot of time to heat up and um

**Dave Jones:** that means there's a delay. The integral component has a very high value now. We're up to We're up to 24 and that means we're going to overshoot our our set point. So, in the next sample, we unfortunately go to neg- we get We end up having an

**Dave Jones:** error of -4 because I've overshoot our temperature. We're at 14° and 10 - 14 is -4. And if you add these areas to the -4 area here, then we end up putting an effort of 20. The slight reduction in effort

**Dave Jones:** because this oven has basically no thermal mass, apparently, um results in the error reducing a little bit. And that again lowers our control effort to 19. And after the next sample, we've finally got zero error, but that's not the end

**Dave Jones:** of the story because our control effort is still greater than zero. So, effort does converge to a value above zero. It It needs to keep heating, but it should be stable at some point, and it isn't yet. At the next sample, we notice it's

**Dave Jones:** gone up to one, and that area adds to 20, and at that point the oven's temperature is stable, apparently. It's the fastest heating oven in the world. It's heated up in 8 seconds. So, really great. Notice that the

**Dave Jones:** waveform here ends up going like this a little bit. And that that trough there here is called overshoot, and this is something very um this is a a problem that integral controllers face. They have a thing called integral windup, and

**Dave Jones:** this is the building up of the this area here behind the the current reading. And there are lots of ways to deal with this. Um many controllers just say, "You will never have more integral windup than value X. It will just limit the the

**Dave Jones:** possible um integral value." So, if your limit was was 20, um then this would just limit it to this. Um and it would never go above 20. We've talked about proportional controllers and integral controllers, and from proportional controllers, we

**Dave Jones:** get our response speed, how fast the system will respond. And from integral controllers, hopefully we get zero error. So, why would we want a derivative controller? It sounds like we've got what we want. Well, not quite. In the scenario where you've got a

**Dave Jones:** steady state system, it's reached steady state, and we've got this nice solid line, you want to be able to reject disturbances. And what is a disturbance? Well, say someone sneezes in front of a pendulum, and then the error goes like this.

**Dave Jones:** With an integral controller, it takes a while for system to build up any control effort. So, the integral controller doesn't really respond well in this scenario at all. With a proportional controller, it does respond, but proportional controllers don't um they don't have the

**Dave Jones:** response speed before the the value ends up getting large. A proportional controller is just a constant times the error. So, what do we do? Well, what we can do is take the derivative. That means the rate of change. And what is the rate of change

**Dave Jones:** when the someone sneezes in front of the pendulum? It's very high. So, with a very high rate of change, we get this nice opposing Well, it could be depending on the sign of the constant. We get this nice

**Dave Jones:** opposing force that as soon as a disturbance occurs, we can resist it and move back to our set point and allow the integral controller to resume its normal business. Now, there are problems with um derivative controllers, really big

**Dave Jones:** problems. And these um mainly the limitations of sensors, um the digi- discretization, and all kinds of things like that mean that any noise on the line, you end up taking the rate of change of noise, which ends up being well, pretty

**Dave Jones:** damn noisy. So, you keep putting control effort in um which which is from the noise, and you don't really want to be doing um this this sort of thing because it ends up causing kind of like a instability in the system. It makes the

**Dave Jones:** system very noisy and audibly noisy in the case of pendulums and and the case of cruise control, the vehicle would be like shaking or something. An example of this equation is actually in a damper. A damper is something that absorbs energy,

**Dave Jones:** and it stops um endless oscillations in things. And this is actually the same form um the equation is in the same form as the damper equation. That's the equation that represents this mechanical element. And these are This is a

**Dave Jones:** uh fundamental element in car suspension. If you just had a spring, you'd be bouncing all over the place. If you um add the damper, you can make sure that your car kind of smoothly smoothly copes with shock as it did with

**Dave Jones:** disturbances before. The other thing that the derivative controller does is absorb energy. So, it does resist change in any scenario, including change which results from control effort. So, it has its pitfalls. That is that can be a pitfall.

**Dave Jones:** The derivative component can also help to reduce the settling time of a system. Um this is improving the settling time. This is because the derivative component um it acts against change of error. So, if the system has reached its set point,

**Dave Jones:** then it's going to resist any change away from that set point. And this includes overshoot. So, this is the equation which might be scary to some many that represents a PID controller. The proportional controller added to the integral controller added to the

**Dave Jones:** derivative controller. And now, this form isn't what you see in control textbooks very often because the form here is actually easier to work with with um a process called tuning. Tuning is the process of improving the constants in front of the

**Dave Jones:** controllers, the the proportional, integral, and derivative controllers, to improve the response of the system. You might want it to respond faster to disturbances. You might want it to reach steady state faster. You might want it to be slower. And

**Dave Jones:** this form makes tuning a bit easier because it allows you to use a process called Ziegler-Nichols tuning. Um which gives you a starting point for the values of these constants. You wouldn't want to You wouldn't want to rely on just that process, but it does

**Dave Jones:** give you a starting point for the constants in front of the components. So, let's talk about tuning. So, if we have a response that looks like this, what should we do? Well, in this scenario, we don't want it to ring like

**Dave Jones:** this. We don't want it to have this this this period here. Um uh T D. Um we don't want it to have that. We want it to look like this. We've We've got our constants from the Ziegler-Nichols tuning process, and we

**Dave Jones:** want to improve it. We want to We want to make it closer to our shape. So, what do we do? Well, oscillations like this are caused by the component of the integral and the proportional component. And if the

**Dave Jones:** integral component has a dominant um is a dominant component, then it's very likely that integral windup is causing this overshoot. So, let's try to reduce our integral component. Now, it's likely that you end up with something like this. Um

**Dave Jones:** and that might's not still be with your response. So, you you notice that the integral component is no longer significant in the control effort when compared to the proportional component. So, now let's reduce the proportional component. Now, that doesn't oscillate anymore, but

**Dave Jones:** we we do want it to perform a little bit of faster. So, what do we do? Well, the integral component now, we can change it and probably we can increase it. We know that our value of the integral component

**Dave Jones:** is somewhere between the constant that it was initially and after our tuning. So, let's take the average of those two values. Let's call them K1 + K2. And that will be the new integral constant. And now, we probably will get

**Dave Jones:** a little bit of overshoot. Um but now we've got that response time. Now, we haven't really got any derivative component yet. So, we now want to start working on that. We're now testing our disturbance rejection. So, now we're testing the response to

**Dave Jones:** disturbances. So, we start bumping it and we notice that in the normal case it decays really slowly. We want it to behave like that first curve. So, we increase the derivative component so that it's still relatively insignificant in the initial curve, but

**Dave Jones:** when there is huge rates of change like this, it has significance. So, it it is more significant than proportional component. So, we increase the value um maybe by a few percent, 10% or something. And then we see how that

**Dave Jones:** response ends up. And you'll probably end up with something like that. So, you do it again. And now you notice that you end up with the response you want as you slowly iteratively improve the coefficients. Now, each time you change

**Dave Jones:** one of these variables, the response you're probably kind of wrecking your tuning for the other variables. So, you have to retune those as well. Um and this process is an iterative process. You you slowly improve it and there's

**Dave Jones:** actually an absolute ton of methods of doing this. Um there's probably thousands of them. There there are tons of methods to get the initial values and I think Ziegler-Nichols the ultimate cycle method is probably the easiest and I'm going to show you how to use that in

**Dave Jones:** a moment. We know how to tune, but we don't know how to get a starting point. We What are we tuning from? Well, the way to get a starting point is to do the following. In most systems it's accept Well, many

**Dave Jones:** systems it's acceptable to um test the unit a fair bit before you end up having to use it. So, what we do in this process is we have the unit with its with just a proportional controller. We have

**Dave Jones:** let's say the oven. We have the oven with just that proportional controller. So, we have this this oven and we've got a digital controller sensing the temperature sensing the temperature and adjusting the oven accordingly. So, what do we

**Dave Jones:** want to do? Well, if we make the proportional component too large, then we end up with a system that does this.

**Dave Jones:** And the response gets these ever-increasing sinusoids, and this is very unstable. This is This is the the basic definition of an unstable system. What we want to do is have it a stable sine wave so that the amplitude

**Dave Jones:** is roughly not changing. Actually, that that's that's the way Ziegler-Nichols is done, but I think you should probably aim for something that is stable but decays extremely slowly. You're looking at the error, and you want the error to have this just

**Dave Jones:** constant sinusoid, which uh might seem a bit weird cuz that's exactly not what we want to happen, but this is how we do the Ziegler-Nichols tuning. We start off with a constant for KP, the proportional controller, that just

**Dave Jones:** oscillates like this. Now, when you have this constant, you can use the equations that many have come up with that use this value to create a starting point for your system's controller. From before, we have our KP value. And

**Dave Jones:** when the KP is equal to the gain that results in a stable sinusoid, then it is called K U. So, KU is the gain at which you got a stable sinusoid. Now, presumably, you can measure the sinusoid's period. I

**Dave Jones:** assume you can measure the sinusoid's period, and that value is quite important because we're going to use it in this tuning method, and that value is called TU. With KU and TU, you can use them in this equation here

**Dave Jones:** to get default values for the the controller coefficients. So, 0.6 KU * 0.6 * the value of KU is the coefficient for the proportional controller and you can use that value as a starting point. TU divided by 2, that's the period

**Dave Jones:** divided by 2 is the coefficient for the the constant for the integral controller and the the period divided by 8 is the the constant in front of the derivative controller. So, that actually gives us everything. We now have an

**Dave Jones:** initial value for KP, KI, and KD because we have an initial value for KP, TI, and TD. And to tune the values, all you do is expand this equation and then you can tune the values in front of the controller as if you had

**Dave Jones:** the controller before and it's much it's easier to do the iterative improvement tuning on this equation than it is on this equation in my opinion. So, after you get these TI values and TD values, I would convert it to the form you see

**Dave Jones:** above here. That is simply by doing this. You just the KI equals KP on TI and KD equals TD. KD and that's it. Now, I am aware that control theory can be a little bit dry. So, this is just the start. This is the

**Dave Jones:** boring part of this. What we have coming is a nice little inverted pendulum balancing robot which will just wander around the office balancing and this is going to be designed, uh 3D printed, and then we're going to use that Ziegler-Nichols tuning to just

**Dave Jones:** get it to balance in a empirical way. If anyone wants to know more about this, leave them in the comments below. If anyone wants to know the theory, the mathematical the theory behind this and how you can derive

**Dave Jones:** controllers from math alone. Leave it in the comments below, vote up that comment, and I'd be happy to do that. So, thanks. Okay, so I finished shooting my video. I finished editing, and then I find this beautiful plot on Wikipedia.

**Dave Jones:** But, it's worth it. This plot shows the effect of a step response on a system and the effect of changing the PID constants in front of the components. So, the first thing they tune here is the proportional component,

**Dave Jones:** and then the integral component, then the derivative component. And the plot kind of shows the the change of the response of the system. Now, this system this plot here is showing how a system responds to a step input. That is where

**Dave Jones:** the set point, where the system should be, is set to one, and you kind of just view how that looks. So, initially you notice about this system is that it has some steady-state error. That means that the system's

**Dave Jones:** response doesn't converge to the set point. And the way you deal with this is by increasing the integral component. They do this, and they remove the steady-state error. Unfortunately, as they increase the integral and proportional component, overshoot of the system substantially

**Dave Jones:** increases. The way they deal with that here is by increasing the derivative component. And because the derivative component resists change, it it it it's it hates change. It does help in reducing the oscillations, as oscillations are of course change and

**Dave Jones:** overshoot is change. It really just wants the line to be flat and stationary. So, I hope this plot helped. I had to add it in after rendering. Um see you.

**Dave Jones:** Mhm.
