let img;

let horizontalKernel = [
  [-1, -2, -1],
  [0, 0, 0],
  [1, 2, 1]
];
let verticalKernel = [
  [-1, 0, 1],
  [-2, 0, 2],
  [-1, 0, 1]
];

var stride = 1;

// Function to calculate the maximum value in an array iteratively since the built in max() function throws a stack limit reached exception...
function maxIter(arr) {
  let currentMax = arr[0];
  for (let i = 1; i < arr.length; ++i) {
    if (arr[i] > currentMax) {
      currentMax = arr[i];
    }
  }
  return currentMax;
}

// Likewise, a min value finding function since the build in one throws an error
function minIter(arr) {
  let currentMin = arr[0];
  for (let i = 1; i < arr.length; ++i) {
    if (arr[i] < currentMin) {
      currentMax = arr[i];
    }
  }
  return currentMin;
}

// Apply the provided kernel to the provided image at the given input pixel
function applyKernel(img, kernel, x, y) {
  let total = 0;
  for (let xOff = 0; xOff < kernel.length; ++xOff) {
    for (let yOff = 0; yOff < kernel.length; ++yOff) {
      total += img.get(x + (xOff - 1), y + (xOff - 1))[0] * kernel[xOff][yOff];
    }
  }
  return total;

}

function preload() {
  img = loadImage('/assets/projects/p5js-experiments/edges/assets/rose2.jpg');
  // Make the image grey
  img.filter(GRAY);
}

function setup() {
  var canvas = createCanvas(400, 400);
  canvas.parent('canvas-wrapper2');
  background(0);

  let newPixels = [];
  for (let y = 1; y < img.height - 1; ++y) {
    for (let x = 1; x < img.width - 1; ++x) {

      newPixels.push(
        // This isn't ideal, can't seem to get pythagorean distance working and performant
        applyKernel(img, horizontalKernel, x, y) +
        applyKernel(img, verticalKernel, x, y)
      );
    }

    if (y % 50 == 0) {
      console.log("row" + y + "complete");
    }
  }

  let mii = minIter(newPixels);
  let mai = maxIter(newPixels);
  for (let y = 0; y < img.height - 2; ++y) {
    let yIndex = (img.width - 2) * y;
    for (let x = 0; x < img.width - 2; ++x) {
      let index = yIndex + x
      stroke(map(newPixels[index], mii, mai, 0, 255));
      point(x, y);
    }

    if (y % 50 == 0) {
      console.log("row" + y + "drawn");
    }
  }
}

//function draw() {
  // Do nothing for now
//}
