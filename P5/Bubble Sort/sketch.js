let values = [];
let w;
let states = [];

function setup() {
  w = random(10);
  createCanvas(windowWidth, windowHeight);

  values = new Array(floor(width / w));

  for (let i = 0; i < values.length; i++) {
    values[i] = float(random(height));
    states[i] = -1;
  }

  print("Unsorted Array:" + values);

  bubbleSort(values, 0, values.length);

  print("Sorted Array:" + values);
}
async function bubbleSort(arr, start, end) {
  if (start >= end) {
    return;
  }

  for (var i = 0; i < end - 1; i++) {
    for (var j = 0; j < end - i - 1; j++) {
      if (arr[j] >= arr[j + 1]) {
        states[j] = 1;

    
        await swap(arr, j, j + 1);
        states[j + 1] = 0;
      }
      states[j] = 2;
    }
  }
  return arr;
}
function draw() {
  background(255);

  for (let i = 0; i < values.length; i++) {
    stroke(0);
    fill(0);

    if (states[i] == 0) {
      stroke(255);
      fill(255, 0, 0);
    } else if (states[i] == 1) {
  
      fill("#58FA82");
    } else {
      fill(0);
    }
    rect(i * w, height - values[i], w, values[i]);
  }
}
async function swap(arr, a, b) {
  await sleep(0);
  let t = arr[a];
  arr[a] = arr[b];
  arr[b] = t;
}
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
