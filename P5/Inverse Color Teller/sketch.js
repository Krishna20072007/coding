let sliderR, sliderG, sliderB;

function setup() {
  createCanvas(windowWidth, windowHeight - 23);
  sliderR = createSlider(0, 255, 0, 1);
  sliderG = createSlider(0, 255, 0, 1);
  sliderB = createSlider(0, 255, 0, 1);

  sliderR.changed(chang);
  sliderG.changed(chang);
  sliderB.changed(chang);
}

function draw() {
  background(sliderR.value(), sliderG.value(), sliderB.value());
  noStroke();
  fill(255 - sliderR.value(), 255 - sliderG.value(), 255 - sliderB.value());
  ellipse(width / 2, height / 2, 32, 32);
}

function chang() {
  console.log(
    "Background Color",
    ":",
    sliderR.value(),
    sliderG.value(),
    sliderB.value()
  );
  console.log(
    "Inverted of Background Color",
    ":",
    255 - sliderR.value(),
    255 - sliderG.value(),
    255 - sliderB.value()
  );
  console.clear();
}
