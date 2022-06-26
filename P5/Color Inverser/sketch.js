let circ1;
let r, g, b;
let sliderR, sliderG, sliderB;


function setup() {
  createCanvas(400, 400);
  sliderR = createSlider(0, 255, 0, 1);
  div = createElement("div");
  sliderG = createSlider(0, 255, 0, 1);
  div = createElement("div");
  sliderB = createSlider(0, 255, 0, 1);
  
}

function draw() {
  r = sliderR.value();
  g = sliderG.value();
  b = sliderB.value();
  
  background(r, g, b);
  frameRate(1)
  
  
  circ1 = new circ(random(width), random(height), 16);
  circ1.move();
  circ1.show();
  circ1.restrict()

  circ2 = new circ(random(width), random(height), 16);
  circ2.move();
  circ2.show();
  circ2.restrict()
  

  circ3 = new circ(random(width), random(height), 16);
  circ3.move();
  circ3.show();
  circ3.restrict()
  

  circ4 = new circ(random(width), random(height), 16);
  circ4.move();
  circ4.show();
  circ4.restrict()
  

  circ5 = new circ(random(width), random(height), 16);
  circ5.move();
  circ5.show();
  circ5.restrict()

  circ6 = new circ(random(width), random(height), 16);
  circ6.move();
  circ6.show();
  circ6.restrict()

  circ7 = new circ(100, 100, 16);
  circ7.move();
  circ7.show();
  circ7.restrict()
}
