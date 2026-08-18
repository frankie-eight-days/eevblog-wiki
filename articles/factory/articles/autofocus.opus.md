# autofocus

Autofocus is the automatic adjustment of a lens or sensor position to bring a subject into sharp focus, and in electronics work it is what makes a camera usable as a working instrument rather than a fixed-distance recording device. On an inspection microscope it removes the need to re-level the stand every time a board is moved or tilted, allowing a sloping or stepped assembly to be examined point by point without touching the mechanics.[1125][FLsCLAf-ahg] On a bench or studio camera it determines whether an object held up to the lens snaps into focus or the image drifts in and out while the system searches.[vSq9Acgo418][6n4IQ2nvTw0] The same mechanism that makes a camera convenient in one setting makes it unusable in another: an autofocus system that continually re-evaluates the scene is an asset for close-up work and a liability for a fixed talking-head shot.[6n4IQ2nvTw0]

## Sensing methods

Two distinct approaches appear in camera hardware. Phase-detection systems use dedicated focus sensors, and a large array of them supports very fast acquisition along with subject tracking.[vSq9Acgo418] Contrast-based systems derive focus from the image itself, which works without any auxiliary sensor but is slower.[282]

The distinction is visible in the physical layout of a camera. Some camcorders carry a separate high-speed focus window on the body, distinct from the taking lens.[282] Fitting a close-up macro lens with a thick surround over the front of such a camera can physically block that window; focus still works, because the camera falls back to deriving focus from the image, but it is no longer as fast.[282] A cheaper 10x close-up lens with a larger viewable area leaves the window clear and preserves the instant autofocus, at the cost of optical quality.[282]

Mechanically, autofocus is a motor-driven positioning problem. In a video microscope camera the sensor itself can be seen travelling in and out behind the lens.[1125] In an optometrist's autorefractor, a lead screw and motor move the camera assembly: the operator brings the instrument into range by hand, and the motor then performs the fine adjustment.[1554] In a visual presenter, autofocus and zoom control occupy their own PCB alongside the motor that drives the optical zoom group.[278]

## Autofocus in inspection microscopes

Autofocus changes the workflow of a digital soldering and inspection microscope more than any other feature. Traditional digital microscopes require the height of the head to be adjusted for each subject; an autofocusing camera removes that step entirely.[1125] With a nominal 180x lens set for a working distance of about 100 mm, anything within that height range is focused automatically, from a flat board right up to the maximum height of the stand, so the stand need not be touched again once the initial distance is set.[1125] A tilted board can be examined at its edge, in its centre, or at its lowest point with no mechanical intervention.[1125]

Range depends strongly on the optics in front of the camera. Adding a 0.35x Barlow lens extends the autofocus range to at least 150 mm, and in practice to around 300 mm at a working distance of roughly 370 mm, enough to hold a board near vertical and still focus on its far end.[1143]

A region-of-interest control makes autofocus selective rather than scene-wide. The ROI box can be enabled or disabled and set small or large; placing a chosen feature — a capacitor, a via, the top of an IC package — inside the box drives the system to focus on that feature specifically, which is what makes autofocus useful on a tilted board where different features sit at different heights.[FLsCLAf-ahg] The same idea appears as a focus square that keeps a moving or tilting subject sharp.[1125]

Autofocus is also bundled with other automatic adjustments in microscope cameras: automatic brightness and iris control alongside auto exposure, on an F1.6 lens system capable of a 12 mm field of view at maximum zoom.[590] A 40x zoom inspection microscope will re-acquire focus after the head is tilted.[521]

## Focus hunting

The characteristic failure mode of a continuous autofocus system is hunting: repeated cycling between near and far focus without settling. On a 4K microscope, pressing the autofocus button produces two full in-and-out sweeps before the system locks, and the same hunting cycle runs again before each still capture.[1640] The system may lock, drift slightly off, and then start hunting again when the subject is changed.[1640] A flexible stand aggravates the problem and must be locked in place, or the system will hunt continuously.[1640] Autofocus of this quality is a bit dicky and is the weakest part of an otherwise acceptable instrument.[1640]

The same behaviour on a webcam is triggered by ordinary movement. Simply raising the hands and gesturing is enough to send the system hunting between foreground and background, which is disqualifying for presenting work to camera.[6n4IQ2nvTw0] The practical fix is to abandon continuous autofocus entirely and set fixed or manual focus, after which gesturing has no effect on the image.[6n4IQ2nvTw0] Where a camera offers no such setting, the only remedy is a firmware change.[6n4IQ2nvTw0]

Failure can also take the form of not focusing at all rather than hunting. A webcam may hold the operator's face out of focus and only acquire it when the operator looks directly at the lens, which is impractical when working from a monitor.[1608] A DSLR that refuses to focus with all the correct autofocus settings enabled may simply be closer to the subject than its minimum focus distance allows.[j-AqRB8Q-9w] Zoom is another limit: at extreme optical zoom a focus system that works well at moderate magnification can fail to resolve surface-mount components at all.[278]

## Acquisition speed

Speed separates otherwise similar cameras. Between two webcams of the same family, one focuses noticeably quicker on a far-field to near-field transition, which is the transition that matters when objects are held up to the lens.[17Y6XEoGuLw] The slower of the two fails to focus promptly on a board brought up from below, and does not lock on even when the board fills the frame, despite being capable of focusing on it.[17Y6XEoGuLw] Faster acquisition on that specific transition is a decisive advantage for close-up demonstration work.[17Y6XEoGuLw]

Acquisition speed is also a function of aperture, because a wider aperture gives a shallower depth of field and therefore a longer distance for the lens to travel before the subject is sharp. Testing against a target roughly 40 to 50 cm from the camera, focus locks faster at f4.0 than at f2.8, both bringing a board in and returning to the background, precisely because the mechanism has further to go at the wider aperture.[364] This makes bench lighting an indirect autofocus variable: well over a thousand lux on the bench permits a permanently higher f-stop, a deeper depth of field, and correspondingly less autofocus work.[364]

## Subject tracking and selective focus

Modern camera autofocus is subject-aware rather than distance-aware. Eye tracking follows a specific eye and holds it in focus; if the subject leaves the active frame the system falls back to face tracking against a registered face.[vSq9Acgo418][DRq8p5FT3hU] A dedicated product-shot mode shifts focus to an object placed in front of the lens.[vSq9Acgo418] Tracking is not infallible — a furry microphone windshield entering the frame can momentarily divert it.[DRq8p5FT3hU]

Selective focus can also be driven the other way, by a defocus function that deliberately throws the background out of focus for a shallower look; the further the background is from the subject, the more defocused it can be made for a given lens.[1362] Whether the system holds that defocus or reverts to tracking the subject's eye depends on which mode wins.[1362]

Touch-selectable focus lets a subject be nominated directly: touching a distant object on the screen pulls focus to it, and leaving manual focus returns focus instantly to the previous subject.[2] A focus-assist function that temporarily magnifies the image while the focus ring is turned, then returns to the normal view, supports manual focus alongside the automatic system.[2] The same instant autofocus carries across a camcorder family, with a 58 mm filter thread that allows existing macro lenses to be reused.[650]

Half-pressing the shutter release to acquire focus and fully pressing to expose is the conventional two-stage control, and the two stages can fail independently — a repaired camera may focus correctly on the half press yet refuse to take the photograph on the full press.[1428]

## When autofocus is not present or not wanted

Not every camera has it. A fixed-focus camera requires the lens to be twiddled by hand to get the image sharp, regardless of what automatic white balance and exposure it may carry.[1239] Even where autofocus exists, a microscope may lack powered focus and require the head to be raised and lowered manually.[1640]

Conversely, autofocus is one of several automatic functions that can simply be left on when conditions do not permit careful setup. For handheld field shooting, running auto exposure, auto white balance and autofocus together is the sensible default, since attempting manual control while moving is not worth the effort.[786] Autofocus paired with automatic settings has been a standard consumer camcorder feature since the analog era.[375][807] Its presence as a discrete control is long-established: an early digital SLR carried autofocus and manual focus buttons on the front of the body beside the lens release.[495]
