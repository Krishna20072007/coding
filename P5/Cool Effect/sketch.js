let locationn, colorX, colorY

function setup() {
  createCanvas(windowWidth, windowHeight);
   
}

function draw() {
  locationn = createVector(mouseX, mouseY)
  
  colorX = map(locationn.x, 0, width, 255, 0)
  colorY = map(locationn.y, 0, width, 0, 255)
  background(colorX, colorY, colorX, colorY);
  
  
  
}