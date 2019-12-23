let video;
var prev;
let threshold = 300
let thresholdSquared = (threshold * threshold);
var vScale = 6;

function colorDistance(r1, g1, b1, r2, g2, b2) {
    return (r2 - r1) * (r2 - r1) +
        (g2 - g1) * (g2 - g1) +
        (b2 - b1) * (b2 - b1);
}

function preload() {
    video = createVideo('assets/dance.mp4');
    prev = createImage(640, 360)
}

function setup() {
    createCanvas(640, 480);

    video.hide();
    video.loop();
    video.size(width / vScale, height / vScale);

    background(51);
}

function draw() {
    // Only do the processing if the video and previous frames are set and the widths are > 0
    if (!(video && prev)) return;
    if (video.width == 0) return;
    if (prev.width == 0) return;

    video.loadPixels();
    prev.loadPixels();
    loadPixels();

    // Loop through all the pixels
    for (var y = 0; y < video.height; y++) {
        let yIndex = (y * video.width);
        for (var x = 0; x < video.width; x++) {
            var index = (video.width - x + 1 + yIndex) * 4;
            var r = video.pixels[index + 0];
            var g = video.pixels[index + 1];
            var b = video.pixels[index + 2];

            var r2 = prev.pixels[index + 0];
            var g2 = prev.pixels[index + 1];
            var b2 = prev.pixels[index + 2];

            var distance = colorDistance(r, g, b, r2, g2, b2);

            var col = map(distance, 0, 65025, 0, 150)

            noStroke();
            if (distance <= thresholdSquared) {
                fill(179, 135, 230, col);
                rectMode(CENTER);
                rect(width - (x * vScale), (y * vScale) - 6 * vScale, vScale, vScale);
            }
        }
    }

    video.copy(prev, 0, 0, video.width, video.height, 0, 0, video.width, video.height);
}